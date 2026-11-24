import type { APIRoute, InferGetStaticPropsType } from "astro";
import { formatProblemDate, getWeeklyProblemPaths, problemMarkdownHref, problemViews } from "@/lib/weekly-problems";

export const prerender = true;
export const getStaticPaths = getWeeklyProblemPaths;

export const GET: APIRoute<InferGetStaticPropsType<typeof getStaticPaths>> = ({ props, site, url }) => {
  const { entry, view } = props;
  const { data } = entry;
  const body = { "": data.statement, solution: data.solution, editorial: entry.body }[view.segment];
  if (!body) throw new Error(`Missing ${view.label} Markdown for ${entry.id}`);

  const sections = [
    `# ${data.title}`,
    `${view.label} · ${formatProblemDate(data.date)} · [${data.sourceLabel}](${data.source})`,
  ];
  if (view.segment === "") {
    sections.push(`${data.topic} · Difficulty ${data.difficulty}/10 · ${data.estimatedTime} min`);
  }
  sections.push(body);
  if (view.segment && data.referenceCode) {
    const code = data.referenceCode.endsWith("\n") ? data.referenceCode : data.referenceCode + "\n";
    sections.push("## C++ implementation", "```cpp\n" + code + "```");
  }
  const related = problemViews.filter(other => other.segment !== view.segment).map(other => {
    const href = new URL(problemMarkdownHref(entry.id, other.segment), site ?? url);
    return `[${other.label}](${href.href})`;
  });
  sections.push(related.join(" · "));

  return new Response(sections.join("\n\n") + "\n", {
    headers: { "Content-Type": "text/markdown; charset=utf-8" },
  });
};
