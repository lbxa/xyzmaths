import { getCollection } from "astro:content";

export const problemViews = [
  { segment: "", label: "Problem" },
  { segment: "solution", label: "Solution" },
  { segment: "editorial", label: "Editorial" },
] as const;
export type ProblemView = (typeof problemViews)[number];

export async function getWeeklyProblems() {
  const entries = await getCollection("weeklyProblems");
  return entries.sort((a, b) => b.data.date.getTime() - a.data.date.getTime() || a.id.localeCompare(b.id));
}

export async function getWeeklyProblemPaths() {
  const problems = await getWeeklyProblems();
  return problems.flatMap(entry => problemViews.map(view => ({
    params: { slug: entry.id, view: view.segment || undefined },
    props: { entry, view },
  })));
}

export function problemHref(id: string, segment: ProblemView["segment"] = "") {
  const base = `/pow/${id}/`;
  return segment ? base + segment + "/" : base;
}

export function problemMarkdownHref(id: string, segment: ProblemView["segment"] = "") {
  return problemHref(id, segment) + "index.md";
}

const dateFormat = new Intl.DateTimeFormat("en-AU", {
  day: "numeric", month: "long", year: "numeric", timeZone: "UTC",
});

export function formatProblemDate(date: Date) {
  return dateFormat.format(date);
}
