---
title: "k-Tree"
description: "Count weighted root paths that reach a target sum while using at least one large edge."
date: "2026-07-07"
source: "https://codeforces.com/problemset/problem/431/C"
sourceLabel: "Codeforces 431C"
topic: "Dynamic Programming / Trees"
difficulty: 6
estimatedTime: 45
statement: |
  In an infinite rooted tree, every vertex has one child for each integer weight from $1$ to $k$. Moving to that child adds its edge weight to the path. Starting at the root and moving only to children, how many paths have total weight $n$ and use at least one edge of weight $d$ or greater?

  **Input**

  A single line contains $n$, $k$, and $d$, in that order. The bounds are $1\le n,k\le 100$ and $1\le d\le k$.

  **Output**

  Print the number of qualifying paths modulo $10^9+7$.
solution: |
  Each sequence of edge weights specifies one path from the root. Let $C_r(s)$ count the paths of total weight $s$ when each edge has weight at most $r$. The empty path gives $C_r(0)=1$, and $C_r(s)=0$ for $s<0$. Removing the last edge of weight $i$ leaves total weight $s-i$, so for $s>0$,

  $$
  C_r(s)=\sum_{i=1}^{r}C_r(s-i).
  $$

  Evaluate the recurrence up to $n$ for $r=k$ and $r=d-1$. Subtracting the paths whose weights all fall below $d$ gives $C_k(n)-C_{d-1}(n)$. Reduce each sum and the final difference modulo $10^9+7$. Filling the tables in increasing order of $s$ takes $O(nk)$ time and $O(n)$ space.

  For $n=3$, $k=3$, and $d=2$, the qualifying weight sequences are $(3)$, $(1,2)$, and $(2,1)$. The answer is $3$.
---

The tree is infinite, but we can describe a path just by listing its edge weights in order. Once we know the next weight, there is exactly one child we can move to. For example, $(1,2)$ and $(2,1)$ lead to different vertices even though both paths have total weight $3$.

The threshold on the largest edge suggests counting the paths we should discard. Let $A_s$ count all paths of total weight $s$ using weights from $1$ to $k$. Let $B_s$ count paths of the same total using only weights from $1$ to $d-1$. Every path counted by $A_s$ either uses an edge of weight at least $d$ or belongs to $B_s$. The answer is therefore $A_n-B_n$.

## Count paths by their final edge

There is one empty path, so $A_0=B_0=1$. Set both counts to zero for negative totals. If a path of weight $s>0$ ends in an edge of weight $i$, removing that edge leaves a path of weight $s-i$. Conversely, each path of weight $s-i$ has exactly one extension by an edge of weight $i$. Grouping paths by that final weight gives

$$
\begin{aligned}
A_s &= \sum_{i=1}^{k} A_{s-i},\\
B_s &= \sum_{i=1}^{d-1} B_{s-i}.
\end{aligned}
$$

Both sums use smaller totals, so we can fill a table in increasing order of $s$. The same function computes either table when given its largest permitted weight. If $d=1$, the second sum is empty and $B_s=0$ for every positive $s$, as every nonempty path already qualifies.

## Worked example

Take $n=3$, $k=3$, and $d=2$. The four paths of total weight $3$ have weight lists $(1,1,1)$, $(1,2)$, $(2,1)$, and $(3)$. Only $(1,1,1)$ uses weights strictly below $2$. Subtracting it leaves $4-1=3$ qualifying paths.

## Time and space

Each table has $n+1$ entries and each entry sums at most $k$ earlier values. The two calls together take $O(nk)$ time and use $O(n)$ auxiliary space. We reduce each addition modulo $M=10^9+7$ and add $M$ before reducing the final difference so the printed residue is nonnegative.
