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

export const mathematicalAnalysis: Book = {
  slug: "maths-analysis",
  title: "Introduction to Mathematical Analysis",
  href: "/notes/maths-analysis/",
  author: "Lucas Barbosa",
  description: "Graduate course notes on real analysis, from countability and completeness to limits, differentiation, and the convergence of sequences of functions.",
  manuscript: {
    href: "/books/maths-analysis/manuscript.pdf",
    assetStem: "introduction-to-mathematical-analysis",
    archivedPdf: "https://github.com/lbxa/maths-analysis/releases/download/v6/introduction-to-mathematical-analysis-v6.pdf",
  },
  frontispiece: {
    image: "figures/number-systems.svg",
    destination: "analysis-i/sets-and-foundations/#fig:number-systems",
    caption: "Containment of the number systems",
    alt: "Nested rectangles place the natural, rational, real algebraic, real, and complex numbers inside one another. The transcendental reals lie outside the algebraic rectangle.",
  },
};

export const books: readonly Book[] = [linearAlgebra, mathematicalAnalysis];
