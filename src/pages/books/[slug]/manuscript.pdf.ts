import type { APIRoute } from "astro";
import { books, type Book } from "@/lib/books";

export const prerender = false;

interface Release {
  tag_name: string;
  draft: boolean;
  prerelease: boolean;
  assets: { name: string; state: string; browser_download_url: string }[];
}

const releasesApi = "https://api.github.com/repos/lbxa/xyzmaths/releases";
const cacheSeconds = 300;
const editions = new Map<string, { href: string; expires: number }>();

async function publishedPdf(book: Book) {
  const prefix = book.slug + "-v";
  const signal = AbortSignal.timeout(5000);
  let highest = 0;
  let href: string | undefined;
  for (let page = 1; ; page++) {
    const response = await fetch(`${releasesApi}?per_page=100&page=${page}`, {
      headers: { Accept: "application/vnd.github+json", "User-Agent": "XYZ-Maths-Books" },
      signal,
    });
    // The release API answers 404 while the shared repository is private.
    if (response.status === 404) return;
    if (!response.ok) throw new Error(`GitHub releases returned HTTP ${response.status}`);
    const releases = await response.json() as Release[];
    for (const release of releases) {
      if (release.draft || release.prerelease || !release.tag_name.startsWith(prefix)) continue;
      const version = release.tag_name.slice(prefix.length);
      if (!/^[1-9]\d*$/.test(version) || Number(version) <= highest) continue;
      const filename = `${book.manuscript.assetStem}-v${version}.pdf`;
      const asset = release.assets.find(item => item.name === filename && item.state === "uploaded");
      if (asset) {
        highest = Number(version);
        href = asset.browser_download_url;
      }
    }
    if (!response.headers.get("Link")?.includes('rel="next"')) return href;
  }
}

export const GET: APIRoute = async ({ params }) => {
  const book = books.find(entry => entry.slug === params.slug);
  if (!book) return new Response("Book not found.", { status: 404 });

  const previous = editions.get(book.slug);
  let href = previous?.href ?? book.manuscript.archivedPdf;
  if (!previous || previous.expires <= Date.now()) {
    try {
      href = await publishedPdf(book) ?? book.manuscript.archivedPdf;
      if (href) editions.set(book.slug, { href, expires: Date.now() + cacheSeconds * 1000 });
    } catch {
      // Keep a known published edition reachable during timeouts or API rate limiting.
      if (!href) return new Response("GitHub Releases is temporarily unavailable.", {
        status: 503, headers: { "Retry-After": "60" },
      });
    }
  }
  if (!href) return new Response("A manuscript has yet to be published for this book.", { status: 404 });
  return new Response(null, {
    status: 302, headers: { Location: href, "Cache-Control": `public, max-age=${cacheSeconds}` },
  });
};

export const HEAD = GET;
