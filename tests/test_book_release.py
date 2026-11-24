"""Exercise the release decision with real Git, pdfLaTeX, and Biber in a temporary repo."""

from contextlib import chdir
from importlib import import_module
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
release = import_module("scripts.prepare-book-release")


class BookReleaseTest(unittest.TestCase):
    def setUp(self):
        directory = self.enterContext(tempfile.TemporaryDirectory())
        self.enterContext(chdir(directory))
        self.book = Path("books/sample")
        shutil.copytree(ROOT / "tests/book-release", self.book)
        shutil.copyfile(ROOT / "books/maths-analysis/Makefile", self.book / "Makefile")
        shutil.copytree(ROOT / "mk", "mk")
        shutil.copyfile(ROOT / ".gitignore", ".gitignore")
        subprocess.run(["git", "init", "--quiet"], check=True)
        self.enterContext(patch.dict(os.environ, {
            "GITHUB_REPOSITORY": "test/books", "GITHUB_OUTPUT": "outputs", "PUSH_BEFORE": "",
        }))
        self.release_notes = {}
        real_check_output = subprocess.check_output

        def check_output(args, **kwargs):
            if args[:2] == ["gh", "api"]:
                return "\n".join(self.release_notes)
            if args[:3] == ["gh", "release", "view"]:
                return self.release_notes[args[3]]
            return real_check_output(args, **kwargs)

        self.enterContext(patch.object(subprocess, "check_output", check_output))

    def commit_book(self):
        subprocess.run(["git", "add", "--", self.book], check=True)
        subprocess.run(["git", "-c", "user.name=Test", "-c", "user.email=test@example.org",
                        "-c", "commit.gpgsign=false", "commit", "-qm", "Change fixture"], check=True)
        os.environ["GITHUB_SHA"] = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()

    def edition(self):
        self.commit_book()
        outputs = Path(os.environ["GITHUB_OUTPUT"])
        outputs.unlink(missing_ok=True)
        release.prepare("sample")
        if not outputs.exists():
            return None
        values = dict(line.split("=", 1) for line in outputs.read_text().splitlines())
        tag = values["tag"]
        digest = values["manuscript_sha256"]
        self.assertRegex(digest, r"^[0-9a-f]{64}$")
        self.assertTrue((self.book / "build/release" / values["filename"]).read_bytes().startswith(b"%PDF"))
        subprocess.run(["git", "-c", "tag.gpgsign=false", "tag", tag], check=True)
        self.release_notes[tag] = f"<!-- xyzmaths-inputs-v1: {digest} -->"
        return tag

    def replace(self, name, old, new):
        path = self.book / name
        content = path.read_text()
        self.assertIn(old, content)
        path.write_text(content.replace(old, new))

    def test_editions_across_the_book_directory_move(self):
        current = self.book
        legacy = Path("content") / current.name
        legacy.parent.mkdir()
        current.rename(legacy)
        self.book = legacy
        self.commit_book()
        before_move = os.environ["GITHUB_SHA"]
        os.environ["PUSH_BEFORE"] = before_move

        subprocess.run(["git", "mv", legacy, current], check=True)
        self.book = current
        self.assertIsNone(self.edition())

        subprocess.run(["git", "-c", "tag.gpgsign=false", "tag", "sample-v1", before_move], check=True)
        self.release_notes["sample-v1"] = "Edition published before the move."
        self.replace("main.tex", "\\begin{document}", "% editorial note\n\\begin{document}")
        self.assertIsNone(self.edition())
        self.replace("main.tex", "example.org/first", "example.org/second")
        self.assertEqual(self.edition(), "sample-v2")

    def test_editions_follow_the_published_manuscript(self):
        self.assertEqual(self.edition(), "sample-v1")
        (self.book / "handout.tex").write_text("Standalone handout.")
        with patch.object(release, "render", wraps=release.render) as render:
            self.assertIsNone(self.edition())
            self.assertEqual(render.call_count, 1)

        self.replace("sections/first topic.tex", "rectangle", "rect% nonprinting comment\nangle")
        self.replace("references.bib", "Uncited notes", "Other uncited notes")
        self.assertIsNone(self.edition())

        self.replace("main.tex", "example.org/first", "example.org/second")
        self.assertEqual(self.edition(), "sample-v2")
        self.release_notes["sample-v2"] = "An older release without a checksum."
        self.replace("main.tex", "\\begin{document}", "% editorial note\n\\begin{document}")
        self.assertIsNone(self.edition())

        self.replace("references.bib", "Cited notes", "Revised notes")
        self.assertEqual(self.edition(), "sample-v3")
        (self.book / "supplement.tex").write_text("\\rule{3em}{1em}")
        self.assertEqual(self.edition(), "sample-v4")
        (self.book / "supplement.tex").unlink()
        self.assertEqual(self.edition(), "sample-v5")

        self.replace("main.tex", "\\begin{document}", r"\undefinedFixtureCommand\begin{document}")
        with self.assertRaises(subprocess.CalledProcessError):
            self.edition()
        self.assertFalse(Path(os.environ["GITHUB_OUTPUT"]).exists())
