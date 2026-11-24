---
key: "hw03:kernel-image-and-adapted-bases"
source: "problems/hw03/06-kernel-image-and-adapted-bases/problem"
title: "Exercise"
number: "4.3.18"
assignment: "hw03"
question: 6
statement-page: "linear-algebra-i/kernel-image-and-rank"
solution-page: "appendices/exercise-solutions"
---

Let $V,W$ be finite-dimensional vector spaces, with $\dim V=m$ and $\dim W=n$, and let $L:V\to W$ be a linear map. Consider the sets

$$
K=\{v\in V:L(v)=0\}\subset V
$$

and

$$
L(V)=\{L(v):v\in V\}\subset W.
$$

Set $k=\dim K$. Recall that the empty set is a basis of the zero subspace.

:::list

1.  **(a)** Prove that $K$ is a subspace of $V$.

2.  **(b)** Prove that $L(V)$ is a subspace of $W$.

3.  **(c)** Prove that there exists a row matrix basis $E=\begin{bmatrix}e_1&\cdots&e_m\end{bmatrix}$ of $V$ such that

    $$
    \begin{aligned}
              \begin{bmatrix}L(e_1)&\cdots&L(e_{m-k})\end{bmatrix}
                &\text{ is a basis of }L(V),\text{ and}\\
              \begin{bmatrix}e_{m-k+1}&\cdots&e_m\end{bmatrix}
                &\text{ is a basis of }K.
            \end{aligned}
    $$

4.  **(d)** Prove that

    $$
    \dim(K)+\dim(L(V))=\dim(V).
    $$

    This is known as the rank-nullity theorem.

5.  **(e)** Prove that there exist row matrix bases $E$ of $V$ and $F$ of $W$ such that $L(E)=FM$, where $r=m-k$ and

    $$
    M=\left[
              \begin{array}{c|c}
                I_{r\times r}&0_{r\times(m-r)}\\
                \hline
                0_{(n-r)\times r}&0_{(n-r)\times(m-r)}
              \end{array}
            \right].
    $$

:::
