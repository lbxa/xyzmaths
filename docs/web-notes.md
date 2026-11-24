# Linear Algebra on the web

The XYZ Books catalog at `/books/` links to the Linear Algebra reading edition
and its released manuscript PDF. The canonical overview at `/notes/linear-algebra/`
follows the active inputs in the book’s `main.tex`. Each chapter, appendix
and front-matter entry has its own static
HTML reading page and a Markdown edition. The assignment view lives at
`/notes/linear-algebra/problems/`.

The manuscript link at `/books/linear-algebra/manuscript.pdf` resolves the
highest public `linear-algebra-vN` GitHub Release with its uploaded PDF.
Until the shared repository has a public edition, readers receive v3 from
the original Linear Algebra repository. The catalog and the reader use the
same link, so publishing a PDF does not require rebuilding the website.

**Copy for LLM** copies the current page as Markdown with its exercises,
footnotes, captions, links and original TeX equations. The first chapter’s
Markdown file is available at
`/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases.md`.
`index.md` contains the book overview and `problems.md` contains all statements
in assignment order.

Figures appear in the main reading column with their captions, including those
printed in the book’s margin. If a print figure separates a sentence from the
equation it introduces, the web edition places the figure after the equation.
Numbered text notes sit beside their references when the reading pane has
at least 42rem of usable width. In a narrower pane, in print, or with
JavaScript disabled, each note follows its source passage. The note number
and return link work in both layouts. Pages without text notes use the full pane.

## Build and verify

Use the repository’s Node 26 environment, Bun and Python 3.10 or later.
Install the website dependencies with `bun install --frozen-lockfile`.
The repository includes the generated Markdown and artwork. A website-only
build can use these files on a machine without the manuscript conversion tools.

```sh
bun run notes:check
bun run build
```

After changing the manuscript or the converter, make Pandoc, latexmk, Biber,
pdfLaTeX, and Poppler’s `pdftocairo` available. The TeX installation needs the book’s
ordinary packages, TikZ and the `standalone` class. The first export used
Pandoc 3.6.4 and TeX Live 2025. The converter looks for Pandoc on `PATH` or
at `.tools/pandoc`. Set `PANDOC` to use a different executable.

```sh
bun run notes:generate
bun run notes:test
```

The test builds the website and checks both editions against the manuscript.
It checks chapter and assignment order, repeated statements, solutions and
pending notices, internal destinations, figure order, image assets, margin-note
backlinks and selective file writes. It also compares the TeX and display mode
of each equation in each public Markdown file with its rendered MathML annotation.
With Chrome or Chromium installed, it checks where the reader places figures
and notes on a wide screen. Set `CHROME_BIN` to select a specific executable.
To repeat the checks after building, run `python3 -B tests/verify_web_notes.py`.

Run `bun run notes:test:changes` with the full conversion toolchain to test
changes in temporary copies of the Linear Algebra book. The suite builds
Astro pages after moving exercises, adding nested lists and margin notes,
filling a pending solution, changing shared notation or citations, and
replacing artwork. It compares a moved exercise’s number and the starting
pages of its chapter and appendix to an independent print build. It also
checks failed conversions, concurrent repairs, and reuse without TeX.

Preview the site with `bun run dev --background`. Astro also requests a
fresh export on a build or when a manuscript input changes in development.
The static notes and graphics are written under
`dist/client/notes/linear-algebra/`.

## How the manuscript becomes a collection

1. The converter fingerprints the Linear Algebra inputs, converter sources,
   pinned KaTeX and Satteri versions and the Pandoc, latexmk, Biber,
   pdfLaTeX and Poppler versions. It
   checks the generated files against their SHA-256 hashes. A matching export
   skips conversion. With a complete local toolchain it also checks the
   installed versions. A website-only checkout uses the recorded versions.
2. A clean latexmk build in a temporary copy supplies the sidebar’s printed
   chapter and appendix page numbers from the finished table of contents.
   The subsequent draft pdfLaTeX pass supplies counters for unlabelled results
   and the lists of figures, tables and theorems. Active TeX inputs supply the
   reading order. The adapter recognizes the book’s Tufte commands, theorem
   environments and shared exercise conventions.
3. Pandoc reads the assembled document, resolves citations and writes
   Markdown. Inline math uses `$…$` and display math uses `$$` fences,
   with manuscript equation numbers retained. The converter checks the TeX
   with KaTeX before publishing. It parses the generated Markdown and fails
   the conversion if a formula goes missing, gains a copy, or changes display
   mode. TikZ drawings compile to SVG using the book’s notation and libraries.
   Diagrams display at 150% of their print dimensions, up to the width of the
   reading column. Select a diagram to open the original SVG for closer inspection.
4. The converter writes the generated files under
   [src/generated/notes/linear-algebra](../src/generated/notes/linear-algebra).
   Include the changed fragments, assets and `checksums.sha256` with manuscript
   changes. A changed input triggers a whole-book conversion to resolve counters,
   citations and cross-chapter links. Only files with new bytes are written.
   Retired pages, exercises and figures are removed. Use
   `bun run notes:generate --force` to repeat the conversion with current inputs.
5. Astro’s loader reads the files into `bookPages`, `bookExercises` and
   `bookFigures`. Satteri parses the Markdown, including the book’s directives
   for numbered results, captions and exercise placements. KaTeX renders
   accessible HTML and MathML at build time. The chapter, appendix and problem
   index each use the same exercise statements. The standalone handouts supply
   assignment order. The loader also expands each page as portable Markdown
   with absolute reader and figure links for the public `.md` route.

### Generated files

| File within the generated book | Contents |
| --- | --- |
| `pages/<page-id>.md` | YAML frontmatter records title, group, order, part, print page and the manuscript’s heading hierarchy and stable anchors. The body holds the chapter or appendix. The directives `::statement{key="…"}` and `::solution{key="…"}` mark exercise placements. |
| `exercises/<assignment-or-lecture>/<problem>/statement.md` | One canonical Markdown statement with its manuscript key, source, number and placements in frontmatter. |
| `exercises/<assignment-or-lecture>/<problem>/solution.md` | The supplied Markdown solution or the manuscript’s pending notice. |
| `figures/<asset>` | Individual SVGs and any original raster image files, ready to serve at the existing figure URLs. |
| `checksums.sha256` | The inputs fingerprint, rendering date, tool versions and a checksum of the entire file list, followed by a SHA-256 checksum and relative path per file. |

Use `getCollection("bookExercises")` for another problem view. Each entry
has its source path, print number, chapter, appendix, assignment and question
number. Astro’s `render(entry)` supplies the typeset statement and
`entry.body` supplies the portable Markdown. The solution is available as
`entry.data.solutionMarkdown` and as rendered HTML in `entry.data.solution`.
Canonical chapter and appendix anchors use
the manuscript’s `ex:` and `sol:` labels.

## Extending the converter

Book-specific TeX commands are adapted in `scripts/web-notes/manuscript.py`.
Pandoc document handling and link resolution live in
`scripts/web-notes/render.py`. Markdown serialization and publication
live in `scripts/web-notes/fragments.py`. The web renderer and portable
Markdown export share the directive vocabulary in `src/lib/note-markdown.mjs`.
Unknown raw TeX, an unsupported equation,
missing artwork, or inconsistent exercise placement fails generation before
the previous collection is replaced. Add a mapping and exercise it against
the rendered pages when introducing a new manuscript convention.

Mathematical Analysis can use the same collection model after its own
notation, environments and exercise conventions have been checked. Once a
book’s overview, chapters and exercise index are available, add its entry to
the [book list](../src/lib/books.ts) shared by the catalog and reader selector.

The upstream references describe the document and loader interfaces.
[Pandoc manual](https://pandoc.org/MANUAL.html) ·
[Astro Content Loader API](https://docs.astro.build/en/reference/content-loader-reference/) ·
[KaTeX rendering options](https://katex.org/docs/options)
