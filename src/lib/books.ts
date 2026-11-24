export interface Book {
  slug: string;
  title: string;
  href: string;
  author: string;
  description: string;
  manuscript: {
    href: string;
    assetStem: string;
    archivedPdf?: string;
  };
  frontispiece?: { image: string; destination: string; caption: string; alt: string };
}

export const linearAlgebra: Book = {
  slug: "linear-algebra",
  title: "Linear Algebra",
  href: "/notes/linear-algebra/",
  author: "Lucas Barbosa",
  description: "Graduate course notes on vector spaces and linear maps, from bases and coordinates to determinants, eigenvalues, and inner products.",
  manuscript: {
    href: "/books/linear-algebra/manuscript.pdf",
    assetStem: "linear-algebra",
    archivedPdf: "https://github.com/lbxa/linear-algebra/releases/download/v3/linear-algebra-v3.pdf",
  },
  frontispiece: {
    image: "figures/linear-map-grid-overview.svg",
    destination: "linear-algebra-i/vector-spaces-and-bases/#fig:linear-algebra-i:shear-grid-overview",
    caption: "A shear of the coordinate plane",
    alt: "A square coordinate grid beside its sheared image, with horizontal rows and slanted columns.",
  },
};

// Add a book here when its reading edition has published web routes.
export const books: readonly Book[] = [linearAlgebra];
