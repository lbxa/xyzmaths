import { Button as ButtonPrimitive } from "@base-ui/react/button"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "cn"
import { touchTarget } from "./touch-target"

const buttonVariants = cva(
  [
    touchTarget,
    "group/button inline-flex shrink-0 cursor-pointer items-center justify-center rounded-control border border-transparent bg-clip-padding py-phi-fine font-mono text-(length:--text-meta)/(--text-meta--line-height) font-medium whitespace-nowrap select-none",
    "focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ink disabled:pointer-events-none disabled:opacity-50",
    "aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg[data-icon]]:size-phi-2",
  ],
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/80",
        outline:
          "border-rule bg-canvas text-ink hover:bg-ink hover:text-canvas",
        secondary:
          "bg-secondary text-secondary-foreground hover:bg-[color-mix(in_oklch,var(--secondary),var(--foreground)_5%)] aria-expanded:bg-secondary aria-expanded:text-secondary-foreground",
        ghost:
          "hover:bg-muted hover:text-foreground aria-expanded:bg-muted aria-expanded:text-foreground dark:hover:bg-muted/50",
        destructive:
          "bg-destructive/10 text-destructive hover:bg-destructive/20 focus-visible:border-destructive/40 focus-visible:ring-destructive/20 dark:bg-destructive/20 dark:hover:bg-destructive/30 dark:focus-visible:ring-destructive/40",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "gap-phi-tight px-phi-0",
        xs: "gap-phi-fine px-phi-tight [&_svg:not([width])]:size-(--text-meta)",
        sm: "gap-phi-fine px-phi-tight [&_svg:not([width])]:size-phi-2",
        lg: "gap-phi-0 px-phi-0 text-base",
        icon: "px-phi-tight [&_svg:not([width])]:size-phi-2",
        "icon-xs": "px-phi-tight [&_svg:not([width])]:size-(--text-meta)",
        "icon-sm": "px-phi-tight [&_svg:not([width])]:size-phi-2",
        "icon-lg": "px-phi-0 [&_svg:not([width])]:size-phi-3",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function Button({
  className,
  variant = "default",
  size = "default",
  ...props
}: ButtonPrimitive.Props & VariantProps<typeof buttonVariants>) {
  return (
    <ButtonPrimitive
      data-slot="button"
      className={state => cn(buttonVariants({ variant, size }), typeof className === "function" ? className(state) : className)}
      {...props}
    />
  )
}

export { Button, buttonVariants }
