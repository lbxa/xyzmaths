::::::div{class="proof"}

*Solution.* *Part (i).* Suppose $R_1>1$. Choose $L$ such that

$$
1<L<R_1.
$$

By the definition of the lower limit, there is $N\in\mathbb{N}$ such that

$$
\forall n\ge N\quad
    \frac{a_{n+1}}{a_n}>L>1.
$$

Since $a_n>0$, we obtain

$$
a_{n+1}>La_n>a_n.
$$

In other words, $(a_n)$ is strictly increasing from index $N$ onwards. Consequently,

$$
\forall n\ge N\quad a_n\ge a_N>0.
$$

Thus the terms $a_n$ cannot converge to zero. This violates the necessary condition for a convergent series, which requires $a_n\to0$.

To see the contradiction directly, take $\varepsilon=a_N/2$. If $a_n\to0$, there would be $N'\in\mathbb{N}$ such that

$$
\forall n\ge N'\quad
    |a_n-0|<\frac{a_N}{2}.
$$

This would give $a_n<a_N/2$. For $n\ge\max\{N,N'\}$, this contradicts $a_n\ge a_N$. Therefore the series does not converge. [Figure C.21](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw04:divergence-convergence-band) recalls the tail condition used in this contradiction.

:::::div{class="margin-figure"}

::::figure{id="fig:hw04:divergence-convergence-band"}

[![A convergence-band recall. Beyond N, every term must lie strictly between L-\\varepsilon and L+\\varepsilon. This example has limit L=1; the proof above tests convergence to 0.](/notes/maths-analysis/figures/convergence-band.svg){.tikz-diagram}](/notes/maths-analysis/figures/convergence-band.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.21. A convergence-band recall. Beyond $N$, every term must lie strictly between $L-\varepsilon$ and $L+\varepsilon$. This example has limit $L=1$; the proof above tests convergence to $0$.

:::

::::

:::::

*Part (ii).* Suppose $R_2>1$. Choose $L$ such that

$$
1<L<R_2.
$$

Again, the definition of the lower limit gives $N\in\mathbb{N}$ such that

$$
\forall n\ge N\quad
    (a_n)^{1/n}\ge L.
$$

Raising both sides to the positive integer power $n$ gives $a_n\ge L^n$. Since $L>1$, we have $L^n\to+\infty$. Hence $a_n\to+\infty$, so $a_n$ cannot converge to zero. The necessary term condition therefore shows that $\sum_{n=1}^{\infty}a_n$ diverges. ◻

::::::
