import { useEffect, useId, useState } from "react";
import { ControlTooltip, TooltipProvider } from "@/components/ui/tooltip";
import { BookContentsIcon } from "@/components/ui/icons";
import { FileTree } from "@/components/ui/file-tree";
import ContentsLink from "@/components/ContentsLink";
import { Separator } from "@/components/ui/separator";
import type { ContentsEntry } from "@/lib/book-contents";
import { normalizeHref, trailTo, watchPageFragment } from "@/lib/contents-location";

interface Props {
  entries: ContentsEntry[];
  currentPath: string;
  bookHref: string;
}

function selectionFor({ entries, currentPath, bookHref }: Props, hash: string) {
  const path = normalizeHref(currentPath);
  const trail = (hash && trailTo(entries, path + hash)) || trailTo(entries, path);
  if (trail) return { selected: trail.at(-1), open: trail.filter(entry => entry.children?.length) };
  const part = path === normalizeHref(bookHref)
    && entries.find(entry => entry.children?.length && entry.href?.startsWith(bookHref + "#"));
  return { selected: undefined, open: part ? [part] : [] };
}

export default function BookContents({ entries, currentPath, bookHref }: Props) {
  const headingId = useId();
  const [initial] = useState(() => selectionFor({ entries, currentPath, bookHref }, ""));
  const [selected, setSelected] = useState(initial.selected);
  const [expanded, setExpanded] = useState(() => new Set(initial.open));

  useEffect(() => watchPageFragment(hash => {
    const { selected, open } = selectionFor({ entries, currentPath, bookHref }, hash);
    setSelected(selected);
    setExpanded(previous => open.every(entry => previous.has(entry)) ? previous : new Set([...previous, ...open]));
  }), [entries, currentPath, bookHref]);

  function toggle(entry: ContentsEntry, open: boolean) {
    setExpanded(previous => {
      const next = new Set(previous);
      if (open) next.add(entry);
      else next.delete(entry);
      return next;
    });
  }

  const overview = !selected && normalizeHref(currentPath) === normalizeHref(bookHref);
  return (
    <TooltipProvider><nav aria-labelledby={headingId} className="min-w-0 font-serif text-ink">
      <div className="flex items-center justify-between gap-phi-1">
        <h2 id={headingId} className="text-lede font-bold">Book contents</h2>
        <ControlTooltip tip="Go to the book overview"><ContentsLink
          href={bookHref}
          aria-label="Overview"
          aria-current={overview ? "page" : undefined}
          className="inline-flex size-phi-4 shrink-0 items-center justify-center aria-[current]:bg-ink/5"
        >
          <BookContentsIcon aria-hidden="true" focusable="false" className="size-phi-2" />
        </ContentsLink></ControlTooltip>
      </div>
      <Separator className="my-phi-2" />
      <FileTree entries={entries} selected={selected} expanded={expanded} onToggle={toggle} />
    </nav></TooltipProvider>
  );
}
