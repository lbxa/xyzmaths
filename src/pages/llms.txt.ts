import type { APIRoute } from "astro";
import { books } from "@/lib/books";
import { getWeeklyProblems, problemMarkdownHref } from "@/lib/weekly-problems";

export const prerender = true;

export const GET: APIRoute = async ({ site, url }) => {
  const problems = await getWeeklyProblems();

  function item(title: string, path: string, description?: string) {
    const label = title.replace(/[\\[\]]/g, "\\$&").replace(/\s+/g, " ");
    const link = `- [${label}](${new URL(path, site ?? url).href})`;
    return description ? `${link}: ${description.replace(/\s+/g, " ")}` : link;
  }

  const lines = [
    "# XYZ Maths",
    "",
    "> Mathematics books and weekly problem editorials by Lucas Barbosa.",
    "",
    "Each book’s Markdown table of contents links to its chapters and appendices. Each weekly problem opens with the statement and links to its solution and worked editorial.",
    "",
    "## XYZ Books",
    "",
    item("Book catalogue", "/books/"),
    ...books.flatMap(book => [
      item(book.title, book.href + "index.md", book.description),
      item(`${book.title} exercises by assignment`, book.href + "problems.md"),
    ]),
    "",
    "## XYZ PoW",
    "",
    item("Problem of the Week archive", "/pow/", "Browse all problems, newest first."),
    ...problems.map(({ id, data }) => item(data.title, problemMarkdownHref(id), data.description)),
    "",
    "## Optional",
    "",
    ...books.map(book => item(`${book.title} manuscript (PDF)`, book.manuscript.href)),
  ];

  return new Response(lines.join("\n") + "\n", {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
};
