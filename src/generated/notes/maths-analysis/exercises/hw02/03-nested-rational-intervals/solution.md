::::::div{class="proof"}

*Solution.* For $n\geq1$, define

$$
m_n=\lfloor10^n\sqrt2\rfloor,\qquad
  a_n=\frac{m_n}{10^n},\qquad b_n=\frac{m_n+1}{10^n},
$$

and let $I_n=[a_n,b_n]\cap\mathbb{Q}$. Since $m_n\in\mathbb{Z}$, both endpoints are rational. Thus $I_n$ is nonempty (it contains $a_n$), bounded, and closed relative to $\mathbb{Q}$, being the intersection of a closed subset of $\mathbb{R}$ with $\mathbb{Q}$.

Because $\sqrt2$ is irrational, the definition of the floor function gives $m_n<10^n\sqrt2<m_n+1$. Consequently,

$$
a_n<\sqrt2<b_n,\qquad b_n-a_n=10^{-n}.
$$

[Figure C.12](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw02:rational-nested-intervals) illustrates these rational intervals around the excluded point $\sqrt2$.

:::::div{class="margin-figure"}

::::figure{id="fig:hw02:rational-nested-intervals"}

[![Schematic intervals \[a\_n,b\_n\]\\cap\\mathbb\{Q\}. Hollow markers indicate that \\sqrt2\\notin\\mathbb\{Q\}; all endpoints are rational.](/notes/maths-analysis/figures/rational-nested-intervals.svg){.tikz-diagram}](/notes/maths-analysis/figures/rational-nested-intervals.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.12. Schematic intervals $[a_n,b_n]\cap\mathbb{Q}$. Hollow markers indicate that $\sqrt2\notin\mathbb{Q}$; all endpoints are rational.

:::

::::

:::::

Multiplying by $10$ gives $10m_n<10^{n+1}\sqrt2<10m_n+10$. Taking floors therefore yields

$$
10m_n\leq m_{n+1}\leq10m_n+9.
$$

It follows that

$$
a_{n+1}=\frac{m_{n+1}}{10^{n+1}}\geq a_n,
  \qquad
  b_{n+1}=\frac{m_{n+1}+1}{10^{n+1}}\leq b_n.
$$

Thus $I_{n+1}\subseteq I_n$. In fact, the inclusion is strict because the lengths of the corresponding real intervals decrease by a factor of $10$. By the density of $\mathbb{Q}$ in $\mathbb{R}$, any nonempty open portion removed contains a rational number, so at least one point of $I_n$ does not belong to $I_{n+1}$.

The inequalities

$$
0<\sqrt2-a_n<10^{-n},\qquad
  0<b_n-\sqrt2<10^{-n}
$$

show that $a_n\to\sqrt2$ and $b_n\to\sqrt2$. If $x\in\bigcap_{n=1}^{\infty}I_n$, then $x\in\mathbb{Q}$ and $a_n\leq x\leq b_n$ for every $n$. Since both endpoint sequences converge to $\sqrt2$, the squeeze theorem applied to the constant sequence with value $x$ gives $x=\sqrt2$, contradicting $x\in\mathbb{Q}$.[^60] Therefore

$$
\bigcap_{n=1}^{\infty}I_n=\varnothing.
$$

What fails is the *completeness of $\mathbb{Q}$*. The corresponding closed intervals in $\mathbb{R}$ have intersection $\{\sqrt2\}$, but this point is absent from $\mathbb{Q}$. ◻

::::::

:::notes{id="footnotes-59"}

[^60]: *Squeeze theorem.* If $u_n\leq v_n\leq w_n$ and $u_n,w_n\to\ell$, then $v_n\to\ell$.

:::
