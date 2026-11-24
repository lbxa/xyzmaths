import { navigate } from "astro:transitions/client";
import { ControlTooltip, TooltipProvider } from "@/components/ui/tooltip";
import type { Book } from "@/lib/books";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

interface Props {
  books: readonly Pick<Book, "slug" | "title" | "href">[];
  currentBook?: string;
}

export default function BookSelector({ books, currentBook }: Props) {
  const items = books.map((book) => ({ value: book.slug, label: book.title }));

  function openBook(slug: string | null) {
    const book = books.find((candidate) => candidate.slug === slug);
    if (book && book.slug !== currentBook) {
      void navigate(book.href);
    }
  }

  return (
    <TooltipProvider><Select items={items} value={currentBook ?? null} onValueChange={openBook}>
      <ControlTooltip tip="Choose a book to read"><SelectTrigger aria-label="Book" className="max-w-full">
        <SelectValue placeholder="Choose a title" />
      </SelectTrigger></ControlTooltip>
      <SelectContent align="start">
        <SelectGroup>
          {items.map((item) => (
            <SelectItem key={item.value} value={item.value}>
              {item.label}
            </SelectItem>
          ))}
        </SelectGroup>
      </SelectContent>
    </Select></TooltipProvider>
  );
}
