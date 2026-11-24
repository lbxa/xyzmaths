---
key: "hw01:basis-extension"
source: "problems/hw01/09-basis-extension/problem"
title: "Extending an independent set"
number: "1.2.19"
assignment: "hw01"
question: 9
statement-page: "linear-algebra-i/vector-spaces-and-bases"
solution-page: "appendices/exercise-solutions"
---

Let $V$ be a vector space over $\mathbb F$, where $\mathbb F$ denotes $\mathbb{R}$ or $\mathbb{C}$, and let $V$ have dimension $n$.

:::list

1.  **(a)** Prove that every linearly independent subset of $V$ is finite and can be extended to a basis of $V$.

2.  **(b)** Deduce that any $n$ linearly independent vectors form a basis, and that any set of $n$ vectors spanning $V$ is a basis.

3.  **(c)** Prove that a subspace $W\subseteq V$ with $\dim W=n$ must equal $V$. Give an example showing that an infinite-dimensional space can have a proper subspace of the same dimension. Exhibit bases to justify the comparison.

:::

*Hint.* For (a), show that adjoining $v\notin\operatorname{span}(S)$ to an independent set $S$ preserves independence. Use the comparison theorem to bound the number of steps.
