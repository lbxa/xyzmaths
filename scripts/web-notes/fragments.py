"""Serialize Markdown with YAML frontmatter and publish only changed files."""

import hashlib
import json
import os
from pathlib import Path
import tempfile


MANIFEST = "checksums.sha256"
ARTWORK = {".svg", ".png", ".jpg", ".jpeg", ".webp"}


def frontmatter(metadata):
    # JSON scalars and flow arrays are valid YAML, including quotes and Unicode.
    fields = [f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in metadata.items()
              if value is not None]
    return "---\n" + "\n".join(fields) + "\n---\n\n"


def fragments(pages, exercises, figures):
    files = {}
    for page in pages:
        attrs = {key: page[key] for key in ("title", "group", "order", "part", "page")}
        if page["outline"]:
            attrs["outline"] = page["outline"]
        blocks = []
        for block in page["blocks"]:
            if "markdown" in block:
                blocks.append(block["markdown"])
            else:
                role, key = next(iter(block.items()))
                blocks.append(f'::{role}{{key={json.dumps(key, ensure_ascii=False)}}}')
        files[f"pages/{page['id']}.md"] = (frontmatter(attrs) + "\n\n".join(blocks) + "\n").encode()
    for exercise in exercises:
        directory = Path(exercise["source"]).relative_to("problems").parent
        if ".." in directory.parts:
            raise ValueError(f"Expected a book-relative exercise path: {exercise['source']}")
        header = frontmatter({
            "key": exercise["key"], "source": exercise["source"], "title": exercise["title"],
            "number": exercise["number"], "assignment": exercise["assignment"], "question": exercise["question"],
            "statement-page": exercise["statementPage"], "solution-page": exercise["solutionPage"],
        })
        files[f"exercises/{directory.as_posix()}/statement.md"] = (header + exercise["statement"].rstrip() + "\n").encode()
        files[f"exercises/{directory.as_posix()}/solution.md"] = (exercise["solution"].rstrip() + "\n").encode()
    for name, data in figures.items():
        files[f"figures/{name}"] = data
    return files


def inventory(directory):
    hashes = {}
    # The previous edition used HTML fragments. Retire them with the same transactional inventory.
    for area, extensions in (("pages", {".md", ".html"}), ("exercises", {".md", ".html"}), ("figures", ARTWORK)):
        for path in (directory / area).rglob("*"):
            if path.suffix in extensions and path.is_file():
                try:
                    data = path.read_bytes()
                except FileNotFoundError:
                    # A concurrent publication can retire the file during a freshness check.
                    continue
                hashes[path.relative_to(directory).as_posix()] = hashlib.sha256(data).hexdigest()
    return hashes


def manifest(metadata, hashes):
    header = "".join(f"# {key} {value}\n" for key, value in metadata.items())
    entries = "".join(f"{digest}  {name}\n" for name, digest in sorted(hashes.items())).encode()
    # Detect an incomplete copy even when the omitted files and checksum lines agree.
    return (header + f"# outputs {hashlib.sha256(entries).hexdigest()}\n").encode() + entries


def atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    out = tempfile.NamedTemporaryFile(dir=path.parent, delete=False)
    temporary = Path(out.name)
    try:
        with out:
            out.write(data)
        temporary.chmod(0o644)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def publish(directory, files, metadata):
    previous = inventory(directory)
    hashes = {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}
    changed = [name for name in files if hashes[name] != previous.get(name)]
    removed = previous.keys() - files.keys()
    for name in changed:
        atomic_write(directory / name, files[name])
    for name in removed:
        path = directory / name
        path.unlink()
        parent = path.parent
        while parent.parent != directory and not any(parent.iterdir()):
            parent.rmdir()
            parent = parent.parent
    # Commit the inventory last. An interrupted write is detected and repaired on the next run.
    marker = directory / MANIFEST
    stamp = manifest(metadata, hashes)
    if not marker.exists() or marker.read_bytes() != stamp:
        atomic_write(marker, stamp)
    return len(changed), len(removed)
