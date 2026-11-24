"use client"

import type { ComponentProps } from "react"
import { Toggle as TogglePrimitive } from "@base-ui/react/toggle"
import { ToggleGroup as ToggleGroupPrimitive } from "@base-ui/react/toggle-group"
import { cn } from "cn"
import { touchTarget } from "./touch-target"

function ToggleGroup<Value extends string>({
  className,
  ...props
}: ComponentProps<typeof ToggleGroupPrimitive<Value>>) {
  return (
    <ToggleGroupPrimitive
      data-slot="toggle-group"
      className={state => cn(
        "group/toggle-group inline-flex w-fit shrink-0 items-stretch gap-phi-2 font-mono text-meta pointer-fine:gap-0 data-[orientation=vertical]:flex-col",
        typeof className === "function" ? className(state) : className,
      )}
      {...props}
    />
  )
}

function ToggleGroupItem<Value extends string>({
  className,
  ...props
}: ComponentProps<typeof TogglePrimitive<Value>>) {
  return (
    <TogglePrimitive
      data-slot="toggle-group-item"
      className={state => cn(
        touchTarget,
        "inline-flex shrink-0 cursor-pointer items-center justify-center gap-phi-tight rounded-control border border-rule bg-canvas px-phi-tight py-phi-fine text-ink select-none",
        "pointer-fine:group-data-[orientation=horizontal]/toggle-group:not-first:rounded-s-none pointer-fine:group-data-[orientation=horizontal]/toggle-group:not-last:rounded-e-none pointer-fine:group-data-[orientation=horizontal]/toggle-group:not-first:border-s-0",
        "pointer-fine:group-data-[orientation=vertical]/toggle-group:not-first:rounded-t-none pointer-fine:group-data-[orientation=vertical]/toggle-group:not-last:rounded-b-none pointer-fine:group-data-[orientation=vertical]/toggle-group:not-first:border-t-0",
        "hover:not-aria-pressed:bg-ink/10 aria-pressed:border-ink aria-pressed:bg-ink aria-pressed:text-canvas disabled:pointer-events-none disabled:opacity-50",
        "focus-visible:z-1 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ink",
        "[&_svg]:pointer-events-none [&_svg]:shrink-0",
        typeof className === "function" ? className(state) : className,
      )}
      {...props}
    />
  )
}

export { ToggleGroup, ToggleGroupItem }
