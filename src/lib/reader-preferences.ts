export const readerOptions = {
  readerTheme: ["original", "quiet", "paper", "bold", "calm", "focus"],
  colorMode: ["automatic", "light", "dark"],
  readerSize: ["80", "90", "100", "110", "125", "150", "175", "200"],
} as const;

export type Preference = keyof typeof readerOptions;
export type ReaderPreferences = { [K in Preference]: (typeof readerOptions)[K][number] };

export const readerDefaults: ReaderPreferences = {
  readerTheme: "original",
  colorMode: "automatic",
  readerSize: "100",
};
export const preferencePrefix = "xyzmaths:appearance:";
export const preferenceEvent = "xyzmaths:appearance-change";
const keys = Object.keys(readerOptions) as Preference[];

function validValue<K extends Preference>(key: K, value?: string | null): ReaderPreferences[K] {
  const choices: readonly string[] = readerOptions[key];
  return value && choices.includes(value) ? value as ReaderPreferences[K] : readerDefaults[key];
}

export function getReaderPreferences(): ReaderPreferences {
  const { dataset } = document.documentElement;
  return {
    readerTheme: validValue("readerTheme", dataset.readerTheme),
    colorMode: validValue("colorMode", dataset.colorMode),
    readerSize: validValue("readerSize", dataset.readerSize),
  };
}

export function setReaderPreference<K extends Preference>(key: K, value: ReaderPreferences[K]) {
  document.documentElement.dataset[key] = value;
  try {
    localStorage.setItem(preferencePrefix + key, value);
  } catch {
    // The document retains the choice when the browser disables storage.
  }
  window.dispatchEvent(new Event(preferenceEvent));
}

export function syncStoredPreference(event: StorageEvent) {
  try {
    if (event.storageArea !== window.localStorage) return;
  } catch {
    return;
  }
  if (event.key === null) {
    Object.assign(document.documentElement.dataset, readerDefaults);
  } else {
    const key = keys.find(key => event.key === preferencePrefix + key);
    if (!key) return;
    document.documentElement.dataset[key] = validValue(key, event.newValue);
  }
  window.dispatchEvent(new Event(preferenceEvent));
}
