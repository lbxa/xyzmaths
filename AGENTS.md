## Styling

Always use Tailwind CSS utility classes for styling. Do not add component-scoped `<style>` blocks, CSS modules, or new handwritten CSS rules unless the user explicitly requests them or Tailwind cannot express the required styling. Keep `src/styles/global.css` limited to the Tailwind import and truly global theme or base styles.

Treat `DESIGN_SYSTEM.md` as the canonical visual and interaction specification. New pages and components must preserve its hacker-academic character rather than introducing a separate aesthetic.

Use `src/styles/tokens.css` as the source of truth for design tokens. Extend existing tokens instead of scattering arbitrary color, font, radius, or shadow values through components.

Use the `phi-*` spacing tokens for all padding, margin, gaps, and layout intervals. The scale follows the golden ratio: 6, 10, 16, 26, 42, 68, 110, 178, and 288px at the default root size. Choose the token by semantic scale—compact, text, section, panel, or layout—and do not use Tailwind's numeric spacing utilities or arbitrary spacing values. Use the named `meta`, `lede`, `heading`, and `title` type tokens for hierarchy.

### Visual direction

Build toward a Web 1.0 hacker-academic aesthetic with restrained digital brutalism:

- Favor document-first, raw-HTML-like structure over card-heavy application UI.
- Leave unstyled content in the browser's generic `serif` family. Do not substitute Tailwind's `ui-serif` preset or a named serif stack. Use the monospace token selectively for code, metadata, terminal-like labels, and technical navigation.
- Use a white document canvas with black text, set against black when a surrounding page or display frame is present.
- Keep links recognizably Web 1.0: blue, underlined, and purple when visited unless usability requires a different state.
- Create hierarchy with semantic headings, paragraphs, lists, tables, and horizontal rules rather than ornamental components.
- Prefer dense, credible technical content with generous unused space around the document.
- Keep navigation narrow and list-like. Use minimal imagery, animation, gradients, shadows, and decoration.
- When framing the page, use a simple dark rounded surround that evokes an old terminal or computer display; keep the document surface itself square and plain.
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
