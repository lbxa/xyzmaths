::::::div{class="proof"}

*Solution.* Fix an odd integer $n\geq3$ and let $p(x)=x^n$. We first show that $p$ is strictly increasing on the whole real line. If $0\leq x<y$, the strict increase of nonnegative integer powers gives $x^n<y^n$. If $x<y\leq0$, then $0\leq-y<-x$, so

$$
(-y)^n<(-x)^n.
$$

Since $n$ is odd, this becomes $-y^n<-x^n$, or $x^n<y^n$. Finally, if $x<0<y$, then $x^n<0<y^n$. These cases cover every pair $x<y$, so $p$ is strictly increasing and therefore injective.

To prove surjectivity, take any $t\in\mathbb{R}$. If $t\geq0$, the existence of nonnegative roots supplies an $x\geq0$ with $x^n=t$. If $t<0$, let $u=(-t)^{1/n}>0$ and take $x=-u$. Since $n$ is odd,

$$
x^n=(-u)^n=-u^n=-(-t)=t.
$$

Thus every real number has an $n$th root. Injectivity shows that this root is unique, so the inverse function

$$
g(t)=t^{1/n}
$$

is well defined on all of $\mathbb{R}$.

To show that $g$ is strictly increasing, take $s<t$. If $g(s)\geq g(t)$, the increase of $p$ would give

$$
s=p(g(s))\geq p(g(t))=t,
$$

a contradiction. Hence $g(s)<g(t)$, which also proves injectivity. For any $x\in\mathbb{R}$, we have $g(x^n)=x$, so $g$ is surjective as well. Therefore the real $n$th root function is a strictly increasing bijection from $\mathbb{R}$ to itself. [Figure C.16](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw03:odd-root-inverse) illustrates this inverse relationship for $n=3$.

:::::div{class="margin-figure"}

::::figure{id="fig:hw03:odd-root-inverse"}

[![The graphs of y=x^3 and y=x^\{1/3\} are reflections of one another across y=x. Both are strictly increasing.](/notes/maths-analysis/figures/odd-root-inverse.svg){.tikz-diagram}](/notes/maths-analysis/figures/odd-root-inverse.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.16. The graphs of $y=x^3$ and $y=x^{1/3}$ are reflections of one another across $y=x$. Both are strictly increasing.

:::

::::

:::::

 ◻

::::::
