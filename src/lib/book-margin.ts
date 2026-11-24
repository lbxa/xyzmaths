/** Extra space before each item in a column that already has a regular gap. */
export function marginOffsets(items: readonly { top: number; height: number }[], gap: number) {
  let bottom = 0;
  return items.map(({ top, height }, index) => {
    const earliest = bottom + (index === 0 ? 0 : gap);
    const extra = Math.max(0, top - earliest);
    bottom = earliest + extra + height;
    return extra;
  });
}

interface MarginNote {
  note: HTMLLIElement;
  reference: HTMLElement;
  placeholder: Comment;
}

function fragmentId(hash: string) {
  try {
    return decodeURIComponent(hash.slice(1));
  } catch {
    return hash.slice(1);
  }
}

function findMarginNotes(body: HTMLElement): MarginNote[] {
  const doc = body.ownerDocument;
  const notes: MarginNote[] = [];
  for (const note of body.querySelectorAll<HTMLLIElement>("li[data-margin-note]:not(:has(figure, img))")) {
    const back = note.querySelector<HTMLAnchorElement>("a.footnote-back[href]");
    const reference = back && doc.getElementById(fragmentId(back.hash));
    if (!reference || !body.contains(reference)) continue;
    notes.push({ note, reference, placeholder: doc.createComment("Manuscript margin note") });
  }
  return notes.sort((a, b) => {
    if (a.reference === b.reference) return 0;
    return a.reference.compareDocumentPosition(b.reference) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1;
  });
}

export function mountBookMargin(spread: HTMLElement) {
  const body = spread.querySelector<HTMLElement>("[data-reading-body]");
  const rail = spread.querySelector<HTMLElement>("#right-aside");
  const list = rail?.querySelector<HTMLOListElement>("[data-margin-items]");
  if (!body || !rail || !list) return;
  const notes = findMarginNotes(body);
  if (!notes.length) return;

  const listeners = new AbortController();
  const { signal } = listeners;
  const emptySources = new Map<HTMLElement, string | null>();
  let active = false;
  let printing = false;
  let frame = 0;

  function position() {
    const top = list!.getBoundingClientRect().top;
    const gap = parseFloat(getComputedStyle(list!).rowGap) || 0;
    // Read every box before writing. The list stays in normal flow even when
    // several notes must extend below the final lines of the manuscript.
    const measurements = notes.map(({ reference, note }) => ({
      top: reference.getBoundingClientRect().top - top,
      height: note.getBoundingClientRect().height,
    }));
    marginOffsets(measurements, gap).forEach((offset, index) => {
      const style = notes[index].note.style;
      const value = `${offset}px`;
      if (style.getPropertyValue("--margin-offset") !== value) style.setProperty("--margin-offset", value);
    });
  }

  function schedule() {
    if (frame || signal.aborted) return;
    frame = requestAnimationFrame(() => {
      frame = 0;
      layout();
    });
  }

  function setWide(wide: boolean) {
    if (active === wide) return;
    active = wide;
    const focus = spread.ownerDocument.activeElement;
    const restoreFocus = focus instanceof HTMLElement && notes.some(({ note }) => note.contains(focus));
    if (wide) {
      for (const { note, placeholder } of notes) {
        note.replaceWith(placeholder);
        list!.appendChild(note);
      }
      for (const section of body!.querySelectorAll<HTMLElement>(".footnotes:not(:has(li))")) {
        emptySources.set(section, section.getAttribute("aria-hidden"));
        section.setAttribute("aria-hidden", "true");
      }
      spread.setAttribute("data-margin-active", "");
      rail!.hidden = false;
    } else {
      for (const { note, placeholder } of notes) {
        placeholder.replaceWith(note);
        note.style.removeProperty("--margin-offset");
      }
      for (const [section, previous] of emptySources) {
        if (previous === null) section.removeAttribute("aria-hidden");
        else section.setAttribute("aria-hidden", previous);
      }
      emptySources.clear();
      rail!.hidden = true;
      spread.removeAttribute("data-margin-active");
    }
    if (restoreFocus && focus.isConnected) focus.focus({ preventScroll: true });
  }

  function layout() {
    // The reader's container query decides whether the manuscript and notes fit side by side.
    setWide(!printing && getComputedStyle(spread).display === "grid");
    if (active) position();
  }

  const sizes = new ResizeObserver(schedule);
  sizes.observe(spread);
  sizes.observe(body);
  const column = body.querySelector("#reading-column");
  if (column) sizes.observe(column);
  for (const { note } of notes) sizes.observe(note);
  const readerLayout = new MutationObserver(schedule);
  readerLayout.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["data-reading-width", "data-reader-size", "data-reader-theme"],
  });
  spread.addEventListener("load", schedule, { capture: true, signal });
  spread.addEventListener("error", schedule, { capture: true, signal });
  document.fonts?.addEventListener("loadingdone", schedule, { signal });
  document.fonts?.ready.then(schedule);
  window.addEventListener("resize", schedule, { signal });
  window.addEventListener("beforeprint", () => { printing = true; setWide(false); }, { signal });
  window.addEventListener("afterprint", () => { printing = false; schedule(); }, { signal });
  layout();

  return () => {
    listeners.abort();
    sizes.disconnect();
    readerLayout.disconnect();
    cancelAnimationFrame(frame);
    setWide(false);
  };
}
