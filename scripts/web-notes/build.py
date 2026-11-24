"""Generate each book's web edition from an isolated manuscript snapshot."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

from fragments import ARTWORK, MANIFEST, atomic_write, fragments, inventory, manifest, publish
from manuscript import Manuscript, chapter_pages, instrument, notation, tex_labels
from render import render

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TEX_SOURCES = {".tex", ".bib", ".bbx", ".cbx", ".sty", ".cls"}
EXTENSIONS = TEX_SOURCES | ARTWORK | {".pdf"}


def sources(book):
    for directory, folders, names in os.walk(book):
        folders[:] = [p for p in folders if p not in {"build", "images", ".git", "output"}]
        for name in names:
            path = Path(directory, name)
            if path.suffix in EXTENSIONS and (path.suffix != ".pdf" or "figures" in path.relative_to(book).parts):
                yield path


def fingerprint(files, versions):
    digest = hashlib.sha256()
    converter = list(HERE.glob("*.py")) + [HERE / "figures.tex", HERE / "math.mjs"]
    packages = json.loads((ROOT / "package.json").read_text())["devDependencies"]
    for name in ("katex", "satteri"):
        digest.update(f"{name}={packages[name]}\0".encode())
    for tool, version in sorted(versions.items()):
        digest.update(f"{tool}={version}\0".encode())
    for path in sorted(files + converter):
        digest.update(path.relative_to(ROOT).as_posix().encode() + b"\0")
        data = path.read_bytes()
        if path.suffix in TEX_SOURCES or path.suffix in {".py", ".mjs"}:
            data = data.replace(b"\r\n", b"\n")
        digest.update(hashlib.sha256(data).digest())
    return digest.hexdigest()


def biber_version_cache(command):
    binary = Path(shutil.which(command)).resolve()
    with binary.open("rb") as stream:
        if stream.read(2) == b"#!":
            # A system Perl script can pick up new modules without changing the script.
            return None
    info = binary.stat()
    identity = (str(binary), info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns)
    key = hashlib.sha256(repr(identity).encode()).hexdigest()
    return ROOT / ".astro" / "web-notes" / f"biber-{key}"


def toolchain(previous, tool_env):
    pandoc = os.environ.get("PANDOC") or shutil.which("pandoc") or str(ROOT / ".tools/pandoc")
    commands = {"pandoc": pandoc, "pdflatex": "pdflatex", "pdftocairo": "pdftocairo",
                "latexmk": "latexmk", "biber": "biber"}
    # A site-only checkout can verify the published export without installing the TeX toolchain.
    if not all(shutil.which(command) for command in commands.values()):
        return pandoc, {tool: previous.get(tool, "") for tool in commands}
    versions = {}
    for tool, command in commands.items():
        # Self-contained Biber distributions extract the entire executable for --version.
        cache = biber_version_cache(command) if tool == "biber" else None
        if cache:
            try:
                cached = cache.read_text()
                if cached.startswith("biber version: ") and len(cached.splitlines()) == 1:
                    versions[tool] = cached
                    continue
            except (OSError, UnicodeError):
                pass
        flag = "-v" if tool == "pdftocairo" else "--version"
        version = subprocess.check_output([command, flag], env=tool_env, text=True, stderr=subprocess.STDOUT)
        versions[tool] = version.splitlines()[0].strip()
        if cache:
            try:
                atomic_write(cache, versions[tool].encode())
            except OSError:
                pass  # A read-only checkout can still verify its export.
    return pandoc, versions


def run(args, cwd, env=None):
    proc = subprocess.run(args, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if proc.returncode:
        log = proc.stdout[-5000:].decode(errors="replace")
        raise ValueError(f"{args[0]} failed in {cwd}:\n{log}")


def graphics(manuscript, work, env):
    assets = {}
    diagrams = [(name, path) for name, path in manuscript.figures.items() if path.suffix == ".tex"]
    if diagrams:
        shutil.copyfile(HERE / "figures.tex", work / "web-figures.tex")
        libraries = [line for line in (work / "preamble.tex").read_text().splitlines()
                     if line.startswith(r"\usetikzlibrary")]
        settings = [rf"\input{{{path.as_posix()}}}" for path in manuscript.figure_settings]
        (work / "web-figure-settings.tex").write_text("\n".join([notation(work), *libraries, *settings]))
        (work / "web-figure-inputs.tex").write_text("\n".join(
            r"\input{" + path.relative_to(work).as_posix() + "}" for _, path in diagrams))
        run(["pdflatex", "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "web-figures.tex"], work, env)
    for i, (name, _) in enumerate(diagrams, 1):
        output = work / (name + ".svg")
        run(["pdftocairo", "-svg", "-f", str(i), "-l", str(i), "web-figures.pdf", str(output)], work)
        assets[output.name] = output.read_bytes()
    for name, path in manuscript.figures.items():
        if path.suffix == ".pdf":
            output = work / (name + ".svg")
            run(["pdftocairo", "-svg", "-f", "1", "-l", "1", str(path), str(output)], work)
            assets[output.name] = output.read_bytes()
        elif path.suffix in ARTWORK:
            assets[path.name] = path.read_bytes()
    return assets


def generate(book, files, binary, epoch, tool_env):
    for executable in (binary, "pdflatex", "pdftocairo", "latexmk", "biber"):
        if not shutil.which(executable):
            raise SystemExit(f"Missing {executable}. See docs/web-notes.md for the web note build prerequisites.")
    with tempfile.TemporaryDirectory(prefix="xyzmaths-notes-") as temp:
        work = Path(temp).resolve()
        for path in files:
            dest = work / path.relative_to(book)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, dest)
        env = {**tool_env, "SOURCE_DATE_EPOCH": str(epoch), "FORCE_SOURCE_DATE": "1", "TZ": "UTC"}
        # The first pass omits contents and bibliography pages. Read page numbers
        # from the unmodified manuscript only after its pagination has settled.
        run(["latexmk", "-pdf", "-no-shell-escape", "-interaction=nonstopmode",
             "-halt-on-error", "main.tex"], work, env)
        pagination = chapter_pages(work / "main.toc")
        instrument(work)
        run(["pdflatex", "-draftmode", "-no-shell-escape", "-interaction=nonstopmode",
             "-halt-on-error", "main.tex"], work, env)
        manuscript = Manuscript(work, tex_labels(work / "main.aux"), book.name)
        date = datetime.fromtimestamp(epoch, timezone.utc)
        manuscript.year = str(date.year)
        manuscript.print_date = date.strftime("%B %Y")
        pages = render(manuscript, binary, pagination)
        figures = graphics(manuscript, work, env)
        return fragments(pages, manuscript.problems.values(), figures)


def build_book(book, opts, tool_env):
    directory = ROOT / "src/generated/notes" / book.name
    marker = directory / MANIFEST
    stamp = marker.read_bytes() if marker.is_file() else b""
    previous = dict(line[2:].split(" ", 1) for line in stamp.decode(errors="replace").splitlines()
                    if line.startswith("# ") and " " in line[2:])
    files = list(sources(book))
    pandoc, versions = toolchain(previous, tool_env)
    checksum = fingerprint(files, versions)
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch is None and previous.get("inputs") == checksum and previous.get("epoch", "").isdecimal():
        epoch = previous["epoch"]
    if epoch is None:
        committed = ""
        if shutil.which("git"):
            committed = subprocess.run(["git", "log", "-1", "--format=%ct", "--", str(book)],
                                       cwd=ROOT, text=True, capture_output=True).stdout.strip()
        epoch = committed or max(p.stat().st_mtime for p in files)
    epoch = int(epoch)
    metadata = {"inputs": checksum, "epoch": epoch, **versions}
    if not opts.force and previous.get("inputs") == checksum and manifest(metadata, inventory(directory)) == stamp:
        return
    if opts.check:
        raise SystemExit(f"{book.name} fragments are missing, modified or stale. Run bun run notes:generate --book {book.name}.")
    output = generate(book, files, pandoc, epoch, tool_env)
    # Competing CLI and dev-server exports may render concurrently. Serialize the short
    # publication step on this existing file, and recheck the sources after acquiring it.
    with Path(__file__).open("rb") as lock:
        if os.name == "nt":
            import msvcrt
            msvcrt.locking(lock.fileno(), msvcrt.LK_LOCK, 1)
        else:
            import fcntl
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        if fingerprint(list(sources(book)), versions) != checksum:
            raise SystemExit("Manuscript or converter changed during generation. Run notes:generate again.")
        changed, removed = publish(directory, output, metadata)
    print(f"{book.name}: {len(output)} files, {changed} written, {removed} removed.")


def main(tool_env):
    books = {path.parent.name: path.parent for path in sorted((ROOT / "books").glob("*/main.tex"))}
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book", choices=books, help="Generate only this book (default: all manuscripts).")
    parser.add_argument("--check", action="store_true", help="Exit unsuccessfully if an export is missing or stale.")
    parser.add_argument("--force", action="store_true", help="Rebuild even if all inputs match.")
    opts = parser.parse_args()
    selected = [books[opts.book]] if opts.book else books.values()
    for book in selected:
        build_book(book, opts, tool_env)


if __name__ == "__main__":
    # MacTeX's Biber unpacks temporary files even for --version. Concurrent
    # exports need separate tool directories for both the probe and the build.
    with tempfile.TemporaryDirectory(prefix="xyzmaths-note-tools-") as tool_dir:
        main({**os.environ, "TMPDIR": tool_dir})
