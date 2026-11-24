import { getCollection } from "astro:content";
import type { APIRoute } from "astro";

export const prerender = true;
export async function getStaticPaths() {
  return (await getCollection("bookFigures")).map((entry) => ({
    params: { book: entry.data.book, asset: entry.data.asset }, props: { content: entry.data.content },
  }));
}

export const GET: APIRoute = ({ params, props }) => {
  const extension = params.asset!.split(".").pop()!;
  const type = extension === "svg" ? "image/svg+xml" : `image/${extension === "jpg" ? "jpeg" : extension}`;
  const body = extension === "svg" ? props.content : Uint8Array.from(atob(props.content), (char) => char.charCodeAt(0));
  return new Response(body, { headers: { "Content-Type": type } });
};
