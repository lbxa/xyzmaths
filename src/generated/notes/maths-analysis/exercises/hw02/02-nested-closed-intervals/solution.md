::::::div{class="proof"}

*Solution.* Let

$$
I_n=[n,\infty),\qquad n\geq1.
$$

Each $I_n$ is a nonempty closed interval in $\mathbb{R}$, since $n\in I_n$ and its complement $(-\infty,n)$ is open. Moreover,

$$
I_{n+1}=[n+1,\infty)\subset[n,\infty)=I_n,
$$

Thus the intervals are nested, as shown in [Figure C.10](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw02:unbounded-intervals).

For any $x\in\mathbb{R}$, the Archimedean property gives a positive integer $n>x$. Then $x\notin[n,\infty)=I_n$. Consequently, no real number belongs to every $I_n$, and

$$
\bigcap_{n=1}^{\infty}I_n=\varnothing.
$$

:::::div{class="margin-figure"}

::::figure{id="fig:hw02:unbounded-intervals"}

[![Each ray \[n,\\infty) includes its finite left endpoint and extends indefinitely to the right.](/notes/maths-analysis/figures/unbounded-intervals.svg){.tikz-diagram}](/notes/maths-analysis/figures/unbounded-intervals.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.10. Each ray $[n,\infty)$ includes its finite left endpoint and extends indefinitely to the right.

:::

::::

:::::

The missing hypothesis in the nested interval property is *boundedness*. All the intervals $I_n$ are unbounded, and their left endpoints eventually exceed every fixed real number. ◻

::::::
