import assert from "node:assert/strict";
import { test } from "node:test";
import { createContext } from "astro/middleware";
import { GET } from "../src/pages/books/[slug]/manuscript.pdf";

function download(slug: string) {
  return GET(createContext({
    request: new Request(`https://xyzmaths.org/books/${slug}/manuscript.pdf`),
    params: { slug }, defaultLocale: "en",
  }));
}

function release(tag: string, filename: string, state = "uploaded") {
  const url = `https://github.com/lbxa/xyzmaths/releases/download/${tag}/${filename}`;
  return { tag_name: tag, draft: false, prerelease: false, assets: [{ name: filename, state, browser_download_url: url }] };
}

test("a public book PDF supersedes the archived v3 after the shared repository becomes public", async () => {
  let published = false;
  let now = Date.now();
  const originalClock = Date.now;
  const originalFetch = globalThis.fetch;
  const pages: string[] = [];
  const newest = release("linear-algebra-v11", "linear-algebra-v11.pdf");
  Date.now = () => now;
  globalThis.fetch = async input => {
    const page = new URL(input instanceof Request ? input.url : input).searchParams.get("page")!;
    pages.push(page);
    if (!published) return new Response(null, { status: 404 });
    if (page === "2") return Response.json([newest]);
    assert.deepEqual(pages, ["1"]);
    return Response.json([
      { ...release("linear-algebra-v16", "linear-algebra-v16.pdf"), draft: true },
      release("maths-analysis-v15", "linear-algebra-v15.pdf"),
      release("linear-algebra-v14", "assignment-v14.pdf"),
      release("linear-algebra-v13", "linear-algebra-v13.pdf", "open"),
      { ...release("linear-algebra-v12", "linear-algebra-v12.pdf"), prerelease: true },
      release("linear-algebra-v9", "linear-algebra-v9.pdf"),
    ], { headers: { Link: '<https://api.github.com/repos/lbxa/xyzmaths/releases?per_page=100&page=2>; rel="next"' } });
  };

  try {
    const archived = await download("linear-algebra");
    assert.equal(archived.status, 302);
    assert.equal(archived.headers.get("Location"), "https://github.com/lbxa/linear-algebra/releases/download/v3/linear-algebra-v3.pdf");
    assert.deepEqual(pages, ["1"]);

    pages.length = 0;
    published = true;
    now += 60 * 60 * 1000;
    const current = await download("linear-algebra");
    assert.equal(current.status, 302);
    assert.equal(current.headers.get("Location"), newest.assets[0].browser_download_url);
    assert.deepEqual(pages, ["1", "2"]);
  } finally {
    globalThis.fetch = originalFetch;
    Date.now = originalClock;
  }
});

test("an unknown book returns 404 without requesting a release", async () => {
  let called = false;
  const originalFetch = globalThis.fetch;
  globalThis.fetch = async () => {
    called = true;
    return new Response(null, { status: 404 });
  };
  try {
    assert.equal((await download("unknown-book")).status, 404);
    assert.equal(called, false);
  } finally {
    globalThis.fetch = originalFetch;
  }
});
