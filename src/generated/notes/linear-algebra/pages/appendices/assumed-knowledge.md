---
title: "Assumed knowledge"
group: "Appendices"
order: 17
page: "123"
outline: [{"id": "sec:appendix:set-theory", "title": "B.1 Set theory", "level": 2}, {"id": "sec:linear-algebra-i:set-equality-proofs", "title": "Proving equality of sets", "level": 3}, {"id": "sec:appendix:map-properties", "title": "B.2 Injective, surjective, and bijective maps", "level": 2}, {"id": "injectivity-1", "title": "Injectivity", "level": 3}, {"id": "surjectivity", "title": "Surjectivity", "level": 3}, {"id": "bijectivity", "title": "Bijectivity", "level": 3}, {"id": "examples-in-euclidean-spaces-1", "title": "Examples in Euclidean spaces", "level": 3}, {"id": "an-injective-plane-inclusion.", "title": "An injective plane inclusion.", "level": 5}, {"id": "a-surjective-coordinate-projection.", "title": "A surjective coordinate projection.", "level": 5}, {"id": "a-bijective-coordinate-swap.", "title": "A bijective coordinate swap.", "level": 5}]
---

# Appendix B. Assumed knowledge {id="ch:appendix:assumed-knowledge"}

## B.1 Set theory {id="sec:appendix:set-theory"}

### Proving equality of sets {id="sec:linear-algebra-i:set-equality-proofs"}

:::div{class="pending-review"}

To prove that sets $S$ and $T$ are equal, we show that they have exactly the same elements. This requires both inclusions,

$$
S=T\quad\Longleftrightarrow\quad
  S\subseteq T\ \text{and}\ T\subseteq S.
$$

**First inclusion, $S\subseteq T$.** Let $x\in S$ be arbitrary. Use the description of $S$ to show that $x$ also belongs to $T$. Since $x$ was arbitrary, this proves that every element of $S$ belongs to $T$.

**Reverse inclusion, $T\subseteq S$.** Now let $x\in T$ be arbitrary, and show that $x\in S$. This proves that every element of $T$ belongs to $S$. With both inclusions established, conclude that $S=T$.

Both branches in [Figure B.1](/notes/linear-algebra/appendices/assumed-knowledge/#fig:linear-algebra-i:set-equality-proof-tree) must be completed. Each starts with membership in one set and establishes membership in the other.

:::

::::figure{id="fig:linear-algebra-i:set-equality-proof-tree"}

[![A proof tree for set equality. Both inclusions are required, and each is proved by considering an arbitrary element of the set on the left.](/notes/linear-algebra/figures/set-equality-proof-tree.svg){.tikz-diagram}](/notes/linear-algebra/figures/set-equality-proof-tree.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure B.1. A proof tree for set equality. Both inclusions are required, and each is proved by considering an arbitrary element of the set on the left.

:::

::::

## B.2 Injective, surjective, and bijective maps {id="sec:appendix:map-properties"}

Let $f:A\to B$ be a function, also called a map. The set $A$ is its *domain*, and $B$ is its *codomain*. Every element of $A$ has exactly one output in $B$. This requirement alone does not say whether every element of $B$ is reached or whether two different inputs can have the same output.

### Injectivity {id="injectivity-1"}

The map $f$ is *injective*, or *one-to-one*, if distinct inputs have distinct outputs. Equivalently,

$$
f(a_1)=f(a_2)\quad\Longrightarrow\quad a_1=a_2.
$$

[^11] Each codomain element has at most one input mapping to it. Some codomain elements may have no such input, as the top panel of [Figure B.2](/notes/linear-algebra/appendices/assumed-knowledge/#fig:recall:map-properties) shows.

:::notes{id="footnotes-10"}

[^11]: As a mnemonic, think of the *in* in *injective* as a reminder to check the *inputs*. Different inputs must remain distinguishable through their outputs.

:::

### Surjectivity {id="surjectivity"}

The map $f$ is *surjective*, or *onto*, if every element of the codomain is the output of at least one input. Equivalently,

$$
\text{for every }b\in B,\text{ there exists }a\in A
  \text{ such that }f(a)=b.
$$

Different inputs may have the same output. In the middle panel of [Figure B.2](/notes/linear-algebra/appendices/assumed-knowledge/#fig:recall:map-properties), every codomain element receives an arrow, and two inputs share an output.

### Bijectivity {id="bijectivity"}

The map $f$ is *bijective* if it is both injective and surjective. Every codomain element then has exactly one input mapping to it. This gives a one-to-one correspondence between the entire domain and codomain, as in the bottom panel of [Figure B.2](/notes/linear-algebra/appendices/assumed-knowledge/#fig:recall:map-properties). Bijectivity imposes both conditions, so it is stronger than either condition alone.

::::figure{id="fig:recall:map-properties"}

[![Three maps between finite sets. Each dot is an element. The top map is injective and leaves an output unused. The middle map is surjective and reaches every output, but two inputs share an output. The bottom map is bijective and reaches every output exactly once. These finite-set diagrams illustrate the definitions. The ellipses are not pictures of vector subspaces.](/notes/linear-algebra/figures/map-properties.svg){.tikz-diagram}](/notes/linear-algebra/figures/map-properties.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure B.2. Three maps between finite sets. Each dot is an element. The top map is injective and leaves an output unused. The middle map is surjective and reaches every output, but two inputs share an output. The bottom map is bijective and reaches every output exactly once. These finite-set diagrams illustrate the definitions. The ellipses are not pictures of vector subspaces.

:::

::::

### Examples in Euclidean spaces {id="examples-in-euclidean-spaces-1"}

The same definitions apply to maps between spaces such as $\mathbb{R}^2$ and $\mathbb{R}^3$. The domain and codomain are part of each example.

##### An injective plane inclusion. {id="an-injective-plane-inclusion."}

Consider

$$
Z:\mathbb{R}^2\to\mathbb{R}^3,\qquad Z(x,y)=(x,y,0).
$$

Different pairs retain their distinct first two coordinates, so $Z$ is injective. Its image is the $xy$-plane. It is not surjective onto $\mathbb{R}^3$, since an output with a nonzero third coordinate is never reached. [Figure B.3](/notes/linear-algebra/appendices/assumed-knowledge/#fig:recall:plane-inclusion) shows a pair and its image in that plane.

::::figure{id="fig:recall:plane-inclusion"}

[![Schematic inclusion Z\:\\mathbb\{R\}^2\\to\\mathbb\{R\}^3. The shaded region depicts part of the xy-plane, which continues beyond the drawing. The marked input maps to a point in this plane. Distinct input coordinates remain distinct after inclusion.](/notes/linear-algebra/figures/map-plane-inclusion.svg){.tikz-diagram}](/notes/linear-algebra/figures/map-plane-inclusion.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure B.3. Schematic inclusion $Z:\mathbb{R}^2\to\mathbb{R}^3$. The shaded region depicts part of the $xy$-plane, which continues beyond the drawing. The marked input maps to a point in this plane. Distinct input coordinates remain distinct after inclusion.

:::

::::

##### A surjective coordinate projection. {id="a-surjective-coordinate-projection."}

Consider

$$
U:\mathbb{R}^3\to\mathbb{R}^2,\qquad U(x,y,z)=(y,z).
$$

Every pair $(y,z)$ is attained, for instance from $(0,y,z)$, so $U$ is surjective. It is not injective, since changing $x$ leaves the output unchanged. [Figure B.4](/notes/linear-algebra/appendices/assumed-knowledge/#fig:recall:coordinate-projection) shows inputs differing in the $x$-direction sharing an output.

::::figure{id="fig:recall:coordinate-projection"}

[![Schematic projection U\:\\mathbb\{R\}^3\\to\\mathbb\{R\}^2. The marked inputs lie on a line parallel to the x-axis and have the same y,z coordinates. They map to the same pair. Every pair in the codomain is attained.](/notes/linear-algebra/figures/map-coordinate-projection.svg){.tikz-diagram}](/notes/linear-algebra/figures/map-coordinate-projection.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure B.4. Schematic projection $U:\mathbb{R}^3\to\mathbb{R}^2$. The marked inputs lie on a line parallel to the $x$-axis and have the same $y,z$ coordinates. They map to the same pair. Every pair in the codomain is attained.

:::

::::

##### A bijective coordinate swap. {id="a-bijective-coordinate-swap."}

Consider

$$
B:\mathbb{R}^2\to\mathbb{R}^2,\qquad B(x,y)=(y,x).
$$

Each output $(a,b)$ has exactly one preimage, namely $(b,a)$. Thus $B$ is bijective. Swapping coordinates again recovers the original input. [Figure B.5](/notes/linear-algebra/appendices/assumed-knowledge/#fig:recall:coordinate-swap) shows the reflection across the line $x=y$.

::::figure{id="fig:recall:coordinate-swap"}

[![Schematic coordinate swap in \\mathbb\{R\}^2. The dashed diagonal in each coordinate system is x=y. The marked point and its image have exchanged coordinates. Each output has exactly one input.](/notes/linear-algebra/figures/map-coordinate-swap.svg){.tikz-diagram}](/notes/linear-algebra/figures/map-coordinate-swap.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure B.5. Schematic coordinate swap in $\mathbb{R}^2$. The dashed diagonal in each coordinate system is $x=y$. The marked point and its image have exchanged coordinates. Each output has exactly one input.

:::

::::
