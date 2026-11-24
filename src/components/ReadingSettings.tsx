import { useEffect, useState } from "react";
import { cn } from "cn";
import { Button } from "@/components/ui/button";
import { CloseIcon, ContrastIcon } from "@/components/ui/icons";
import { Popover, PopoverClose, PopoverContent, PopoverHeader, PopoverTitle, PopoverTrigger } from "@/components/ui/popover";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Separator } from "@/components/ui/separator";
import { ControlTooltip, TooltipProvider } from "@/components/ui/tooltip";
import { getReaderPreferences, preferenceEvent, readerDefaults, readerOptions, setReaderPreference, type ReaderPreferences } from "@/lib/reader-preferences";

const themeTips = {
  original: "Classic ink and paper",
  quiet: "Soft, cool greys",
  paper: "Warm ivory paper",
  bold: "Strong contrast and heavier book text",
  calm: "Earthy, muted browns",
  focus: "Muted olive tones",
};
const titleCase = (word: string) => word.charAt(0).toUpperCase() + word.slice(1);
const modes = readerOptions.colorMode.map(value => ({ value, label: titleCase(value) }));

function TextSizeControl({ size }: { size: ReaderPreferences["readerSize"] }) {
  const steps = readerOptions.readerSize;
  const index = steps.indexOf(size);
  return (
    <div role="group" aria-label="Book text size"
      className="group/size relative grid min-w-0 grid-cols-2 items-center rounded-full bg-settings-control">
      <ControlTooltip tip="Make book text and equations smaller">
        <Button variant="ghost" aria-label="Decrease text size" aria-controls="reader-manuscript"
          disabled={index === 0} onClick={() => setReaderPreference("readerSize", steps[index - 1])}
          className="min-h-touch-target rounded-s-full rounded-e-none hover:bg-ink/10">
          <span aria-hidden="true" className="font-interface text-base leading-none">A</span>
        </Button>
      </ControlTooltip>
      <ControlTooltip tip="Make book text and equations larger">
        <Button variant="ghost" aria-label="Increase text size" aria-controls="reader-manuscript"
          disabled={index === steps.length - 1} onClick={() => setReaderPreference("readerSize", steps[index + 1])}
          className="min-h-touch-target rounded-s-none rounded-e-full hover:bg-ink/10">
          <span aria-hidden="true" className="font-interface text-heading leading-none">A</span>
        </Button>
      </ControlTooltip>
      <div className="pointer-events-none absolute inset-y-0 start-1/2 grid -translate-x-1/2 place-items-center">
        {size === "100" && <span aria-hidden="true" className="col-start-1 row-start-1 h-phi-3 w-px bg-ink/25 group-focus-within/size:invisible group-hover/size:invisible" />}
        <output aria-label="Current book text size" className={cn(
          "col-start-1 row-start-1 text-xs text-ink/75 tabular-nums",
          size === "100" && "opacity-0 group-focus-within/size:opacity-100 group-hover/size:opacity-100",
        )}>{size}%</output>
      </div>
    </div>
  );
}

function AppearanceControl({ mode, compact }: { mode: ReaderPreferences["colorMode"]; compact: boolean }) {
  return (
    <Select items={modes} value={mode} onValueChange={value => {
      if (value) setReaderPreference("colorMode", value);
    }}>
      <ControlTooltip tip={mode === "automatic" ? "Appearance follows your device. Choose a mode." : `${titleCase(mode)} appearance. Choose a mode.`}>
        <SelectTrigger variant="pill" aria-label="Appearance">
          <ContrastIcon />
          {!compact && <span className="me-auto">Appearance</span>}
          <SelectValue className="flex-none text-sm">
            {compact && mode === "automatic" ? "Auto" : titleCase(mode)}
          </SelectValue>
        </SelectTrigger>
      </ControlTooltip>
      <SelectContent align="end" sideOffset={6} className="rounded-swatch border-ink/20 bg-settings-panel p-phi-0 font-interface shadow-settings">
        <SelectGroup>
          {modes.map(item => <SelectItem key={item.value} value={item.value} className="pointer-coarse:min-h-touch-target">{item.label}</SelectItem>)}
        </SelectGroup>
      </SelectContent>
    </Select>
  );
}

export default function ReadingSettings({ reader = false }: { reader?: boolean }) {
  const [preferences, setPreferences] = useState(readerDefaults);
  const title = reader ? "Reading settings" : "Appearance settings";
  useEffect(() => {
    const refresh = () => setPreferences(getReaderPreferences());
    refresh();
    window.addEventListener(preferenceEvent, refresh);
    return () => window.removeEventListener(preferenceEvent, refresh);
  }, []);

  return (
    <TooltipProvider><Popover>
      <ControlTooltip tip={reader ? "Adjust book text size, appearance and theme" : "Change site appearance and theme"}>
        <PopoverTrigger aria-label={title} render={<Button variant="outline" />}>
          <span aria-hidden="true" className="font-serif text-base leading-none">Aa</span>
          <span className={reader ? "max-sm:sr-only" : "min-[24rem]:max-sm:sr-only"}>{reader ? "Settings" : "Appearance"}</span>
        </PopoverTrigger>
      </ControlTooltip>
      <PopoverContent align="end">
        <div className="grid gap-phi-1">
          <PopoverHeader>
            <PopoverTitle>Themes &amp; Settings</PopoverTitle>
            <ControlTooltip tip="Close settings">
              <PopoverClose aria-label="Close settings" render={<Button variant="ghost" size="icon"
                className="absolute end-0 size-phi-3 rounded-full text-ink/65 hover:bg-ink/10 hover:text-ink" />}>
                <CloseIcon />
              </PopoverClose>
            </ControlTooltip>
          </PopoverHeader>
          <Separator role="presentation" className="bg-ink/15" />
        </div>
        <div className={reader ? "grid grid-cols-[minmax(0,1fr)_auto] gap-phi-1" : "grid"}>
          {reader && <TextSizeControl size={preferences.readerSize} />}
          <AppearanceControl mode={preferences.colorMode} compact={reader} />
        </div>
        <RadioGroup aria-label="Theme" value={preferences.readerTheme} className="gap-phi-1"
          onValueChange={(value: ReaderPreferences["readerTheme"]) => setReaderPreference("readerTheme", value)}>
          {readerOptions.readerTheme.map(theme =>
            <ControlTooltip key={theme} tip={themeTips[theme]}>
              <RadioGroupItem value={theme} data-reader-theme={theme}>
                <span aria-hidden="true" className="font-serif text-heading leading-none [font-weight:var(--book-weight)]">Aa</span>
                <span className="text-sm leading-tight font-medium">{titleCase(theme)}</span>
              </RadioGroupItem>
            </ControlTooltip>
          )}
        </RadioGroup>
      </PopoverContent>
    </Popover></TooltipProvider>
  );
}
