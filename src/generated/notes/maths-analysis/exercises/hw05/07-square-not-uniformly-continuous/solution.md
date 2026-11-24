::::::div{class="proof"}

*Solution.* To disprove uniform continuity, we need one fixed output tolerance that no single input tolerance can guarantee over all of $\mathbb{R}$. Choose $\varepsilon_0=1$.

Let $\delta>0$ be arbitrary. By the Archimedean property, choose $n\in\mathbb{N}$ with $n>1/\delta$, and set

$$
x_n=n,\qquad y_n=n+\frac1n.
$$

These inputs are less than $\delta$ apart, since

$$
|y_n-x_n|=\frac1n<\delta.
$$

However, their outputs satisfy

$$
\begin{aligned}
    |f(y_n)-f(x_n)|
      &=\left(n+\frac1n\right)^2-n^2\\
      &=n^2+2+\frac1{n^2}-n^2\\
      &=2+\frac1{n^2}>1=\varepsilon_0.
  
\end{aligned}
$$

Thus every $\delta>0$ fails for the same $\varepsilon_0=1$, so $f$ is not uniformly continuous on $\mathbb{R}$.

What goes wrong is visible in the factorisation

$$
|y^2-x^2|=|y-x||y+x|.
$$

Even when $|y-x|$ is small, the factor $|y+x|$ can be arbitrarily large. In our construction the inputs get closer together as they move to the right, while the output gap stays above $2$. [Figure C.28](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw05:square-output-gap) shows one pair from this sequence.

:::::div{class="margin-figure"}

::::figure{id="fig:hw05:square-output-gap"}

[![ A local view of y=x^2 for the pair x\_n=n, y\_n=n+1/n when n=3. A horizontal gap of 1/n produces a vertical gap of 2+1/n^2. The two axes use different scales.](/notes/maths-analysis/figures/square-output-gap.svg){.tikz-diagram}](/notes/maths-analysis/figures/square-output-gap.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.28. A local view of $y=x^2$ for the pair $x_n=n$, $y_n=n+1/n$ when $n=3$. A horizontal gap of $1/n$ produces a vertical gap of $2+1/n^2$. The two axes use different scales.

:::

::::

:::::

 ◻

::::::
