# XYZ Maths

## Books

The site and both Tufte-LaTeX books share this repository. Start a book task
by reading the selected book's instructions and README. Paths such as
`main.tex`, `problems/`, and `build/` in a book guide are relative to that
book directory. Keep each book's mathematical scope, editorial permissions,
notation, bibliography, and source records with the book.

| Book | Instructions | Outline and placement maps |
| --- | --- | --- |
| Linear Algebra | [Book guide](books/linear-algebra/AGENTS.md) | [Book README](books/linear-algebra/README.md) |
| Introduction to Mathematical Analysis | [Book guide](books/maths-analysis/AGENTS.md) | [Book README](books/maths-analysis/README.md) |

### Authoring workflows

- [Lecture notes to book chapter](.agents/skills/lecture-notes-to-book-chapter/SKILL.md) covers source inspection, transcription, coverage, and chapter placement.
- [Homework to book exercises](.agents/skills/homework-to-book-exercises/SKILL.md) covers assignment identity, shared statements, the solutions appendix, and standalone handouts.
- [Homework solutions to book](.agents/skills/homework-solutions-to-book/SKILL.md) preserves the author's proof strategy and marks substantive repairs under the selected book's review rules.
- [Editor](.agents/skills/editor/SKILL.md) guides motivated exposition, proofs, diagrams, margin notes, and topic order.
- [Tacit knowledge](.agents/skills/tacit-knowledge/SKILL.md) records durable decisions and their reasons in the relevant chapter, appendix, or book README.

### Shared book conventions

Work in the smallest relevant topic file. Use two-space indentation, numbered
lowercase hyphenated filenames, explicit `\input` lists, and stable labels
independent of the filenames. Each book's `main.tex` selects its parts,
`preamble.tex` configures layout, and `macros.tex` defines notation and
environments. Keep the standalone formula sheet in sync by reusing the
appendix source. Follow the course's topic order in summaries and appendices.

Write for a reader outside the class. Keep lecture dates, source provenance,
and import progress in internal records. Preserve the author's reasoning and
the lecturer's progression. Essential hypotheses, theorem applications, and
conclusions belong in the proof body. Reserve the Tufte margin for optional
guides. Use `\autoref` for numbered objects, caption and label figures, and
refer to them in nearby text. Review changed pages at their printed size.

Each book's README owns its homework placement map. Keep one row per supplied
question, including deferred questions, with course and question identity,
both source paths, topic, placement, appendix order, stable key, and status.
Update the map when any of these change. Assignment basenames and keys must
be unique across the parts of **that book**. Both books can have an `hw01`.
The handout reuses the statement and solution in assignment order. The main
text inputs the statement once. The appendix restates the complete statement
before the solution in book order. Preserve both links and check for duplicate
numbers, labels, and destinations. Keep a pending notice for missing solutions.

Use imperative commit subjects and keep contributions focused. Record book
contributions in the relevant `sections/front-matter/acknowledgements.tex`.
In pull requests, identify the topics, sources, build results, and related
issues. Include page screenshots for layout changes.

After TeX edits, run `make check` in the affected book. After shared build
changes, run `make check` at the XYZ Maths root for both books. Check affected
PDFs for margin collisions, overflow, resolved references, and citations.
Check mathematical correctness and source fidelity separately. Keep local
lecture images in the book's ignored `images/` and generated files in its
`build/`. Commit editable figures and their attribution. Each book retains
its own licences and third-party notices.

The [book tooling guide](docs/book-tooling.md) covers shared editor settings,
handout build modes, and the Codex Stop hook. Keep machine-specific tool paths
in the editor's User settings.

## Direct file authoring

Edit source and human-written text directly with file editing tools or the
application editor. Keep implementation code visible in ordinary modules
and functions. Put notebook explanations and conclusions in Markdown cells.
Package existing documentation. Reserve programmatic serialization for runtime
data such as measurements, logs, and checkpoints.

## Context7 documentation

Use Context7 for questions about a library, framework, SDK, API, CLI, or
cloud service. Resolve the library ID unless supplied, choose the most
relevant authoritative match and version, then query its docs for each
distinct concept. Ordinary prose edits, mathematical reasoning, and
refactoring independent of library APIs do not need a documentation lookup.

## Website styling

Always use Tailwind CSS utility classes for styling. Do not add component-scoped `<style>` blocks, CSS modules, or new handwritten CSS rules unless the user explicitly requests them or Tailwind cannot express the required styling. Keep `src/styles/global.css` limited to the Tailwind import and truly global theme or base styles.

Treat `DESIGN_SYSTEM.md` as the canonical visual and interaction specification. New pages and components must preserve its hacker-academic character rather than introducing a separate aesthetic.

Use `src/styles/tokens.css` as the source of truth for design tokens. Extend existing tokens instead of scattering arbitrary color, font, radius, or shadow values through components.

Use the `phi-*` spacing tokens for all padding, margin, gaps, and layout intervals. The scale follows the golden ratio and runs from 2px to 288px at the default root size. Use `phi-fine` (2px) and `phi-tight` (4px) for thin control padding. Choose the token by semantic scale—compact, text, section, panel, or layout—and do not use Tailwind's numeric spacing utilities or arbitrary spacing values. Use the named `meta`, `lede`, `heading`, and `title` type tokens for hierarchy.

### Interface icons

Use official **Hugeicons Stroke Rounded** for website controls, including new shadcn components. Import named SVG components from `@/components/ui/icons` in Astro and React. To add a glyph, save its official SVG in `src/assets/icons/`, record its gallery and pinned source in [the asset credits](src/assets/icons/CREDITS.md), and export it from [the shared icon module](src/components/ui/icons.ts). The build applies the control's text colour and hides decorative artwork from assistive technology.

Use an icon alone for familiar actions such as copying or closing. Give each icon-only button a descriptive accessible name, a hover title, and visible keyboard focus. Use the shared touch target for toolbar and drawer buttons. Keep a disclosure and its adjacent navigation link independently clickable. Pair an icon with visible text when readers need to identify a panel, book, or chapter. Use the native 24px size for toolbar actions and 16px beside text. In shadcn buttons, mark a companion icon with `data-icon="inline-start"` or `data-icon="inline-end"`.

Drive state icons from the control's actual state. Announce operation results in a live region and show a readable recovery message when an action fails.

### Visual direction

Build toward a Web 1.0 hacker-academic aesthetic with restrained digital brutalism:

- Favor document-first, raw-HTML-like structure over card-heavy application UI.
- Leave unstyled content in the browser's generic `serif` family. Do not substitute Tailwind's `ui-serif` preset or a named serif stack. Use the monospace token selectively for code, metadata, terminal-like labels, and technical navigation.
- Use a white document canvas with black text, set against black when a surrounding page or display frame is present.
- Keep links recognizably Web 1.0: blue, underlined, and purple when visited unless usability requires a different state.
- Create hierarchy with semantic headings, paragraphs, lists, tables, and horizontal rules rather than ornamental components.
- Prefer dense, credible technical content with generous unused space around the document.
- Keep navigation narrow and list-like. Use minimal imagery, animation, gradients, shadows, and decoration.
- Frame the plain manuscript with a rounded dark surround. Use the shared `control` radius for interactive elements and the `panel` radius for floating menus and drawers.
- Aim for technical, institutional, archival, and highly credible—not polished SaaS, playful consumer UI, or glossy futurism.

Concise design prompt: "A Web 1.0 research-lab website with raw HTML structure, monochrome typography, blue underlined links, dense technical content and restrained digital brutalism, presented inside a dark rounded computer-display frame."

## Development

When starting the dev server, use background mode:

```
astro dev --background
```

Manage the background server with `astro dev stop`, `astro dev status`, and `astro dev logs`.

## Documentation

Full documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Using React, Vue, Svelte, or other framework components](https://docs.astro.build/en/guides/framework-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles or using Tailwind](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)
