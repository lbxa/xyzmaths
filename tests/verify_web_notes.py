"""Check the published site, weekly problems and Linear Algebra reading edition."""

from collections import Counter, defaultdict
from functools import cache
from contextlib import contextmanager
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from threading import Thread
import unittest
from urllib.parse import unquote, urljoin, urlsplit
from unittest.mock import patch
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/linear-algebra"
SITE = ROOT / "dist/client"
BASE = "/notes/linear-algebra/"
BOOK_TITLES = {"linear-algebra": "Linear Algebra", "maths-analysis": "Introduction to Mathematical Analysis"}
WEEKLY_SOURCE = ROOT / "src/content/pow"
WEEKLY_PROBLEMS = {
    "disc-game-prize-fund": ("2026-07-08", "https://projecteuler.net/problem=121", "£1", "£2,269"),
    "k-tree": ("2026-07-07", "https://codeforces.com/problemset/problem/431/C", "10^9+7", "4-1=3"),
}
INPUT = re.compile(r"\\input\{([^{}]+)\}")
sys.path.insert(0, str(ROOT / "scripts/web-notes"))
from fragments import ARTWORK, MANIFEST, atomic_write, inventory, manifest, publish


def source(name, book=BOOK):
    path = str(name).removeprefix(r"\analysisroot/")
    tex = (book / Path(path).with_suffix(".tex")).read_text()
    return re.sub(r"(?<!\\)%[^\n]*", "", tex)


def expand(tex, book=BOOK):
    return INPUT.sub(lambda m: expand(source(m[1], book), book), tex)


def markdown_parts(text):
    if not text.startswith("---\n"):
        return {}, text
    head, body = text[4:].split("\n---\n", 1)
    return {key: json.loads(value) for key, value in (line.split(": ", 1) for line in head.splitlines())}, body


def inspect_markdown(bodies, mode="render"):
    result = subprocess.run(["node", ROOT / "tests/read-web-markdown.mjs", mode], input=json.dumps(bodies),
                            text=True, capture_output=True, check=True)
    return json.loads(result.stdout)


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.ids = Counter()
        self.tags = Counter()
        self.links = []
        self.reader_links = []
        self.native_links = []
        self.in_main = False
        self.main_links = []
        self.main_text = []
        self.dates = []
        self.document_title = ""
        self.in_document_title = False
        self.home_link = None
        self.primary_links = []
        self.main_navs = []
        self.nav_links = None
        self.nav_link = None
        self.cpp_blocks = []
        self.cpp_block = None
        self.inline_notes = {}
        self.margin_visible = None
        self.note_references = {}
        self.note_returns = set()
        self.copy_markdown_url = None
        self.reading_controls = []
        self.in_book_selector = False
        self.book_selector_text = []
        self.in_copy_control = False
        self.reading_button = None
        self.stylesheets = []
        self.images = []
        self.equations = []
        self.annotation = None
        self.display_math = False
        self.section_text = defaultdict(list)
        self.article_headings = []
        self.article_figures = []
        self.in_article = False
        self.in_article_header_or_footer = False
        self.in_article_paragraph = False
        self.article_prose = []
        self.metadata = {}
        self.placements = defaultdict(list)
        self.stack = []
        self.text = []
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags[tag] += 1
        key = attrs.get("id")
        if key:
            self.ids[key] += 1
        if tag == "title" and not self.document_title:
            self.in_document_title = True
        if tag == "main":
            self.in_main = True
        if tag == "nav":
            if attrs.get("aria-label") == "Primary":
                self.tags["primary-nav"] += 1
                self.nav_links = self.primary_links
            elif self.in_main:
                self.nav_links = []
                self.main_navs.append(self.nav_links)
        if tag == "time" and self.in_main:
            self.dates.append(attrs.get("datetime"))
        if attrs.get("role") == "combobox" and attrs.get("aria-label") == "Book":
            self.tags["book-selector"] += 1
            self.in_book_selector = True
        if tag == "code" and "language-cpp" in attrs.get("class", "").split():
            self.cpp_block = []
        if tag == "article":
            self.in_article = True
        if self.in_article and tag in {"header", "footer"}:
            self.in_article_header_or_footer = True
        if tag == "p":
            self.in_article_paragraph = self.in_article and not self.in_article_header_or_footer
        if tag == "copy-markdown":
            self.copy_markdown_url = attrs.get("data-markdown-url")
            self.in_copy_control = True
        if tag == "button" and (self.in_copy_control or attrs.get("aria-controls") == "reading-column"):
            self.reading_button = ElementTree.Element("button", attrs)
            self.reading_controls.append(self.reading_button)
        if tag == "svg" and self.reading_button is not None:
            ElementTree.SubElement(self.reading_button, "svg", attrs)
        if self.in_article and tag in {"h2", "h3", "h4", "h5", "h6"} and key:
            self.article_headings.append((int(tag[1]), key))
        if self.in_article and tag == "figure":
            self.article_figures.append(key)
        if self.in_article and tag == "li" and "data-margin-note" in attrs:
            self.inline_notes[key] = int(attrs["value"])
        if tag == "aside" and key == "right-aside":
            self.margin_visible = "hidden" not in attrs
        if tag == "div" and "margin-figure" in attrs.get("class", "").split():
            self.tags["margin-figure"] += 1
        if tag == "section":
            self.stack.append(key)
        if tag == "template":
            if "data-title" in attrs:
                self.metadata = {k.removeprefix("data-"): v for k, v in attrs.items()}
            for role in ("statement", "solution"):
                if "data-" + role in attrs:
                    self.placements[role].append(attrs["data-" + role])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
            if self.in_main:
                self.main_links.append(attrs["href"])
            if self.nav_links is not None:
                self.nav_link = ElementTree.Element("a", attrs)
                self.nav_links.append(self.nav_link)
            elif attrs["href"] == "/" and not self.tags["main"]:
                self.home_link = self.nav_link = ElementTree.Element("a", attrs)
            if "data-astro-reload" in attrs or "download" in attrs:
                self.native_links.append(attrs["href"])
            if attrs.get("role") == "doc-noteref":
                self.note_references[urlsplit(attrs["href"]).fragment] = key
            if attrs.get("role") == "doc-backlink":
                self.note_returns.add(urlsplit(attrs["href"]).fragment)
            if "reader-link" in attrs.get("class", "").split():
                self.reader_links.append(attrs["href"])
        if tag == "link" and "stylesheet" in attrs.get("rel", "").split():
            self.stylesheets.append(attrs["href"])
        if tag == "span" and "katex-html" in attrs.get("class", "").split() and attrs.get("aria-hidden") == "true":
            self.tags["typeset-equation"] += 1
        if tag == "img":
            self.images.append((attrs["src"], attrs.get("alt", "")))
        if tag == "math":
            self.display_math = attrs.get("display") == "block"
        if tag == "annotation" and attrs.get("encoding") == "application/x-tex":
            self.tags["annotated-equation"] += 1
            self.annotation = []

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_document_title = False
        if tag == "main":
            self.in_main = False
        if tag == "nav":
            self.nav_links = None
        if tag == "a":
            self.nav_link = None
        if tag == "code" and self.cpp_block is not None:
            self.cpp_blocks.append("".join(self.cpp_block).rstrip("\n"))
            self.cpp_block = None
        if tag == "button":
            self.reading_button = None
            self.in_book_selector = False
        if tag == "copy-markdown":
            self.in_copy_control = False
        if tag == "annotation" and self.annotation is not None:
            self.equations.append([self.display_math, "".join(self.annotation)])
            self.annotation = None
        if tag == "section":
            self.stack.pop()
        if tag == "article":
            self.in_article = False
        if tag in {"header", "footer"}:
            self.in_article_header_or_footer = False
        if tag == "p":
            self.in_article_paragraph = False

    def handle_data(self, data):
        if self.in_document_title:
            self.document_title += data
        if self.in_main:
            self.main_text.append(data)
        if self.in_book_selector:
            self.book_selector_text.append(data)
        if self.in_article_paragraph:
            self.article_prose.append(data)
        if self.nav_link is not None:
            self.nav_link.text = (self.nav_link.text or "") + data
        if self.cpp_block is not None:
            self.cpp_block.append(data)
        if self.reading_button is not None:
            self.reading_button.text = (self.reading_button.text or "") + data
        if self.annotation is not None:
            self.annotation.append(data)
        self.text.append(data)
        for key in self.stack:
            if key:
                self.section_text[key].append(data)


def compact(parts):
    return "".join("".join(parts).split())


def weekly_views(slug):
    base = f"/pow/{slug}/"
    return {"Problem": base, "Solution": base + "solution/", "Editorial": base + "editorial/"}


@cache
def reader_pages(slug):
    directory = SITE / "notes" / slug
    if not (directory / "index.html").is_file():
        raise AssertionError(f"Build the {slug} reading edition first with bun run build.")
    return {"/" + file.parent.relative_to(SITE).as_posix() + "/": Document(file.read_text())
            for file in directory.rglob("index.html")}


class WebNotes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs = {route: doc for slug in BOOK_TITLES for route, doc in reader_pages(slug).items()}
        routes = ["/", "/books/", "/pow/"]
        cls.weekly_slugs = sorted(file.stem for file in WEEKLY_SOURCE.glob("*.md"))
        for slug in cls.weekly_slugs:
            routes.extend(weekly_views(slug).values())
        cls.collections = {route: Document((SITE / route.strip("/") / "index.html").read_text()) for route in routes}

    def test_primary_navigation_and_book_controls(self):
        for route, doc in (self.collections | self.docs).items():
            with self.subTest(route=route):
                self.assertEqual(doc.tags["primary-nav"], 1)
                links = {urljoin(route, link.get("href")): (link.get("aria-label") or link.text).strip()
                         for link in doc.primary_links}
                self.assertEqual(links.get("/books/"), "XYZ Books")
                self.assertEqual(links.get("/pow/"), "XYZ PoW")
                if route in self.collections:
                    self.assertEqual(doc.tags["book-selector"], 0)
                    self.assertEqual(doc.ids["left-aside"], 0)
                    self.assertEqual(doc.reading_controls, [])
                    self.assertIsNone(doc.copy_markdown_url)
                else:
                    self.assertEqual(doc.tags["book-selector"], 1)
                    self.assertEqual("".join(doc.book_selector_text).strip(), BOOK_TITLES[route.split("/")[2]])

    def test_section_brand_in_header_and_browser_title(self):
        brands = {"": "XYZ Maths", "books": "XYZ Books", "notes": "XYZ Books", "pow": "XYZ PoW"}
        for route, doc in (self.collections | self.docs).items():
            with self.subTest(route=route):
                brand = brands[route.split("/")[1]]
                self.assertIsNotNone(doc.home_link)
                self.assertEqual((doc.home_link.text or "").strip(), brand)
                if route in {"/", "/books/", "/pow/"}:
                    self.assertEqual(doc.document_title, brand)
                else:
                    self.assertTrue(doc.document_title.endswith(" | " + brand), doc.document_title)

    def test_directories_link_to_the_collections_and_manuscript(self):
        home, books = self.collections["/"], self.collections["/books/"]
        self.assertIn("/books/", home.main_links)
        self.assertIn("/pow/", home.main_links)
        for slug, title in BOOK_TITLES.items():
            base = f"/notes/{slug}/"
            manuscript = f"/books/{slug}/manuscript.pdf"
            overview = self.docs[base]
            with self.subTest(book=slug):
                self.assertIn(base, books.main_links)
                self.assertIn(base, home.main_links)
                self.assertIn(title, books.main_text)
                for doc in (home, books, overview):
                    self.assertIn(manuscript, doc.main_links)
                    self.assertIn(manuscript, doc.native_links)
                self.assertIn(base + "problems/", overview.main_links)
        self.assertIn(BASE + "linear-algebra-i/vector-spaces-and-bases/", self.docs[BASE].main_links)

    def test_weekly_problem_navigation(self):
        home = self.collections["/"]
        self.assertTrue(any(weekly_views(slug)["Problem"] in home.main_links for slug in self.weekly_slugs),
                        "The homepage must link to its featured problem")
        for slug in self.weekly_slugs:
            views = weekly_views(slug)
            routes = ["/pow/", *views.values()]
            if views["Problem"] in home.main_links:
                routes.append("/")
            for route in routes:
                with self.subTest(slug=slug, page=route):
                    navs = ({urljoin(route, link.get("href")): link for link in nav}
                            for nav in self.collections[route].main_navs)
                    links = next((nav for nav in navs if set(views.values()) <= nav.keys()), None)
                    self.assertIsNotNone(links, "Missing direct navigation between the three problem views")
                    for label, href in views.items():
                        self.assertEqual((links[href].text or "").strip(), label)
                        self.assertEqual(links[href].get("aria-current") == "page", href == route, href)

    def test_worked_pages_publish_the_canonical_cpp(self):
        for slug in self.weekly_slugs:
            views = weekly_views(slug)
            source_file = WEEKLY_SOURCE / f"{slug}.cpp"
            if slug in WEEKLY_PROBLEMS:
                self.assertTrue(source_file.is_file(), f"Missing the supplied implementation for {slug}")
            if not source_file.is_file():
                continue
            implementation = source_file.read_text().rstrip("\n")
            with self.subTest(slug=slug):
                self.assertTrue(implementation.strip())
                self.assertNotIn(implementation, self.collections[views["Problem"]].cpp_blocks)
            for view in ("Solution", "Editorial"):
                with self.subTest(slug=slug, view=view):
                    doc = self.collections[views[view]]
                    self.assertEqual(doc.cpp_blocks.count(implementation), 1)

    def test_weekly_statements_and_worked_answers(self):
        archive = self.collections["/pow/"]
        for slug, (date, source_url, statement_fact, answer) in WEEKLY_PROBLEMS.items():
            views = weekly_views(slug)
            problem, solution, editorial = (self.collections[views[view]] for view in ("Problem", "Solution", "Editorial"))
            with self.subTest(problem=slug):
                self.assertIn(date, archive.dates)
                for doc in (problem, solution, editorial):
                    self.assertIn(date, doc.dates)
                    self.assertIn(source_url, doc.main_links)
                self.assertIn(statement_fact, compact(problem.main_text))
                self.assertNotIn(answer, compact(problem.main_text))
                self.assertIn(answer, compact(editorial.main_text))
                self.assertNotEqual(compact(solution.article_prose), compact(editorial.article_prose),
                                    "The solution and editorial must each have their own explanation")
                for worked in (solution, editorial):
                    self.assertTrue(worked.equations, "Missing typeset mathematics")
                    self.assertEqual(worked.tags["typeset-equation"], len(worked.equations))
                    self.assertNotIn(compact(worked.article_prose), compact(problem.article_prose),
                                     "The problem statement contains its worked explanation")
                if slug == "k-tree":
                    math = {compact([tex]) for _, tex in solution.equations}
                    for parameter in ("n=3", "k=3", "d=2"):
                        self.assertTrue(any(parameter in tex for tex in math), parameter)
                    self.assertTrue(any(re.fullmatch(r"(?:[0-9+()*/−-]+=)?3", tex) for tex in math),
                                    "The worked example has three qualifying paths")
                else:
                    self.assertIn(answer, compact(solution.main_text))

    def test_reader_pages_offer_both_widths_before_copy(self):
        for route, doc in self.docs.items():
            with self.subTest(route=route):
                self.assertEqual(doc.ids["reading-column"], 1)
                labels = [(button.get("aria-label") or (button.text or "").strip(), button.get("aria-pressed"))
                          for button in doc.reading_controls]
                self.assertEqual(labels, [
                    ("Centred text", "true"), ("Wide text", "false"), ("Copy for LLM", None),
                ])
                for button in doc.reading_controls:
                    self.assertTrue(button.get("aria-description"))
                    icons = button.findall("svg")
                    self.assertTrue(icons)
                    for icon in icons:
                        self.assertEqual(icon.get("aria-hidden"), "true")
                        self.assertEqual(icon.get("focusable"), "false")

    def test_overview_and_part_links_use_reader_navigation_styles(self):
        overview = self.docs[BASE]
        self.assertIn(BASE + "#linear-algebra-i", overview.reader_links)
        self.assertEqual(overview.reader_links, overview.links)

        chapter = BASE + "linear-algebra-i/vector-spaces-and-bases/"
        appendix = BASE + "appendices/exercise-solutions/"
        figure = chapter + "#fig:linear-algebra-i:vector-addition"
        self.assertIn(figure, self.docs[chapter].links)
        self.assertNotIn(figure, self.docs[chapter].reader_links)
        self.assertIn(appendix + "#sol:hw01:axiom-consequences", self.docs[chapter].reader_links)
        self.assertIn(chapter + "#ex:hw01:axiom-consequences", self.docs[appendix].reader_links)

    def test_published_math_uses_katex(self):
        styles = {"/" + css.relative_to(SITE).as_posix() for css in SITE.rglob("*.css")
                  if ".katex-mathml" in css.read_text()}
        for page, doc in (self.collections | self.docs).items():
            if doc.tags["math"]:
                with self.subTest(page=page):
                    self.assertEqual(doc.tags["typeset-equation"], doc.tags["math"])
                    self.assertEqual(doc.tags["annotated-equation"], doc.tags["math"])
                    linked = {urlsplit(urljoin(page, href)).path for href in doc.stylesheets}
                    self.assertTrue(linked & styles or ".katex-mathml" in "".join(doc.text))


class ReadingEditionChecks:
    @classmethod
    def setUpClass(cls):
        cls.book = ROOT / "books" / cls.slug
        cls.fragments = ROOT / "src/generated/notes" / cls.slug
        cls.base = f"/notes/{cls.slug}/"
        cls.docs = reader_pages(cls.slug)
        files = sorted(cls.fragments.rglob("*.md"))
        parts = [markdown_parts(file.read_text()) for file in files]
        documents = {}
        for file, (metadata, body), (html, portable) in zip(files, parts, inspect_markdown([b for _, b in parts])):
            doc = Document(html)
            doc.metadata = metadata
            doc.markdown = portable
            for kind, key in re.findall(r'^::(statement|solution)\{key="([^"]+)"\}$', body, re.M):
                doc.placements[kind].append(key)
            documents[file] = doc
        pages = cls.fragments / "pages"
        cls.pages = {file.relative_to(pages).with_suffix("").as_posix(): documents[file] for file in pages.rglob("*.md")}
        cls.exercises = {}
        for file in (cls.fragments / "exercises").rglob("statement.md"):
            statement = documents[file]
            data = statement.metadata
            cls.exercises[data["key"]] = {**data, "statement": statement, "solution": documents[file.with_name("solution.md")]}
        body = source("main", cls.book).split(r"\begin{document}")[1].split(r"\end{document}")[0]
        cls.tex = expand(body, cls.book)

    def test_book_order_and_repeated_placements(self):
        pages = sorted(self.pages.values(), key=lambda p: int(p.metadata["order"]))
        chapters = [p.metadata["title"] for p in pages if p.metadata["group"] not in ("Front matter", "References", "Back matter")]
        self.assertEqual(chapters, re.findall(r"\\chapter\{([^{}]+)\}", self.tex))
        self.assertEqual(set(self.docs), {self.base, self.base + "problems/", *(self.base + key + "/" for key in self.pages)})
        body = self.tex.split(r"\appendix")[0]
        expected = re.findall(r"\\solutionlink\{([^{}]+)\}", body)
        statements = [key for p in pages for key in p.placements["statement"]]
        solutions = [key for p in pages for key in p.placements["solution"]]
        self.assertEqual(statements, expected)
        self.assertEqual(solutions, re.findall(r"\\solutionheading\{([^{}]+)\}", self.tex))
        self.assertCountEqual(statements, self.exercises)
        self.assertCountEqual(solutions, self.exercises)

    def test_reader_contents_match_the_exported_pages(self):
        numbered_pages = []
        exported_levels = []
        for slug, page in sorted(self.pages.items(), key=lambda item: int(item[1].metadata["order"])):
            with self.subTest(slug=slug):
                meta = page.metadata
                headings = meta.get("outline", [])
                exported_levels.extend(h["level"] for h in headings)
                article = self.docs[self.base + slug + "/"]
                self.assertEqual([(h["level"], h["id"]) for h in headings], article.article_headings)
                self.assertTrue(all(type(h["level"]) is int and h["title"].strip() for h in headings))
                if meta["group"] != "Front matter":
                    numbered_pages.append(int(meta["page"]))
                if meta.get("part"):
                    self.assertTrue(meta["part"].startswith("Part "))
        self.assertEqual(numbered_pages, sorted(numbered_pages))
        levels = {"section": 2, "subsection": 3, "subsubsection": 4, "paragraph": 5, "subparagraph": 6}
        commands = re.findall(r"\\(section|subsection|subsubsection|paragraph|subparagraph)\*?\s*(?=[{\[])", self.tex)
        self.assertEqual(exported_levels, [levels[command] for command in commands])

    def test_handout_order_and_solution_text(self):
        index = self.docs[self.base + "problems/"]
        for handout in sorted((self.book / "problems").glob("hw[0-9][0-9].tex")):
            inputs = map(Path, INPUT.findall(source(handout.relative_to(self.book), self.book)))
            paths = [p.with_suffix("").as_posix() for p in inputs if p.stem == "problem"]
            exercises = sorted((e for e in self.exercises.values() if e.get("assignment") == handout.stem),
                               key=lambda ex: int(ex["question"]))
            self.assertEqual([ex["source"] for ex in exercises], paths)
            self.assertEqual([key for key in index.section_text if key.startswith(handout.stem + ":")],
                             [ex["key"] for ex in exercises])
        for key, ex in self.exercises.items():
            with self.subTest(exercise=key):
                chapter = self.docs[self.base + ex["statement-page"] + "/"]
                appendix = self.docs[self.base + ex["solution-page"] + "/"]
                statement = compact(ex["statement"].text)
                solution = compact(ex["solution"].text)
                self.assertTrue(statement and solution)
                for doc, placement in ((chapter, "ex:" + key), (appendix, "sol:" + key), (index, key)):
                    self.assertIn(statement, compact(doc.section_text[placement]))
                self.assertIn(solution, compact(appendix.section_text["sol:" + key]))
                self.assertEqual("Awaitingsolution." in solution,
                                 "Awaiting solution." in source(Path(ex["source"]).with_name("solution"), self.book))
                self.assertIn(self.base + ex["solution-page"] + "/#sol:" + key, chapter.links)
                self.assertIn(self.base + ex["statement-page"] + "/#ex:" + key, appendix.links)

    def test_internal_destinations_and_artwork(self):
        images = set()
        for path, doc in self.docs.items():
            self.assertFalse([key for key, count in doc.ids.items() if count != 1], path)
            for link in doc.links:
                url = urlsplit(urljoin(path, link))
                if url.netloc or url.scheme or not url.path.startswith(self.base):
                    continue
                if url.path.startswith(self.base + "figures/") or url.path.endswith(".md"):
                    self.assertTrue((SITE / url.path.lstrip("/")).is_file(), link)
                    continue
                target = self.docs[url.path]
                if url.fragment:
                    self.assertIn(unquote(url.fragment), target.ids, f"{path} -> {link}")
            for src, alt in doc.images:
                self.assertTrue(alt.strip() and alt != "image", (path, src))
                self.assertTrue(src.startswith(self.base + "figures/"), (path, src))
                self.assertTrue((SITE / src.lstrip("/")).is_file(), src)
                images.add(Path(src).name)
        self.assertEqual(images, {f.name for f in (self.fragments / "figures").glob("*") if f.suffix in ARTWORK})
        for name in images:
            data = (SITE / self.base.strip("/") / "figures" / name).read_bytes()
            self.assertTrue(data == (self.fragments / "figures" / name).read_bytes(), f"Altered figure: {name}")
            if name.endswith(".svg"):
                svg = ElementTree.fromstring(data)
                _, _, width, height = map(float, svg.attrib["viewBox"].split())
                self.assertGreater(min(width, height), 0, name)
                self.assertTrue(any(e.tag.endswith(("path", "image", "use")) for e in svg.iter()), name)

    def test_citations_resolve_to_this_books_bibliography(self):
        references = self.base + "references/"
        cited = {key.strip() for group in re.findall(r"\\cite(?:\[[^\]]*\]){0,2}\{([^{}]+)\}", self.tex)
                 for key in group.split(",")}
        self.assertTrue(cited)
        targets = {urljoin(route, href) for route, doc in self.docs.items()
                   for href in doc.main_links if urlsplit(href).fragment.startswith("ref-")}
        self.assertTrue(all(target.startswith(references + "#") for target in targets))
        for key in cited:
            with self.subTest(citation=key):
                self.assertIn(references + "#ref-" + key, targets)
                self.assertIn("ref-" + key, self.docs[references].ids)

    def test_math_and_margin_notes(self):
        original = list(self.pages.items())
        original.extend((ex[field + "-page"], ex[field]) for ex in self.exercises.values()
                        for field in ("statement", "solution"))
        notes = [urljoin(self.base + page + "/", link) for page, doc in original for link in doc.links
                 if re.search(r"#fn\d+$", link)]
        primary = re.sub(r"\\begin\{restatedproblem\}.*?\\end\{restatedproblem\}", "", self.tex, flags=re.S)
        self.assertEqual(len(notes), len(re.findall(r"\\(?:marginnote|sidenote|footnote|historynote)\b", primary)))
        for link in notes:
            target, anchor = link.split("#")
            self.assertIn(target + "#" + anchor.replace("fn", "fnref"),
                          {urljoin(target, href) for href in self.docs[target].links})
        totals = sum((doc.tags for _, doc in original), Counter())
        portraits = re.findall(r"\\historyportrait(?:pair)?\b", primary)
        self.assertEqual(totals["margin-figure"], primary.count(r"\begin{marginfigure}") + len(portraits))
        self.assertGreater(totals["math"], 0)
        self.assertGreater(totals["mtable"], 0)
        self.assertEqual(totals["math"], totals["annotated-equation"])
        for doc in self.docs.values():
            self.assertFalse(doc.placements)
            self.assertNotIn("tufte@stored@", "".join(doc.text))
            self.assertNotIn(r"\xyzweb", "".join(doc.text))

    def test_all_figures_follow_manuscript_order_in_the_articles(self):
        figures = re.finditer(r"\\begin\{(marginfigure|figure\*?)\}(.*?)\\end\{\1\}", self.tex, re.S)
        labelled = []
        for figure in figures:
            kind, body = figure.groups()
            label = re.search(r"\\label\{(fig:[^{}]+)\}", body)
            self.assertIsNotNone(label, f"Missing figure label for {kind}: {body[:100]}")
            labelled.append((figure.start(), label[1]))
        for portrait in re.finditer(r"\\historyportrait\*?\s*\{([^{}]+)\}", self.tex):
            labelled.append((portrait.start(), "fig:portrait:" + portrait[1]))
        for pair in re.finditer(r"\\historyportraitpair\*?(?:\s*\{[^{}]*\}){6}\s*\{([^{}]+)\}", self.tex):
            labelled.append((pair.start(), "fig:portrait:" + pair[1]))
        manuscript = [label for _, label in sorted(labelled)]
        pages = sorted(self.pages, key=lambda slug: int(self.pages[slug].metadata["order"]))
        # The appendix gives a restated exercise's figures local HTML IDs.
        articles = [figure.removeprefix("restated-") if figure else figure
                    for slug in pages for figure in self.docs[self.base + slug + "/"].article_figures]
        self.assertEqual(articles, manuscript)

    def test_margin_notes_keep_an_inline_copy_and_a_link_back_to_the_passage(self):
        for path, doc in self.docs.items():
            with self.subTest(page=path):
                self.assertEqual(set(doc.inline_notes), set(doc.note_references))
                self.assertEqual(doc.note_returns, set(doc.note_references.values()))
                for note, number in doc.inline_notes.items():
                    self.assertGreater(number, 0)
                    self.assertEqual(doc.ids[note], 1)
                if doc.inline_notes:
                    self.assertEqual(doc.ids["right-aside"], 1)

    def test_public_markdown_matches_reader_and_expands_shared_exercises(self):
        self.assertFalse(list(self.fragments.rglob("*.html")))
        copies = {}
        for route, doc in self.docs.items():
            resource = self.base + "index.md" if route == self.base else route.rstrip("/") + ".md"
            self.assertEqual(doc.copy_markdown_url, resource)
            self.assertNotIn(resource, doc.reader_links)
            self.assertIn("Copy for LLM", doc.text)
            text = (SITE / resource.lstrip("/")).read_text()
            self.assertTrue(text.startswith("# "), resource)
            self.assertNotRegex(text, r'(?m)^::|:span\[|\{id="|<template|<span class="katex|\]\(/notes/')
            for src, _ in doc.images:
                self.assertIn("https://xyzmaths.org" + src, text, resource)
            copies[route] = text
        math = inspect_markdown(list(copies.values()), "equations")
        for (route, doc), equations in zip(self.docs.items(), math):
            with self.subTest(route=route):
                self.assertEqual(equations, doc.equations)
        for ex in self.exercises.values():
            statement = ex["statement"].markdown.strip()
            appendix = copies[self.base + ex["solution-page"] + "/"]
            self.assertIn(statement, copies[self.base + ex["statement-page"] + "/"])
            self.assertIn(statement, copies[self.base + "problems/"])
            self.assertIn(statement, appendix)
            self.assertIn(ex["solution"].markdown.strip(), appendix)


class LinearAlgebraEdition(ReadingEditionChecks, unittest.TestCase):
    slug = "linear-algebra"


class AnalysisEdition(ReadingEditionChecks, unittest.TestCase):
    slug = "maths-analysis"


class ReaderBrowser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browsers = [os.environ.get("CHROME_BIN"), "chromium", "chromium-browser", "google-chrome", "google-chrome-stable",
                    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
        cls.chrome = next((path for name in browsers if name and (path := shutil.which(name))), None)
        if not cls.chrome:
            raise unittest.SkipTest("Headless Chromium is unavailable")

    def dump_dom(self, url, folder, *options):
        result = subprocess.run([
            self.chrome, "--headless", "--no-first-run", "--disable-background-networking",
            f"--user-data-dir={folder / 'profile'}", *options, "--dump-dom", url,
        ], capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    @contextmanager
    def reader_site(self):
        class ReaderFiles(SimpleHTTPRequestHandler):
            def translate_path(self, path):
                if path == "/copy-markdown.html":
                    return str(ROOT / "tests/web-notes/copy-markdown.html")
                return super().translate_path(path)

            def log_message(self, *args):
                pass

        with ThreadingHTTPServer(("127.0.0.1", 0), partial(ReaderFiles, directory=SITE)) as server:
            thread = Thread(target=server.serve_forever)
            thread.start()
            try:
                yield f"http://127.0.0.1:{server.server_port}"
            finally:
                server.shutdown()
                thread.join()

    def test_copy_after_tooltip_hydrates(self):
        with self.reader_site() as site, tempfile.TemporaryDirectory() as tmp:
            html = self.dump_dom(site + "/copy-markdown.html", Path(tmp), "--virtual-time-budget=8000")
        result = re.search(r"<output>([^<]*)</output>", html)
        self.assertIsNotNone(result, "The browser did not run the copy fixture")
        self.assertEqual(result[1], "Copied the chapter")

    def test_margin_uses_the_width_left_for_reading(self):
        chapter = BASE + "linear-algebra-i/kernel-image-and-rank/"
        # The contents drawer frees up space below the two-column tablet layout.
        with self.reader_site() as site, tempfile.TemporaryDirectory() as tmp:
            for width, beside in ((1100, True), (820, False), (760, True), (390, False)):
                with self.subTest(width=width):
                    html = self.dump_dom(site + chapter, Path(tmp), f"--window-size={width},900",
                                         "--virtual-time-budget=3000")
                    doc = Document(html)
                    notes = set(doc.note_references)
                    self.assertTrue(notes)
                    self.assertEqual(doc.margin_visible, beside)
                    self.assertEqual(set(doc.inline_notes), set() if beside else notes)
                    for note in notes:
                        self.assertEqual(doc.ids[note], 1)

    def test_wide_layout_only_moves_illustration_free_notes(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            page = folder / "book-margin.html"
            shutil.copyfile(ROOT / "tests/web-notes/book-margin.html", page)
            subprocess.run(["bun", "build", ROOT / "src/lib/book-margin.ts", "--target=browser",
                            "--outfile", folder / "book-margin.js"], check=True, capture_output=True)
            html = self.dump_dom(page.as_uri(), folder, "--allow-file-access-from-files", "--window-size=1600,900")
        output = re.search(r"<output>([^<]+)</output>", html)
        self.assertIsNotNone(output, "The browser did not run the margin fixture")
        placement = json.loads(output[1])
        for mode in ("inline", "wide", "restored"):
            with self.subTest(mode=mode):
                self.assertEqual(placement[mode]["passages"],
                                 ["first", "ordinary", "middle", "margin-figure", "last"])
                self.assertEqual(placement[mode]["figures"], ["ordinary", "margin-figure", "nested-figure"])
                self.assertEqual(placement[mode]["asideFiguresAndImages"], 0)
        self.assertEqual(placement["wide"]["rail"], ["math-note"])
        self.assertEqual(placement["wide"]["inlineNotes"], ["figure-note", "image-note"])
        self.assertEqual(placement["inline"]["inlineNotes"], ["math-note", "figure-note", "image-note"])
        self.assertEqual(placement["restored"], placement["inline"])


class FragmentPublication(unittest.TestCase):
    def test_generator_rejects_missing_duplicate_or_reclassified_math(self):
        original = [["DisplayMath", "x+1", 1]]
        for changed in ("No equation.", "$x+1$", "$$\nx+1\n$$\n\n$$\nx+1\n$$"):
            with self.subTest(markdown=changed):
                result = subprocess.run(["node", ROOT / "scripts/web-notes/math.mjs"], text=True,
                                        input=json.dumps({"equations": original, "bodies": [changed]}),
                                        capture_output=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Markdown math parity failed", result.stderr)

    def test_interrupted_publication_is_detected_and_retry_completes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            old = {"pages/a.md": b"before", "pages/b.md": b"before", "pages/retired.html": b"retire"}
            new = {"pages/a.md": b"after", "pages/b.md": b"after"}
            metadata = {"inputs": "original"}
            publish(root, old, metadata)
            stamp = (root / MANIFEST).read_bytes()

            def interrupt_second_write(path, data):
                if path.name == "b.md":
                    raise OSError("interrupted publication")
                atomic_write(path, data)

            with patch("fragments.atomic_write", side_effect=interrupt_second_write):
                with self.assertRaisesRegex(OSError, "interrupted publication"):
                    publish(root, new, {"inputs": "edited"})
            self.assertEqual((root / MANIFEST).read_bytes(), stamp)
            self.assertNotEqual(manifest(metadata, inventory(root)), stamp)
            self.assertEqual(publish(root, new, {"inputs": "edited"}), (1, 1))
            self.assertEqual((root / MANIFEST).read_bytes(), manifest({"inputs": "edited"}, inventory(root)))

    def test_reuse_repair_and_pruning(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            files = {"pages/chapter.md": b"one", "pages/retired/topic.md": b"old",
                     "exercises/hw04/statement.md": b"two", "figures/test.svg": b"svg"}
            meta = {"inputs": "first"}
            self.assertEqual(publish(root, files, meta), (4, 0))
            for name in (*files, MANIFEST):
                os.utime(root / name, (1000, 1000))
            self.assertEqual(publish(root, files, meta), (0, 0))
            self.assertTrue(all((root / name).stat().st_mtime == 1000 for name in (*files, MANIFEST)))

            files["pages/chapter.md"] = b"changed"
            del files["pages/retired/topic.md"]
            del files["figures/test.svg"]
            self.assertEqual(publish(root, files, {"inputs": "second"}), (1, 2))
            self.assertEqual((root / "exercises/hw04/statement.md").stat().st_mtime, 1000)
            self.assertFalse((root / "figures/test.svg").exists())
            self.assertFalse((root / "pages/retired").exists())

            (root / "pages/chapter.md").unlink()
            (root / "exercises/hw04/statement.md").write_bytes(b"damaged")
            stamp = (root / MANIFEST).read_bytes()
            self.assertNotEqual(manifest({"inputs": "second"}, inventory(root)), stamp)
            self.assertEqual(publish(root, files, {"inputs": "second"}), (2, 0))
            self.assertEqual(manifest({"inputs": "second"}, inventory(root)), stamp)


class ContentsList(HTMLParser):
    """Keep the list hierarchy and its links and buttons from one sidebar landmark."""

    def __init__(self, html):
        super().__init__()
        self.in_contents = False
        self.root = ElementTree.Element("nav")
        self.stack = [self.root]
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "aside":
            self.in_contents = attrs.get("aria-label") == "Book contents"
        if self.in_contents and tag in {"li", "a", "button", "svg"}:
            self.stack.append(ElementTree.SubElement(self.stack[-1], tag, attrs))
        elif self.in_contents and tag == "path" and self.stack[-1].tag == "svg":
            ElementTree.SubElement(self.stack[-1], tag, attrs)

    def handle_endtag(self, tag):
        if tag == "aside":
            self.in_contents = False
        elif self.in_contents and tag in {"li", "a", "button", "svg"}:
            self.stack.pop()

    def handle_data(self, data):
        node = self.stack[-1]
        if node.tag in {"a", "button"}:
            node.text = (node.text or "") + data


class PublishedBookContents(unittest.TestCase):
    def test_contents_labels_distinguish_groups_pages_and_sections(self):
        artwork = {}
        for kind, name in (("group", "folder"), ("page", "page"), ("section", "section")):
            svg = ElementTree.parse(ROOT / "src/assets/icons" / f"{name}.svg")
            artwork[kind] = [path.get("d") for path in svg.findall("{*}path")]
        for slug in ("linear-algebra-i/vector-spaces-and-bases", "front-matter/copyright",
                     "appendices/notation", "problems"):
            route = BASE + slug + "/"
            nav = ContentsList((SITE / route.strip("/") / "index.html").read_text()).root
            self.assertIsNotNone(nav.find(f".//a[@href='{route}'][@aria-current='page']"), route)
            for item in nav.iter("li"):
                label = item.find("a")
                expected = "group"
                if label is None:
                    label = item.find("button")
                else:
                    target = urlsplit(urljoin(route, label.get("href")))
                    if not target.fragment:
                        expected = "page"
                    elif target.path != BASE:
                        expected = "section"
                self.assertIsNotNone(label, route)
                with self.subTest(route=route, label=label.text):
                    self.assertEqual(item.get("data-entry-kind"), expected)
                    icons = label.findall("svg[@data-icon='inline-start']")
                    self.assertEqual(len(icons), 1)
                    self.assertEqual([path.get("d") for path in icons[0].findall("path")], artwork[expected])
                    self.assertEqual(icons[0].get("aria-hidden"), "true")
                    self.assertEqual(icons[0].get("focusable"), "false")

    def test_chapter_contents_follow_the_manuscript_hierarchy(self):
        part = "linear-algebra-i"
        route = BASE + part + "/vector-spaces-and-bases/"
        html = (SITE / route.strip("/") / "index.html").read_text()
        nav = ContentsList(html).root

        def linked_children(parent):
            return {urljoin(route, link.get("href")): item for item in parent.findall("li")
                    for link in item.findall("a")}

        labels = [button.get("aria-label") or button.text for button in nav.iter("button")]
        self.assertNotIn("Chapters", labels)
        parts = linked_children(nav)
        self.assertIn(BASE + "#" + part, parts)
        chapters = linked_children(parts[BASE + "#" + part])
        self.assertIn(route, chapters)
        topics = linked_children(chapters[route])

        expected = {}
        for level, anchor in Document(html).article_headings:
            href = route + "#" + anchor
            if level == 2:
                section = href
                expected[section] = []
            elif level == 3:
                expected[section].append(href)
        self.assertTrue(any(expected.values()), "The sample chapter must have sections and subsections.")
        self.assertEqual(list(topics), list(expected))
        for href, subsections in expected.items():
            with self.subTest(section=href):
                toggle = topics[href].find("button[@aria-expanded]")
                self.assertEqual(toggle is not None, bool(subsections))
                rendered = linked_children(topics[href])
                if rendered or (toggle is not None and toggle.get("aria-expanded") == "true"):
                    self.assertEqual(list(rendered), subsections)


if __name__ == "__main__":
    unittest.main()
