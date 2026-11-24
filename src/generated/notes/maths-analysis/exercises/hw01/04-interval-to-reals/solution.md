:::::div{class="proof"}

*Solution.* A map from $A$ to $B$ is a bijection if it is both one-to-one and onto. This means that every element of $B$ is the image of exactly one element of $A$. [Figure C.3](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw01:bijections) contrasts bijections with a map that fails both conditions.

::::figure{id="fig:hw01:bijections"}

[![The first two maps are bijections. The third map is neither one-to-one nor onto. Crossing arrows do not prevent a map from being bijective.](/notes/maths-analysis/figures/bijections.svg){.tikz-diagram}](/notes/maths-analysis/figures/bijections.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.3. The first two maps are bijections. The third map is neither one-to-one nor onto. Crossing arrows do not prevent a map from being bijective.

:::

::::

The tangent function is a bijection from $(-\pi/2,\pi/2)$ onto $\mathbb{R}$. To use it on $(0,1)$, we first multiply the input by $\pi$ and then subtract $\pi/2$. These steps give the composition

$$
(0,1)\xrightarrow{\,\times\pi\,}(0,\pi)
    \xrightarrow{\,-\pi/2\,}
    \left(-\frac\pi2,\frac\pi2\right)
    \xrightarrow{\,\tan\,}\mathbb{R}.
$$

We can therefore define

$$
f(x)=\tan\left(\pi x-\frac\pi2\right),
    \qquad 0<x<1.
$$

For $0<x<1$, the angle $\pi x-\pi/2$ lies strictly between $-\pi/2$ and $\pi/2$, so $f(x)$ is defined and real. We verify bijectivity by giving its inverse. For $y\in\mathbb{R}$, put

$$
g(y)=\frac12+\frac{\arctan y}{\pi}.
$$

Here $\arctan y$ is the unique angle in $(-\pi/2,\pi/2)$ whose tangent is $y$. Thus $0<g(y)<1$, and

$$
f(g(y))=\tan(\arctan y)=y.
$$

This proves that $f$ is onto. Conversely, for $x\in(0,1)$, the angle lies in the principal interval, so

$$
g(f(x))=\frac12+
    \frac{\arctan(\tan(\pi x-\pi/2))}{\pi}=x.
$$

If $f(x_1)=f(x_2)$, applying $g$ gives $x_1=x_2$. Therefore $f$ is also one-to-one and hence is a bijection.

[Figure C.4](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw01:tangent-overview) shows the central branch of $y=\tan t$ in blue and the transformed graph alongside it. The horizontal change $x=t/\pi+1/2$ compresses that branch by a factor of $1/\pi$ and shifts it to the right by $1/2$. Its domain becomes $(0,1)$, while its range remains all of $\mathbb{R}$.

::::figure{id="fig:hw01:tangent-overview"}

[![The left panel highlights the central tangent branch on (-\\pi/2,\\pi/2). The right panel shows this branch after the change of input. The vertical asymptotes now occur at x=0 and x=1. The horizontal axes use different scales.](/notes/maths-analysis/figures/tangent-overview.svg){.tikz-diagram}](/notes/maths-analysis/figures/tangent-overview.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.4. The left panel highlights the central tangent branch on $(-\pi/2,\pi/2)$. The right panel shows this branch after the change of input. The vertical asymptotes now occur at $x=0$ and $x=1$. The horizontal axes use different scales.

:::

::::

 ◻

:::::
