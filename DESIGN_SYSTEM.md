# XYZ Maths Design System

## Design thesis

XYZ uses a **Web 1.0 hacker-academic aesthetic** with restrained **digital brutalism**. The interface should feel technical, institutional, archival, and highly credible—closer to a university research page, GNU documentation, an early personal website, or an open-source project homepage than a contemporary product site.

> A Web 1.0 research-lab website with raw HTML structure, monochrome typography, blue underlined links, dense technical content and restrained digital brutalism, presented inside a dark rounded computer-display frame.

## Core traits

- Document-first layout
- Near-default semantic HTML styling
- White document canvas on a black surround
- Dense text balanced by generous unused space
- Browser-default serif text with selective system monospace
- Blue underlined manuscript references and purple visited references
- Simple lists and narrow navigation
- Minimal imagery
- Little animation or decoration
- Hierarchy created through headings, lists, tables, and rules
- A rounded dark frame resembling an old terminal or computer display

## Foundations

### Structure

Start with semantic document elements: headings, paragraphs, lists, definitions, tables, blockquotes, figures, and horizontal rules. Navigation should read like an index or table of contents. Prefer one strong reading column over cards, dashboards, or modular marketing sections.

### Typography

Book notes and their contents lists use the `font-serif` token, which prefers the reader’s local Times New Roman. Unstyled text uses the browser's generic `serif` family. Use the monospace token only for document codes, metadata, technical labels, navigation controls, and literal code.

Inline and display equations inherit the surrounding text’s font size, including in captions and footnotes. KaTeX supplies the math fonts and scales subscripts, superscripts, and fraction components. Wide display equations scroll horizontally inside the reading column.

Use the named `meta`, `lede`, `heading`, and `title` tokens to create hierarchy. Typography should remain matter-of-fact and readable rather than editorially decorative.

### Color

The palette is deliberately small:

- `canvas`: white document surface
- `ink`: black text and strong rules
- `frame`: near-black outer display
- `rule`: neutral structural lines
- `link`: classic hyperlink blue
- `link-visited`: classic visited-link purple

Do not introduce gradients, soft brand palettes, tinted cards, or decorative accent colors without a functional need.

### Spacing

The `phi-*` spacing scale in `src/styles/tokens.css` runs through 2, 4, 6, 10, 16, 26, 42, 68, 110, 178, and 288px at the default root size. Use `phi-fine` (2px) and `phi-tight` (4px) for control padding.

Use smaller intervals inside text and controls, middle intervals between related sections, and larger intervals for panels or layout regions. Generous space should surround dense content; it should not be inserted as empty decoration between every element.

### Surfaces and framing

Frame the white reading surface with the display radius (26px). Give popups and the exposed corners of floating drawers the panel radius (10px). Docked sidebars share a straight divider with the manuscript.

### Links and controls

Reader navigation uses plain ink text before and after a visit. Apply this to the overview, chapter directory, contents panels, reading tools, and links to exercises and solutions. Bold marks the current contents entry. Give navigation controls a subtle neutral background on hover and an ink outline on keyboard focus.

References in manuscript prose, including figures, theorems, and citations, use blue underlined text and turn purple after a visit.

Use the control radius (6px) on buttons, selectors, menu items, and navigation highlights. Give controls a thin inset, typically 2px vertically and 4px horizontally. On touchscreens, centre a touch target of at least 44px around each toolbar button and the book selector, with space between adjacent targets. Joined controls round their outer corners.

Use monochrome Hugeicons Stroke Rounded for interface actions. Copy and Close can stand alone as icons. Keep panel names and chapter destinations visible beside their icons. Use the same checkmark for a selected option or a successful copy, with an accessible name or announcement that identifies its meaning.

Give reader controls a short action description with the shared Base UI tooltip. Use `ControlTooltip` inside React and the hydrated `TooltipButton` or `TooltipLink` in Astro. Keep each control’s accessible name available on touch and before hydration. Tooltips open on hover or keyboard focus. Escape dismisses the tooltip first when its control is inside an open panel.

Interaction should be immediate and restrained. Add motion only when it materially explains a spatial change, and respect reduced-motion preferences.

### Imagery

Use imagery sparingly. Appropriate assets include mathematical diagrams, archival scans, research-handout graphics, and functional illustrations. Avoid stock photography, ornamental hero art, lifestyle imagery, and decorative icon clouds.

## Composition rules

- The header title reads **XYZ Maths** on the homepage, **XYZ Books** in the catalog and book reader, and **XYZ PoW** in the problem archive and its entries. It links to the homepage. Use the same full names in browser titles and primary navigation. Give each collection a document-style index. Only the book reader has a book selector, contents tree, reading controls and manuscript margin.
- Link each weekly problem, its solution and its editorial from the archive and the top of all three pages. Keep the statement spoiler-free. Give the direct answer and calculation in the solution, and explain how to find and justify the method in the editorial. Show the publication date and credit the problem source.
- Centre the manuscript and its reading-order links together in a column up to 72ch wide. Wide mode fills the main pane within its 16px phone and 26px desktop gutters. Keep prose left-aligned in both modes.
- Align the reading controls to the right edge of the main pane. Place the two Hugeicons text-width buttons immediately before **Copy for LLM** and show the selected width in reverse contrast.
- Let headings and rules carry hierarchy before adding containers.
- Preserve real whitespace around the document while allowing the document itself to be information-dense.
- Place the book selector beside the header title. Show the current book in the control and list books that have a web edition.
- The left contents use a file tree. Folders mark book divisions, document icons mark pages, and paragraph icons mark sections within a page. Chapters sit directly beneath their part, and each heading sits beneath its nearest parent. Open the branch leading to the current destination. A chevron toggles the branch independently of its title link. Keep print page numbers aligned on the right.
- Keep every figure and its caption in manuscript order in the main reading column, including figures printed in the LaTeX margin. Place a figure after a displayed equation when it would otherwise separate the equation from its introduction.
- Use the right margin for numbered text notes. Align each with its reference and stack nearby notes so they stay readable. The manuscript and notes scroll together. Pages without text notes use the full reading pane.
- Show the margin when the reading pane has at least 42rem of usable width. In narrower panes, show notes inline beside their source passages. Keep the contents visible on tablets and accessible from the header on phones. Preserve linked note numbers and return links in either layout.

## Avoid

- SaaS-style cards, pills, badges, dashboards, and feature grids
- Large decorative gradients, glows, glass effects, or soft shadows
- Excessive border radii inside the document
- Sans-serif product typography
- Manuscript references that are hard to distinguish from surrounding text
- Animation added only for polish
- Large imagery that displaces useful content
- Generic marketing copy and glossy futurism

## Implementation contract

- `src/styles/tokens.css` is the source of truth for design tokens.
- `src/styles/global.css` contains only Tailwind and global token imports or truly global base behavior.
- Components use Tailwind utilities backed by named tokens.
- Arbitrary values require a genuine one-off structural need; spacing must always use `phi-*` tokens.
- Accessibility and semantic HTML take precedence over visual imitation of old websites.
