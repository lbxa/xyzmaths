::::::div{class="proof"}

*Solution.* Let $\mathbb{A}$ be the set of real algebraic numbers and $\mathbb{T}$ the set of real transcendental numbers. An algebraic number is a root of a nonzero polynomial with integer coefficients. A transcendental number is not such a root. Hence

$$
\mathbb{R}=\mathbb{A}\cup\mathbb{T},
  \qquad\mathbb{A}\cap\mathbb{T}=\varnothing.
$$

First, we show that $\mathbb{A}$ is countable. For each $n\ge1$, consider the nonzero polynomials

$$
P(X)=c_0+c_1X+\cdots+c_nX^n,
  \qquad c_j\in\mathbb{Z},\quad |c_j|\le n.
$$

Each of the $n+1$ coefficients has $2n+1$ possible values, so there are at most $(2n+1)^{n+1}$ such polynomials. A nonzero polynomial of degree at most $n$ has at most $n$ distinct real roots. Thus the set $F_n$ of all their real roots is finite.

Every algebraic number is a root of a nonzero integer polynomial. Taking $n$ at least as large as its degree and the absolute values of all its coefficients places that root in $F_n$. Conversely, every root in $F_n$ is algebraic. Hence

$$
\mathbb{A}=\bigcup_{n=1}^{\infty}F_n.
$$

Within each finite set $F_n$, list the roots in increasing order. Read these finite lists in the order $F_1,F_2,\ldots$, skipping repeated roots. Each root is reached after finitely many steps. This proves that $\mathbb{A}$ is countable. Every $n\in\mathbb{N}$ is a root of $X-n$, so $\mathbb{N}\subseteq\mathbb{A}$. Thus $\mathbb{A}$ is infinite, and $|\mathbb{A}|=\aleph_0$.

:::::div{class="margin-figure"}

::::figure{id="fig:hw01:continuum-gap"}

[![CH excludes intermediate cardinalities. Since \\mathbb\{T\} is uncountable and contained in \\mathbb\{R\}, its cardinality must equal \\aleph.](/notes/maths-analysis/figures/continuum-gap.svg){.tikz-diagram}](/notes/maths-analysis/figures/continuum-gap.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.8. CH excludes intermediate cardinalities. Since $\mathbb{T}$ is uncountable and contained in $\mathbb{R}$, its cardinality must equal $\aleph$.

:::

::::

:::::

Now suppose that $\mathbb{T}$ were countable. Then $\mathbb{R}=\mathbb{A}\cup\mathbb{T}$ would be a union of two countable sets and therefore countable. This contradicts the uncountability of $\mathbb{R}$. Hence $\mathbb{T}$ is uncountable. Since $\mathbb{T}\subseteq\mathbb{R}$, we have

$$
\aleph_0<|\mathbb{T}|\le|\mathbb{R}|=\aleph.
$$

By CH there is no cardinality strictly between $\aleph_0$ and $\aleph$, as illustrated in [Figure C.8](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw01:continuum-gap). The lower endpoint is already excluded, so the only possibility is

$$
|\mathbb{T}|=\aleph.
$$

 ◻

::::::
