---
key: "hw03:polynomial-differentiation-powers"
source: "problems/hw03/01-polynomial-differentiation-powers/problem"
title: "Exercise"
number: "4.4.1"
assignment: "hw03"
question: 1
statement-page: "linear-algebra-i/kernel-image-and-rank"
solution-page: "appendices/exercise-solutions"
---

Let $\mathcal P_n(\mathbb{R})$ be the vector space of all polynomials of degree at most $n$ in the variable $x$ with real coefficients, including the zero polynomial. Take $n=3$. A basis of $\mathcal P_3(\mathbb{R})$ is

$$
E=\begin{bmatrix}1&x&x^2&x^3\end{bmatrix}.
$$

:::list

1.  **(a)** Recall that differentiation is a linear map,

    $$
    \begin{aligned}
              D:\mathcal P_3(\mathbb{R})&\to\mathcal P_3(\mathbb{R})\\
              f&\mapsto f'
            \end{aligned}
    $$

    Find the matrix $M$ such that

    $$
    D(E)=EM.
    $$

2.  **(b)** Find the matrix $N$ such that

    $$
    D^2(E)=EN,
    $$

    where $D^2=D\circ D:\mathcal P_3(\mathbb{R})\to\mathcal P_3(\mathbb{R})$.

:::
