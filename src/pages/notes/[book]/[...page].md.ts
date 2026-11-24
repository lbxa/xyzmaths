import type { APIRoute } from "astro";
import { getBookAssignments, getBookOverview, getBookPagePaths, getBookPaths } from "../../../lib/book-contents";
import type { Book } from "../../../lib/books";

export const prerender = true;

export async function getStaticPaths() {
  return [
    ...(await getBookPagePaths()).map(({ params, props: { book, entry } }) => ({ params, props: { book, body: entry.body } })),
    ...getBookPaths().flatMap(({ params, props }) => ["index", "problems"].map(page => ({
      params: { ...params, page }, props,
    }))),
  ];
}

export const GET: APIRoute = async ({ params, props, site, url }) => {
  const book: Book = props.book;
  const base = new URL(book.href, site ?? url).href;
  let body = props.body;
  if (params.page === "index") {
    const { groups, firstChapter } = await getBookOverview(book);
    const contents = groups.map(({ title, entries, numbered }) =>
      `## ${title}\n\n` + entries.map((entry, i) =>
        `${numbered ? (i + 1) + "." : "-"} [${entry.data.title}](${base}${entry.data.path}.md)`).join("\n"));
    const figure = book.frontispiece;
    body = [`# ${book.title}`, book.author, book.description,
      firstChapter && `[Start reading](${base}${firstChapter.data.path}.md)`,
      `[Download manuscript (PDF)](${new URL(book.manuscript.href, base).href})`,
      `[Browse all problems by assignment](${base}problems.md)`,
      figure && `[![${figure.alt}](${base}${figure.image})](${base}${figure.destination})\n\n[${figure.caption}](${base}${figure.destination})`,
      ...contents].filter(Boolean).join("\n\n") + "\n";
  } else if (params.page === "problems") {
    const assignments = await getBookAssignments(book);
    const sections = assignments.map(({ title, problems }) => {
      const items = problems.map(({ title, entry }) => {
        const { key, number, statementPage, solutionPage } = entry.data;
        return [`### ${title}`, entry.body!.trimEnd(),
          `[Exercise ${number} in the chapter](${base}${statementPage}/#ex:${key}) · [Appendix solution](${base}${solutionPage}/#sol:${key})`].join("\n\n");
      });
      return [`## ${title}`, ...items].join("\n\n");
    });
    body = ["# All problems", ...sections].join("\n\n") + "\n";
  }
  if (typeof body !== "string") throw new Error(`Missing Markdown for ${params.page}`);
  return new Response(body, { headers: { "Content-Type": "text/markdown; charset=utf-8" } });
};
