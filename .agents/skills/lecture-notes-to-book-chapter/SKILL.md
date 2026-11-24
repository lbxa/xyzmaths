---
name: lecture-notes-to-book-chapter
description: Transcribe supplied lecture notes, photos, scans, or PDFs into an XYZ Maths book while preserving its course progression and source records.
---

# Lecture notes to book chapter

Use the supplied lecture pages as the source for the selected book. For the
author's homework proof drafts, use
[homework-solutions-to-book](../homework-solutions-to-book/SKILL.md).

## 1. Inspect the project and source

- Find the selected book in the [book guides](../../../AGENTS.md#books). Read its `AGENTS.md`, `CONTRIBUTING.md`, README outline and relevant chapter changelog. Follow the active `part.tex` and `chapter.tex` input lists. Check the book's macros and preamble for existing notation and environments.
- Inventory source files in reading order. Preserve originals and keep local copies under the book's ignored `images/`. The repository's [macOS JPEG helper](../../../scripts/jpeg.sh) accepts an input path and an output path.
- View every page at a legible resolution. Group pages by lecture and sequence; do not rely on filenames alone when the handwritten page numbers or headings say otherwise.
- Make a private transcription outline keyed to source page and proposed chapter section before writing. Record every mathematical item, examples, diagrams, caveats, and visible gaps.
- Follow the book's source-record policy. When it calls for a page-by-page coverage table, give every page an actual destination, repetition, metadata, deferral, or source-issue status. Update destinations when material moves.

## 2. Transcribe faithfully and edit carefully

- Include only material supplied by the author or explicitly authorized. Do not fetch lecture slides, homework, or other linked material unless asked. Do not extrapolate future topics from a syllabus.
- Convert shorthand into clear prose while preserving the lecturer's progression, notation, hypotheses, examples, and conclusions. Follow the book's guidance on supporting explanations, missing steps, and whether a lecture question becomes a worked example or a shared exercise.
- Check formulas, indices, dimensions, signs, and quantifiers against the source image. If handwriting is uncertain, inspect a crop or higher-resolution view. When uncertainty remains, leave a precise source comment and ask the author; never silently guess.
- Flag mathematical contradictions, apparent errors, incomplete arguments, and TODOs. Do not put a known false or ambiguous statement in the reader-facing book as if established. Keep the author's intended material visible in an editor comment until clarified, or omit the unresolved claim and report it clearly.
- Place material in the smallest topic file consistent with the active part and chapter outline. Preserve deliberate previews. Follow the book's instructions for adding topics and keep future-course parts disabled until their material is available.
- Retain the distinction between lecture notes and editorial explanation. Do not cite, attribute, or describe a result as proved unless the supplied source supports that claim.

## 3. Maintain book tooling

- Redraw supplied diagrams in TikZ using the book's figure styles. Give each a caption, stable label, and nearby `\autoref` reference. Check endpoints and label clearance at printed size. Follow the book's policy on adding illustrations.
- Reuse shared exercises and solutions according to the book's homework map and macros. Keep statements, solutions, labels, and appendix placement synchronized.
- Update the README, acknowledgements, bibliography, or other project records only when the change requires it under repository instructions.
- Keep TeX source readable and local to the relevant topic files. Use the project's existing environments, notation, input order, and build commands.

## 4. Validate before finishing

- Run `make check` from the selected book directory after LaTeX edits. Resolve build errors and inspect warnings, labels, references, and citations.
- Inspect the resulting PDF pages for typography, line and equation overflow, margin collisions, contents hierarchy, and figure placement. A successful compile alone is not visual validation.
- Compare the final text with the source outline page by page. Confirm that supplied material has not been lost or duplicated and that no unsupported mathematical content was introduced.
- Report converted files, edited chapters, checks performed, and any unresolved transcription or mathematical questions. Leave source images and intermediate outputs in the locations prescribed by the project.
