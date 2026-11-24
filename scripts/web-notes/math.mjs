import { readFileSync } from "node:fs";
import katex from "katex";

export const markdownFeatures = { math: true, attributes: true, directive: true, gfm: { footnotes: {} } };

export function renderEquation(tex, displayMode) {
  try {
    return katex.renderToString(tex, {
      output: "htmlAndMathml",
      displayMode,
      throwOnError: true,
      trust: false,
    });
  } catch (error) {
    throw new Error("Unable to render equation " + tex, { cause: error });
  }
}

if (import.meta.main) {
  const { markdownToMdast } = await import("satteri");
  const { equations, bodies } = JSON.parse(readFileSync(0, "utf8"));
  const remaining = new Map();
  function count(mode, tex, delta) {
    // A table uses the equivalent TeX command for a double bar to keep its columns intact.
    const key = mode + " " + tex.trim().replace(/\\(?:Vert(?![A-Za-z])|\|)[ \t]*/g, "\\|");
    remaining.set(key, (remaining.get(key) ?? 0) + delta);
  }
  for (const [mode, tex, occurrences] of equations) {
    renderEquation(tex, mode === "DisplayMath");
    count(mode, tex, occurrences);
  }
  function visit(node) {
    if (node.type === "math" || node.type === "inlineMath") {
      count(node.type === "math" ? "DisplayMath" : "InlineMath", node.value, -1);
    }
    node.children?.forEach(visit);
  }
  for (const markdown of bodies) visit(markdownToMdast(markdown, { features: markdownFeatures, position: false }));
  for (const [formula, delta] of remaining) {
    if (delta) throw new Error(`Markdown math parity failed (${Math.abs(delta)} ${delta > 0 ? "missing" : "extra"}): ${formula}`);
  }
}
