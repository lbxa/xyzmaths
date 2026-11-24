::::::div{class="proof"}

*Solution.* The identity $f(x)=x$ maps $(0,1)$ to itself, but it misses the endpoints of $[0,1]$, as shown in [Figure C.5](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw01:identity-map). We can make room for them by moving a countable sequence of points.

First assign

$$
f\left(\frac12\right)=0,
  \qquad f\left(\frac13\right)=1.
$$

:::::div{class="margin-figure"}

::::figure{id="fig:hw01:identity-map"}

[![The identity on (0,1) misses the target values 0 and 1. Both endpoints of the graph are excluded.](/notes/maths-analysis/figures/identity-map.svg){.tikz-diagram}](/notes/maths-analysis/figures/identity-map.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.5. The identity on $(0,1)$ misses the target values $0$ and $1$. Both endpoints of the graph are excluded.

:::

::::

:::::

The values $1/2$ and $1/3$ must now be supplied by other inputs. We use $1/4$ and $1/5$ for these values, and then continue shifting the reciprocals to fill the resulting gaps. This gives

$$
f\left(\frac14\right)=\frac12,\quad
  f\left(\frac15\right)=\frac13,\quad
  f\left(\frac16\right)=\frac14,\quad\ldots
$$

[Figure C.6](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw01:reciprocal-shift) illustrates this shift. We leave all other points fixed. Define a map $f$ from $(0,1)$ to $[0,1]$ by

$$
f(x)=
  \begin{cases}
    0, & x=\frac12,\\[2pt]
    1, & x=\frac13,\\[2pt]
    \dfrac1{n-2}, & x=\frac1n,\quad n\in\mathbb{N},\ n\ge4,\\[4pt]
    x, & \text{otherwise}.
  \end{cases}
$$

::::figure{id="fig:hw01:reciprocal-shift"}

[![The reciprocal sequence is shifted to accommodate both endpoints. Every point outside this sequence remains fixed.](/notes/maths-analysis/figures/reciprocal-shift.svg){.tikz-diagram}](/notes/maths-analysis/figures/reciprocal-shift.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.6. The reciprocal sequence is shifted to accommodate both endpoints. Every point outside this sequence remains fixed.

:::

::::

To check bijectivity, put

$$
S=\left\{\frac1n\mid n\in\mathbb{N},\ n\ge2\right\}.
$$

The cases in the definition are disjoint and cover $(0,1)$. Every output lies in $[0,1]$, so the function is well-defined.

Among the inputs in $S$, only $1/2$ maps to $0$, and only $1/3$ maps to $1$. For each integer $m\ge2$, solving $1/(n-2)=1/m$ gives the unique input $1/(m+2)$. Thus $f$ maps $S$ bijectively onto $S\cup\{0,1\}$.

On $(0,1)\setminus S$, the map is the identity, with image $(0,1)\setminus S$. This image is disjoint from $S\cup\{0,1\}$, so no fixed point can give a second preimage for a value already supplied by the reciprocal sequence. Together the two images cover $[0,1]$. Every target value therefore has exactly one preimage, proving that $f$ is a bijection. ◻

::::::
