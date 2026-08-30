# XYZ Mathematics Club Design System

## Design thesis

XYZ uses a **Web 1.0 hacker-academic aesthetic** with restrained **digital brutalism**. The interface should feel technical, institutional, archival, and highly credible—closer to a university research page, GNU documentation, an early personal website, or an open-source project homepage than a contemporary product site.

> A Web 1.0 research-lab website with raw HTML structure, monochrome typography, blue underlined links, dense technical content and restrained digital brutalism, presented inside a dark rounded computer-display frame.

## Core traits

- Document-first layout
- Near-default semantic HTML styling
- White document canvas on a black surround
- Dense text balanced by generous unused space
- Browser-default serif text with selective system monospace
- Blue underlined links and purple visited links
- Simple lists and narrow navigation
- Minimal imagery
- Little animation or decoration
- Hierarchy created through headings, lists, tables, and rules
- A rounded dark frame resembling an old terminal or computer display

## Foundations

### Structure

Start with semantic document elements: headings, paragraphs, lists, definitions, tables, blockquotes, figures, and horizontal rules. Navigation should read like an index or table of contents. Prefer one strong reading column over cards, dashboards, or modular marketing sections.

### Typography

Body copy uses the browser's generic `serif` family. Do not replace it with Tailwind's serif preset or a named font stack. Use the monospace token only for document codes, metadata, technical labels, navigation controls, and literal code.

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

All spatial decisions use the `phi-*` golden-ratio scale in `src/styles/tokens.css`: 6, 10, 16, 26, 42, 68, 110, 178, and 288px at the default root size.

Use smaller intervals inside text and controls, middle intervals between related sections, and larger intervals for panels or layout regions. Generous space should surround dense content; it should not be inserted as empty decoration between every element.

### Surfaces and framing

The principal content surface is plain white and generally square. When the full page is framed, use the dark rounded display surround. Avoid nested rounded cards: the frame is a single environmental device, not a reusable card treatment.

### Links and controls

Text links should remain visibly blue and underlined, with a purple visited state. Buttons should resemble durable document or terminal controls: bordered, compact, typographically direct, and free of glossy effects.

Interaction should be immediate and restrained. Add motion only when it materially explains a spatial change, and respect reduced-motion preferences.

### Imagery

Use imagery sparingly. Appropriate assets include mathematical diagrams, archival scans, research-handout graphics, and functional illustrations. Avoid stock photography, ornamental hero art, lifestyle imagery, and decorative icon clouds.

## Composition rules

- Keep the main article at a readable measure.
- Use narrow side regions as indexes, metadata rails, references, or navigation.
- Let headings and rules carry hierarchy before adding containers.
- Preserve real whitespace around the document while allowing the document itself to be information-dense.
- On wide screens, keep both asides visible and independently scrollable.
- On intermediate screens, retain the right navigation rail and place supplementary information in a left drawer.
- On mobile, let both asides become edge drawers so the document remains primary.

## Avoid

- SaaS-style cards, pills, badges, dashboards, and feature grids
- Large decorative gradients, glows, glass effects, or soft shadows
- Excessive border radii inside the document
- Sans-serif product typography
- Hidden or subtly styled links
- Animation added only for polish
- Large imagery that displaces useful content
- Generic marketing copy and glossy futurism

## Implementation contract

- `src/styles/tokens.css` is the source of truth for design tokens.
- `src/styles/global.css` contains only Tailwind and global token imports or truly global base behavior.
- Components use Tailwind utilities backed by named tokens.
- Arbitrary values require a genuine one-off structural need; spacing must always use `phi-*` tokens.
- Accessibility and semantic HTML take precedence over visual imitation of old websites.
