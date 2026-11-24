::::::div{class="proof"}

*Solution.* Part (i). Since $f'$ is bounded, $|f'(x)|\le M$ for some $M\ge0$ and every $x\in\mathbb{R}$. The function $f$ is differentiable over $\mathbb{R}$, so it is continuous there. Thus, we apply the mean value theorem over the interval $[y,x]$, where $x,y\in\mathbb{R}$ and $x>y$, and choose a $c\in(y,x)$ such that

$$
f'(c)=\frac{f(x)-f(y)}{x-y}.
$$

Choose $L=M+1>0$ to satisfy $L>0$. Since $|f'(c)|\le M<L$, we obtain

$$
\begin{aligned}
      |f'(c)|=\left|\frac{f(x)-f(y)}{x-y}\right|
        &\implies \left|\frac{f(x)-f(y)}{x-y}\right|\le L\\
        &\implies |f(x)-f(y)|\le L|x-y|.
    \end{aligned}
$$

If $x<y$, interchange the two inputs. If $x=y$, both sides are zero. Thus the inequality holds for every $x,y\in\mathbb{R}$.

Part (ii). Take any $x_0\in\mathbb{R}$ and define $x_{n+1}=f(x_n)$ for $n\ge0$. Consider the following, where $x_0,\ldots,x_3\in\mathbb{R}$,

$$
\begin{aligned}
      x_3&=f(x_2),\\
      x_2&=f(x_1),\\
      x_1&=f(x_0).
    \end{aligned}
$$

Assuming a Lipschitz constant satisfying $0<L<1$ exists, we can apply the inequality from part (i). For this part, $L$ denotes the constant in the contraction hypothesis.

$$
\begin{aligned}
      |f(x_2)-f(x_1)|\le L|x_2-x_1|
        &\implies |x_3-x_2|\le L|x_2-x_1|,\\
      |f(x_1)-f(x_0)|\le L|x_1-x_0|
        &\implies |x_2-x_1|\le L|x_1-x_0|\\
        &\implies |x_3-x_2|\le L^2|x_1-x_0|.
    \end{aligned}
$$

Repeated application of the contraction inequality yields

$$
|x_{n+1}-x_n|\le L^n|x_1-x_0|,
    \qquad n\ge0.
$$

Suppose $0<L<1$. Then

$$
|x_1-x_0|\ge |x_2-x_1|\ge |x_3-x_2|,
$$

which implies that each successive step is no larger than the previous one. [Figure C.30](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw07:contractive-steps) illustrates shrinking steps that alternate around a fixed point.

:::::div{class="margin-figure"}

::::figure{id="fig:hw07:contractive-steps"}

[![ For f(t)=1-t/2 and x\_0=0, the filled points are x\_0,x\_1,x\_2,x\_3. The open point is the fixed point x^\*=2/3. From top to bottom, the arrows show successive steps of lengths 1, 1/2, and 1/4, with alternating directions.](/notes/maths-analysis/figures/contractive-steps.svg){.tikz-diagram}](/notes/maths-analysis/figures/contractive-steps.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.30. For $f(t)=1-t/2$ and $x_0=0$, the filled points are $x_0,x_1,x_2,x_3$. The open point is the fixed point $x^*=2/3$. From top to bottom, the arrows show successive steps of lengths $1$, $1/2$, and $1/4$, with alternating directions.

:::

::::

:::::

It follows that the total distance from start to finish is less than or equal to the sum of all steps,

$$
|x_3-x_0|\le |x_3-x_2|+\cdots+|x_1-x_0|.
$$

Generalizing this for arbitrary $m>n$ gives the following calculation. For tails shorter than four steps, retain only the increments with indices $n\le k<m$ in the expanded list.

$$
\begin{aligned}
      |x_m-x_n|
        &\le |x_m-x_{m-1}|+\cdots+|x_{n+3}-x_{n+2}|\\
        &\qquad+|x_{n+2}-x_{n+1}|+|x_{n+1}-x_n|\\
        &=\sum_{k=n}^{m-1}|x_{k+1}-x_k|\\
        &\le\sum_{k=n}^{m-1}L^k|x_1-x_0|\\
        &=|x_1-x_0|\sum_{k=n}^{m-1}L^k\\
        &=|x_1-x_0|\frac{L^n-L^m}{1-L}\\
        &\le |x_1-x_0|\frac{L^n}{1-L}
          \qquad(L^m>0)\\
        &=\frac{|x_1-x_0|}{1-L}L^n.
    \end{aligned}
$$

The final bound is independent of $m$. Taking the limit as $n\to\infty$, we have

$$
\lim_{n\to\infty}\frac{|x_1-x_0|}{1-L}L^n=0,
    \qquad 0<L<1.
$$

Hence, for every $\epsilon>0$, there exists $N\in\mathbb{N}$ such that

$$
\frac{|x_1-x_0|}{1-L}L^n<\epsilon
    \qquad\forall n\ge N.
$$

Consequently, for every $m>n\ge N$,

$$
|x_m-x_n|<\epsilon,
$$

establishing $(x_n)$ as a Cauchy sequence over $\mathbb{R}$. The same bound for $m<n$ follows by interchanging the indices, and $m=n$ gives zero. By the Cauchy completeness theorem in $\mathbb{R}$, there exists $x^*\in\mathbb{R}$ such that $x_n\to x^*$. Finally, since $f$ is continuous and $x_n=f(x_{n-1})$, taking $n\to\infty$ gives

$$
\begin{aligned}
      x^*&=\lim_{n\to\infty}x_n\\
        &=\lim_{n\to\infty}f(x_{n-1})\\
        &=f\left(\lim_{n\to\infty}x_{n-1}\right)\\
        &=f(x^*).
    \end{aligned}
$$

Therefore, $x^*$ is a fixed point of $f$.

For part (iii), assume there are two distinct fixed points $x^*=f(x^*)$ and $y^*=f(y^*)$. Applying the contraction inequality gives

$$
\begin{aligned}
      |f(x^*)-f(y^*)|
        &\le L|x^*-y^*|,\qquad 0<L<1\\
      \implies |x^*-y^*|
        &\le L|x^*-y^*|.
    \end{aligned}
$$

Since $x^*\ne y^*$, we have $|x^*-y^*|>0$, so we can divide both sides by $|x^*-y^*|$ to give $L\ge1$, which contradicts $L<1$. Therefore, two distinct fixed points cannot exist and the fixed point $x^*$ is unique. ◻

::::::
