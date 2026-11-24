import { Tooltip as TooltipPrimitive } from "@base-ui/react/tooltip"
import { cn } from "cn"
import { useId, useState, type ReactElement } from "react"

function TooltipProvider({
  delay = 400,
  ...props
}: TooltipPrimitive.Provider.Props) {
  return (
    <TooltipPrimitive.Provider
      data-slot="tooltip-provider"
      delay={delay}
      {...props}
    />
  )
}

function Tooltip({ ...props }: TooltipPrimitive.Root.Props) {
  return <TooltipPrimitive.Root data-slot="tooltip" {...props} />
}

function TooltipTrigger({ ...props }: TooltipPrimitive.Trigger.Props) {
  return <TooltipPrimitive.Trigger {...props} />
}

function TooltipContent({
  className,
  side = "top",
  sideOffset = 4,
  align = "center",
  alignOffset = 0,
  children,
  ...props
}: TooltipPrimitive.Popup.Props &
  Pick<
    TooltipPrimitive.Positioner.Props,
    "align" | "alignOffset" | "side" | "sideOffset"
  >) {
  return (
    <TooltipPrimitive.Portal>
      <TooltipPrimitive.Positioner
        align={align}
        alignOffset={alignOffset}
        side={side}
        sideOffset={sideOffset}
        className="isolate z-50"
      >
        <TooltipPrimitive.Popup
          data-slot="tooltip-content"
          className={cn(
            "max-w-phi-8 rounded-control bg-ink px-phi-1 py-phi-0 font-mono text-xs leading-snug text-canvas shadow-sm print:hidden",
            className
          )}
          {...props}
        >
          {children}
        </TooltipPrimitive.Popup>
      </TooltipPrimitive.Positioner>
    </TooltipPrimitive.Portal>
  )
}

function ControlTooltip({ tip, children }: { tip: string; children: ReactElement }) {
  const id = useId();
  const [open, setOpen] = useState(false);
  return (
    <Tooltip onOpenChange={setOpen}>
      <TooltipTrigger aria-description={tip} aria-describedby={open ? id : undefined} render={children} />
      <TooltipContent id={id} role="tooltip">{tip}</TooltipContent>
    </Tooltip>
  )
}

export { ControlTooltip, Tooltip, TooltipTrigger, TooltipContent, TooltipProvider }
