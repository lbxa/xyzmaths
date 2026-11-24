export function normalizeHref(href: string) {
  return href.replace(/\/(?=#|$)/, "");
}

export function trailTo<T extends { href?: string; children?: T[] }>(entries: T[], href: string): T[] | undefined {
  for (const entry of entries) {
    if (entry.href && normalizeHref(entry.href) === href) return [entry];
    const trail = entry.children && trailTo(entry.children, href);
    if (trail) return [entry, ...trail];
  }
}

export function currentFragment() {
  try {
    return decodeURIComponent(window.location.hash);
  } catch {
    return window.location.hash;
  }
}

export function watchPageFragment(onChange: (fragment: string) => void) {
  const sync = () => onChange(currentFragment());
  // Astro can push a same-page link into history without firing hashchange.
  const afterLink = (event: MouseEvent) => {
    const link = event.target instanceof Element && event.target.closest<HTMLAnchorElement>("a[href]");
    if (link && link.origin === location.origin && link.pathname === location.pathname && link.search === location.search
        && !event.metaKey && !event.ctrlKey && !event.shiftKey && !event.altKey) {
      queueMicrotask(sync);
    }
  };
  sync();
  document.addEventListener("click", afterLink);
  document.addEventListener("astro:page-load", sync);
  window.addEventListener("hashchange", sync);
  window.addEventListener("popstate", sync);
  return () => {
    document.removeEventListener("click", afterLink);
    document.removeEventListener("astro:page-load", sync);
    window.removeEventListener("hashchange", sync);
    window.removeEventListener("popstate", sync);
  };
}
