"""Read the active book in TeX input order and adapt its editorial markup for Pandoc."""

from collections import Counter
from pathlib import Path
import re


INPUT = re.compile(r"\\input\s*\{([^{}]+)\}")
LABEL = re.compile(r"\\label\s*\{([^{}]+)\}")
RESULTS = "theorem|lemma|proposition|corollary|definition|example|remark|exercise"
RESULT = re.compile(r"\\begin\{(" + RESULTS + r")\}(?:\[([^\]]*)\])?")
RESTATEMENT = re.compile(
    r"\\solutionheading\{([^{}]+)\}\s*\\begin\{restatedproblem\}\s*"
    r"\\input\{([^{}]+)\}\s*\\end\{restatedproblem\}\s*\\input\{([^{}]+)\}"
)


def uncomment(text):
    return re.sub(r"\\[%\\]|%[^\n]*(?:\n|$)", lambda m: "" if m[0].startswith("%") else m[0], text)


def group(text, start):
    """Read one balanced TeX argument, including nested math and escaped braces."""
    if text[start:start + 1] != "{":
        raise ValueError(f"Expected a braced argument near {text[start:start + 60]!r}")
    depth = 0
    for m in re.finditer(r"\\.|[{}]", text[start:], re.S):
        if m[0] == "{":
            depth += 1
        elif m[0] == "}":
            depth -= 1
            if depth == 0:
                end = start + m.end()
                return text[start + 1:end - 1], end
    raise ValueError(f"Unclosed argument near {text[start:start + 60]!r}")


def command(text, name, nargs, convert, optional=False):
    pattern = re.compile(r"\\" + name + r"(?![a-zA-Z@])\s*" + (r"(?:\[[^\]]*\]\s*)?" if optional else ""))
    output, end = [], 0
    for match in pattern.finditer(text):
        if match.start() < end:
            continue
        output.append(text[end:match.start()])
        end = match.end()
        args = []
        for _ in range(nargs):
            while end < len(text) and text[end].isspace():
                end += 1
            arg, end = group(text, end)
            args.append(arg)
        output.append(convert(*args))
    return "".join(output) + text[end:]


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def notation(book):
    return "\n".join(re.findall(r"^\\newcommand\{\\[A-Z]\}\{[^\n]+\}$",
                                (book / "macros.tex").read_text(), re.M))


def instrument(book):
    """Give even unlabelled results the book's actual TeX counter in the scratch copy."""
    for area in ("sections", "problems"):
        for path in (book / area).rglob("*.tex"):
            source = uncomment(path.read_text())
            def number(match):
                if LABEL.match(source[match.end():].lstrip()):
                    return match[0]
                key = f"web:{path.relative_to(book).with_suffix('').as_posix()}:{match.start()}"
                return match[0] + r"\label{" + key + "}"
            path.write_text(RESULT.sub(number, source))


def tex_labels(aux):
    labels = {}
    for line in aux.read_text().splitlines():
        if not line.startswith(r"\newlabel{"):
            continue
        key, end = group(line, len(r"\newlabel"))
        fields, _ = group(line, end)
        values = []
        end = 0
        while end < len(fields) and fields[end] == "{":
            value, end = group(fields, end)
            values.append(value)
        if len(values) >= 4:
            labels[key] = (values[0], values[2], values[3].split(".")[0])
    return labels


def chapter_pages(toc):
    """Index the finished print contents by numbered destination or unnumbered title."""
    pages = {}
    for line in toc.read_text().splitlines():
        start = re.match(r"\\contentsline\s*\{chapter\}\s*", line)
        if start:
            title, end = group(line, start.end())
            page, end = group(line, end)
            destination, _ = group(line, end)
            key = destination if title.startswith(r"\numberline") else title
            pages[key] = page
    return pages


def printed_list(book, suffix, kind, labels):
    """Use TeX's actual lists. A Tufte label can contain a deferred caption macro."""
    keys = {number: key for key, (number, _, label_kind) in labels.items() if label_kind == kind}
    items = []
    prefix = re.compile(r"\\contentsline\s*\{" + kind + r"\}")
    for line in (book / f"main.{suffix}").read_text().splitlines():
        match = prefix.match(line)
        if match:
            entry, _ = group(line, match.end())
            counter = re.match(r"\\numberline\s*", entry)
            number, end = group(entry, counter.end())
            caption = entry[end:].strip()
            if caption.startswith("{"):
                caption, _ = group(caption, 0)
            caption = caption.removeprefix(r"\ignorespaces").lstrip()
            if number not in keys:
                raise ValueError(f"Missing manuscript label for {kind} {number}")
            items.append((keys[number], caption))
    return items


class Manuscript:
    def __init__(self, book, labels):
        self.book = book
        self.labels = labels
        self.markers = []
        self.figures = {}
        self.problems = {}
        self.placements = Counter()
        self.restatements = Counter()
        self.stack = []
        self.main = uncomment((book / "main.tex").read_text())
        self.assignments = {}
        for hw in sorted((book / "problems").glob("hw[0-9][0-9].tex")):
            inputs = map(Path, INPUT.findall(uncomment(hw.read_text())))
            problem_paths = (p.with_suffix("").as_posix() for p in inputs if p.stem == "problem")
            for number, path in enumerate(problem_paths, 1):
                if path in self.assignments:
                    raise ValueError(f"Repeated handout problem {path}")
                self.assignments[path] = (hw.stem, number)

    def marker(self, kind, value, inline=False):
        index = len(self.markers)
        self.markers.append((kind, value))
        token = rf"\xyzweb{{{index}}}"
        return token if inline else "\n\n" + token + "\n\n"

    def source_path(self, name):
        path = (self.book / name).resolve()
        if not path.is_relative_to(self.book) or not path.is_file():
            raise ValueError(f"Missing or external manuscript input {name!r} in {self.stack}")
        return path

    def reference(self, key):
        if key not in self.labels:
            raise ValueError(f"Unresolved manuscript reference {key}")
        number, title, kind = self.labels[key]
        kind = {"section": "§", "subsection": "§", "appendix": "Appendix"}.get(kind, kind.title())
        text = (kind + " " + number).strip() if number else title
        return rf"\hyperlink{{{key}}}{{{text}}}"

    def problem(self, name):
        path = Path(name).with_suffix("").as_posix()
        original = self.source_path(path + ".tex").read_text()
        labels = [key for key in LABEL.findall(original) if key.startswith("ex:")]
        if len(labels) != 1:
            raise ValueError(f"Expected one stable exercise label in {name}")
        key = labels[0][3:]
        if re.findall(r"\\solutionlink\{([^{}]+)\}", original) != [key]:
            raise ValueError(f"Solution link disagrees with exercise {key}")
        record = self.problems.get(key)
        if record and record["source"] != path:
            raise ValueError(f"Duplicate exercise key {key}")
        if not record:
            environment = RESULT.search(original)
            assignment, number = self.assignments.get(path, (None, None))
            if path.startswith("problems/hw") and not assignment:
                raise ValueError(f"Exercise {path} has no handout placement")
            record = dict(key=key, source=path, assignment=assignment, question=number,
                          number=self.labels[labels[0]][0], title=environment[2] or "Exercise")
            self.problems[key] = record
        return record

    def restate(self, match):
        key, statement, solution = match.groups()
        record = self.problem(statement)
        if record["key"] != key or Path(solution).with_suffix("") != Path(record["source"]).with_name("solution"):
            raise ValueError(f"Appendix sources disagree for {key}")
        self.restatements[key] += 1
        return (self.marker("solution", key) + self.expand(solution) + self.marker("end", key))

    def register_figure(self, path):
        if path.stem in self.figures and self.figures[path.stem] != path:
            raise ValueError(f"Ambiguous figure name {path.stem}")
        self.figures[path.stem] = path

    def include(self, match):
        name = Path(match[1]).with_suffix("").as_posix()
        if name.startswith("figures/"):
            path = self.source_path(name + ".tex")
            self.register_figure(path)
            return rf"\includegraphics{{/notes/linear-algebra/figures/{path.stem}.svg}}"
        if Path(name).name == "problem":
            key = self.problem(name)["key"]
            self.placements[key] += 1
            return self.marker("statement", key) + self.expand(name) + self.marker("end", key)
        return self.expand(name)

    def expand(self, name):
        path = self.source_path(str(Path(name).with_suffix(".tex")))
        if path in self.stack:
            raise ValueError(f"Cyclic input {self.stack + [path]}")
        self.stack.append(path)
        text = uncomment(path.read_text())
        text = re.sub(r"\\(?:begingroup|endgroup|raggedbottom)\b", "", text)
        if name == "sections/front-matter/copyright":
            text = r"\chapter*{Copyright}" + "\n" + text
        # Transform this file before expanding its inputs. The scratch TeX snapshot
        # supplies the same numbering used in print, including unlabelled results.
        text = RESTATEMENT.sub(self.restate, text)
        text = INPUT.sub(self.include, text)
        self.stack.pop()
        return text

    def prepare(self):
        body = self.main.split(r"\begin{document}", 1)[1].split(r"\end{document}", 1)[0]
        text = INPUT.sub(self.include, body)
        for key in self.problems:
            if self.placements[key] != 1 or self.restatements[key] != 1:
                raise ValueError(f"Expected one chapter placement and one appendix restatement for {key}")
        missing = self.assignments.keys() - {record["source"] for record in self.problems.values()}
        if missing:
            raise ValueError(f"Handout problems missing from the book: {', '.join(sorted(missing))}")
        # Pandoc reads standard LaTeX. Adapt only the book's structure and print conventions.
        text = re.sub(r"\\part(\*?)\{([^{}]+)\}\s*(?:\\label\{([^{}]+)\})?",
                      lambda m: self.marker("part", (m[2], m[3])), text)
        text = re.sub(r"\\printbibliography(?:\[[^\]]*\])?", lambda _: r"\chapter*{References}" +
                      self.marker("references", ""), text)
        for cmd, title, kind, suffix in (("listoffigures", "List of figures", "figure", "lof"),
                                         ("listoftables", "List of tables", "table", "lot"),
                                         ("listoftheorems", "List of theorems", "theorem", "loe")):
            if "\\" + cmd not in text:
                continue
            items = [r"\item " + self.reference(key) + " " + caption
                     for key, caption in printed_list(self.book, suffix, kind, self.labels)]
            text = text.replace("\\" + cmd, rf"\chapter*{{{title}}}" + "\n\\begin{itemize}\n" +
                                "\n".join(items) + "\n\\end{itemize}\n")
        text = re.sub(r"\\(?:frontmatter|mainmatter|backmatter|appendix|maketitle|tableofcontents)\b", "", text)
        text = command(text, "addcontentsline", 3, lambda *_: "")
        text = re.sub(r"\\newcommand\{\\(?:formulagroup|notationmeaning)\}\[\d+\]\s*",
                      r"\\xyzdefinition", text)
        text = command(text, "xyzdefinition", 1, lambda _: "")
        text = command(text, "formulagroup", 2, lambda title, key: "\n\n" + rf"\textbf{{{title}}} " +
                       self.reference(key) + "\n\n")
        text = command(text, "notationmeaning", 1, lambda body: body)
        text = command(text, "handoutonly", 1, lambda _: "")
        text = command(text, "solutionlink", 1, lambda _: "")
        text = command(text, "marginnote", 1, lambda body: rf"\footnote{{{body}}}", optional=True)
        text = command(text, "sidenote", 1, lambda body: rf"\footnote{{{body}}}", optional=True)
        text = command(text, "autoref", 1, self.reference)
        text = command(text, "autopageref", 1, lambda key: rf"\hyperlink{{{key}}}{{the linked page}}")
        text = command(text, "pendingreviewtext", 1, lambda body: r"\textcolor{pendingreviewcolor}{" + body + "}")
        text = re.sub(r"\\begin\{pendingreview\}", lambda _: self.marker("open", ("div", {"class": "pending-review"})), text)
        text = text.replace(r"\end{pendingreview}", self.marker("close", ""))
        text = re.sub(r"\\begin\{marginfigure\}(?:\[[^\]]*\])?", lambda _:
                      self.marker("open", ("div", {"class": "margin-figure"})) + r"\begin{figure}", text)
        text = text.replace(r"\end{marginfigure}", r"\end{figure}" + self.marker("close", ""))
        text = text.replace("{figure*}", "{figure}")
        text = re.sub(r"\\(?:begin|end)\{(?:fullwidth|samepage)\}|\\begin\{multicols\}\{\d+\}|\\end\{multicols\}", "", text)
        text = re.sub(r"\\(?:begingroup|endgroup|raggedcolumns|raggedbottom|columnbreak|newpage|clearpage|nopagebreak|nobreak|vfill|null|smallskip|small|noindent|centering)\b", "", text)
        text = re.sub(r"\\titlespacing\*?\{[^{}]*\}(?:\{[^{}]*\}){3}", "", text)
        text = command(text, "setlength", 2, lambda *_: "")
        text = command(text, "thispagestyle", 1, lambda _: "")
        text = re.sub(r"\\renewcommand\{\\arraystretch\}\{[^}]*\}", "", text)
        text = text.replace(r"\the\year", " " + self.year).replace(r"\monthyear", self.print_date)
        for control, field in (("thanklessauthor", "author"), ("thanklesspublisher", "publisher")):
            value = re.search(r"\\" + field + r"\{([^{}]+)\}", self.main)[1]
            text = text.replace("\\" + control, value)
        text = re.sub(r"\\par\b", "\n\n", text)
        text = command(text, "smallcaps", 1, lambda value: value)
        text = re.sub(r"\\includegraphics(?:\[[^\]]*\])?\{([^{}]+)\}", self.image, text)
        text = self.result_environments(text)
        text = re.sub(r"\\begin\{equation\}(.*?)\\end\{equation\}", self.equation, text, flags=re.S)
        text = self.enumerations(text)
        return notation(self.book) + "\n" + text

    def result_environments(self, text):
        # Shared exercises get their heading from the collection, in each of its views.
        shared = re.compile(r"\\begin\{exercise\}(?:\[[^\]]*\])?\s*\\label\{ex:([^{}]+)\}(.*?)\\end\{exercise\}", re.S)
        text = shared.sub(lambda m: m[2] if m[1] in self.problems else m[0], text)
        pattern = re.compile(RESULT.pattern + r"\s*\\label\{([^{}]+)\}")
        def begin(match):
            env, title, key = match.groups()
            number = self.labels[key][0]
            head = env.title() + " " + number + (f" ({title})" if title else "")
            return self.marker("open", ("div", {"class": f"result {env}", "id": key})) + rf"\textbf{{{head}.}} "
        text = pattern.sub(begin, text)
        return re.sub(r"\\end\{(?:" + RESULTS + r")\}", lambda _: self.marker("close", ""), text)

    def equation(self, match):
        key = LABEL.search(match[1])
        if not key:
            return match[0]
        body = LABEL.sub("", match[1]).rstrip()
        if not re.search(r"\\tag\*?\s*\{", body):
            body += rf"\tag{{{self.labels[key[1]][0]}}}"
        return (self.marker("open", ("div", {"class": "equation", "id": key[1]})) +
                r"\[" + body + r"\]" + self.marker("close", ""))

    def image(self, match):
        source = match[1]
        if source.startswith("/notes/linear-algebra/figures/"):
            return match[0]
        name = Path(source)
        extensions = (".pdf", ".png", ".jpg", ".jpeg", ".svg", ".webp")
        candidates = [name] if name.suffix else [name.with_suffix(ext) for ext in extensions]
        paths = [folder / candidate for folder in (Path(), Path("figures")) for candidate in candidates
                 if candidate.suffix in extensions]
        found = next((path for path in paths if (self.book / path).is_file()), None)
        if found is None:
            raise ValueError(f"Missing or unsupported manuscript graphic {source}")
        path = self.source_path(found)
        self.register_figure(path)
        name = path.stem + ".svg" if path.suffix == ".pdf" else path.name
        return rf"\includegraphics{{/notes/linear-algebra/figures/{name}}}"

    def enumerations(self, text):
        # The Tufte class uses two optional arguments, e.g. [({A}1)][4].
        # Preserve the displayed item identities, including homework subparts.
        lists = "enumerate|itemize|description"
        pat = re.compile(r"\\begin\{(" + lists + r")\}(?:\[([^\]]*)\]\[\d+\])?|\\end\{(" + lists + r")\}|\\item\b")
        stack = []
        def item(match):
            if match[1]:
                style = match[2] if match[1] == "enumerate" else None
                stack.append([style, 0])
                return self.marker("open", ("list", {})) + r"\begin{enumerate}" if style else match[0]
            if match[3]:
                style, _ = stack.pop()
                return r"\end{enumerate}" + self.marker("close", "") if style else match[0]
            if not stack or not stack[-1][0]:
                return match[0]
            style, n = stack[-1]
            stack[-1][1] += 1
            label = re.sub(r"\{([^}]+)\}|[1a]", lambda m: m[1] if m[1] else
                           (str(n + 1) if m[0] == "1" else chr(97 + n)), style)
            return rf"\item \textbf{{{label}}} "
        return pat.sub(item, text)
