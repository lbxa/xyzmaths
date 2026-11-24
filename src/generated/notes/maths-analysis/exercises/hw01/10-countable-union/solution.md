:::::div{class="proof"}

*Solution.* Since each $A_n$ is countably infinite, there exists a bijection from $\mathbb{N}$ to $A_n$. Using the axiom of countable choice, select one such bijection for each $n$. This gives a list without repetition within each row, which we write as

$$
A_n=\{a_{n,1},a_{n,2},a_{n,3},\ldots\}.
$$

Put these lists into rows. Reading one whole row first would never reach the next row. Instead, follow successive diagonals $n+m=2,3,\ldots$, alternating direction as in [Figure C.2](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw01:diagonal-enumeration). This gives

$$
a_{1,1},\ a_{1,2},\ a_{2,1},\ a_{3,1},
  \ a_{2,2},\ a_{1,3},\ a_{1,4},\ldots.
$$

::::figure{id="fig:hw01:diagonal-enumeration"}

[![Follow the arrows along diagonals of constant n+m. Every entry is reached after finitely many steps.](/notes/maths-analysis/figures/diagonal-enumeration.svg){.tikz-diagram}](/notes/maths-analysis/figures/diagonal-enumeration.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.2. Follow the arrows along diagonals of constant $n+m$. Every entry is reached after finitely many steps.

:::

::::

Each diagonal is finite, and each $a_{n,m}$ has only finitely many diagonals before its own. Hence every entry is eventually reached. Every element of $A$ occurs in some row, so this sequence contains all of $A$.

The sets may overlap. Skip any value already listed, keeping only its first occurrence. Every element has a first occurrence at a finite position, so none is lost by this procedure. The retained list contains each element of $A$ exactly once. Since $A_1\subseteq A$ is infinite, the retained list is also infinite. Numbering its entries in order gives a bijection from $\mathbb{N}$ to $A$. Therefore

$$
|A|=\aleph_0.
$$

 ◻

:::::
