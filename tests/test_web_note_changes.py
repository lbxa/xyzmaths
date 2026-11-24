"""Run manuscript-change and recovery scenarios against isolated copies of the real book."""

from concurrent.futures import ThreadPoolExecutor
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from urllib.parse import urljoin

from verify_web_notes import BASE, BOOK, Document, ROOT, compact, inspect_markdown, markdown_parts
from fragments import MANIFEST, fragments, inventory
from render import render


KEY = "hw04:rank-nullity"
SOURCE = "problems/hw04/02-rank-nullity"
RANK = "sections/linear-algebra-i/04-kernel-image-and-rank/03-rank.tex"
OTHER_CHAPTER = "sections/linear-algebra-i/03-linear-equations-and-maps/chapter.tex"


def link_or_copy(source, target):
    try:
        os.link(source, target)
    except OSError:
        shutil.copy2(source, target)


class StructuralOutline(unittest.TestCase):
    def test_display_lead_in_precedes_inline_print_figures(self):
        figure = (":::::div{.margin-figure}\n\n::::figure\n\n![Diagram](/diagram.svg)\n\n"
                  ":::figcaption\n\nCaption $a$.\n\n:::\n\n::::\n\n:::::")
        display = "$$\nx=y.\n$$"
        blocks = "\n\n".join
        cases = [
            (blocks(["With these coordinates,", figure, figure.replace("$a$", "$b$"), display]), ["x=y.", "a", "b"]),
            (blocks(["A complete sentence.", figure, display]), ["a", "x=y."]),
            (blocks(["We obtain:", figure.replace("{.margin-figure}", ""), display]), ["a", "x=y."]),
            (blocks(["We obtain:", figure, blocks([":::div", display, ":::"])]), ["a", "x=y."]),
        ]
        outputs = inspect_markdown([source for source, _ in cases])
        copy_equations = inspect_markdown([copy for _, copy in outputs], "equations")
        for (_, expected), (html, _), copied in zip(cases, outputs, copy_equations):
            with self.subTest(order=expected):
                self.assertEqual([tex for _, tex in Document(html).equations], expected)
                self.assertEqual(copied, Document(html).equations)
        html, copy = outputs[0]
        self.assertRegex(html, r'With these coordinates,</p>\s*<span class="katex-display">')
        self.assertIn(blocks(["With these coordinates,", display]), copy)

    def test_markdown_math_figures_and_grouped_notes(self):
        fixture = ROOT / "tests/web-notes/markdown-fidelity.tex"
        book = SimpleNamespace(book=BOOK, base=BASE, prepare=fixture.read_text, markers=[], figures={}, problems={}, labels={})
        binary = os.environ.get("PANDOC") or shutil.which("pandoc") or ROOT / ".tools/pandoc"
        (fragment,) = fragments(render(book, binary, {}), [], {}).values()
        _, markdown = markdown_parts(fragment.decode())
        html, portable = inspect_markdown([markdown])[0]
        reader = Document(html)
        self.assertEqual(reader.images, [(BASE + "figures/fixture.svg", r"The set \{0\} under L:V\to W.")])
        self.assertIn("costs $5", "".join(reader.text))
        self.assertEqual(reader.tags["aside"], 1)
        self.assertTrue(all(reader.ids[anchor] == 1 for anchor in ("fn1", "fn2", "fnref1", "fnref2")))
        for number in (1, 2):
            self.assertIn(f'<li id="fn{number}" value="{number}" data-margin-note="">', html)
            self.assertIn(f'aria-label="Read margin note {number}"', html)
            self.assertIn(f'aria-label="Return to reference {number}"', html)
            for target in (f"#fn{number}", f"#fnref{number}"):
                self.assertIn(target, reader.reader_links)
            self.assertIn(f'[^{number}]:', portable)
        self.assertEqual([equation for display, equation in reader.equations if not display],
                         ["|x|", "x+1", r"\{0\}", r"L:V\to W", "|a|", r"\Vert v\Vert"])
        displays = [tex for display, tex in reader.equations if display]
        self.assertEqual(len(displays), 1)
        self.assertIn(r"\begin{aligned}", displays[0])
        self.assertEqual(inspect_markdown([portable], "equations")[0], reader.equations)
        self.assertIn("https://xyzmaths.org/notes/linear-algebra/figures/fixture.svg", portable)

    def test_all_structural_heading_levels(self):
        # The Tufte class omits subsubsection and subparagraph in print. Exercise
        # those HTML levels at the Pandoc boundary without changing the manuscript.
        fixture = ROOT / "tests/web-notes/structural-headings.tex"
        book = SimpleNamespace(book=BOOK, base=BASE, prepare=fixture.read_text, markers=[], figures={}, problems={},
                               labels={"sec:fixture:outline": ("1.1", "Outline fixture section", "section")})
        binary = os.environ.get("PANDOC") or shutil.which("pandoc") or ROOT / ".tools/pandoc"
        pages = render(book, binary, {})
        (markdown,) = fragments(pages, [], {}).values()
        meta, body = markdown_parts(markdown.decode())
        page = Document(inspect_markdown([body])[0][0])
        headings = meta["outline"]
        self.assertEqual([h["level"] for h in headings], [2, 3, 4, 5, 6])
        self.assertEqual([h["id"] for h in headings], [
            "sec:fixture:outline", "outline-fixture-subsection", "outline-fixture-subsubsection",
            "outline-fixture-paragraph", "outline-fixture-subparagraph",
        ])
        self.assertEqual([h["title"] for h in headings], [
            "1.1 Outline fixture section", "Outline fixture subsection", "Outline fixture subsubsection",
            "Outline fixture paragraph", "Outline fixture subparagraph",
        ])
        for heading in headings:
            self.assertEqual(page.ids[heading["id"]], 1)


class BookChanges(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(prefix="xyzmaths-note-changes-")
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name).resolve()
        self.book = self.root / "books/linear-algebra"
        self.export = self.root / "src/generated/notes/linear-algebra"
        self.marker = self.export / MANIFEST
        shutil.copytree(ROOT / "books", self.root / "books", ignore=shutil.ignore_patterns("build", "images", "output", ".git"))
        for folder in ("src", "public", "scripts/web-notes"):
            shutil.copytree(ROOT / folder, self.root / folder)
        for name in ("astro.config.mjs", "tsconfig.json", "wrangler.jsonc", "package.json", "bun.lock"):
            shutil.copy2(ROOT / name, self.root / name)
        # Astro compiles its own .astro components by real path. Keep package paths
        # inside this project and leave all build caches private to the fixture.
        shutil.copytree(ROOT / "node_modules", self.root / "node_modules", symlinks=True, copy_function=link_or_copy,
                        ignore=shutil.ignore_patterns(".vite", ".astro", ".mf", ".cache"))
        self.env = {**os.environ, "ASTRO_TELEMETRY_DISABLED": "1", "WRANGLER_SEND_METRICS": "false",
                    "WRANGLER_LOG_PATH": str(self.root / "logs/wrangler.log")}
        if not self.env.get("PANDOC") and not shutil.which("pandoc") and (ROOT / ".tools/pandoc").is_file():
            self.env["PANDOC"] = str(ROOT / ".tools/pandoc")
        self.generate()
        self.env["SOURCE_DATE_EPOCH"] = re.search(r"^# epoch (\d+)$", self.marker.read_text(), re.M)[1]

    def command(self, args, *, success=True, env=None, cwd=None):
        result = subprocess.run(args, cwd=cwd or self.root, env=env or self.env, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True, timeout=180)
        self.assertEqual(result.returncode == 0, success, result.stdout[-5000:])
        return result.stdout

    def generate(self, *args, book="linear-algebra", **kwargs):
        scope = ["--book", book] if book else []
        return self.command([sys.executable, "-B", "scripts/web-notes/build.py", *scope, *args], **kwargs)

    def replace(self, file, old, new):
        text = file.read_text()
        self.assertEqual(text.count(old), 1, file)
        file.write_text(text.replace(old, new))

    def page(self, slug):
        return (self.root / "dist/client" / BASE.strip("/") / slug / "index.html").read_text()

    def test_identical_exercise_keys_stay_in_their_books(self):
        common_key = "hw04:polynomial-root-limit"
        analysis_export = self.export.with_name("maths-analysis")
        analysis_stamp = (analysis_export / MANIFEST).read_bytes()
        self.env.pop("SOURCE_DATE_EPOCH", None)
        statement = self.book / SOURCE / "problem.tex"
        self.replace(statement, rf"\label{{ex:{KEY}}}", rf"\label{{ex:{common_key}}}")
        self.replace(statement, rf"\solutionlink{{{KEY}}}", rf"\solutionlink{{{common_key}}}")
        appendix = self.book / "sections/appendices/exercise-solutions.tex"
        self.replace(appendix, rf"\solutionheading{{{KEY}}}", rf"\solutionheading{{{common_key}}}")
        offline = {**self.env, "PATH": str(self.root / "empty-path"), "PANDOC": "absent-pandoc"}
        self.generate("--check", book="maths-analysis", env=offline)
        self.assertIn("linear-algebra", self.generate("--check", book=None, env=offline, success=False))
        self.command(["bun", "run", "build"])
        self.assertEqual((analysis_export / MANIFEST).read_bytes(), analysis_stamp)

        statements = {}
        for slug, folder in (("linear-algebra", "hw04/02-rank-nullity"), ("maths-analysis", "hw04/01-polynomial-root-limit")):
            metadata, body = markdown_parts((self.export.with_name(slug) / "exercises" / folder / "statement.md").read_text())
            self.assertEqual(metadata["key"], common_key)
            html, _ = inspect_markdown([body])[0]
            statements[slug] = compact(Document(html).text)
            base = f"/notes/{slug}/"
            for page, anchor in ((metadata["statement-page"], "ex:"), (metadata["solution-page"], "sol:"), ("problems", "")):
                with self.subTest(book=slug, page=page):
                    reader = Document((self.root / "dist/client" / base.strip("/") / page / "index.html").read_text())
                    self.assertIn(statements[slug], compact(reader.section_text[anchor + common_key]))
                    self.assertEqual(reader.ids[anchor + common_key], 1)
                    target = (metadata["statement-page"] + "/#ex:" if anchor == "sol:"
                              else metadata["solution-page"] + "/#sol:")
                    self.assertIn(base + target + common_key, reader.links)
        self.assertNotEqual(statements["linear-algebra"], statements["maths-analysis"])

    def test_move_rename_and_reorder_exercise(self):
        old_output = self.export / "exercises" / Path(SOURCE).relative_to("problems")
        original, _ = markdown_parts((old_output / "statement.md").read_text())
        new_source = SOURCE + "-moved"
        (self.book / SOURCE).rename(self.book / new_source)
        statement = rf"\input{{{SOURCE}/problem}}"
        self.replace(self.book / RANK, statement, rf"\autoref{{ex:{KEY}}}")
        dest = self.book / OTHER_CHAPTER
        dest.write_text(dest.read_text() + rf"\input{{{new_source}/problem}}" + "\n")
        appendix = self.book / "sections/appendices/exercise-solutions.tex"
        appendix.write_text(appendix.read_text().replace(SOURCE + "/", new_source + "/"))

        handout = self.book / "problems/hw04.tex"
        text = handout.read_text()
        pairs = list(re.finditer(r"\\input\{problems/hw04/[^}]+/problem\}\s*\\input\{[^}]+/solution\}", text))
        first, second = pairs[:2]
        self.assertIn(SOURCE, second[0])
        moved = second[0].replace(SOURCE, "./" + new_source).replace("}", ".tex}")
        handout.write_text(text[:first.start()] + moved + text[first.end():second.start()] +
                           first[0] + text[second.end():])
        self.command(["bun", "run", "build"])
        new_output = old_output.with_name(old_output.name + "-moved")
        meta, _ = markdown_parts((new_output / "statement.md").read_text())
        self.assertFalse(old_output.exists())
        self.assertEqual((meta["key"], meta["assignment"], meta["question"]), (KEY, "hw04", 1))
        self.assertNotEqual(meta["statement-page"], original["statement-page"])
        self.assertNotEqual(meta["number"], original["number"])
        print_build = self.root / "print"
        print_build.mkdir()
        self.command(["latexmk", "-pdf", "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error",
                      f"-outdir={print_build}", "main.tex"], cwd=self.book)
        aux = (print_build / "main.aux").read_text()
        printed = re.search(r"\\newlabel\{ex:" + re.escape(KEY) + r"\}\{\{([^{}]+)\}", aux)
        self.assertIsNotNone(printed)
        self.assertEqual(meta["number"], printed[1])
        for path in (meta["statement-page"], meta["solution-page"]):
            metadata, fragment = markdown_parts((self.export / "pages" / (path + ".md")).read_text())
            label = re.search(r'^# .*?\{id="([^"]+)"', fragment, re.M)[1]
            printed_page = re.search(r"\\newlabel\{" + re.escape(label) + r"\}\{\{[^{}]*\}\{([^{}]+)\}", aux)
            self.assertEqual(metadata["page"], printed_page[1])
        number = "Exercise " + meta["number"]
        chapter = Document(self.page(meta["statement-page"]))
        old = Document(self.page(original["statement-page"]))
        appendix = Document(self.page(meta["solution-page"]))
        index = Document(self.page("problems"))
        chapter_target = BASE + meta["statement-page"] + "/#ex:" + KEY
        self.assertNotIn("ex:" + KEY, old.ids)
        self.assertIn(number, "".join(chapter.section_text["ex:" + KEY]))
        self.assertIn(number, "".join(appendix.section_text["sol:" + KEY]))
        self.assertIn("Problem 1", "".join(index.section_text[KEY]))
        for doc in (old, appendix, index):
            self.assertIn(chapter_target, doc.links)
        self.assertIn(f'href="{chapter_target}">{number}</a>', self.page(original["statement-page"]))

    def test_nested_list_and_margin_note_in_three_views(self):
        statement = self.book / SOURCE / "problem.tex"
        insert = (ROOT / "tests/web-notes/exercise-insert.tex").read_text()
        link = rf"\solutionlink{{{KEY}}}"
        self.replace(statement, link, insert + "\n" + link)
        self.command(["bun", "run", "build"])
        artifact = self.export / "exercises" / Path(SOURCE).relative_to("problems") / "statement.md"
        meta, _ = markdown_parts(artifact.read_text())
        other = self.export / "exercises/hw04/01-kernel-image-and-rank/statement.md"
        other_meta, _ = markdown_parts(other.read_text())
        other_url = BASE + other_meta["statement-page"] + "/#ex:" + other_meta["key"]
        for slug in (meta["statement-page"], meta["solution-page"], "problems"):
            html = self.page(slug)
            with self.subTest(page=slug, feature="nested list"):
                start = html.index("First fixture case.")
                end = html.index("Second fixture case.", start)
                self.assertRegex(html[start:end], r"(?s)<ul[^>]*>\s*<li>.*?Inner fixture one.*?</li>\s*<li>.*?Inner fixture two.*?</li>\s*</ul>")
                self.assertRegex(html[start:end], r"\(b\)</strong>\s*$")
            with self.subTest(page=slug, feature="local footnote and backlink"):
                doc = Document(html)
                note = re.search(r'(<li id="([^"]+)"[^>]*>)\s*(?:<p>)?Fixture margin note', html)
                self.assertIsNotNone(note)
                target = note[2]
                number = re.fullmatch(r'(?:restated-)?fn(\d+)', target)[1]
                self.assertIn(f'value="{number}"', note[1])
                self.assertIn("data-margin-note", note[1])
                page_url = BASE + slug + "/"
                urls = {urljoin(page_url, href) for href in doc.links}
                for anchor in (target, target.replace("fn", "fnref")):
                    self.assertEqual(doc.ids[anchor], 1, anchor)
                    self.assertTrue(page_url + "#" + anchor in urls, f"Missing local link to {anchor} on {slug}")
                self.assertIn(other_url, doc.links)

    def test_renamed_tikz_and_new_raster_keep_their_bytes(self):
        name = "vector-basis-coordinates"
        new = name + "-renamed"
        published = self.root / "dist/client" / BASE.strip("/") / "figures"
        self.command(["bun", "run", "build"])
        svg = (published / f"{name}.svg").read_bytes()
        (self.book / f"figures/{name}.tex").rename(self.book / f"figures/{new}.tex")
        topic = self.book / "sections/linear-algebra-i/02-matrices-and-vector-coordinates/02-change-of-basis-for-vectors.tex"
        self.replace(topic, rf"\input{{figures/{name}}}", rf"\input{{figures/{new}}}")
        png = (self.root / "public/favicon-32.png").read_bytes()
        (self.book / "figures/fixture-raster.png").write_bytes(png)
        topic.write_text(topic.read_text() + "\n" + r"\begin{figure}\includegraphics{figures/fixture-raster.png}"
                         r"\caption{Raster figure fixture.}\label{fig:fixture-raster}\end{figure}" + "\n")
        self.command(["bun", "run", "build"])
        for folder in (published, self.export / "figures"):
            self.assertFalse((folder / f"{name}.svg").exists())
            self.assertTrue((folder / f"{new}.svg").read_bytes() == svg, "SVG changed during rename")
            self.assertEqual((folder / "fixture-raster.png").read_bytes(), png)
        page = Document(self.page("linear-algebra-i/matrices-and-vector-coordinates"))
        url = BASE + f"figures/{new}.svg"
        self.assertIn(url, page.links)
        self.assertIn(url, [src for src, alt in page.images])
        self.assertIn(BASE + "figures/fixture-raster.png", [src for src, alt in page.images])

    def test_pending_solution_updates_only_its_fragment(self):
        solution = self.book / "problems/hw01/01-axiom-consequences/solution.tex"
        if "Awaiting solution." not in solution.read_text():
            solution.write_text(r"\noindent\emph{Awaiting solution.}" + "\n")
            self.generate()
        before = inventory(self.export)
        solution.write_text(r"\begin{proof}[Solution]Fixture solution with \(1+1=2\).\end{proof}" + "\n")
        self.command(["bun", "run", "build"])
        after = inventory(self.export)
        folder = "exercises/hw01/01-axiom-consequences"
        self.assertEqual(before.keys(), after.keys())
        self.assertEqual([name for name in before if before[name] != after[name]], [folder + "/solution.md"])
        meta, _ = markdown_parts((self.export / folder / "statement.md").read_text())
        appendix = Document(self.page(meta["solution-page"]))
        section = "".join(appendix.section_text["sol:" + meta["key"]])
        self.assertIn("Fixture solution with", section)
        self.assertNotIn("Awaiting solution.", section)

    def test_shared_notation_and_bibliography_reach_the_site(self):
        drawing = self.export / "figures/span-and-dependence.svg"
        original = drawing.read_bytes()
        self.replace(self.book / "macros.tex", r"\newcommand{\R}{\mathbb{R}}", r"\newcommand{\R}{\mathbf{R}}")
        bibliography = self.book / "bibliography.bib"
        entry = re.search(r"@online\{OpenCVLinearFilters,.*?^}", bibliography.read_text(), re.M | re.S)
        self.assertIsNotNone(entry)
        fixture_url = "https://example.org/fixture-reference"
        revised, count = re.subn(r"url = \{[^{}]+\}", "url = {" + fixture_url + "}", entry[0])
        self.assertEqual(count, 1)
        self.replace(bibliography, entry[0], revised)
        self.command(["bun", "run", "build"])
        statement = self.export / "exercises" / Path(SOURCE).relative_to("problems") / "statement.md"
        meta, _ = markdown_parts(statement.read_text())
        for slug in (meta["statement-page"], meta["solution-page"], "problems"):
            self.assertIn(r"\mathbf{R}", self.page(slug))
        self.assertTrue(drawing.read_bytes() != original, "The TikZ label did not pick up the new notation")
        served = self.root / "dist/client" / BASE.strip("/") / "figures" / drawing.name
        self.assertTrue(served.read_bytes() == drawing.read_bytes())
        self.assertIn(fixture_url, Document(self.page("references")).links)
        self.assertIn(BASE + "references/#ref-OpenCVLinearFilters", Document(self.page(meta["statement-page"])).links)

    def test_crlf_and_website_edits_can_reuse_export_offline(self):
        stamp = self.marker.read_bytes()
        offline = {**self.env, "PATH": str(self.root / "empty-path"), "PANDOC": "absent-pandoc"}
        offline.pop("SOURCE_DATE_EPOCH", None)
        chapter = self.book / RANK
        chapter.write_bytes(chapter.read_bytes().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n"))
        layout = self.root / "src/layouts/BookNotes.astro"
        layout.write_bytes(layout.read_bytes() + b"\n")
        self.generate(env=offline)
        self.generate("--check", env=offline)
        self.assertEqual(self.marker.read_bytes(), stamp)
        chapter.write_bytes(chapter.read_bytes() + b"\r\nEdited fixture paragraph.\r\n")
        self.assertIn("stale", self.generate("--check", env=offline, success=False))
        self.assertIn("Missing", self.generate(env=offline, success=False))
        self.assertEqual(self.marker.read_bytes(), stamp)

    def test_invalid_edits_preserve_last_good_export(self):
        before = {file: file.stat().st_mtime_ns for file in self.export.rglob("*") if file.is_file()}
        hashes = inventory(self.export)
        chapter = self.book / RANK
        original = chapter.read_text()
        for label, edit, error in (
            ("unknown reference", r"\autoref{sec:absent-fixture}", "Unresolved manuscript reference"),
            ("duplicate placement", rf"\input{{{SOURCE}/problem}}", "Expected one chapter placement"),
            ("missing input", r"\input{missing-fixture}", "missing-fixture"),
            ("unresolved citation", r"\cite{absent-fixture}", "absent-fixture"),
        ):
            with self.subTest(label):
                chapter.write_text(original + "\n" + edit + "\n")
                self.assertIn(error, self.generate(success=False))
                self.assertEqual(inventory(self.export), hashes)
                self.assertEqual({file: file.stat().st_mtime_ns for file in before}, before)
        chapter.write_text(original)
        self.generate("--check")

    def test_incomplete_export_and_competing_repairs(self):
        before = inventory(self.export)
        stamp = self.marker.read_bytes()
        dropped = "pages/references.md"
        (self.export / dropped).unlink()
        # An incomplete copy can lose both an artifact and its line in the inventory.
        self.marker.write_bytes(b"".join(line for line in stamp.splitlines(keepends=True)
                                         if not line.endswith(f"  {dropped}\n".encode())))
        self.generate("--check", success=False)
        (self.export / "figures/orphan.svg").write_bytes(b"<svg/>")
        with ThreadPoolExecutor(max_workers=2) as pool:
            logs = list(pool.map(lambda _: self.generate("--force"), range(2)))
        self.assertEqual(sum(int(re.search(r"(\d+) written", log)[1]) for log in logs), 1)
        self.assertEqual(sum(int(re.search(r"(\d+) removed", log)[1]) for log in logs), 1)
        self.assertEqual(inventory(self.export), before)
        self.assertEqual(self.marker.read_bytes(), stamp)
        self.generate("--check", env={**self.env, "PANDOC": str(self.root / "uninstalled-pandoc")})


if __name__ == "__main__":
    unittest.main(verbosity=2)
