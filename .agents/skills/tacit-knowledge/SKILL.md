---
name: tacit-knowledge
description: Record durable mathematical and editorial decisions for an XYZ Maths book in the changelog of its chapter, appendix, or book README.
---

# Capture Tacit Knowledge

Preserve durable book memory in the relevant README changelog. Record agreed
decisions and their reasons, rather than conversational history or obvious
source edits. Use the [book guides](../../../AGENTS.md#books) to locate the
selected book's `AGENTS.md`, course scope, and exercise placement rules.

## Capture criteria

Capture a decision when future agents would otherwise need to rediscover it:

- Chapter order, prerequisite dependencies, proof treatment, or intended detail.
- Author clarifications of notation, course scope, examples, or exercises.
- Deliberate forward references, deferred topics, or unresolved source issues.
- Layout workarounds, shared exercise rules, or diagram conventions with a
  non-obvious rationale.

Do not record transient build status, generic advice, tentative suggestions,
or unverified mathematical claims as established results. A record of a proof
gap does not authorize filling it. Capture decisions within the authorized
task scope; a discussion-only review does not itself authorize README edits.

## Locate and record the decision

1. Use the explicit chapter and part input lists to identify the owning area.
2. Work inside the selected book. Use the README beside the owning
   `chapter.tex` for chapter decisions, `sections/appendices/README.md` for
   appendix decisions, and the book's `README.md` for shared notation,
   builds, or decisions spanning chapters.
3. Create a chapter README only when durable knowledge needs recording. Add or
   update its `## Changelog` with a dated entry using the current local date.
   Keep entries newest-first unless an existing convention differs; combine
   related same-day notes rather than repeating them.
4. State each decision and its reason in one or two sentences. Name concrete
   topics, stable labels, shared source paths, or LaTeX environments as useful.

Use this format when no changelog convention exists:

```markdown
## Changelog

### YYYY-MM-DD

- Captured decision: reason future agents should preserve it.
```

Record a shared rationale once at book level and link to it where useful.
Keep the book's placement maps authoritative for inclusion and order. Maintain
its existing source coverage tables when their recorded destinations change.
