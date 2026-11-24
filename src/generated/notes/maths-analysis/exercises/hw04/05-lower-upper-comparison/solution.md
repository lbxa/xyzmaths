:::div{class="proof"}

*Solution.* Recall the tail infima and suprema of the ratios.

$$
\alpha_n=\inf\left\{\frac{a_j}{b_j}\mid j\ge n\right\},
    \qquad
    \beta_n=\sup\left\{\frac{a_j}{b_j}\mid j\ge n\right\}.
$$

$$
\begin{aligned}
    r&=\sup_n\alpha_n=\lim_{n\to\infty}\alpha_n,\\
    R&=\inf_n\beta_n=\lim_{n\to\infty}\beta_n.
  
\end{aligned}
$$

We can think of $r$ and $R$ as long-term lower and upper bounds with the following precise meaning. A bound strictly below $r$ or strictly above $R$ holds on a sufficiently late tail.

*Part (i).* Since $r>0$, there is $c>0$ with $c<r$. Choose a finite such $c$, also when $r=+\infty$. Since $r=\sup_n\alpha_n$, some $N\in\mathbb{N}$ has $\alpha_N>c$. Thus

$$
\forall n\ge N\quad \frac{a_n}{b_n}\ge c.
$$

Since $b_n>0$, this gives $a_n\ge cb_n$ for every $n\ge N$.

Sum over this tail, where the comparison is known to hold. For $m\ge N$,

$$
\sum_{n=N}^{m}a_n\ge c\sum_{n=N}^{m}b_n.
$$

Removing the first $N-1$ terms does not change divergence.

Since $b_n>0$, its partial sums are increasing and tend to $+\infty$. Therefore the partial sums of $\sum a_n$ also tend to $+\infty$. Hence $\sum_{n=1}^{\infty}a_n$ diverges.

*Part (ii).* Since $R<\infty$, choose $M>R$. The ratios are nonnegative, so $R\ge0$ and $M>0$. Since $R=\inf_n\beta_n$, some $N\in\mathbb{N}$ has $\beta_N<M$. It follows that

$$
\forall n\ge N\quad \frac{a_n}{b_n}\le M,
    \qquad 0\le a_n\le Mb_n.
$$

We know that $\sum_{n=1}^{\infty}b_n=L$ is finite.

Put $A_m=\sum_{n=1}^{m}a_n$. For every $m\ge N$,

$$
\begin{aligned}
    A_m
      &=\sum_{n=1}^{N-1}a_n+\sum_{n=N}^{m}a_n\\
      &\le\sum_{n=1}^{N-1}a_n+M\sum_{n=N}^{m}b_n\\
      &\le\sum_{n=1}^{N-1}a_n+ML.
  
\end{aligned}
$$

The finite prefix is zero when $N=1$. Earlier partial sums are bounded by the same constant because the terms are nonnegative.

This establishes a finite upper bound. Since $a_n\ge0$, the partial sums are monotone nondecreasing. Therefore, by the monotone convergence theorem, $A_m$ tends to a finite limit. Hence $\sum_{n=1}^{\infty}a_n$ converges.

Direct comparison gives the same conclusion on the tail. Adding the finite prefix preserves convergence. ◻

:::
