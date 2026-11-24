::::::div{class="proof"}

*Solution.* Since $\sqrt{2}<2$, we have $5-\sqrt{2}>0$. The existence and uniqueness of nonnegative cube roots therefore gives a number

$$
c=(5-\sqrt{2})^{1/3}>0,\qquad c^3=5-\sqrt{2}.
$$

If $a\leq0$, then $a^3\leq0<c^3$, so $a\notin A$. On the nonnegative real numbers, $x \mapsto x^3$ is strictly increasing. Hence $a^3>c^3$ holds exactly when $a>c$, and therefore

$$
A=(c,\infty).
$$

For part (a), take

$$
B=\mathbb{R}\setminus A=(-\infty,c].
$$

Then $A\cup B=\mathbb{R}$ and $A\cap B=\varnothing$. Both sets are nonempty, since $c+1\in A$ and $c\in B$. For every $b\in B$ and $a\in A$, we have

$$
b\leq c<a.
$$

Thus $B$ is the lower part and $A$ is the upper part of a Dedekind partition, as shown in [Figure C.14](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw03:cubic-partition).

:::::div{class="margin-figure"}

::::figure{id="fig:hw03:cubic-partition"}

[![Schematic partition with the boundary included in B and excluded from A. The two intervals together cover the real line.](/notes/maths-analysis/figures/cubic-partition.svg){.tikz-diagram}](/notes/maths-analysis/figures/cubic-partition.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.14. Schematic partition with the boundary included in $B$ and excluded from $A$. The two intervals together cover the real line.

:::

::::

:::::

For part (b), the displayed inequality shows that $c$ is a boundary for this partition. To see that it is unique, suppose $d$ is another boundary. Since $c\in B$, we must have $c\leq d$. If $d>c$, then

$$
a=\frac{c+d}{2}\in A,\qquad a<d,
$$

contradicting the boundary inequality $d\leq a$. Thus $d=c$, so the Dedekind cut is $(5-\sqrt{2})^{1/3}$.

Geometrically, the two proposed boundaries would leave $(c,d)$ uncovered. Every element of $B$ is at most $c$, and the proposed boundary $d$ would require every element of $A$ to be at least $d$. The midpoint lies in neither region, contradicting $A\cup B=\mathbb{R}$, as illustrated in [Figure C.15](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw03:dedekind-cut-uniqueness).

:::::div{class="margin-figure"}

::::figure{id="fig:hw03:dedekind-cut-uniqueness"}

[![Schematic regions allowed by two proposed boundaries c\<d. They force B\\subseteq(-\\infty,c\] and A\\subseteq\[d,\\infty). Their gap contains (c+d)/2, contradicting A\\cup B=\\mathbb\{R\}.](/notes/maths-analysis/figures/dedekind-cut-uniqueness.svg){.tikz-diagram}](/notes/maths-analysis/figures/dedekind-cut-uniqueness.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.15. Schematic regions allowed by two proposed boundaries $c<d$. They force $B\subseteq(-\infty,c]$ and $A\subseteq[d,\infty)$. Their gap contains $(c+d)/2$, contradicting $A\cup B=\mathbb{R}$.

:::

::::

:::::

For part (c), $c$ is a lower bound of $A$. Any $d>c$ fails to be a lower bound, because $(c+d)/2$ belongs to $A$ and is smaller than $d$. Hence $c$ is the greatest lower bound of $A$. Also, $c$ is an upper bound of $B$ and belongs to $B$, so it is its greatest element and therefore its least upper bound. Consequently,

$$
\inf A=\sup B=(5-\sqrt{2})^{1/3}.
$$

 ◻

::::::
