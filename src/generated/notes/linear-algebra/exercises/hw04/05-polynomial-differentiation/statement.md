---
key: "hw04:polynomial-differentiation"
source: "problems/hw04/05-polynomial-differentiation/problem"
title: "Exercise"
number: "4.4.2"
assignment: "hw04"
question: 5
statement-page: "linear-algebra-i/kernel-image-and-rank"
solution-page: "appendices/exercise-solutions"
---

Let $\mathcal P_3(\mathbb{R})$ be the vector space of real polynomials of degree at most $3$, including the zero polynomial, and define $\mathcal P_2(\mathbb{R})$ similarly. Consider the differentiation map

$$
D:\mathcal P_3(\mathbb{R})\to\mathcal P_2(\mathbb{R}),\qquad D(p)=p'.
$$

:::list

1.  **(a)** Find $\ker D$, $\operatorname{im}D$, the nullity of $D$, and the rank of $D$.

2.  **(b)** Determine whether $D$ is injective and whether it is surjective.

3.  **(c)** Find the matrix of $D$ with respect to

    $$
    E=\begin{bmatrix}1&x&x^2&x^3\end{bmatrix},
            \qquad F=\begin{bmatrix}1&x&x^2\end{bmatrix}.
    $$

4.  **(d)** Find a new ordered basis $E'$ of $\mathcal P_3(\mathbb{R})$, beginning with a basis of $\ker D$, for which the matrix relative to $E'$ and $F$ is

    $$
    \begin{bmatrix}
              0&1&0&0\\
              0&0&1&0\\
              0&0&0&1
            \end{bmatrix}.
    $$

:::
