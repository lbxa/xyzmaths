::::::div{class="proof"}

*Solution.* Let

$$
I_n=\left(0,\frac1n\right),\qquad n\geq1.
$$

Each $I_n$ is a nonempty bounded interval because it contains $1/(2n)$ and is contained in $(0,1)$. Since $1/(n+1)<1/n$,

$$
I_{n+1}=\left(0,\frac1{n+1}\right)
    \subset I_n.
$$

Thus the intervals are nested, as shown in [Figure C.9](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw02:open-intervals).

:::::div{class="margin-figure"}

::::figure{id="fig:hw02:open-intervals"}

[![The nested intervals I\_n=(0,1/n) exclude 0.](/notes/maths-analysis/figures/open-intervals.svg){.tikz-diagram}](/notes/maths-analysis/figures/open-intervals.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.9. The nested intervals $I_n=(0,1/n)$ exclude $0$.

:::

::::

:::::

To prove that their intersection is empty, let $x\in\mathbb{R}$. If $x\leq0$, then $x\notin I_1$. If $x>0$, the Archimedean property gives a positive integer $n>1/x$.[^59] Then $1/n<x$ and $x\notin I_n$. Hence every real number is excluded from at least one interval, and therefore

$$
\bigcap_{n=1}^{\infty}I_n=\varnothing.
$$

The nested interval property guarantees a nonempty intersection for nested nonempty bounded closed intervals in $\mathbb{R}$. Here the missing hypothesis is *closedness*. Every finite intersection is nonempty, but the only point common to all the closures $[0,1/n]$ is $0$, which is excluded from every $I_n$. ◻

::::::

:::notes{id="footnotes-58"}

[^59]: *Archimedean property.* For every $M\in\mathbb{R}$, there is a positive integer $n>M$.

:::
