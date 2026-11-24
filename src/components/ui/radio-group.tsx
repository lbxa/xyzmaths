import { Radio as RadioPrimitive } from "@base-ui/react/radio";
import { RadioGroup as RadioGroupPrimitive } from "@base-ui/react/radio-group";
import { cn } from "cn";

export function RadioGroup<Value extends string>({ className, ...props }: RadioGroupPrimitive.Props<Value>) {
  return <RadioGroupPrimitive data-slot="radio-group" className={cn("grid w-full grid-cols-3", className)} {...props} />;
}

export function RadioGroupItem({ className, ...props }: RadioPrimitive.Root.Props) {
  return (
    <RadioPrimitive.Root
      data-slot="radio-group-item"
      className={state => cn(
        "flex aspect-square min-h-touch-target min-w-0 cursor-pointer flex-col items-center justify-center gap-phi-0 rounded-swatch border border-ink/15 bg-canvas text-ink select-none",
        "hover:not-data-checked:border-ink/50 data-checked:border-3 data-checked:border-ink forced-colors:data-checked:border-[Highlight] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-link",
        typeof className === "function" ? className(state) : className,
      )}
      {...props}
    />
  );
}
