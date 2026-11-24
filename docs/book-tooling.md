# Working on the books

Open the XYZ Maths directory as your editor workspace. Each book has its own
`main.tex`, formula sheet, homework entries, and output directory. The
[Linear Algebra guide](../books/linear-algebra/AGENTS.md) and the
[Mathematical Analysis guide](../books/maths-analysis/AGENTS.md) describe
their editorial conventions.

## Build commands

Install Make and a TeX Live or MacTeX distribution with pdfLaTeX, Tufte-LaTeX,
latexmk, Biber, makeindex, biblatex, marginfix, and needspace. From XYZ Maths,
`make books` builds both main PDFs and `make check` checks both books.
For one book, run the commands below in its directory, or use Make's
`-C` option, for example `make -C books/maths-analysis problem HW=hw02`.

| From the book directory | Result |
| --- | --- |
| `make` or `make book` | Builds `build/main.pdf` with its references and bibliography. |
| `make formula-sheet` | Builds `build/formula-sheet.pdf` from the shared appendix. |
| `make problem HW=hw02` | Builds `build/problems/hw02.pdf`. The default assignment is `hw01`. |
| `make problems` | Builds all existing `problems/hw*.tex` entries, including variants. |
| `make check` | Builds the book, formula sheet, and every handout in both supported working directories. |
| `make check-texshop` | Builds every handout from `problems/` with output beside the source. |
| `make watch` or `make watch-problems HW=hw02` | Rebuilds the selected document while editing. Stop with Ctrl-C. |
| `make clean` | Removes generated document and auxiliary files for these builds. |

Common recipes live in [mk/book.mk](../mk/book.mk). Linear Algebra also has
`make export-problem HW=hw04`, which uses latexpand to write a portable copy
to `build/export/hw04.tex`. Edit the shared sources and regenerate the export.
For Overleaf, upload the selected book directory and use `main.tex` with
pdfLaTeX. Each book includes its own project styles, figures, and bibliography.

On macOS, the [JPEG conversion script](../scripts/jpeg.sh) takes an input
image and an output filename. Keep the original scan and converted copy in
the selected book's ignored `images/` directory.

## VS Code and Cursor

The [workspace settings](../.vscode/settings.json) select latexindent and the
LaTeX Workshop recipe **latexmk (Biber and references)**. The recipe runs in
the directory containing the selected TeX root, writes the PDF beside that
source, and runs the required bibliography and reference passes. Magic program
comments are disabled for recipe selection. Root-file hints still select the
appropriate book or handout. Run **LaTeX Workshop: Build LaTeX project** to
refresh a preview. A citation displayed as its raw key needs a completed
bibliography pass.

Keep portable team choices in the workspace settings. To configure a local
executable, use **Preferences: Open User Settings (JSON)** in your active
profile. For example, a MacTeX installation outside the editor's `PATH` may
need the following entry in the user's existing settings object.

```json
{
  "latex-workshop.formatting.latexindent.path": "/Library/TeX/texbin/latexindent"
}
```

The formatter needs its Perl dependencies installed locally. See the
[LaTeX Workshop formatting guide](https://github.com/James-Yu/LaTeX-Workshop/wiki/Format)
and [recipe working-directory documentation](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile#latex-workshoplatexbuildfromfolder).

## TeXShop homework previews

Open a book's `problems/hwNN.tex` in TeXShop and choose **Typeset**. Its
`pdflatexmk` directive runs the required passes and writes the PDF beside the
source. While editing a nested statement or solution, its first-line directive
selects the complete handout.

```tex
% !TEX root = ../../hwNN.tex
```

Keep the book's root detection and input search path ahead of its preamble
and macros. Graphics and bibliography resources must resolve from both the
book directory and `problems/`. Keep the template and new handouts in sync.
When changing the template, compile it from both directories as well. The
automatic checks discover `hw*.tex` only.

If TeXShop's engine menu lacks `pdflatexmk`, move `pdflatexmk.engine` from
`~/Library/TeXShop/Engines/Inactive/Latexmk/` into `~/Library/TeXShop/Engines/`
and restart TeXShop. See the [TeXShop engine guide](https://github.com/texshop/texshop/blob/master/DocumentSources/TeXShop%20Tips%20%26%20Tricks/TeXShop%20TipsAndTricks.tex).

## Codex Stop hook

The [workspace hook](../.codex/hooks.json) calls the
[book check script](../scripts/codex-stop-check.sh). It checks the book
containing the session's working directory and any book with staged,
unstaged, or untracked changes. Changes to the root Makefile or common book
recipes check both. A site-only change from the repository root skips TeX.

Each checked book writes its own `build/codex-stop-check.log`. A failed
check reports its log in Codex. Review and trust the root hook through
`/hooks` to enable it for this checkout.

## Published PDFs

Each book has its own GitHub release series. Every edition contains that
book's main PDF and uses the next version in its series.

| Book | Publication workflow | Release tags |
| --- | --- | --- |
| Linear Algebra | [Publish Linear Algebra](../.github/workflows/publish-linear-algebra.yml) | [linear-algebra-vN](https://github.com/lbxa/xyzmaths/releases?q=tag%3Alinear-algebra-v) |
| Introduction to Mathematical Analysis | [Publish Mathematical Analysis](../.github/workflows/publish-maths-analysis.yml) | [maths-analysis-vN](https://github.com/lbxa/xyzmaths/releases?q=tag%3Amaths-analysis-v) |

On a push to `main`, each workflow first compares the Git tree IDs of its
book directory before and after the push. A website-only push stops here.
This check covers every file in the push, including large book imports.

For a changed directory, `make release-pdf` builds `main.tex` and asks
`latexmk` for its dependencies. The workflow computes a SHA-256 checksum
from the sorted paths and contents of the tracked inputs. These include the
bibliography files Biber reads, figures, local styles, and shared exercises.
Editing a standalone handout or an unused figure leaves the checksum alone.

Each release stores its input checksum in an HTML comment in its GitHub
release notes. A matching checksum skips publication. When the inputs
differ, the workflow rebuilds the tagged edition with the same pdfTeX
installation, build path, and timestamp as the candidate. pdfTeX omits
automatic PDF dates, trailer IDs, and engine-specific metadata. Comparing
the resulting PDFs catches changes to diagrams and hyperlink destinations
while allowing edits such as TeX comments to keep the existing edition.

An older release without a checksum uses the same rebuild check. Before
the first release, the workflow compares against the book at the start of
the push if it existed there. A push that changes both manuscripts produces
two releases. Each PDF is also available as a workflow artifact for 90 days.

Run `python3 -m unittest discover -s tests` from the repository root to
exercise the release decisions with Git, pdfLaTeX, and Biber in a temporary
repository.
