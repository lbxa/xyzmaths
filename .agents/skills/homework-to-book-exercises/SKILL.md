---
name: homework-to-book-exercises
description: Import a supplied assignment into an XYZ Maths book as shared exercise statements, appendix entries, and a standalone homework handout. Use for assignment transcription, placement, or updates.
---

# Homework to book exercises

Start with the [book guides](../../../AGENTS.md#books) and work inside the
selected book. Read its `AGENTS.md`, the homework placement map in its
`README.md`, `macros.tex`, the target topic files, and
`sections/appendices/exercise-solutions.tex`. Use an existing handout from
the same book as a model. For the author's supplied proofs, use
[homework-solutions-to-book](../homework-solutions-to-book/SKILL.md).

## Capture the supplied assignment

- Preserve the original source in the project's ignored source location.
  Inventory every page, original question number, and subpart before editing.
  Record source page and question provenance in shared statement comments.
- Inspect every PDF page visually as well as extracting text. Preserve wording,
  hypotheses, quantifiers, notation, indices, matrix entries, endpoints, subpart order,
  and punctuation. When verbatim copying is requested, retain apparent source
  errors and flag them in the source record instead of silently correcting them.
  Resolve uncertain glyphs from a closer view; report anything still unreadable.
- A PDF supplies rendered mathematics, not recoverable original TeX source.
  Reconstruct faithful TeX without claiming to have recovered the original code.
  Commands such as “Prove” in the assignment are exercise statements, not
  authorization to write missing solutions.

## Author once and reuse

For a new assignment, choose an unused `hwNN` basename and stable topic keys
after checking existing files and map rows across both parts of the selected
book. Record the original assignment number even if the book's basename differs.
For updates, reuse the mapped identity and existing shared files.

For each original question without shared files, create
`problems/hwNN/NN-topic/problem.tex` and its adjacent `solution.tex`.
Keep all subparts together. Use the shared `exercise` environment with
`\label{ex:hwNN:topic}`. Put `\solutionlink{hwNN:topic}` after the full
statement and any hints, immediately before `\end{exercise}`. It links to
`sol:hwNN:topic` in the main text and is suppressed in handouts and appendix
restatements. Keep keys independent of numeric directory prefixes.

Preserve subpart labels and set them before the list calculates indentation.
Use the selected book's list conventions and inspect wrapped-line alignment.

When neither existing nor newly supplied material contains a solution, put
`\noindent\emph{Awaiting solution.}` in the solution file and mark the map
accordingly. Preserve existing supplied solutions during statement updates.
Add supplied solutions only within the authorized scope; no empty proof
environment or fabricated argument.
Follow the book's solution formatting for completed multipart proofs.
Keep pending notices outside proof environments.

- **Main text:** input only the shared statement, once, in the smallest existing
  topic where the assessed content and prerequisites are available. Assess the
  whole question, including every subpart. Defer unsuitable placements in the
  map rather than inventing prerequisite notes or future chapters.
- **Appendix:** repeat the complete shared statement, followed by the shared
  solution, in main-text exercise order. Use the existing pattern:

  ```tex
  \solutionheading{hwNN:topic}
  \begin{restatedproblem}
    \input{problems/hwNN/NN-topic/problem}
  \end{restatedproblem}
  \input{problems/hwNN/NN-topic/solution}
  ```

  This preserves the book exercise number, its return link, and the solution
  anchor without duplicate numbering or margin links.
- **Handout:** copy the book's `problems/template.tex` to the new
  entry file, leaving the template unchanged. Input each statement and solution
  pair in original assignment order and preserve original question numbering.
  Keep assignment titles, running heads, question-label overrides, and handout
  layout local to that entry file. Let questions flow naturally in the handout
  and in the appendix.

Reuse figure sources too. Later mentions reference the existing exercise;
they do not input it again.

## Preserve both handout build modes

Retain the template's TeXShop `pdflatexmk` and pdfLaTeX directives, book-root
detection, and input path before loading the preamble. The root is also used
for graphics and bibliography resources. Each nested `problem.tex` and
`solution.tex` starts with `% !TEX root = ../../hwNN.tex` pointing to its
actual handout. Keep the handout a complete document. Use portable relative
paths for its dependencies.

## Synchronize records and validate

Update one homework-map row per supplied question, including deferred questions,
in the same change. Reconcile actual input locations, shared paths, stable keys,
status, and appendix order across all embedded exercises, including lecture
exercises. Update source coverage, bibliography, and acknowledgements as required
by the project.

Run `make check` in the book directory. It builds each handout both there and
in `problems/` with separate caches. If the template changed, also compile it
from both directories. Compare the rendered statements against every original page,
separately from compilation success. Inspect book and handout layouts, original
handout numbering, complete appendix restatements, pending notices, unresolved
references, and duplicate labels or destinations. Verify that each margin link
reaches its solution page and each appendix exercise number returns to the
original exercise.

For a requested single-file export, check the selected book's Makefile.
Where it provides `make export-problem HW=hwNN`, compile the resulting
`build/export/hwNN.tex` in isolation. Keep any portable copy derived from
the shared sources.
