# Introduction to Mathematical Analysis

Use the [XYZ Maths book conventions and skills](../../AGENTS.md#books) along
with this guide. Paths below are relative to `books/maths-analysis/`.

## Project Structure & Organization

Collaborative Tufte-style notes cover Mathematical Analysis I and II.

- `main.tex` assembles the book; `preamble.tex` holds packages and layout; `macros.tex` defines shared notation and theorem environments.
- `formula-sheet.tex` is a standalone entry that inputs `sections/appendices/formula-sheet.tex`; keep its ordered formulas and proof reminders in the shared topic files under `sections/appendices/formula-sheet/`.
- `sections/analysis-i/part.tex` orders nine chapter directories. Each numbered directory contains `chapter.tex` and one numbered `.tex` file per topic, e.g. `01-sets-and-foundations/06-supremum.tex`.
- `sections/analysis-ii/part.tex` is reserved and excluded from the book until needed.
- `sections/front-matter/` holds copyright, introduction, and acknowledgements; `sections/appendices/` contains notation, assumed knowledge, and the solutions chapter.
- `problems/hwNN.tex` are standalone homework handouts using the shared preamble and macros.
- `problems/hwNN/NN-topic/problem.tex` holds a shared exercise statement; the adjacent `solution.tex` holds its solution. Do not add an `exercises/` subdirectory.
- `figures/` holds mathematical diagrams and credited historical portraits. `bibliography.bib` holds shared references. `build/` contains ignored generated output.

## Builds and homework placement

Run the [shared book commands](../../docs/book-tooling.md#build-commands) in
this directory. Preserve the homework template's `\analysisroot` detection
and `\input@path` before loading the preamble. Graphics, shared statements,
and the bibliography must resolve from both the book directory and
`problems/`. Each nested homework fragment points to its homework entry,
and chapter fragments point to `main.tex`. See the
[TeXShop preview guide](CUSTOMISATION.md#texshop-homework-previews).

Maintain the [homework placement map](README.md#homework-placement-map) using
the [shared homework workflow](../../.agents/skills/homework-to-book-exercises/SKILL.md).
Use the map's Included, Not yet included, or Deferred status and record pending
solutions. Explain deliberate forward uses in the text. Let the handout and
appendix paginate naturally. Use `\handoutonly{...}` for a handout-specific
layout hint in a shared solution. Keep the template unchanged unless requested.
For an example, see [Homework 02](problems/hw02.tex). For alphabetic subparts,
set `\labelenumi` before `\begin{enumerate}` and check wrapped-line alignment.

## Editorial Principles

For the author's supplied homework solutions, use the project
[homework-solutions-to-book skill](../../.agents/skills/homework-solutions-to-book/SKILL.md).
Preserve their proof strategy, character, tone, notation, and valid working.
Correct mathematical errors and gaps with focused amendments. Do not substitute
a different proof by default or merely to match the assistant's preferred style.
Preserve expanded terms before summation notation when the author uses them
to explain a pattern. State how to truncate a short sum rather than removing
the expanded working.

Preserve the author's style and the course's flow of topics when turning lecture notes into publishable text. Capture all supplied mathematical content, including examples and questions. Improve clarity and organization without expanding the notes into an unrelated textbook; add only the supporting explanation needed for a coherent foundation.

Keep the lecturer's syllabus chapters and sections, including their titles and order, as the organising framework. Reorganise content within that framework to introduce tools before their substantial use and before exercises that require them. Keep early motivation concise and return to its proof after the prerequisites. Consult this book's README and the relevant chapter changelogs before structural edits, and record agreed decisions and their rationale there.

Maintain the same mathematical topic order in summaries, formula sheets,
recaps, and appendix reference material as in the book's chapter and section
inputs. Group related entries under clear topic headings, with finite-sum
background before sequences and infinite series and sequence criteria in
their chapter order. Place additions with their topic rather than appending
them in editing order. Preserve deliberate prerequisite recalls and closing
syntheses, linking them to their main treatment instead of duplicating or
reordering the syllabus.

Keep the rendered book independent of the semester schedule. Week numbers,
lecture dates or numbers, import batches, and coverage progress belong only
in internal README records, source filenames, and non-rendered TeX comments.
In reader-facing prose, headings, captions, and front matter, describe
mathematical topics and refer to chapters or sections. Preserve necessary
statements about assumptions, omitted proofs, and prerequisite dependencies.

Write the mathematical exposition as a self-contained book. Do not refer
readers to unpublished class discussions or handwritten lecture notes with
phrases such as "the lecture explains", "the notes state", or "as we did in
class", and do not cite those notes as if they were a published source.
Credit Professor Yisong Yang of NYU Courant in the acknowledgements instead.
Keep original classroom wording and source provenance in non-rendered TeX
comments and internal README records. Retain explicit assumptions and proof
omissions in mathematical terms, and preserve citations to identifiable,
retrievable published sources, including external published lecture notes.
For a lecture import, keep page provenance in source comments. Add a
page-by-page README coverage table when the author requests one. Preserve
the foundations chapter's early treatment of convergence, iteration, and
completeness before the later sequences chapter.

Present imported lecture questions and tasks as examples with mathematical
titles, using the shared `example` environment rather than headings such as
"A question from the lecture". Give the working needed to make the example
self-contained using established tools, and keep its original classroom
prompt in internal source comments. Preserve the shared homework exercise
system for actual assignments.

Use shared mathematical environments and styles so the same kind of content has consistent typography wherever it appears. Reusing an exercise in an appendix must preserve its identity and presentation as an exercise.

## Style & Contribution Conventions

Work in the smallest relevant topic file. Use two-space indentation, lowercase hyphenated names, and explicit `\input` lists. Number files for reading order; keep labels independent of numeric prefixes, e.g. `sec:analysis-i:supremum`. Use `ch:`, `sec:`, `thm:`, `eq:`, `fig:`, and `ex:` prefixes. Keep shared notation in `macros.tex` and figure names topic-specific. Use black and gray for diagrams by default; reserve colour for a specific highlight or distinction.

Use `\autoref{...}` for numbered object references throughout the book and handouts, including body text, margin notes, captions, and proof headings. The shared definitions in `macros.tex` supply full, capitalised names such as Figure, Table, Theorem, Lemma, Proposition, Corollary, Definition, Property, Example, Exercise, and Remark. Equations render as `Equation (1.2)`; sections and subsections render as `§ 1.2`. Do not prepend an object name or `\S`, use bare `\ref` or `\eqref`, or type reference numbers by hand. For a range, reference both endpoints with `\autoref`, for example `\autoref{sec:first}--\autoref{sec:last}`. Use `\autoref*` only when intentionally suppressing a link, and retain `\pageref` for page numbers and descriptive `\hyperref` links for solution navigation. Define new numbered result environments through `\newsharedtheorem` so their automatic names remain distinct while they share the theorem counter. Preserve the late `hyperref` load and shared `caption` setup in `preamble.tex`.

- In displayed equations, use `\quad` to separate leading quantifiers from their statements.
- In set-builder notation, use `\mid` and rely on LaTeX's automatic spacing.
- Add `\,` only when a small extra gap improves readability; do not add it automatically to every set.

Mark only additions and replacements awaiting author review, at the smallest
readable span. Keep the author's unchanged wording, equations, proof heading,
and conclusion in their normal colour; do not wrap an existing proof or section
just because some of it was edited. Use the shared `pendingreview` environment
in `macros.tex` for a wholly new or replaced passage, and
`\pendingreviewtext{...}` for an inline correction or part of an equation.
The muted slate blue (`#486581`) denotes pending editorial status.
For a wholly new theorem, proof, or example, keep its normal environment
inside the wrapper, preserving its typography, numbering, and links.
Use this component rather than local colour commands, and reserve its colour
for review status.
After the author approves a passage, remove only its review wrapper so the
content returns to the surrounding text colour. Do not remove pending status
without the author's approval.

Write proofs in clear English with complete sentences and proper grammar and punctuation. Do not use colons in proof prose. The main body must form a complete, continuous proof when the margin is ignored. Keep essential theorem and lemma invocations, the relevant hypotheses, their application, and every logical step and conclusion in the body. Reserve the right margin for visual guides, optional reminders of general results, and secondary observations. Do not move a necessary justification into a sidenote merely because it mentions a theorem or lemma, and avoid repeating the same reminder throughout a handout.

Present final answers and proof conclusions as ordinary displayed equations,
without `\boxed`, `\fbox`, or other enclosing outlines. Use the shared proof
environment's QED marker to signal completion and keep the conclusion's
typography consistent with the surrounding mathematics.

Align margin notes with the relevant passage and leave them unnumbered, without footnote-style markers in the body. Match figure-caption text size to ordinary margin text. Author mathematical diagrams in TikZ with consistent styling; use margin figures for compact illustrations and full-width figures when they need the space.

Keep margin placement in the shared `preamble.tex` configuration. It uses
`marginfix` to stack complete figures and captions with a 12pt gap and a
6pt bottom reserve, moving excess margin content intact to the next page.
Optional margin offsets are preferred callout positions, not guaranteed
placements. Do not insert negative space, smashed content, or manual page
breaks to fit a crowded margin. Give a diagram that cannot fit in one margin
a main-text or full-width figure instead of shrinking its labels. Preserve
Tufte's standard height handling for ordinary and full-width figures. Their
margin captions must not reserve vertical space in the main text; leave the
class's internal caption handling unchanged.

Use bold caption labels and numbers followed by a full stop, for example **Figure 1.1.** or **Table 2.1.**, with ordinary-weight caption text. Apply this through the shared `caption` configuration in `preamble.tex` for every float type in the book and handouts; retain Tufte's margin font and alignment rather than formatting individual captions by hand.

Replace `TUFTE PLACEHOLDER` blocks with reviewed notes; remove unused specimen assets/helpers. Cite sources with stable keys. Coordinate reordering and shared-file edits to reduce conflicts. Preserve the documented `nohyper` contents workaround unless testing a deliberate layout revision.

Use the alphabetic AMS reference style, with bracketed author-based labels such as `[Can83]` and `[Rod20]` and an alphabetically ordered bibliography after the main content and before the appendices. The shared preamble uses Biber, the project AMS style in `styles/analysis-ams.bbx`, and the bundled `ams-alphabetic` citation style. Preserve their portable paths for standalone homework builds. Generate labels from bibliography metadata, including disambiguation where needed; do not substitute numbered citations or type labels by hand. Citation keys must resolve to readable references rather than appearing as raw keys or margin footnotes.

Match the bibliography entry typography in the author's reference paper,
as documented in `styles/README.md`: author initials, upright article and
webpage titles, italic journal and book titles, and journal details in
`volume(issue):pages, year` order. Repeat authors in each entry, retain
clickable DOI/URL links, and use structured metadata rather than formatting
publication details inside `.bib` fields. Keep the same shared style in the
book and standalone documents.

### Historical context and portraits

Add concise, optional historical context at the substantive treatment of
named or securely attributable results, definitions, propositions, and
methods. Use `\historynote{...}` so new notes remain pending review.
Explain the original problem, relevant date and collaborators or predecessors,
the reason for the formulation, and a useful mathematical impact. Avoid
repeating a biography at every later occurrence or on the formula sheet.
Do not infer discovery from an eponym or assign an anonymous elementary
fact to a famous person without evidence. Distinguish composition,
communication, publication, proof, and later modern reformulation.

Cite original mathematical texts, letters, or manuscripts for historical
claims; identify later historical interpretations as such. The historical
review and its primary evidence are different sources. Record provenance
limits and disputed dates in `docs/history-inventory.md`.

Use margin-width portraits with the shared `\historyportrait` and
`\historyportraitpair` helpers. Single portraits fill the margin; paired
portraits each use 49% of its width with a 2% gap, in one unbreakable row.
Preserve native proportions without a small height cap that reduces these
widths. Refer to each figure from its historical
note. Retain source, creator/date when established, reproduction licence,
and acquisition metadata in `figures/portraits/`. A university reproduction
gallery is an image source, not proof of an original object's provenance.
Do not substitute a similarly named person or present a later imagined
depiction as a contemporary likeness. Keep borrowed image licences
separate from the book's original CC BY-NC-ND 4.0 text.

### TikZ diagram design

A diagram should clarify a specific mathematical idea through accurate geometry,
simple visual hierarchy, and generous whitespace. Clean spacing is a requirement
of the first finished version. Check the rendered result before presenting it.

- Plan the layout at its final printed size. Use margin figures for compact
  illustrations and full-width figures when the content needs more room. Keep
  text readable at the normal margin font size; simplify the layout or give it
  more space when it becomes crowded.
- Give labels clear space around their entire visible shape. Letters must not
  touch or cross lines, curves, point markers, arrowheads, or other labels.
  Use explicit physical offsets such as `below=5pt` or `right=4pt` as starting
  points, then check the actual gap. Account for marker radii, text height,
  superscripts, and descenders; a default `below` or `left` anchor does not
  guarantee clearance.
- Align comparable elements and use consistent row spacing, label positions,
  and gutters. Leave enough room between rows for both their labels and their
  distance arrows. Give the plot, legend, and caption distinct space.
- Place labels in open regions of the drawing. Put an origin label in a clear
  quadrant and keep axis names away from arrowheads. When curve names cannot
  fit comfortably beside their curves, use a separate legend with matching
  line samples. Preserve the mathematical strokes when resolving collisions.
- Keep the visual hierarchy restrained. Use black for the main construction
  and gray or dashed lines for secondary guides. Remove unnecessary tick
  labels and annotations when they compete with the idea being illustrated.
  Keep line weights, arrowheads, marker sizes, and fonts consistent across
  related diagrams.
- Use the shared thin `0.5pt` line weight for ordinary diagram edges, axes,
  and outlines throughout the book. Inherit it from `interval diagram` or
  `analysis diagram`; do not introduce `thick`, `semithick`, or a larger local
  line width for a new figure. Check the resolved width of additional styles,
  since a style such as `analysis curve` can override the picture's default.
  Use gray, dashes, or light fills for distinctions instead of heavier strokes.
  Compare the rendered strokes with an existing diagram at the same printed
  size, as well as checking label clearance.
- Use the shared styles in `figures/interval-styles.tex` for interval diagrams,
  including their line weights, endpoint diameters, arrowheads, fonts, and row
  spacing. Open and closed endpoints differ by fill only. Use explicit physical
  radii for circular point markers, e.g. `circle[radius=1.6pt]`, so unequal
  TikZ `x` and `y` units do not flatten them into ellipses.
- Preserve the mathematical meaning. Represent unbounded intervals with arrows,
  never a point at infinity; use ellipses to continue a sequence rather than
  inventing a final interval. Label schematic drawings explicitly and do not
  show excluded limit points as included endpoints. For function plots, draw
  the stated function, label arrowed axes, mark relevant intercepts, and put
  arrowheads on continued branches. Use equal axis units when the geometry
  depends on angles or reflection, such as inverse graphs across `y=x`.
- Every figure or diagram needs a caption, a stable label, and an explicit
  nearby body reference using `\autoref{fig:...}`. A caption alone does not
  count as an in-text reference. Match caption text size to ordinary margin text.
- Compile and visually inspect every edited diagram in the book and each
  affected handout. Check it at the final printed size for legibility, then
  zoom in to catch touching letters and strokes. Inspect the whole page for
  clipping, caption crowding, and collisions with adjacent margin content.
  Revise and render again until these defects are resolved; compilation success
  alone does not establish a clean diagram.

## Validation

Run the shared book checks after edits. Verify that each edited figure has
a nearby body reference, that its number resolves, and that proofs stand
on their own when the margin is ignored.
