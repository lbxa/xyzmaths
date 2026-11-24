# Mathematical Analysis editor setup

Open XYZ Maths in your editor and use the shared [workspace settings and
LaTeX Workshop recipe](../../docs/book-tooling.md#vs-code-and-cursor).
This book bundles its AMS bibliography styles in `styles/`. Author-based
labels such as `[Can83]` and `[Rod20]` appear after Biber and the subsequent
LaTeX passes complete.

## TeXShop homework previews

Follow the [handout setup](../../docs/book-tooling.md#texshop-homework-previews).
This book's template sets `\analysisroot` before loading the preamble, so
shared inputs, graphics, and bibliography resources resolve from the book
directory and from `problems/`. A nested statement or solution selects its
own handout through its first-line root directive.

## Codex Stop hook

The [shared Stop hook](../../docs/book-tooling.md#codex-stop-hook) writes this
book's check output to `build/codex-stop-check.log` here.
