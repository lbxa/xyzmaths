---
title: "Matrices and vector coordinates"
group: "Linear Algebra I"
order: 8
part: "Part I · Linear Algebra I"
page: "29"
outline: [{"id": "sec:linear-algebra-i:matrix-multiplication", "title": "2.1 Matrix multiplication", "level": 2}, {"id": "multiplication-by-columns", "title": "Multiplication by columns", "level": 3}, {"id": "reading-a-transformation-from-its-columns", "title": "Reading a transformation from its columns", "level": 3}, {"id": "exercises-on-matrix-multiplication", "title": "Exercises on matrix multiplication", "level": 3}, {"id": "sec:linear-algebra-i:change-of-basis-for-vectors", "title": "2.2 Change of basis formula for vectors", "level": 2}]
---

# Chapter 2. Matrices and vector coordinates {id="ch:linear-algebra-i:matrices-and-vector-coordinates"}

## 2.1 Matrix multiplication {id="sec:linear-algebra-i:matrix-multiplication"}

In [§ 1.2](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#sec:linear-algebra-i:linear-combinations-and-bases), a basis described a vector by its coefficients. A matrix uses such coefficients to form a new linear combination of its columns. This interpretation will explain both matrix multiplication and the representation of linear maps.

A matrix with $r$ rows and $c$ columns has size $r\times c$. Write $\mathrm M_{r\times c}(\mathbb F)$ for the space of $r$-by-$c$ matrices with entries in $\mathbb F$. More generally, $\mathrm M_{r\times c}(V)$ denotes the $r$-by-$c$ arrays with entries in a vector space $V$. The notation $\mathcal M_{r\times c}$ also denotes scalar-valued matrices of this size when the field is understood.

### Multiplication by columns {id="multiplication-by-columns"}

Let $A=[A_1,\ldots,A_s]\in\mathrm M_{r\times s}(\mathbb F)$. For a column $b=(b^1,\ldots,b^s)^T$, multiplication by $A$ is defined by the linear combination of its columns

$$
Ab=\sum_{k=1}^s A_kb^k\in\mathbb F^r.
$$

If $B=[B_1,\ldots,B_t]\in\mathrm M_{s\times t}(\mathbb F)$, define its product with $A$ column by column,

$$
AB=[AB_1,\ldots,AB_t]\in\mathrm M_{r\times t}(\mathbb F).
$$

Thus the number of columns of $A$ must equal the number of rows of $B$. We write $I_{r\times r}$ for the identity matrix and $0$ for a zero matrix of the required size.

### Reading a transformation from its columns {id="reading-a-transformation-from-its-columns"}

Consider the shear from [Subsection\* 1.2](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#sec:linear-algebra-i:bases-to-transformations). In standard coordinates its matrix and its action are

$$
S=\begin{bmatrix}1&1\\0&1\end{bmatrix},
  \qquad
  S\begin{bmatrix}x\\y\end{bmatrix}
    =x\begin{bmatrix}1\\0\end{bmatrix}
      +y\begin{bmatrix}1\\1\end{bmatrix}
    =\begin{bmatrix}x+y\\y\end{bmatrix}.
$$

The first column is the image of $e_1=(1,0)^T$, and the second is the image of $e_2=(0,1)^T$. In particular, $S(e_1)=e_1$, so the first basis vector is fixed. For a general input, the first output coordinate is $x+y$, while the second is $y$. Multiplication by $(x,y)^T$ takes $x$ copies of the first image and $y$ copies of the second. This is precisely the rule

$$
S(xe_1+ye_2)=xS(e_1)+yS(e_2).
$$

Thus the matrix records the action on the basis, and the product recovers the action on every vector. The grid in [Figure 1.4](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#fig:linear-algebra-i:shear-grid-overview) visualizes this same calculation at many input points at once.

The identity matrix provides the corresponding unchanged grid. Its columns are $e_1,e_2$, so $I_2(x,y)^T=(x,y)^T$. The distinction between applying a matrix to move a vector and using a matrix to change the coordinates of a fixed vector is developed in [§ 2.2](/notes/linear-algebra/linear-algebra-i/matrices-and-vector-coordinates/#sec:linear-algebra-i:change-of-basis-for-vectors).

### Exercises on matrix multiplication {id="exercises-on-matrix-multiplication"}

::statement{key="hw02:matrix-product-entries"}

::statement{key="hw02:matrix-product-associativity"}

::statement{key="hw02:block-shear-inverses"}

::statement{key="hw02:characterizing-the-identity"}

::statement{key="hw02:matrix-commutation"}

::statement{key="hw02:zero-products"}

::statement{key="hw02:upper-triangular-subspace"}

::statement{key="hw02:two-by-two-matrix-identities"}

## 2.2 Change of basis formula for vectors {id="sec:linear-algebra-i:change-of-basis-for-vectors"}

The coordinates introduced by a basis describe a vector relative to that basis. A second basis gives a second description of the same vector. The matrix in this section translates between those descriptions. When a linear transformation is applied, it produces an output vector, as in the shear of [Figure 1.4](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#fig:linear-algebra-i:shear-grid-overview). Both calculations use matrices because both reconstruct vectors from linear combinations.

Let $E=[e_1,\ldots,e_n]$ and $F=[f_1,\ldots,f_n]$ be two ordered bases of $V$. Each vector $f_j$ has coordinates in the basis $E$, so there is a matrix $M\in\mathbb F^{n\times n}$ whose $j$-th column contains those coordinates. In matrix notation,

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:vector-basis-coordinates"}

[![The same vector v in two bases of the real plane, shown schematically. Dashed lines complete the components. The coordinates satisfy a=Mb when F=EM.](/notes/linear-algebra/figures/vector-basis-coordinates.svg){.tikz-diagram}](/notes/linear-algebra/figures/vector-basis-coordinates.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 2.1. The same vector $v$ in two bases of the real plane, shown schematically. Dashed lines complete the components. The coordinates satisfy $a=Mb$ when $F=EM$.

:::

::::

:::::

$$
F=EM.
$$

Because $F$ is also a basis, there is a matrix $N$ with $E=FN$. Substituting these expressions into one another gives $E=EMN$ and $F=FNM$. Uniqueness of coefficients in each basis gives $MN=I_n$ and $NM=I_n$. Thus $N=M^{-1}$. The change-of-basis matrix is invertible, and it converts coordinates in either direction.

If $v\in V$ has coordinate columns $a$ in basis $E$ and $b$ in basis $F$, then $v=Ea=Fb$. Using $F=EM$,

$$
v=Fb=EMb,
  \qquad a=Mb,
  \qquad b=M^{-1}a.
$$

Thus $M$ converts $F$-coordinates to $E$-coordinates, and $M^{-1}$ converts $E$-coordinates to $F$-coordinates.

The vector stays fixed while its coordinate column changes. [Figure 2.1](/notes/linear-algebra/linear-algebra-i/matrices-and-vector-coordinates/#fig:linear-algebra-i:vector-basis-coordinates) shows the two decompositions in the real plane.
