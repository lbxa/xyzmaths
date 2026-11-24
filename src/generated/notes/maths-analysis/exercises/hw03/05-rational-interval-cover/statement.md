---
key: "hw03:rational-interval-cover"
source: "problems/hw03/05-rational-interval-cover/problem"
title: "Exercise"
number: "1.9.11"
assignment: "hw03"
question: 5
statement-page: "analysis-i/sets-and-foundations"
solution-page: "appendices/exercise-solutions"
---

Let the rational numbers in $[0,1]$ be enumerated by $q_0,q_1,\ldots,q_n,\ldots$. Let $\varepsilon>0$ and cover this set $Q=\{q_n\}$ by

$$
U_\varepsilon=\bigcup_{n=0}^{\infty}I_n(\varepsilon),
$$

$$
I_n(\varepsilon)=(q_n-\varepsilon 2^{-n},q_n+\varepsilon 2^{-n}),
    \qquad n=0,1,2,\ldots.
$$

That is, $Q\subset U_\varepsilon$.

:::list

1.  **(a)** Show that the sum of the lengths of the intervals $\{I_n(\varepsilon)\}$ satisfies the bound

    $$
    \sum_{n=0}^{\infty}|I_n(\varepsilon)|\leq4\varepsilon.
    $$

2.  **(b)** Since $\varepsilon>0$ can be arbitrarily small, the set $Q$ can be covered by intervals of arbitrarily small total length indicating that $Q$ is a rather “sparse” subset of $[0,1]$. In view of this fact, give your explanation regarding the “incompleteness” of $Q$ in $[0,1]$.

:::
