---
key: "hw01:recursive-sequences"
source: "problems/hw01/07-recursive-sequences/problem"
title: "A vector space of recursively defined sequences"
number: "1.2.17"
assignment: "hw01"
question: 7
statement-page: "linear-algebra-i/vector-spaces-and-bases"
solution-page: "appendices/exercise-solutions"
---

Let $\mathbb F$ be $\mathbb{R}$ or $\mathbb{C}$. Let $V$ consist of the infinite sequences $(x_0,x_1,\ldots)$, where each $x_k\in\mathbb F$, that satisfy

$$
x_{n+2}=x_{n+1}+x_n\qquad(n\ge0).
$$

:::list

1.  **(a)** Prove that $V$ is a vector space where vector addition is

    $$
    (x_0,x_1,\ldots)+(y_0,y_1,\ldots)
              =(x_0+y_0,x_1+y_1,\ldots)
    $$

    and scalar multiplication is

    $$
    s(x_0,x_1,\ldots)=(sx_0,sx_1,\ldots).
    $$

    Construct a basis and determine its dimension.

2.  **(b)** Prove that the only sequence in $V$ with finitely many nonzero terms is the zero sequence.

:::

*Hint.* For (a), consider the two sequences with initial values $(x_0,x_1)=(1,0)$ and $(x_0,x_1)=(0,1)$.
