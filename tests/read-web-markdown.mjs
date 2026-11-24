import { readFileSync } from "node:fs";
import { markdownToMdast } from "satteri";
import { createNoteRenderer, portableMarkdown } from "../src/lib/note-markdown.mjs";

// Inspect the committed fragments independently of Astro's content store.
const render = createNoteRenderer();
const placement = () => ({ html: "", markdown: "" });
function equations(node, result) {
  if (node.type === "math" || node.type === "inlineMath") result.push([node.type === "math", node.value]);
  node.children?.forEach(child => equations(child, result));
  return result;
}
const notes = JSON.parse(readFileSync(0, "utf8"));
const results = notes.map(markdown => process.argv[2] === "equations"
  ? equations(markdownToMdast(markdown, { features: { math: true, gfm: true } }), [])
  : [render(markdown, placement), portableMarkdown(markdown, "https://xyzmaths.org", placement)]);
process.stdout.write(JSON.stringify(results));
