::::::div{class="proof"}

*Solution.* For part (a), the initial values and the recurrence show by induction that $F_n\geq0$ for every $n\geq0$, and $F_n\geq1$ for every $n\geq1$. For $n\geq1$, the recurrence gives

$$
F_{n+1}-F_n=F_{n-1}\geq0.
$$

Together with $F_1\geq F_0$, this proves that the sequence is nondecreasing. It is strictly increasing from $F_2$ onward, since $F_{n-1}>0$ when $n\geq2$. The only repeated adjacent values are $F_1=F_2=1$.

For part (b), suppose $(F_n)$ is bounded above. Since it is nondecreasing, the monotone convergence theorem gives $F_n\to L$ as $n\to\infty$. The shifted sequences $F_{n-1}$ and $F_{n-2}$ also tend to $L$, so the recurrence and the limit laws give

$$
L=\lim_{n\to\infty}F_n
      =\lim_{n\to\infty}F_{n-1}+\lim_{n\to\infty}F_{n-2}
      =L+L.
$$

Subtracting $L$ gives $L=0$.

But $F_n\geq1$ for every $n\geq1$, so taking limits gives $L\geq1$. This contradicts $L=0$. Therefore the sequence is unbounded above.

For part (c), the ratios are well defined because their denominators are positive. We have $r_2=1$. For $n\geq3$, substitute the recurrence into the numerator and split the fraction to obtain

$$
\begin{aligned}
    r_n&=\frac{F_n}{F_{n-1}}\\
       &=\frac{F_{n-1}+F_{n-2}}{F_{n-1}}\\
       &=\frac{F_{n-1}}{F_{n-1}}+\frac{F_{n-2}}{F_{n-1}}\\
       &=1+\frac{F_{n-2}}{F_{n-1}}.
  
\end{aligned}
$$

By part (a), we have $0<F_{n-2}\leq F_{n-1}$. Dividing by the positive number $F_{n-1}$ gives

$$
0<\frac{F_{n-2}}{F_{n-1}}\leq1.
$$

Adding $1$ now gives $1<r_n\leq2$. Including $r_2$, we conclude that

$$
\forall n\geq2,\quad 1\leq r_n\leq2.
$$

Thus the ratio sequence is bounded.

For part (d), assume that $r_n\to L$. The bounds above give $1\leq L\leq2$, so $L$ is nonzero.

:::::div{class="margin-figure"}

::::figure{id="fig:hw03:golden-ratio-fixed-point"}

[![The positive intersection satisfies \\varphi=1+1/\\varphi. Dotted guides locate both coordinates at \\varphi\\approx1.618. The axes use equal units.](/notes/maths-analysis/figures/golden-ratio-fixed-point.svg){.tikz-diagram}](/notes/maths-analysis/figures/golden-ratio-fixed-point.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.19. The positive intersection satisfies $\varphi=1+1/\varphi$. Dotted guides locate both coordinates at $\varphi\approx1.618$. The axes use equal units.

:::

::::

:::::

To express $r_n$ in terms of $r_{n-1}$, recall from part (c) that, for $n\geq3$,

$$
r_n=\frac{F_n}{F_{n-1}}=1+\frac{F_{n-2}}{F_{n-1}}.
$$

The preceding ratio is $r_{n-1}=F_{n-1}/F_{n-2}$. Since both Fibonacci terms are positive, we can take its reciprocal to obtain

$$
\frac{1}{r_{n-1}}
      =\frac{1}{F_{n-1}/F_{n-2}}
      =\frac{F_{n-2}}{F_{n-1}}.
$$

Substituting this into the expression for $r_n$ gives the recurrence

$$
r_n=1+\frac{1}{r_{n-1}},\qquad n\geq3.
$$

The shifted sequence $r_{n-1}$ also tends to $L$. Since $L\neq0$, the limit laws give

$$
L=1+\frac{1}{L}.
$$

Geometrically, $(L,L)$ lies on both $y=x$ and $y=1+1/x$, as shown in [Figure C.19](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw03:golden-ratio-fixed-point). Multiplying by $L$ and bringing all terms to one side gives

$$
L^2=L+1,\qquad L^2-L-1=0.
$$

The two roots are $(1+\sqrt{5})/2$ and $(1-\sqrt{5})/2$. The second is negative and cannot satisfy $L\geq1$. Therefore the assumed limit is the golden ratio

$$
L=\frac{1+\sqrt{5}}{2}=\varphi\approx1.6180339887.
$$

 ◻

::::::

The identity $\varphi-1=1/\varphi$ also has a geometric interpretation.

:::::div{class="margin-figure"}

::::figure{id="fig:hw03:golden-rectangle-spiral"}

[![A golden rectangle subdivides into squares with side lengths 1,\\varphi^\{-1\},\\varphi^\{-2\},\\ldots. The golden spiral passes through successive corners. Each quarter-turn inward shrinks the distance from its centre by 1/\\varphi. The subdivision continues indefinitely.](/notes/maths-analysis/figures/golden-rectangle-spiral.svg){.tikz-diagram}](/notes/maths-analysis/figures/golden-rectangle-spiral.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.20. A golden rectangle subdivides into squares with side lengths $1,\varphi^{-1},\varphi^{-2},\ldots$. The golden spiral passes through successive corners. Each quarter-turn inward shrinks the distance from its centre by $1/\varphi$. The subdivision continues indefinitely.

:::

::::

:::::

A rectangle with side lengths $1$ and $\varphi$ leaves a smaller, rotated copy of itself when a unit square is removed. Repeating this step gives the squares in [Figure C.20](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw03:golden-rectangle-spiral). The golden spiral winds through their corners, shrinking its distance from the centre by $1/\varphi$ with each quarter-turn ([Duan 2019](/notes/maths-analysis/references/#ref-Duan2019GoldenSpirals)).
