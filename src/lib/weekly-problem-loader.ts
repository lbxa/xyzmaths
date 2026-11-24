import type { Loader } from "astro/loaders";
import { readdir, readFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { createNoteRenderer, readNote } from "./note-markdown.mjs";

// Typeset weekly problems during content sync with the same KaTeX settings as the books.
export const weeklyProblemLoader: Loader = {
  name: "weekly-problems",
  async load({ config, store, parseData, generateDigest, watcher, logger }) {
    const directory = fileURLToPath(new URL("content/pow", config.srcDir));
    const render = createNoteRenderer();

    async function sync() {
      const files = new Set((await readdir(directory, { withFileTypes: true }))
        .filter(file => file.isFile()).map(file => file.name));
      const stale = new Set(store.keys());
      for (const file of files) {
        if (!file.endsWith(".md")) continue;
        const id = file.slice(0, -3);
        const filePath = join(directory, file);
        const source = await readFile(filePath, "utf8");
        stale.delete(id);
        const { attrs, markdown } = readNote(filePath, source.replaceAll("\r\n", "\n"));
        if (!markdown) throw new Error(`Missing worked editorial in ${filePath}`);
        const program = id + ".cpp";
        const referenceCode = files.has(program) ? await readFile(join(directory, program), "utf8") : undefined;
        const data = await parseData({ id, filePath, data: { ...attrs, referenceCode } });
        const html = render(markdown);
        const digest = generateDigest({ data, html });
        if (store.get(id)?.digest !== digest) store.set({ id, digest, data, rendered: { html } });
      }
      for (const id of stale) store.delete(id);
    }

    await sync();
    if (!watcher) return;
    watcher.add(directory);
    let pending = Promise.resolve();
    watcher.on("all", (event, path) => {
      if (["add", "change", "unlink"].includes(event) && /\.(md|cpp)$/.test(path) && dirname(resolve(path)) === directory) {
        pending = pending.then(sync).catch(error => logger.error(String(error)));
      }
    });
  },
};
