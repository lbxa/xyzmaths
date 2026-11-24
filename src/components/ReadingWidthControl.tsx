import { useEffect, useState } from "react";
import { ControlTooltip, TooltipProvider } from "@/components/ui/tooltip";
import { CentredTextIcon, WideTextIcon } from "@/components/ui/icons";
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group";
import { getReadingWidth, setReadingWidth, type ReadingWidth } from "@/lib/reading-width";

export default function ReadingWidthControl() {
  const [width, selectWidth] = useState<ReadingWidth | null>(null);
  useEffect(() => selectWidth(getReadingWidth()), []);

  return (
    <TooltipProvider><ToggleGroup<ReadingWidth>
      aria-label="Text width"
      className={width === null ? "invisible" : undefined}
      value={[width ?? "centred"]}
      onValueChange={([next], details) => {
        if (!next) {
          details.cancel();
          return;
        }
        setReadingWidth(next);
        selectWidth(next);
      }}
    >
      <ControlTooltip tip="Use a centred reading column"><ToggleGroupItem value="centred" aria-label="Centred text" aria-controls="reading-column">
        <CentredTextIcon />
      </ToggleGroupItem></ControlTooltip>
      <ControlTooltip tip="Use the full reading width"><ToggleGroupItem value="wide" aria-label="Wide text" aria-controls="reading-column">
        <WideTextIcon />
      </ToggleGroupItem></ControlTooltip>
    </ToggleGroup></TooltipProvider>
  );
}
