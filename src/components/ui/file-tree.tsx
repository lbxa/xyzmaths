import { cn } from "cn";
import { Button, buttonVariants } from "@/components/ui/button";
import { Collapsible, CollapsibleContent, CollapsibleTrigger } from "@/components/ui/collapsible";
import { ChevronRightIcon, FolderIcon, PageIcon, SectionIcon } from "@/components/ui/icons";
import { ControlTooltip } from "@/components/ui/tooltip";
import type { ContentsEntry } from "@/lib/book-contents";
import { readerLinkStyle } from "@/lib/reader-links";

interface FileTreeState {
  selected?: ContentsEntry;
  expanded: ReadonlySet<ContentsEntry>;
  onToggle: (entry: ContentsEntry, open: boolean) => void;
}

const icons = { group: FolderIcon, page: PageIcon, section: SectionIcon };
const columns = "grid grid-cols-[var(--tree-disclosure)_minmax(0,1fr)]";
const rowStyle = "min-h-(--tree-disclosure) w-full min-w-0 border-0 text-start font-serif text-base leading-snug font-normal whitespace-normal";
const linkStyle = cn(buttonVariants({ variant: "ghost", size: "sm" }), readerLinkStyle, rowStyle,
  "col-start-2 justify-start pointer-coarse:items-start pointer-coarse:pt-phi-1");
const rootListStyle = "flex flex-col gap-phi-0 [--tree-disclosure:var(--spacing-phi-3)] pointer-coarse:[--tree-disclosure:var(--spacing-touch-target)]";
const childListStyle = "relative ps-phi-2 before:pointer-events-none before:absolute before:inset-y-0 before:start-[calc(var(--tree-disclosure)/2)] before:border-s before:border-rule/30";

function FileTreeNode({ entry, ...state }: FileTreeState & { entry: ContentsEntry }) {
  const Icon = icons[entry.kind];
  const label = (
    <span className="flex w-full min-w-0 items-baseline gap-phi-0">
      <Icon data-icon="inline-start" className="mt-phi-tight self-start text-rule" />
      <span className="min-w-0 flex-1 [overflow-wrap:anywhere]">{entry.title}</span>
      {entry.page && (
        <span aria-hidden="true" className="shrink-0 font-mono text-meta font-normal tabular-nums text-rule">{entry.page}</span>
      )}
    </span>
  );
  const link = entry.href && (
    <ControlTooltip tip={entry.page ? `Print page ${entry.page}` : `Open ${entry.title}`}>
      <a
        href={entry.href}
        className={linkStyle}
        aria-current={state.selected === entry ? (entry.kind === "page" ? "page" : "location") : undefined}
      >
        {label}
      </a>
    </ControlTooltip>
  );

  if (!entry.children?.length) {
    return (
      <li data-entry-kind={entry.kind} className={columns}>
        {link || <span className="col-start-2 [&_svg]:size-phi-2">{label}</span>}
      </li>
    );
  }

  const open = state.expanded.has(entry);
  const action = `${open ? "Collapse" : "Expand"} ${entry.title}`;
  const disclosure = (
    <ControlTooltip tip={action}>
      <CollapsibleTrigger
        aria-label={action}
        render={<Button variant="ghost" size={link ? "icon-sm" : "sm"} />}
        className={cn("border-0 hover:bg-ink/5 [&_svg]:size-phi-2", link
          ? "size-(--tree-disclosure) p-phi-fine"
          : cn(rowStyle, columns, "items-center gap-0! px-0!"))}
      >
        <ChevronRightIcon className={cn("justify-self-center text-rule", open && "rotate-90")} />
        {!link && <span className="min-w-0 px-phi-tight">{label}</span>}
      </CollapsibleTrigger>
    </ControlTooltip>
  );

  return (
    <li data-entry-kind={entry.kind}>
      <Collapsible open={open} onOpenChange={next => state.onToggle(entry, next)}>
        {link ? <div className={cn(columns, "items-start")}>{disclosure}{link}</div> : disclosure}
        <CollapsibleContent>
          <FileTree entries={entry.children} nested {...state} />
        </CollapsibleContent>
      </Collapsible>
    </li>
  );
}

export function FileTree({ entries, nested = false, ...state }: FileTreeState & { entries: ContentsEntry[]; nested?: boolean }) {
  return (
    <ol data-slot={nested ? "file-tree-children" : "file-tree"} className={cn("min-w-0 list-none", nested ? childListStyle : rootListStyle)}>
      {entries.map(entry => <FileTreeNode key={entry.href ?? entry.title} entry={entry} {...state} />)}
    </ol>
  );
}
