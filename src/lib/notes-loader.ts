import type { Loader } from "astro/loaders";
import { execFile } from "node:child_process";
import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import { join, relative } from "node:path";
import { fileURLToPath } from "node:url";
import { promisify } from "node:util";
import { linearAlgebra } from "./books";
import { readerLinkStyle } from "./reader-links";
import { createNoteRenderer, portableMarkdown, readNote } from "./note-markdown.mjs";

const exec = promisify(execFile);
const base = linearAlgebra.href;

interface Exercise {
  key: string; source: string; number: string; title: string;
  assignment: string | null; question: number | null;
  statementPage: string; solutionPage: string; statement: string; solution: string;
  statementMarkdown: string; solutionMarkdown: string;
}
interface Item { id: string; data: Record<string, unknown>; html?: string; body?: string }
type Kind = "pages" | "exercises" | "figures";

async function verifiedFiles(directory: string) {
  const stamp = await readFile(join(directory, "checksums.sha256"), "utf8");
  const outputs = /^# outputs ([a-f0-9]{64})\n/m.exec(stamp);
  if (!outputs) return;
  const inventory = stamp.slice(outputs.index + outputs[0].length);
  if (createHash("sha256").update(inventory).digest("hex") !== outputs[1]) return;
  const files = new Map<string, Buffer>();
  for (const [, digest, path] of inventory.matchAll(/^([a-f0-9]{64})  (.+)$/gm)) {
    let bytes: Buffer;
    try {
      bytes = await readFile(join(directory, path));
    } catch (error) {
      if ((error as NodeJS.ErrnoException).code === "ENOENT") return;
      throw error;
    }
    if (createHash("sha256").update(bytes).digest("hex") !== digest) return;
    files.set(path, bytes);
  }
  return files;
}

function escape(text: string) {
  return text.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;");
}

function exercisePlacement(ex: Exercise, solution: boolean, origin: string) {
  const key = escape(ex.key);
  const title = `Exercise ${ex.number}` + (ex.title === "Exercise" ? "" : ` (${ex.title})`);
  const heading = `<h3>${escape(title)}</h3>`;
  const original = `${base}${ex.statementPage}/#ex:${ex.key}`;
  const appendix = `${base}${ex.solutionPage}/#sol:${ex.key}`;
  if (solution) {
    const restatement = ex.statement.replace(/(\s(?:id="|href="#))([^"]+)"/g, '$1restated-$2"');
    return {
      html: `<section class="exercise" id="sol:${key}">${heading}${restatement}<p><a class="${readerLinkStyle}" href="${escape(original)}">Original exercise</a></p><div class="solution">${ex.solution}</div></section>`,
      markdown: `### ${title}\n\n${ex.statementMarkdown.trimEnd()}\n\n[Original exercise](${origin}${original})\n\n${ex.solutionMarkdown.trimEnd()}`,
    };
  }
  return {
    html: `<section class="exercise" id="ex:${key}">${heading}${ex.statement}<p><a class="${readerLinkStyle}" href="${escape(appendix)}">Solution in the appendix</a></p></section>`,
    markdown: `### ${title}\n\n${ex.statementMarkdown.trimEnd()}\n\n[Solution in the appendix](${origin}${appendix})`,
  };
}

function collections(files: Map<string, Buffer>, origin: string): Record<Kind, Item[]> {
  const pages: (Item & { body: string })[] = [];
  const figures: Item[] = [];
  const exercises = new Map<string, Exercise>();
  const render = createNoteRenderer();
  for (const [path, bytes] of files) {
    if (path.startsWith("figures/")) {
      const content = bytes.toString(path.endsWith(".svg") ? "utf8" : "base64");
      figures.push({ id: path.slice("figures/".length), data: { content } });
    } else if (path.startsWith("pages/") && path.endsWith(".md")) {
      const { attrs, markdown } = readNote(path, bytes.toString("utf8"));
      pages.push({
        id: path.slice("pages/".length, -".md".length),
        data: {
          book: linearAlgebra.slug, title: attrs.title, group: attrs.group, order: Number(attrs.order),
          part: attrs.part, printPage: attrs.page, outline: attrs.outline ?? [],
        },
        body: markdown,
      });
    } else if (path.endsWith("/statement.md")) {
      const { attrs, markdown } = readNote(path, bytes.toString("utf8"));
      const solution = files.get(path.replace(/statement\.md$/, "solution.md"))?.toString("utf8");
      if (!solution || exercises.has(attrs.key)) throw new Error(`Invalid exercise pair in ${path}`);
      exercises.set(attrs.key, {
        key: attrs.key, source: attrs.source, title: attrs.title, number: attrs.number,
        assignment: attrs.assignment ?? null, question: attrs.question ? Number(attrs.question) : null,
        statementPage: attrs["statement-page"], solutionPage: attrs["solution-page"],
        statement: render(markdown), solution: render(solution),
        statementMarkdown: portableMarkdown(markdown, origin + base + attrs["statement-page"] + "/"),
        solutionMarkdown: portableMarkdown(solution, origin + base + attrs["solution-page"] + "/"),
      });
    }
  }
  for (const page of pages) {
    function placement(kind: string, key: string) {
      const exercise = exercises.get(key);
      if (!exercise) throw new Error(`Missing exercise ${key} in ${page.id}`);
      return exercisePlacement(exercise, kind === "solution", origin);
    }
    page.html = render(page.body, placement);
    page.body = portableMarkdown(page.body, origin + base + page.id + "/", placement);
  }
  return {
    pages, figures,
    exercises: Array.from(exercises.values(), ({ statement, statementMarkdown, ...data }) => ({
      id: data.key, data: { ...data, book: linearAlgebra.slug }, html: statement, body: statementMarkdown,
    })),
  };
}

// Share one verified set of fragments across the three concurrent Astro loaders.
let pending: Promise<Record<Kind, Item[]>> | undefined;
function loadBook(root: string, origin: string) {
  return pending ??= (async () => {
    const directory = join(root, "src/generated/notes/linear-algebra");
    for (let attempt = 0; attempt < 2; attempt++) {
      await exec("python3", ["-B", "scripts/web-notes/build.py"], { cwd: root });
      const files = await verifiedFiles(directory);
      if (files?.size) return collections(files, origin);
      // Another process published while this loader was reading. Reopen the new inventory.
    }
    throw new Error("Linear Algebra fragments changed during both reads.");
  })().finally(() => { pending = undefined; });
}

export function notesLoader(kind: Kind): Loader {
  return {
    name: `linear-algebra-${kind}`,
    async load({ config, store, parseData, generateDigest, watcher, logger }) {
      const root = fileURLToPath(config.root);
      async function sync() {
        const origin = config.site ? new URL(config.site).origin : "";
        const records = (await loadBook(root, origin))[kind];
        const entries = await Promise.all(records.map(async ({ id, data, html, body }) => ({
          id, data: await parseData({ id, data }), digest: generateDigest({ data, html, body }), body,
          ...(html === undefined ? {} : { rendered: { html } }),
        })));
        const stale = new Set(store.keys());
        for (const entry of entries) {
          stale.delete(entry.id);
          if (store.get(entry.id)?.digest !== entry.digest) store.set(entry);
        }
        for (const id of stale) store.delete(id);
      }
      await sync();
      if (!watcher) return;
      const inventory = "src/generated/notes/linear-algebra/checksums.sha256";
      watcher.add([join(root, "books/linear-algebra"), join(root, "scripts/web-notes"),
        join(root, "package.json"), join(root, inventory)]);
      let timer: ReturnType<typeof setTimeout>;
      let queue = Promise.resolve();
      watcher.on("all", (event, path) => {
        if (!["add", "change", "unlink"].includes(event)) return;
        const file = relative(root, path).replaceAll("\\", "/");
        if (file !== inventory && file !== "package.json" && (!/^(books\/linear-algebra\/|scripts\/web-notes\/)/.test(file) ||
            /\/(build|images|output|__pycache__)\//.test(file) ||
            !/\.(tex|bib|bbx|cbx|cls|sty|pdf|svg|png|jpe?g|webp|py|mjs)$/.test(file))) return;
        clearTimeout(timer);
        timer = setTimeout(() => {
          queue = queue.then(sync).catch((error) => logger.error(String(error)));
        }, 150);
      });
    },
  };
}
