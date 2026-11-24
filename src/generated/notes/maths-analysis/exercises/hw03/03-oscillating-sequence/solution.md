::::::div{class="proof"}

*Solution.* The sine term repeats every three indices. Let $h=\sqrt{3}/2$. Separating the indices according to their remainder upon division by three gives

$$
\begin{aligned}
    a_{3k}&=\frac{1}{3k}, && k\geq1, \\
    a_{3k+1}&=h+\frac{1}{3k+1}, && k\geq0, \\
    a_{3k+2}&=-h+\frac{1}{3k+2}, && k\geq0.
  
\end{aligned}
$$

The reciprocals tend to zero, so these three subsequences converge to $0$, $h$, and $-h$, respectively. Each of these numbers is therefore a limit point. [Figure C.11](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw03:oscillating-sequence) shows the three groups of terms approaching their limits.

:::::div{class="margin-figure"}

::::figure{id="fig:hw03:oscillating-sequence"}

[![The first eighteen terms. The dashed lines mark \\pm\\sqrt\{3\}/2; the horizontal axis marks the third limit, 0.](/notes/maths-analysis/figures/oscillating-sequence.svg){.tikz-diagram}](/notes/maths-analysis/figures/oscillating-sequence.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.11. The first eighteen terms. The dashed lines mark $\pm\sqrt{3}/2$; the horizontal axis marks the third limit, $0$.

:::

::::

:::::

To show that there are no other limit points, suppose a subsequence converges to $\ell$. Among its infinitely many indices, at least one remainder occurs infinitely often. Keeping only those indices gives a further subsequence of one of the three sequences above. It still converges to $\ell$, so uniqueness of limits forces $\ell$ to be $0$, $h$, or $-h$. Thus the set of all limit points is

$$
\left\{-\frac{\sqrt{3}}{2},0,\frac{\sqrt{3}}{2}\right\}.
$$

To find the lower limit, fix a tail beginning at $N\geq1$. Every term in this tail is greater than $-h$, while terms with indices $3k+2$ occur arbitrarily far out and approach $-h$. Therefore

$$
\inf\{a_n\mid n\geq N\}=-h.
$$

For the upper limit, every term in this tail satisfies $a_n\leq h+1/N$. The tail also contains terms with indices $3k+1$, all of which exceed $h$. Hence

$$
h\leq\sup\{a_n\mid n\geq N\}\leq h+\frac{1}{N}.
$$

Taking the limits of these tail bounds gives

$$
\liminf_{n\to\infty}a_n=-\frac{\sqrt{3}}{2},\qquad
    \limsup_{n\to\infty}a_n=\frac{\sqrt{3}}{2}.
$$

 ◻

::::::
