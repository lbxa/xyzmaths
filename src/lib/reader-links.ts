export const readerLinkStyle =
  "reader-link rounded-control text-ink no-underline hover:bg-ink/5 focus-visible:outline-2 focus-visible:outline-ink aria-[current]:font-bold";

// Rendered exercises can contain reader controls alongside manuscript references.
export const manuscriptLinkStyles =
  "[&_a:not(.reader-link)]:text-link [&_a:not(.reader-link)]:underline [&_a:not(.reader-link):visited]:text-link-visited";
