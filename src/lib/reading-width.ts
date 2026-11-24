export type ReadingWidth = "centred" | "wide";

export const readingWidthStorageKey = "xyzmaths:reading-width";

export function getReadingWidth(): ReadingWidth {
  return document.documentElement.dataset.readingWidth === "wide" ? "wide" : "centred";
}

export function setReadingWidth(width: ReadingWidth) {
  document.documentElement.dataset.readingWidth = width;
  try {
    localStorage.setItem(readingWidthStorageKey, width);
  } catch {
    // The tab keeps its selection even when storage is unavailable.
  }
}
