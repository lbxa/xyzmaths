import type { ComponentProps } from "react";
import { Button } from "@/components/ui/button";
import { ControlTooltip, TooltipProvider } from "@/components/ui/tooltip";

// Each hydrated Astro island has its own React context.
export function TooltipButton({ tip, ...props }: ComponentProps<typeof Button> & { tip: string }) {
  return <TooltipProvider><ControlTooltip tip={tip}><Button {...props} /></ControlTooltip></TooltipProvider>;
}

export function TooltipLink({ tip, ...props }: ComponentProps<"a"> & { tip: string }) {
  return <TooltipProvider><ControlTooltip tip={tip}><a {...props} /></ControlTooltip></TooltipProvider>;
}
