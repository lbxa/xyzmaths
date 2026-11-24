"""Read the active book in TeX input order and adapt its editorial markup for Pandoc."""

from collections import Counter, defaultdict
from pathlib import Path
import re


INPUT = re.compile(r"\\input\s*\{([^{}]+)\}")
LABEL = re.compile(r"\\label\s*\{([^{}]+)\}")
RESULTS = "theorem|lemma|proposition|corollary|definition|property|example|remark|exercise"
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


def history(text):
    """Expand the shared historical-note macros, retaining captions, credits and review status."""
    for star in (r"\*", ""):
        def reviewed(body):
            return body if star else rf"\pendingreviewtext{{{body}}}"

        def portrait(people, key):
            images = " ".join(rf"\includegraphics[alt={{{name}}}]{{portraits/{file}.jpg}}" for file, name, _ in people)
            credits = ",".join([person[2] for person in people] + ["BookofproofsPortraits"])
            citation = rf"~\cite{{{credits}}}"
            if len(people) == 1:
                caption = people[0][1] + "." + citation
            else:
                caption = people[0][1] + " (left) and " + people[1][1] + " (right). Portrait sources" + citation + "."
            return rf"\begin{{marginfigure}}{images}\caption{{{reviewed(caption)}}}\label{{fig:portrait:{key}}}\end{{marginfigure}}"

        text = command(text, "historynote" + star, 1, lambda body: rf"\marginnote{{{reviewed(body)}}}")
        text = command(text, "historyportraitpair" + star, 7,
                       lambda *args: portrait((args[:3], args[3:6]), args[6]))
        text = command(text, "historyportrait" + star, 3,
                       lambda file, name, credit: portrait(((file, name, credit),), file))
    return text


class Manuscript:
    def __init__(self, book, labels, slug):
        self.book = book
        self.base = f"/notes/{slug}/"
        self.labels = labels
        self.markers = []
        self.figures = {}
        self.figure_settings = []
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
        name = path.stem if path.suffix in {".tex", ".pdf", ".svg"} else path.name
        if name in self.figures and self.figures[name] != path:
            raise ValueError(f"Ambiguous figure name {name}")
        self.figures[name] = path

    def include(self, match):
        name = Path(match[1]).with_suffix("").as_posix()
        if name.startswith("figures/"):
            path = self.source_path(name + ".tex")
            if r"\begin{tikzpicture}" not in uncomment(path.read_text()):
                relative = path.relative_to(self.book)
                if relative not in self.figure_settings:
                    self.figure_settings.append(relative)
                return ""
            self.register_figure(path)
            return rf"\includegraphics{{{self.base}figures/{path.stem}.svg}}"
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
        # These labels are local to the enclosing TeX group in an exercise or proof.
        def labelled_list(match):
            label = "a" if match[1] == "alph" else "i"
            return match[2].replace(r"\begin{enumerate}", rf"\begin{{enumerate}}[({label})][1]")
        text = re.sub(r"\\renewcommand\{\\labelenumi\}\{\(\\(alph|roman)\{enumi\}\)\}(.*?)\\endgroup",
                      labelled_list, text, flags=re.S)
        text = re.sub(r"\\(?:begingroup|endgroup|raggedbottom)\b", "", text)
        if name == "sections/front-matter/copyright":
            text = r"\chapter*{Copyright}" + "\n" + text
        # Transform this file before expanding its inputs. The scratch TeX snapshot
        # supplies the same numbering used in print, including unlabelled results.
        text = RESTATEMENT.sub(self.restate, text)
        text = INPUT.sub(self.include, text)
        self.stack.pop()
        return text

    def index(self, text):
        """Link the print index's page numbers to the occurrences in the reading edition."""
        if r"\printindex" not in text:
            return text
        printed = defaultdict(list)
        for key, page in re.findall(r"\\indexentry\{([^{}]+)\}\{([^{}]+)\}", (self.book / "main.idx").read_text()):
            printed[key.removesuffix("|hyperpage")].append(page)
        seen = Counter()
        terms = {}
        def occurrence(term):
            i = seen[term]
            seen[term] += 1
            anchor = f"index:{slug(term)}:{i + 1}"
            node = terms
            for part in term.split("!"):
                links, node = node.setdefault(part, ([], {}))
            links.append(rf"\hyperlink{{{anchor}}}{{{printed[term][i]}}}")
            return rf"\hypertarget{{{anchor}}}{{}}"
        text = command(text, "index", 1, occurrence)
        if seen != {term: len(pages) for term, pages in printed.items()}:
            raise ValueError("Web index occurrences differ from TeX's index")
        def listings(node):
            items = []
            for term, (links, children) in sorted(node.items(), key=lambda entry: entry[0].casefold()):
                items.append(r"\item " + term + (" " + ", ".join(links) if links else ""))
                if children:
                    items.append(listings(children))
            return "\n".join([r"\begin{itemize}", *items, r"\end{itemize}"])
        return text.replace(r"\printindex", self.marker("part", ("Back matter", None)) +
                            r"\chapter*{Index}" + "\n" + listings(terms))

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
        text = self.index(text)
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
        text = re.sub(r"\\ifdefined\s*\\standaloneformulasheet\b(.*?)\\fi\b",
                      lambda m: m[1].partition(r"\else")[2], text, flags=re.S)
        single_formula_group = r"\newcommand{\formulagroup}[1]" in text
        text = re.sub(r"\\newcommand\{\\(?:formulagroup|notationmeaning)\}\[\d+\]\s*",
                      r"\\xyzdefinition", text)
        text = command(text, "xyzdefinition", 1, lambda _: "")
        if single_formula_group:
            text = command(text, "formulagroup", 1, lambda title: "\n\n" + rf"\textbf{{{title}}}" + "\n\n")
        else:
            text = command(text, "formulagroup", 2, lambda title, key: "\n\n" + rf"\textbf{{{title}}} " +
                           self.reference(key) + "\n\n")
        text = command(text, "notationmeaning", 1, lambda body: body)
        text = command(text, "handoutonly", 1, lambda _: "")
        text = command(text, "solutionlink", 1, lambda _: "")
        text = history(text)
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
        text = re.sub(r"\\begin\{minipage\}\{\\linewidth\}((?:(?!\\end\{minipage\}).)*?)\\captionof\{figure\}(.*?)\\end\{minipage\}",
                      lambda m: r"\begin{figure}" + m[1] + r"\caption" + m[2] + r"\end{figure}", text, flags=re.S)
        text = re.sub(r"\\(?:begin|end)\{(?:fullwidth|samepage)\}|\\begin\{multicols\}\{\d+\}|\\end\{multicols\}", "", text)
        text = re.sub(r"\\(?:begingroup|endgroup|raggedcolumns|raggedbottom|columnbreak|newpage|clearpage|nopagebreak|nobreak|vfill|null|smallskip|footnotesize|small|noindent|centering|leavevmode|phantomsection)\b", "", text)
        text = re.sub(r"\\titleformat\{\\(?:chapter|section)\}(?:\[[^\]]*\])?", r"\\xyzformat", text)
        text = command(text, "xyzformat", 4, lambda *_: "")
        text = command(text, "Needspace", 1, lambda _: "")
        text = command(text, "newthought", 1, lambda body: rf"\textsc{{{body}}}")
        text = re.sub(r"\\postdisplaypenalty\s*=\s*[+-]?\d+", "", text)
        # Pandoc already emits the closing square at the end of the proof.
        text = re.sub(r"\\qedhere\b", "", text)
        text = re.sub(r"\\allowdisplaybreaks(?:\[\d+\])?", "", text)
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
        text = re.sub(r"\\includegraphics(\[[^\]]*\])?\{([^{}]+)\}", self.image, text)
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
        text = re.sub(r"\\begin\{conjecture\}(?:\[([^\]]*)\])?",
                      lambda m: self.marker("open", ("div", {"class": "result conjecture"})) +
                      r"\textbf{Conjecture" + (" (" + m[1] + ")" if m[1] else "") + ".} ", text)
        return re.sub(r"\\end\{(?:" + RESULTS + r"|conjecture)\}", lambda _: self.marker("close", ""), text)

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
        options, source = match.groups()
        if source.startswith(self.base + "figures/"):
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
        alt = options if options and options.startswith("[alt=") else ""
        return rf"\includegraphics{alt}{{{self.base}figures/{name}}}"

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
            if style == "(i)":
                value, roman = n + 1, ""
                for unit, numeral in ((1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"),
                                      (90, "xc"), (50, "l"), (40, "xl"), (10, "x"), (9, "ix"),
                                      (5, "v"), (4, "iv"), (1, "i")):
                    count, value = divmod(value, unit)
                    roman += numeral * count
                label = "(" + roman + ")"
            else:
                label = re.sub(r"\{([^}]+)\}|[1a]", lambda m: m[1] if m[1] else
                               (str(n + 1) if m[0] == "1" else chr(97 + n)), style)
            return rf"\item \textbf{{{label}}} "
        return pat.sub(item, text)
