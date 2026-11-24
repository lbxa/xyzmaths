---
key: "hw02:matrix-commutation"
source: "problems/hw02/06-matrix-commutation/problem"
title: "Exercise"
number: "2.1.5"
assignment: "hw02"
question: 6
statement-page: "linear-algebra-i/matrices-and-vector-coordinates"
solution-page: "appendices/exercise-solutions"
---

Recall that matrix multiplication is not necessarily commutative.

:::list

1.  **(a)** For $A\in\mathcal M_{r\times s}$ and $B\in\mathcal M_{p\times q}$, determine exactly when $AB$ and $BA$ are both defined.

2.  **(b)** Determine when $AB$ and $BA$ have the same size.

3.  **(c)** Given $r\ge2$, find matrices $A,B\in\mathcal M_{r\times r}$ such that $AB\ne BA$.

4.  **(d)** Let $E^i_j\in\mathcal M_{r\times r}$ be the matrix whose entry in row $i$ and column $j$ is $1$ and all of whose other entries are $0$. Prove that $\{E^i_j:1\le i,j\le r\}$ is a basis of $\mathcal M_{r\times r}$ and that

    $$
    E^i_jE^k_l=\delta^k_jE^i_l,
    $$

    where $\delta^k_j=1$ if $j=k$ and $0$ otherwise.

5.  **(e)** Prove that if $A\in\mathcal M_{r\times r}$ satisfies $AB=BA$ for every $B\in\mathcal M_{r\times r}$, then $A=cI_{r\times r}$ for some $c\in\mathbb F$.

6.  **(f)** Determine all $A\in\mathcal M_{r\times r}$ that commute with every $E^i_i$, $1\le i\le r$. Conclude that, for $r\ge2$, commuting with every diagonal matrix is a strictly weaker condition than the one in (e).

:::

*Hint.* Compare the entries of $AE^i_j$ and $E^i_jA$.
