---
key: "hw02:newton-iteration"
source: "problems/hw02/06-newton-iteration/problem"
title: "Exercise"
number: "1.11.8"
assignment: "hw02"
question: 6
statement-page: "analysis-i/sets-and-foundations"
solution-page: "appendices/exercise-solutions"
---

Consider the iteration process

$$
x_{n+1}=a+\frac{1}{x_n},\quad n=0,1,2,\ldots,
    \quad a\geq 1,\quad x_0>0,
$$

whose limit gives us the continuous fraction

$$
b=a+\frac{1}{a+\frac{1}{a+\frac{1}{a+\cdots}}}.
$$

That is, $b$ is a fixed point of the function

$$
f(x)=a+\frac{1}{x},\quad x>0,
$$

which is realized as a root of the function $F(x)=x-f(x)$ $(x>0)$.

:::list

1.  **(a)** Show that the iterative algorithm

    $$
    x_{n+1}=\frac{ax_n^2+2x_n}{1+x_n^2},
            \quad n=0,1,2,\ldots,\quad x_0>0,
    $$

    arises from Newton’s method that may be used to approach $b$ of our problem.

2.  **(b)** Assume that $\{x_n\}$ in (a) converges. Verify that the limit is indeed the continuous fraction $b$ defined above.

3.  **(c)** Take $a=\frac{3}{2}$. Prove $0<x_n\leq 2$ for $n=1,2,\ldots$.

4.  **(d)** Prove that $\{x_n\}_{n=1,2,\ldots}$ increases for any $x_0\ne 2$ and is constant when $x_0=2$.

5.  **(e)** Show that $\{x_n\}$ converges to $2$ with any initial state $x_0$ (thereby establishing the “global convergence” of the algorithm).

:::
