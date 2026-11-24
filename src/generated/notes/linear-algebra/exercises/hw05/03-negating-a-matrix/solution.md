:::div{class="proof"}

*Solution.* Let $A$ be a real $n\times n$ matrix with columns $c_1,\ldots,c_n$, and let $D:(\mathbb{R}^n)^n\to\mathbb{R}$ be the normalized determinant function. The columns of $-A$ are $-c_1,\ldots,-c_n$. By multilinearity, each of the $n$ negated columns contributes a factor of $-1$, so

$$
\begin{aligned}
  \det(-A)&=D(-c_1,\ldots,-c_n)\\
    &=(-1)^nD(c_1,\ldots,c_n)\\
    &=(-1)^n\det A.
\end{aligned}
$$

Therefore,

$$
\det(-A)=
  \begin{cases}
    \det A & \text{if \(n\) is even},\\
    -\det A & \text{if \(n\) is odd}.
  \end{cases}
$$

 ◻

:::
