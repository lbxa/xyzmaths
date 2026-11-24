# Linear Algebra editor setup

Open XYZ Maths in your editor and use the shared [workspace settings and
LaTeX Workshop recipe](../../docs/book-tooling.md#vs-code-and-cursor).
The book preview uses the AMS styles in `styles/`. Uncited handouts and the
standalone formula sheet compile without Biber or a bibliography database.

## TeXShop homework previews

Follow the [handout setup](../../docs/book-tooling.md#texshop-homework-previews).
This book's template sets `\bookroot` for shared inputs and graphics.
Homework 4 statement fragments select the complete handout. Open
`problems/hw04-questions.tex` directly to preview the questions-only variant.
Compile a portable homework export in a directory separate from the book.

## Codex Stop hook

The [shared Stop hook](../../docs/book-tooling.md#codex-stop-hook) writes this
book's check output to `build/codex-stop-check.log` here.
