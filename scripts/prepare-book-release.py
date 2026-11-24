"""Prepare a book edition when its LaTeX inputs and reproducible PDF change."""

import filecmp
import hashlib
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


def highest_version(book, tags):
    versions = [0]
    for tag in tags.splitlines():
        match = re.fullmatch(rf"{re.escape(book)}-v([1-9][0-9]*)", tag)
        if match:
            versions.append(int(match[1]))
    return max(versions)


def manuscript_checksum(source, tracked):
    # latexmk writes one unescaped prerequisite per indented line of its Make rule.
    # Other entries include TeX Live files and, on some versions, auxiliary files.
    dependencies = set()
    for line in (source / "build/edition/main.deps").read_text(encoding="utf-8").splitlines():
        if line.startswith("    "):
            path = Path(os.path.normpath(line[4:].removesuffix("\\")))
            if path.is_relative_to(source):
                path = path.relative_to(source)
            if path in tracked:
                dependencies.add(path)
    if Path("main.tex") not in dependencies:
        raise ValueError("latexmk's dependency list is missing the tracked main.tex")

    digest = hashlib.sha256()
    for path in sorted(dependencies):
        digest.update(os.fsencode(path) + b"\0")
        with (source / path).open("rb") as data:
            digest.update(hashlib.file_digest(data, "sha256").digest())
    checksum = digest.hexdigest()
    print(f"Manuscript SHA-256 {checksum} from {len(dependencies)} tracked inputs.")
    return checksum


def historical_tree(revision, book_dir):
    # Tags and pushes from before the move keep their manuscripts under content/.
    for directory in (book_dir, Path("content") / book_dir.name):
        if subprocess.check_output(["git", "ls-tree", revision, "--", directory / "main.tex"]):
            return f"{revision}:{directory.as_posix()}"
    return None


def render(tree, book_dir, work, epoch, output):
    # Use the same directory, input timestamps, toolchain, and recipes for both editions.
    source = work / book_dir
    source.mkdir(parents=True)
    archive = work / "source.tar"
    subprocess.run(
        ["git", "archive", f"--mtime=@{epoch}", "-o", archive, tree],
        check=True,
    )
    subprocess.run(["tar", "-xf", archive, "-C", source], check=True)
    subprocess.run(
        ["make", "-C", source, "-f", (book_dir / "Makefile").resolve(), "release-pdf"],
        env={**os.environ, "SOURCE_DATE_EPOCH": epoch, "FORCE_SOURCE_DATE": "1", "TZ": "UTC"},
        check=True,
    )
    names = subprocess.check_output(["git", "ls-tree", "-rz", "--name-only", tree])
    tracked = {Path(os.fsdecode(name)) for name in names.split(b"\0") if name}
    checksum = manuscript_checksum(source, tracked)
    (source / "build/edition/main.pdf").rename(output)
    shutil.rmtree(source)
    return checksum


def prepare(book):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", book):
        raise ValueError("Expected a book directory name under books/")
    book_dir = Path("books") / book
    commit = os.environ["GITHUB_SHA"]
    before = os.environ.get("PUSH_BEFORE")
    endpoint = f"repos/{os.environ['GITHUB_REPOSITORY']}/releases?per_page=100"
    published_tags = subprocess.check_output(
        ["gh", "api", "--paginate", endpoint,
         "--jq", ".[] | select(.draft == false and .prerelease == false) | .tag_name"],
        text=True,
    )
    previous = highest_version(book, published_tags)
    baseline = None
    published_checksum = None
    if previous:
        baseline = f"{book}-v{previous}"
        ancestry = subprocess.run(["git", "merge-base", "--is-ancestor", commit, baseline])
        if ancestry.returncode == 0:
            print(f"{baseline} already covers this commit.")
            return
        if ancestry.returncode != 1:
            ancestry.check_returncode()
        notes = subprocess.check_output(
            ["gh", "release", "view", baseline, "--repo", os.environ["GITHUB_REPOSITORY"],
             "--json", "body", "--jq", ".body"], text=True,
        )
        marker = re.search(r"^<!-- xyzmaths-inputs-v1: ([0-9a-f]{64}) -->\r?$", notes, re.MULTILINE)
        if marker:
            published_checksum = marker[1]
    elif before and before != "0" * 40:
        baseline = before

    epoch = subprocess.check_output(["git", "show", "-s", "--format=%ct", commit], text=True).strip()
    with tempfile.TemporaryDirectory() as directory:
        work = Path(directory).resolve()
        shutil.copytree("mk", work / "mk")
        candidate = work / "candidate.pdf"
        checksum = render(f"{commit}:{book_dir.as_posix()}", book_dir, work, epoch, candidate)
        if checksum == published_checksum:
            print(f"{book}'s manuscript inputs match {baseline}.")
            return
        reference_tree = historical_tree(baseline, book_dir) if baseline else None
        if previous and not reference_tree:
            raise ValueError(f"Cannot find the {book} manuscript in its published tag {baseline}")
        if reference_tree:
            reference = work / "previous.pdf"
            reference_checksum = render(reference_tree, book_dir, work, epoch, reference)
            if checksum == reference_checksum or filecmp.cmp(candidate, reference, shallow=False):
                print(f"The {book} manuscript matches {baseline}.")
                return

        source = (book_dir / "main.tex").read_text(encoding="utf-8")
        match = re.search(r"^\\title\{([^{}\n]+)\}", source, re.MULTILINE)
        if not match:
            raise ValueError(f"{book_dir}/main.tex must define a plain-text title")
        title = match[1]
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        # A deleted release can leave its Git tag pointing at an older commit.
        existing_tags = subprocess.check_output(["git", "tag", "--list", f"{book}-v*"], text=True)
        version = f"v{max(previous, highest_version(book, existing_tags)) + 1}"
        filename = f"{slug}-{version}.pdf"
        release_dir = book_dir / "build/release"
        release_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(candidate, release_dir / filename)

    with Path(os.environ["GITHUB_OUTPUT"]).open("a", encoding="utf-8") as outputs:
        print(f"tag={book}-{version}", file=outputs)
        print(f"title={title} {version}", file=outputs)
        print(f"filename={filename}", file=outputs)
        print(f"manuscript_sha256={checksum}", file=outputs)


if __name__ == "__main__":
    prepare(sys.argv[1])
