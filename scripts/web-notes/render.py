"""Write the annotated Pandoc document as Markdown and resolve its book-wide references."""

from collections import Counter
from html import escape, unescape
import json
from pathlib import Path
import re
import subprocess

from manuscript import slug


BASE = "/notes/linear-algebra/"
MARKDOWN_WRITER = ["-f", "json", "-t", "gfm+attributes-tex_math_gfm", "--wrap=none"]


def plain(node):
    if isinstance(node, list):
        return "".join(plain(child) for child in node)
    if not isinstance(node, dict) or "t" not in node:
        return ""
    kind, value = node["t"], node.get("c")
    if kind == "Str":
        return value
    if kind in ("Space", "SoftBreak", "LineBreak"):
        return " "
    if kind in ("Math", "Code"):
        return value[1]
    if kind in ("Link", "Span", "Cite"):
        return plain(value[1])
    return plain(value)


def attributes(values):
    fields = [f'{key}="{escape(str(value), quote=True)}"' for key, value in values.items() if value]
    return "{" + " ".join(fields) + "}" if fields else ""


def properties(attr):
    identifier, classes, pairs = attr
    return {"id": identifier, "class": " ".join(classes), **dict(pairs)}


def raw(kind, text):
    return {"t": kind, "c": ["markdown", text]}


def escape_table_math(node):
    """A Markdown table delimiter must never split a TeX expression into two cells."""
    if isinstance(node, list):
        for child in node:
            escape_table_math(child)
    elif isinstance(node, dict) and "c" in node:
        if node["t"] == "Math":
            def escape_bar(match):
                slashes = match[1]
                if len(slashes) % 2:
                    # TeX's double bar has a spelling without a GFM column delimiter.
                    following = match.string[match.end():match.end() + 1]
                    return slashes[:-1] + r"\Vert" + (" " if following.isalpha() else "")
                return slashes + r"\|"
            node["c"][1] = re.sub(r"(\\*)\|", escape_bar, node["c"][1])
        else:
            escape_table_math(node["c"])


def pandoc(binary, args, source):
    proc = subprocess.run([binary, *args], input=source, text=True, capture_output=True)
    if proc.returncode or proc.stderr.strip():
        raise ValueError(f"Pandoc {' '.join(args)}\n{proc.stderr.strip()}")
    return proc.stdout


def render(book, binary, pagination):
    tex = book.prepare()
    tikz_images = {BASE + "figures/" + name + ".svg"
                   for name, path in book.figures.items() if path.suffix == ".tex"}
    document = json.loads(pandoc(binary, ["-f", "latex+raw_tex", "-t", "json", "--citeproc",
        "--bibliography", str(book.book / "bibliography.bib"), "-M", "link-citations=true"], tex))
    equations = Counter()
    def collect_math(node):
        if isinstance(node, list):
            for child in node:
                collect_math(child)
        elif isinstance(node, dict):
            if node.get("t") == "Math":
                mode, source = node["c"]
                equations[(mode["t"], source)] += 1
            elif node.get("t") in ("Figure", "Table"):
                # Only the long caption appears with the figure or table.
                collect_math(node["c"][1][1])
                collect_math(node["c"][2:])
            elif node.get("t") == "Cite":
                collect_math(node["c"][1])
            elif node.get("t") == "Image":
                return  # The image description is plain text.
            else:
                for child in node.values():
                    collect_math(child)
    collect_math(document["blocks"])
    def control(index):
        return raw("RawBlock", f"<!--xyz-web:{index}-->")

    def marker(kind, value):
        index = len(book.markers)
        book.markers.append((kind, value))
        return control(index)

    def number_caption(key, caption):
        if key in book.labels and caption[1] and caption[1][0]["t"] in ("Plain", "Para"):
            number, _, kind = book.labels[key]
            label = {"t": "Str", "c": f"{kind.title()} {number}."}
            caption[1][0]["c"][:0] = [label, {"t": "Space"}]

    def adapt(node):
        if isinstance(node, list):
            result = []
            for item in node:
                adapted = adapt(item)
                result.extend(adapted if isinstance(adapted, tuple) else (adapted,))
            return result
        if not isinstance(node, dict) or "c" not in node:
            return node
        kind, value = node["t"], node["c"]
        if kind == "Str" and re.search(r":(?=[A-Za-z0-9])", value):
            # An ordinary colon in prose or image alt text can resemble a Markdown directive.
            words = re.split(r"(:)(?=[A-Za-z0-9])", value)
            return tuple(raw("RawInline", r"\:") if w == ":" else {"t": "Str", "c": w} for w in words if w)
        if kind == "Note":
            nonlocal note_number
            note_number += 1
            label = f"[^{note_number}]"
            notes.append((label, adapt(value)))
            return raw("RawInline", label)
        if kind in ("Para", "Plain") and any(i["t"] == "Math" and i["c"][0]["t"] == "DisplayMath" for i in value):
            blocks, run = [], []
            for item in value:
                if item["t"] == "Math" and item["c"][0]["t"] == "DisplayMath":
                    if run:
                        blocks.append({"t": kind, "c": adapt(run)})
                    blocks.append(raw("RawBlock", "$$\n" + item["c"][1].strip("\n") + "\n$$"))
                    run = []
                else:
                    run.append(item)
            if run:
                blocks.append({"t": kind, "c": adapt(run)})
            return tuple(blocks)
        if kind == "Header" and value[1][0] in book.labels and "unnumbered" not in value[1][1]:
            number, _, level = book.labels[value[1][0]]
            if number and level in ("chapter", "appendix", "section", "subsection", "subsubsection"):
                prefix = f"{level.title()} {number}." if level in ("chapter", "appendix") else number
                value[2][:0] = [{"t": "Str", "c": prefix}, {"t": "Space"}]
        if kind == "Header" and 2 <= value[0] <= 6:
            outline.append({"id": value[1][0], "title": plain(value[2]), "level": value[0]})
        if kind == "Header":
            # An implicit Markdown slug can differ between renderers. Always publish TeX's anchor.
            attrs = attributes(properties(value[1]))
            return {"t": kind, "c": [value[0], ["", [], []], [*adapt(value[2]), raw("RawInline", " " + attrs)]]}
        if kind in ("RawBlock", "RawInline") and value[0] in ("latex", "tex"):
            mark = re.fullmatch(r"\\xyzweb\{(\d+)\}", value[1].strip())
            if mark:
                return raw(kind, control(int(mark[1]))["c"][1])
            label = re.fullmatch(r"\\label\{([^{}]+)\}", value[1].strip())
            if label:
                anchor = attributes({"id": label[1]})
                return raw(kind, ("::anchor" if kind == "RawBlock" else ":anchor[]") + anchor)
            raise ValueError(f"Unconverted LaTeX {kind}: {value[1][:400]}")
        if kind == "Image":
            alt = "Creative Commons BY-NC-ND" if value[2][0].endswith("/cc-by-nc-nd.svg") else plain(value[1])
            # Pandoc's GFM alt-text writer drops literal TeX braces. Escape
            # the caption as ordinary Markdown text and let Pandoc write the URL.
            alt = re.sub(r"([\\\[\]*_`$:{}<>|])", r"\\\1", alt)
            return {"t": kind, "c": [value[0], [raw("RawInline", alt)], value[2]]}
        if kind == "Figure":
            caption = plain(value[1][1])
            def figure_image(item, linked=False):
                if isinstance(item, list):
                    return [figure_image(child, linked) for child in item]
                if not isinstance(item, dict) or "c" not in item:
                    return item
                if item["t"] != "Image":
                    return {**item, "c": figure_image(item["c"], linked or item["t"] == "Link")}
                attrs, alt, (src, _) = item["c"]
                if not alt:
                    alt.append({"t": "Str", "c": caption})
                if src in tikz_images:
                    attrs[1].append("tikz-diagram")
                    if not linked:
                        link_attrs = ["", ["diagram-link"], [["data-astro-reload", ""]]]
                        return {"t": "Link", "c": [link_attrs, [item], [src, "Open original SVG"]]}
                return item
            value[2] = figure_image(value[2])
            number_caption(value[0][0], value[1])
            return (marker("open", ("figure", properties(value[0]))), *adapt(value[2]),
                    marker("open", ("figcaption", {})), *adapt(value[1][1]),
                    marker("close", ""), marker("close", ""))
        if kind == "Div" and value[0][0] in book.labels and book.labels[value[0][0]][2] == "table":
            for block in value[1]:
                if block["t"] == "Table":
                    number_caption(value[0][0], block["c"][1])
        if kind == "Table":
            number_caption(value[0][0], value[1])
            caption = adapt(value[1][1])
            widths = [str(round(100 * col[1].get("c", 0))) for col in value[2]]
            escape_table_math(value[3:])
            table = {"t": "Table", "c": [value[0], [None, []], *adapt(value[2:])]}
            return (marker("open", ("tabular", {"widths": ",".join(widths)})),
                    marker("open", ("caption", {})), *caption, marker("close", ""),
                    table, marker("close", ""))
        if kind == "Div":
            return (marker("open", ("div", properties(value[0]))), *adapt(value[1]), marker("close", ""))
        if kind == "Cite":
            return tuple(adapt(value[1]))
        if kind == "Span":
            for pair in value[0][2]:
                if pair[0] == "style" and "pendingreviewcolor" in pair[1]:
                    value[0][1].append("pending-review")
                    value[0][2].remove(pair)
            attrs = attributes(properties(value[0]))
            body = adapt(value[1])
            return (raw("RawInline", ":span["), *body, raw("RawInline", "]" + attrs)) if attrs else tuple(body)
        return {"t": kind, "c": adapt(value)}

    blocks = []
    bibliography = None
    outline = []
    note_number = note_group = 0
    for block in document["blocks"]:
        if block["t"] == "Div" and block["c"][0][0] == "refs":
            bibliography = block
            continue
        if block["t"] == "Header" and block["c"][0] == 1:
            _, attr, title = block["c"]
            outline = []
            blocks.append(marker("page", (attr[0], plain(title), outline)))
        notes = []
        blocks.extend(adapt([block]))
        if notes:
            # Keep notes after the same manuscript block, even when a paragraph
            # is split around displays. One block can own several margin notes.
            note_group += 1
            identifier = "footnotes" if note_group == 1 else f"footnotes-{note_group}"
            blocks.append(marker("open", ("notes", {"id": identifier})))
            for label, body in notes:
                content = pandoc(binary, MARKDOWN_WRITER, json.dumps({**document, "blocks": body})).strip()
                blocks.append(raw("RawBlock", label + ": " + content.replace("\n", "\n    ")))
            blocks.append(marker("close", ""))
    for i, block in enumerate(blocks):
        if block["t"] == "RawBlock" and block["c"][1].startswith("<!--xyz-web:"):
            index = int(re.search(r":(\d+)", block["c"][1])[1])
            if book.markers[index][0] == "references":
                if not bibliography:
                    raise ValueError("Missing Pandoc bibliography")
                blocks[i:i+1] = adapt([bibliography])
    document["blocks"] = blocks
    markdown = pandoc(binary, MARKDOWN_WRITER, json.dumps(document))
    pages = partition(markdown, book, pagination)
    bodies = ["\n\n".join(block.get("markdown", "") for block in page["blocks"]) for page in pages]
    bodies.extend(record[field] for record in book.problems.values() for field in ("statement", "solution"))
    audit = {"equations": [(mode, tex, count) for (mode, tex), count in equations.items()], "bodies": bodies}
    proc = subprocess.run(["node", Path(__file__).with_name("math.mjs")], input=json.dumps(audit),
                          text=True, capture_output=True)
    if proc.returncode:
        raise ValueError(proc.stderr)
    return pages


def partition(markdown, book, pagination):
    group = "Front matter"
    part_id = None
    part = None
    pages = []
    page = active = None
    refs = {}
    statement_ids = {}

    def register(key, page_id):
        if key in refs:
            raise ValueError(f"Duplicate HTML anchor {key}")
        refs[key] = BASE + page_id + "/#" + key

    def append(fragment):
        content = fragment.strip()
        if not content:
            return
        if not page:
            raise ValueError(f"Content before first web page: {content[:160]}")
        ids = [unescape(k) for k in re.findall(r'\{id="([^"]+)"', content)]
        for key in ids:
            register(key, page["id"])
        if active:
            field, key = active
            if field == "statement":
                statement_ids.setdefault(key, set()).update(ids)
            record = book.problems[key]
            record[field] = record.get(field, "") + content + "\n\n"
        else:
            page["blocks"].append({"markdown": content})

    pieces = re.split(r"<!--xyz-web:(\d+)-->", markdown)
    events = [(book.markers[int(index)], fragment) for index, fragment in zip(pieces[1::2], pieces[2::2])]
    # Markdown container directives use a longer fence around nested directives.
    fences, stack = {}, []
    for pos, ((kind, _), _) in enumerate(events):
        if kind == "open":
            stack.append(pos)
            fences[pos] = 3
        elif kind == "close":
            fences[pos] = fences[stack.pop()]
            if stack:
                fences[stack[-1]] = max(fences[stack[-1]], fences[pos] + 1)
    if stack:
        raise ValueError("Unclosed manuscript container")
    append(pieces[0])
    for pos, ((kind, value), fragment) in enumerate(events):
        if kind == "open":
            tag, attrs = value
            # Keep the identifier first, including for manuscript-defined result environments.
            append(":" * fences[pos] + tag + attributes({"id": attrs.get("id"), **attrs}))
        elif kind == "close":
            append(":" * fences[pos])
        elif kind == "part":
            group, part_id = value
            number = book.labels[part_id][0] if part_id in book.labels else ""
            part = f"Part {number} · {group}" if number else None
        elif kind == "page":
            label, title, outline = value
            name = slug(label.split(":")[-1])
            group_name = "References" if title == "References" else group
            page_id = "references" if title == "References" else slug(group_name) + "/" + name
            number, _, level = book.labels.get(label, ("", "", ""))
            print_key = f"{level}.{number}" if number else title
            if title == "References":
                print_key = "Bibliography"
            page = dict(id=page_id, title=title, group=group_name, order=len(pages),
                        part=part, page=pagination.get(print_key), outline=outline, blocks=[])
            if any(p["id"] == page_id for p in pages):
                raise ValueError(f"Duplicate page {page_id}")
            pages.append(page)
            if part_id:
                append("::anchor" + attributes({"id": part_id}))
                part_id = None
        elif kind in ("statement", "solution"):
            if active or not page:
                raise ValueError(f"Nested or unplaced exercise {value}")
            active = (kind, value)
            page["blocks"].append({kind: value})
            key = ("ex:" if kind == "statement" else "sol:") + value
            register(key, page["id"])
            book.problems[value][kind + "Page"] = page["id"]
        elif kind == "end":
            if not active or active[1] != value:
                raise ValueError(f"Invalid exercise boundary {value}")
            active = None
        else:
            raise ValueError(f"Unexpected content boundary {kind}")
        append(fragment)
    if active:
        raise ValueError(f"Unclosed exercise {active}")

    def link(fragment, local_ids=()):
        def target(match):
            key = unescape(match[1])
            if key in local_ids:
                return match[0]
            if key not in refs:
                raise ValueError(f"Unresolved Markdown link #{key}")
            return "](" + refs[key] + ")"
        return re.sub(r'\]\(#([^)]+)\)', target, fragment)

    for entry in pages:
        for block in entry["blocks"]:
            if "markdown" in block:
                block["markdown"] = link(block["markdown"])
    for record in book.problems.values():
        for field in ("statement", "solution"):
            if not record.get(field, "").strip():
                raise ValueError(f"Empty {field} for {record['key']}")
            # Footnotes and other anchors inside a shared statement travel with every copy.
            local_ids = statement_ids.get(record["key"], ()) if field == "statement" else ()
            record[field] = link(record[field], local_ids)
    return pages
