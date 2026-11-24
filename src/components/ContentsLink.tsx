import { cn } from "cn";
import type { ComponentProps } from "react";
import { readerLinkStyle } from "@/lib/reader-links";

export default function ContentsLink({ className, ...props }: ComponentProps<"a">) {
  return <a {...props} className={cn(readerLinkStyle, "px-phi-tight py-phi-fine", className)} />;
}
