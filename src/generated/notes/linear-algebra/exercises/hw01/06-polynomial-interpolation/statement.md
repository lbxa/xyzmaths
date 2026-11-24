---
key: "hw01:polynomial-interpolation"
source: "problems/hw01/06-polynomial-interpolation/problem"
title: "A polynomial determined by three values"
number: "1.2.16"
assignment: "hw01"
question: 6
statement-page: "linear-algebra-i/vector-spaces-and-bases"
solution-page: "appendices/exercise-solutions"
---

Let $\mathbb F$ denote $\mathbb{R}$ or $\mathbb{C}$, and work in $\mathcal P_2(\mathbb F)$, the polynomials of degree at most two with coefficients in $\mathbb F$, including the zero polynomial.

:::list

1.  **(a)** Construct $q_{-1},q_0,q_1$ such that, for $j,k\in\{-1,0,1\}$,

    $$
    q_j(k)=
            \begin{cases}
              1,&j=k,\\
              0,&j\ne k.
            \end{cases}
    $$

2.  **(b)** Prove that these polynomials form a basis and that every $p\in\mathcal P_2(\mathbb F)$ satisfies

    $$
    p=p(-1)q_{-1}+p(0)q_0+p(1)q_1.
    $$

3.  **(c)** Find the unique polynomial $p\in\mathcal P_2(\mathbb F)$ for which $p(-1)=2$, $p(0)=-1$, and $p(1)=4$.

:::
