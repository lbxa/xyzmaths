import { defineMdastPlugin, hastToHtml, markdownToHast, markdownToMdast } from "satteri";
import { parse } from "yaml";
import { markdownFeatures as features, renderEquation } from "../../scripts/web-notes/math.mjs";
import { readerLinkStyle } from "./reader-links.ts";

const noteLinkClasses = readerLinkStyle.split(" ");

export function readNote(path, text) {
  const match = /^---\n([\s\S]*?)\n---\n/.exec(text);
  if (!match) throw new Error(`Missing Markdown frontmatter in ${path}`);
  return { attrs: parse(match[1]), markdown: text.slice(match[0].length).trim() };
}

function element(tagName, properties, children = []) {
  return { type: "element", tagName, properties, children };
}

function unwrapParagraph(node) {
  return node.children.length === 1 && node.children[0].tagName === "p"
    ? node.children[0].children : node.children;
}

// Preserve the reader's semantic HTML where Markdown has no native equivalent.
function bookElement(node) {
  if (!node.children) return node;
  node.children = node.children.flatMap(bookElement);
  if (node.tagName === "book-list") {
    const list = node.children.find(child => child.tagName === "ol");
    if (!list) throw new Error("A labelled book list must contain an ordered list");
    list.properties.className = ["book-list"];
    // A manuscript list can also own margin notes following its final item.
    return node.children;
  }
  if (node.tagName === "figcaption" || node.tagName === "caption") {
    node.children = unwrapParagraph(node);
  }
  if (node.tagName === "book-table") {
    const table = node.children.find(child => child.tagName === "table");
    const caption = node.children.find(child => child.tagName === "caption");
    if (!table || !caption) throw new Error("A book table requires a Markdown table and caption");
    const widths = node.properties.widths.split(",").map(Number);
    if (widths.some(Boolean)) {
      const columns = widths.map(width => element("col", width ? { style: `width: ${width}%` } : {}));
      table.children.unshift(element("colgroup", {}, columns));
    }
    table.children.unshift(caption);
    return table;
  }
  if (node.tagName === "book-note-ref") {
    const n = node.properties.number;
    return element("a", { href: `#fn${n}`, id: `fnref${n}`, className: ["footnote-ref", ...noteLinkClasses],
      role: "doc-noteref", ariaLabel: `Read margin note ${n}` },
      [element("sup", {}, [{ type: "text", value: n }])]);
  }
  if (node.tagName === "book-footnote") {
    const n = node.properties.number;
    const back = element("a", { href: `#fnref${n}`, className: ["footnote-back", ...noteLinkClasses],
      role: "doc-backlink", ariaLabel: `Return to reference ${n}` }, [{ type: "text", value: "↩︎" }]);
    const last = node.children.findLast(child => child.type !== "text" || child.value.trim());
    if (last?.tagName === "p") last.children.push(back);
    else node.children.push(back);
    return element("li", { id: `fn${n}`, value: Number(n), dataMarginNote: "" }, node.children);
  }
  if (node.tagName === "book-notes") {
    const items = node.children.filter(child => child.tagName === "li");
    if (!items.length) throw new Error("Missing Markdown footnote definition");
    const start = items[0].properties.value;
    return element("aside", { id: node.properties.id, className: ["footnotes", "footnotes-end-of-block"],
      role: "doc-footnote" }, [element("ol", { start }, items)]);
  }
  return node;
}

const containers = new Map([
  ["div", "div"], ["figure", "figure"], ["figcaption", "figcaption"],
  ["list", "book-list"], ["tabular", "book-table"], ["caption", "caption"], ["notes", "book-notes"],
]);

function directive(node, ctx) {
  const tag = node.name === "anchor" || node.name === "span" ? "span" : containers.get(node.name);
  if (!tag) throw new Error(`Unknown book Markdown directive ${node.name}`);
  ctx.setProperty(node, "data", { hName: tag, hProperties: node.attributes });
}

function missingPlacement(kind, key) {
  throw new Error(`Unexpected ${kind} placement for ${key}`);
}

function printMarginFigure(node) {
  return node?.type === "containerDirective" && node.name === "div" &&
    node.attributes?.class?.split(/\s+/).includes("margin-figure") &&
    node.children.length === 1 && node.children[0].type === "containerDirective" && node.children[0].name === "figure";
}

// Print floats can sit between a lead-in and its equation without interrupting
// either. On the web, put the equation first and retain the original figure text.
function placeInlineMarginFigures(markdown) {
  if (!markdown.includes("margin-figure")) return markdown;
  const edits = [];
  const layout = defineMdastPlugin({
    name: "xyz-maths-inline-figures", options: { position: true },
    containerDirective(figure, ctx) {
      if (!printMarginFigure(figure)) return;
      const siblings = ctx.parent(figure).children;
      const at = ctx.indexOf(figure);
      const lead = siblings[at - 1];
      if (lead?.type !== "paragraph") return;
      let last = at;
      while (printMarginFigure(siblings[last + 1])) last++;
      const display = siblings[last + 1];
      if (display?.type !== "math") return;
      const prose = ctx.textContent(lead).trimEnd();
      if (!prose || /[.!?…]["'”’)]*$/.test(prose)) return;
      const firstFigure = figure.position.start.offset;
      const endOfFigures = siblings[last].position.end.offset;
      const { start, end } = display.position;
      const gap = markdown.slice(endOfFigures, start.offset);
      edits.push([firstFigure, firstFigure, markdown.slice(start.offset, end.offset) + gap], [endOfFigures, end.offset]);
    },
  });
  markdownToMdast(markdown, { features, mdastPlugins: [layout] });
  return applyEdits(markdown, edits);
}

function applyEdits(markdown, edits) {
  let cursor = 0, out = "";
  for (const [start, end, value = ""] of edits.sort((a, b) => a[0] - b[0])) {
    if (start < cursor) throw new Error("Overlapping Markdown source ranges");
    out += markdown.slice(cursor, start) + value;
    cursor = end;
  }
  return out + markdown.slice(cursor);
}

export function createNoteRenderer() {
  const equations = new Map();
  function math(node, ctx) {
    const display = node.type === "math";
    const key = (display ? "display:" : "inline:") + node.value;
    if (!equations.has(key)) equations.set(key, renderEquation(node.value, display));
    ctx.replaceNode(node, { type: "html", value: equations.get(key) });
  }
  return function render(markdown, placement = missingPlacement) {
    markdown = placeInlineMarginFigures(markdown);
    const plugin = defineMdastPlugin({
      name: "xyz-maths-book",
      options: { position: true },
      math, inlineMath: math, containerDirective: directive,
      textDirective(node, ctx) {
        if (node.name === "span" || node.name === "anchor") directive(node, ctx);
        else ctx.replaceNode(node, { type: "text", value: markdown.slice(node.position.start.offset, node.position.end.offset) });
      },
      leafDirective(node, ctx) {
        if (node.name === "statement" || node.name === "solution") {
          ctx.replaceNode(node, { type: "html", value: placement(node.name, node.attributes.key).html });
        } else directive(node, ctx);
      },
      footnoteReference(node, ctx) {
        ctx.replaceNode(node, { type: "emphasis", data: { hName: "book-note-ref",
          hProperties: { number: node.identifier } }, children: [] });
      },
      footnoteDefinition(node, ctx) {
        ctx.replaceNode(node, { type: "blockquote", data: { hName: "book-footnote",
          hProperties: { number: node.identifier } }, children: node.children });
      },
    });
    return hastToHtml(bookElement(markdownToHast(markdown, { features, mdastPlugins: [plugin] })));
  };
}

// Remove reader-only annotations from their parsed source ranges. Keeping the
// original spelling of everything else preserves TeX, lists and pipe tables.
export function portableMarkdown(markdown, pageUrl, placement = missingPlacement) {
  markdown = placeInlineMarginFigures(markdown);
  const edits = [];
  function dropLine(start, end) {
    if (markdown[end] === "\n") end++;
    if (markdown[end] === "\n") end++;
    edits.push([start, end]);
  }
  function visit(node) {
    const start = node.position.start.offset;
    const end = node.position.end.offset;
    if (node.type === "containerDirective") {
      dropLine(start, markdown.indexOf("\n", start));
      dropLine(markdown.lastIndexOf("\n", end - 1) + 1, end);
    } else if (node.type === "leafDirective") {
      if (node.name === "anchor") dropLine(start, end);
      else edits.push([start, end, placement(node.name, node.attributes.key).markdown]);
      return;
    } else if (node.type === "textDirective" && ["span", "anchor"].includes(node.name)) {
      const first = node.children[0], last = node.children.at(-1);
      if (first) edits.push([start, first.position.start.offset], [last.position.end.offset, end]);
      else edits.push([start, end]);
    } else if (node.type === "heading" && node.data?.hProperties) {
      const suffix = /\s+\{[^{}\n]+\}$/.exec(markdown.slice(start, end));
      if (suffix) edits.push([start + suffix.index, end]);
    } else if (node.type === "link" || node.type === "image") {
      if (markdown[end] === "{" && node.data?.hProperties) {
        const attrs = /^\{[^{}\n]+\}/.exec(markdown.slice(end));
        if (attrs) edits.push([end, end + attrs[0].length]);
      }
      if (node.url.startsWith("#") || (node.url.startsWith("/") && !node.url.startsWith("//"))) {
        const target = markdown.lastIndexOf("](" + node.url, end);
        const destination = node.url.startsWith("#") ? pageUrl + node.url
          : pageUrl.startsWith("/") ? node.url : new URL(node.url, pageUrl).href;
        if (target >= start) edits.push([target + 2, target + 2 + node.url.length, destination]);
      }
    }
    node.children?.forEach(visit);
  }
  visit(markdownToMdast(markdown, { features }));
  return applyEdits(markdown, edits).trim() + "\n";
}
