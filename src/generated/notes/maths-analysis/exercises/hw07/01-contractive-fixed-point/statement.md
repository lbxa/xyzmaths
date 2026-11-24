---
key: "hw07:contractive-fixed-point"
source: "problems/hw07/01-contractive-fixed-point/problem"
title: "Exercise"
number: "6.2.5"
assignment: "hw07"
question: 1
statement-page: "analysis-i/differentiation-and-applications"
solution-page: "appendices/exercise-solutions"
---

Let $f$ be a differentiable function over $\mathbb{R}$.

:::list

1.  **(i)** Show that if $f'(x)$ is a bounded function, then $f$ is a Lipschitz function which satisfies

    $$
    |f(x)-f(y)|\le L|x-y|,\qquad x,y\in\mathbb{R},
    $$

    where $L>0$ is a constant called the Lipschitz constant.

2.  **(ii)** If the Lipschitz constant in (i) satisfies $L<1$, the function is called “contractive”. Prove that a contractive function must have a fixed point $x^*$ such that $x^*=f(x^*)$. (Hint: Take any $x_0\in\mathbb{R}$ and consider the iterative sequence $x_n=f(x_{n-1})$ for $n=1,2,\ldots$.)

3.  **(iii)** Show that the fixed point $x^*$ found in (ii) is unique.

:::
