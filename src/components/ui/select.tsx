import * as React from "react"
import { Select as SelectPrimitive } from "@base-ui/react/select"
import { cn } from "cn"
import { CheckIcon, ChevronDownIcon, ChevronUpIcon } from "./icons"
import { touchTarget } from "./touch-target"

const Select = SelectPrimitive.Root

function SelectGroup({ className, ...props }: SelectPrimitive.Group.Props) {
  return (
    <SelectPrimitive.Group
      data-slot="select-group"
      className={className}
      {...props}
    />
  )
}

function SelectValue({ className, ...props }: SelectPrimitive.Value.Props) {
  return (
    <SelectPrimitive.Value
      data-slot="select-value"
      className={cn("min-w-0 flex-1 truncate text-left text-meta", className)}
      {...props}
    />
  )
}

function SelectTrigger({
  className,
  children,
  ...props
}: SelectPrimitive.Trigger.Props) {
  return (
    <SelectPrimitive.Trigger
      data-slot="select-trigger"
      className={cn(
        touchTarget,
        "inline-flex min-h-phi-3 w-fit min-w-0 cursor-pointer items-center gap-phi-tight rounded-control border border-rule bg-canvas px-phi-tight py-phi-fine font-mono text-meta text-ink",
        "hover:border-ink hover:bg-ink/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ink data-popup-open:border-ink disabled:cursor-not-allowed disabled:opacity-50",
        "[&_svg]:size-phi-2",
        className
      )}
      {...props}
    >
      {children}
      <SelectPrimitive.Icon className="flex shrink-0">
        <ChevronDownIcon />
      </SelectPrimitive.Icon>
    </SelectPrimitive.Trigger>
  )
}

function SelectContent({
  className,
  children,
  side = "bottom",
  sideOffset = 0,
  align = "end",
  alignOffset = 0,
  alignItemWithTrigger = false,
  ...props
}: SelectPrimitive.Popup.Props &
  Pick<
    SelectPrimitive.Positioner.Props,
    "align" | "alignOffset" | "side" | "sideOffset" | "alignItemWithTrigger"
  >) {
  return (
    <SelectPrimitive.Portal>
      <SelectPrimitive.Positioner
        side={side}
        sideOffset={sideOffset}
        align={align}
        alignOffset={alignOffset}
        alignItemWithTrigger={alignItemWithTrigger}
        className="isolate z-50"
      >
        <SelectPrimitive.Popup
          data-slot="select-content"
          data-align-trigger={alignItemWithTrigger}
          className={cn(
            "relative flex max-h-(--available-height) w-max min-w-(--anchor-width) max-w-(--available-width) flex-col overflow-hidden rounded-panel border border-rule bg-canvas px-phi-tight py-phi-fine font-mono text-ink",
            className
          )}
          {...props}
        >
          <SelectScrollUpButton />
          <SelectPrimitive.List className="min-h-0 overflow-y-auto overscroll-contain">
            {children}
          </SelectPrimitive.List>
          <SelectScrollDownButton />
        </SelectPrimitive.Popup>
      </SelectPrimitive.Positioner>
    </SelectPrimitive.Portal>
  )
}

function SelectItem({
  className,
  children,
  ...props
}: SelectPrimitive.Item.Props) {
  return (
    <SelectPrimitive.Item
      data-slot="select-item"
      className={cn(
        "group/select-item flex min-h-phi-3 w-full cursor-pointer items-center rounded-control text-start outline-hidden select-none data-disabled:pointer-events-none data-disabled:opacity-50 pointer-coarse:min-h-phi-4",
        className
      )}
      {...props}
    >
      <span className="grid min-h-phi-3 w-full grid-cols-[minmax(0,1fr)_var(--spacing-phi-2)] items-center gap-phi-tight rounded-control px-phi-tight py-phi-fine group-data-highlighted/select-item:bg-ink group-data-highlighted/select-item:text-canvas [&_svg]:size-phi-2">
        <SelectPrimitive.ItemText className="min-w-0 text-meta wrap-anywhere">
          {children}
        </SelectPrimitive.ItemText>
        <SelectPrimitive.ItemIndicator className="pointer-events-none flex justify-self-end">
          <CheckIcon />
        </SelectPrimitive.ItemIndicator>
      </span>
    </SelectPrimitive.Item>
  )
}

function SelectScrollUpButton({
  className,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.ScrollUpArrow>) {
  return (
    <SelectPrimitive.ScrollUpArrow
      data-slot="select-scroll-up-button"
      className={cn(
        "inset-x-phi-tight top-phi-fine flex min-h-phi-3 items-center justify-center rounded-control bg-canvas px-phi-tight py-phi-fine hover:outline hover:outline-rule [&_svg]:size-phi-2",
        className
      )}
      {...props}
    >
      <ChevronUpIcon />
    </SelectPrimitive.ScrollUpArrow>
  )
}

function SelectScrollDownButton({
  className,
  ...props
}: React.ComponentProps<typeof SelectPrimitive.ScrollDownArrow>) {
  return (
    <SelectPrimitive.ScrollDownArrow
      data-slot="select-scroll-down-button"
      className={cn(
        "inset-x-phi-tight bottom-phi-fine flex min-h-phi-3 items-center justify-center rounded-control bg-canvas px-phi-tight py-phi-fine hover:outline hover:outline-rule [&_svg]:size-phi-2",
        className
      )}
      {...props}
    >
      <ChevronDownIcon />
    </SelectPrimitive.ScrollDownArrow>
  )
}

export {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
}
