---
key: "hw02:matrix-product-bilinearity"
source: "problems/hw02/05-matrix-product-bilinearity/problem"
title: "Exercise"
number: "3.2.5"
assignment: "hw02"
question: 5
statement-page: "linear-algebra-i/linear-equations-and-maps"
solution-page: "appendices/exercise-solutions"
---

Matrix multiplication defines a map

$$
\begin{gathered}
      \mathcal M_{p\times q}\times\mathcal M_{q\times r}
        \longrightarrow\mathcal M_{p\times r}\\
      (A,B)\longmapsto AB.
    \end{gathered}
$$

This problem shows that matrix multiplication is a bilinear map.

:::list

1.  **(a)** Show that given $A\in\mathcal M_{p\times q}$, the map

    $$
    \begin{gathered}
              \mathcal M_{q\times r}\longrightarrow\mathcal M_{p\times r}\\
              B\longmapsto AB
            \end{gathered}
    $$

    is linear.

2.  **(b)** Show that given $B\in\mathcal M_{q\times r}$, the map

    $$
    \begin{gathered}
              \mathcal M_{p\times q}\longrightarrow\mathcal M_{p\times r}\\
              A\longmapsto AB
            \end{gathered}
    $$

    is linear.

:::
