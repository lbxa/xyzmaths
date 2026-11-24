::::::div{class="proof"}

*Solution.* *(a)* Since $a|x|\ge0$ for every $x\in\mathbb{R}$, the given bound implies

$$
f(x)\ge a|x|-b\ge-b.
$$

Thus the range $f(\mathbb{R})$ is bounded below. It is nonempty because it contains $f(0)$. By completeness of $\mathbb{R}$, its infimum exists as a real number. Write

$$
m=\inf f(\mathbb{R}),\qquad -b\le m\le f(0).
$$

*(b)* We follow the hint by choosing inputs whose outputs approach $m$. By the defining property of the infimum, for every $n\in\mathbb{N}$ there is an $x_n\in\mathbb{R}$ such that

$$
m\le f(x_n)<m+\frac1n.
$$

Indeed, if no such point existed, $m+1/n$ would be a lower bound for $f(\mathbb{R})$ larger than $m$. These inequalities give $f(x_n)\to m$.

We next show that the inputs $x_n$ stay in a bounded interval. Combining the coercive bound with the choice of $x_n$ gives

$$
\begin{aligned}
    a|x_n|-b&\le f(x_n)<m+\frac1n\le m+1,\\
    a|x_n|&<m+b+1,\\
    |x_n|&<\frac{m+b+1}{a}.
  
\end{aligned}
$$

Since $m\ge-b$ and $a>0$, the number $R=(m+b+1)/a$ is positive and finite. Thus $(x_n)$ is contained in $[-R,R]$. The coercive bound prevents inputs with nearly minimal outputs from escaping to infinity, as illustrated in [Figure C.24](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw05:coercive-minimum).

:::::div{class="margin-figure"}

::::figure{id="fig:hw05:coercive-minimum"}

[![ An example with f(x)=1+x^2 and the lower bound \|x\|-1. Here m=1. If f(x)\<m+1=2, the lower bound forces \|x\|\<3. The indicated points approach the minimum inside this bounded interval.](/notes/maths-analysis/figures/coercive-minimum.svg){.tikz-diagram}](/notes/maths-analysis/figures/coercive-minimum.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.24. An example with $f(x)=1+x^2$ and the lower bound $|x|-1$. Here $m=1$. If $f(x)<m+1=2$, the lower bound forces $|x|<3$. The indicated points approach the minimum inside this bounded interval.

:::

::::

:::::

By the Bolzano–Weierstrass theorem, there is a subsequence $(x_{n_k})$ converging to some $x_0\in\mathbb{R}$. Continuity of $f$ at $x_0$ gives

$$
f(x_{n_k})\longrightarrow f(x_0).
$$

But the same subsequence satisfies

$$
m\le f(x_{n_k})<m+\frac1{n_k},
$$

so $f(x_{n_k})\to m$ as $n_k\to\infty$. By uniqueness of limits, $f(x_0)=m=\inf f(\mathbb{R})$. Hence $f$ attains its global minimum. ◻

::::::
