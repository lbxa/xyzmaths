import { getCollection } from "astro:content";
import type { Book } from "./books";

export interface ContentsEntry {
  kind: "group" | "page" | "section";
  title: string;
  href?: string;
  page?: string;
  children?: ContentsEntry[];
}

export interface HeadingLink extends ContentsEntry {
  href: string;
  children?: HeadingLink[];
}

type Heading = { id: string; title: string; level: number };

export async function getBookPages(book: Book) {
  const pages = await getCollection("bookPages", ({ data }) => data.book === book.slug);
  return pages.sort((a, b) => a.data.order - b.data.order);
}

export async function getBookOverview(book: Book) {
  const groups = Array.from(Map.groupBy(await getBookPages(book), ({ data }) => data.group), ([title, entries]) => ({
    id: entries[0].id.split("/")[0], title, entries,
    numbered: Boolean(entries[0].data.part && title !== "References"),
  }));
  // Both editions open with the chapters. The reader sidebar follows print order.
  return {
    groups: [...groups.filter(group => group.numbered), ...groups.filter(group => !group.numbered)],
    firstChapter: groups.find(group => group.numbered)?.entries[0],
  };
}

export async function getBookAssignments(book: Book) {
  const exercises = await getCollection("bookExercises", ({ data }) => data.book === book.slug);
  const assignments = Map.groupBy(exercises, ({ data }) => data.assignment ?? "lecture");
  return [...assignments].sort(([a], [b]) => a.localeCompare(b)).map(([id, entries]) => ({
    id,
    title: id === "lecture" ? "Lecture exercises" : `Homework ${Number(id.slice(2))}`,
    problems: entries.sort((a, b) => (a.data.question ?? 0) - (b.data.question ?? 0)).map(entry => {
      const { question, number, title } = entry.data;
      const label = question === null ? `Exercise ${number}` : `Problem ${question}`;
      return { entry, title: title === "Exercise" ? label : `${label} · ${title}` };
    }),
  }));
}

function nestHeadings(headings: Heading[], pageHref: string) {
  const roots: HeadingLink[] = [];
  const ancestors: { level: number; entry: HeadingLink }[] = [];
  for (const { level, id, title } of headings) {
    while (ancestors.length && ancestors[ancestors.length - 1].level >= level) {
      ancestors.pop();
    }
    const entry: HeadingLink = { kind: "section", title, href: pageHref + "#" + id };
    const parent = ancestors.at(-1)?.entry;
    if (parent) {
      parent.children ??= [];
      parent.children.push(entry);
    } else {
      roots.push(entry);
    }
    ancestors.push({ level, entry });
  }
  return roots;
}

export async function getBookContents(book: Book) {
  const [pages, assignments] = await Promise.all([getBookPages(book), getBookAssignments(book)]);
  const groups = new Map<string, ContentsEntry & { children: ContentsEntry[] }>();
  const readingOrder: HeadingLink[] = [];
  for (const { id, data } of pages) {
    const title = data.part ?? data.group;
    let group = groups.get(title);
    if (!group) {
      group = { kind: "group", title, children: [] };
      if (data.part) group.href = book.href + "#" + id.split("/")[0];
      groups.set(title, group);
    }
    const href = book.href + id + "/";
    const page: HeadingLink = {
      kind: "page", title: data.title, href, page: data.printPage, children: nestHeadings(data.outline, href),
    };
    group.children.push(page);
    readingOrder.push(page);
  }

  const problemsHref = book.href + "problems/";
  const problems: HeadingLink = {
    kind: "page", title: "All problems", href: problemsHref,
    children: assignments.map(({ id, title, problems }) => ({
      kind: "section", title, href: problemsHref + "#" + id,
      children: problems.map(({ entry, title }) => ({ kind: "section", title, href: problemsHref + "#" + entry.id })),
    })),
  };
  const entries = Array.from(groups.values(), group =>
    !group.href && group.children.length === 1 && group.children[0].title === group.title
      ? group.children[0] : group);
  entries.push(problems);
  readingOrder.push(problems);
  return { entries, readingOrder };
}
