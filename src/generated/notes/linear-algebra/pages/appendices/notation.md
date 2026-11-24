---
title: "Notation"
group: "Appendices"
order: 16
page: "117"
outline: [{"id": "sec:appendix:notation-spaces", "title": "A.1 Scalars, spaces, and sets", "level": 2}, {"id": "sec:appendix:notation-indices", "title": "A.2 Coordinates and matrix indices", "level": 2}, {"id": "summation-conventions", "title": "Summation conventions", "level": 3}, {"id": "sec:appendix:notation-bases-and-maps", "title": "A.3 Ordered bases and maps", "level": 2}, {"id": "sec:appendix:notation-kernel-and-image", "title": "A.4 Kernel, image, and function spaces", "level": 2}, {"id": "sec:appendix:notation-permutations", "title": "A.5 Permutations and multilinear notation", "level": 2}, {"id": "symbols-whose-meaning-depends-on-context", "title": "Symbols whose meaning depends on context", "level": 3}, {"id": "sec:appendix:notation-forms-and-eigenvalues", "title": "A.6 Forms and eigenvalues", "level": 2}, {"id": "sec:appendix:notation-inner-products-and-norms", "title": "A.7 Inner products and norms", "level": 2}]
---

# Appendix A. Notation {id="ch:appendix:notation"}

This appendix explains the symbols and reading conventions used in the book. Meanings are local to the stated space, map, or matrix. [Appendix D](/notes/linear-algebra/appendices/formula-sheet/#ch:appendix:formula-sheet) collects the corresponding formulas.

## A.1 Scalars, spaces, and sets {id="sec:appendix:notation-spaces"}

:::::div{id="tab:appendix:notation-spaces"}

::::tabular{widths="23,72"}

:::caption

Table A.1. Scalars, vector spaces, and span.

:::

| Symbol | Meaning |
|:---|:---|
| $\mathbb F$ | The field of scalars. |
| $\mathbb{R},\mathbb{C}$ | The real and complex numbers, respectively. |
| $\mathbb F^n$ | Coordinate vectors with $n$ entries in $\mathbb F$. |
| $V,W$ | Vector spaces. The letters $v,w$ usually denote their vectors. |
| $V^n$ | Ordered $n$-tuples of vectors in $V$, the inputs to an $n$-input multilinear function. |
| $\dim V$ | The dimension of $V$. |
| $\operatorname{span}(S)$ | All finite linear combinations of vectors in $S$. |

::::

:::::

[Table A.1](/notes/linear-algebra/appendices/notation/#tab:appendix:notation-spaces) uses the locally specified scalar field. [Chapter 5](/notes/linear-algebra/linear-algebra-i/determinants/#ch:linear-algebra-i:determinants) uses real vector spaces. An ordered basis written with an ordinary letter $F$ is distinct from the scalar field $\mathbb F$.

In set notation, $v\in V$ means that $v$ is an element of $V$, while $S\subseteq V$ means that $S$ is a subset of $V$. The symbols $\varnothing$ and $\{0\}$ denote the empty set and the set containing the zero vector, respectively. In a set such as $\{v\in V\mid L(v)=0\}$, the vertical bar means “such that”. A colon is also used for this purpose. :span[For the set-equality proof template, see [Subsection\* B.1](/notes/linear-algebra/appendices/assumed-knowledge/#sec:linear-algebra-i:set-equality-proofs).]{class="pending-review"}

The symbol $0$ can denote a scalar, vector, or zero matrix. Subscripts in $0_V$ and $0_W$ specify the space containing the zero vector. Thus $\ker L=\{0_V\}$ describes a subspace with one element, whereas $\dim\ker L=0$ describes its dimension.

## A.2 Coordinates and matrix indices {id="sec:appendix:notation-indices"}

For a matrix $M=(M^i_j)$, the notation means that

$$
M^i_j=\text{entry in row \(i\), column \(j\)}.
$$

The *upper* index selects the row, and the *lower* index selects the column. In notation that places both indices below the letter, the same entry would be written $m_{ij}$, with the row index first. For example, $M^2_3$ is the entry in the second row and third column. Here the superscript is an index, not a power.

The notation $M_j$ denotes the entire $j$-th column. Its entries are

$$
M_j=\begin{bmatrix}M^1_j&\cdots&M^r_j\end{bmatrix}^{T}
  \qquad\text{for a matrix with \(r\) rows.}
$$

The superscript $T$ means transpose, so the displayed row becomes a column. The expression $v=(v^1,\ldots,v^n)^T$ is a coordinate column, and $v^i$ is its $i$-th scalar coordinate. By contrast, $v_j$ usually labels the $j$-th vector in a list. In the expression

$$
v_j=\sum_{i=1}^n b^i_j e_i,
$$

the lower index $j$ selects the vector, and the upper index $i$ selects its coordinate in the basis direction $e_i$.

The size $r\times c$ always means $r$ rows and $c$ columns. Both $\mathrm M_{r\times c}(\mathbb F)$ and $\mathbb F^{r\times c}$ denote matrices of this size with scalar entries. The notation $\mathrm M_{r\times c}(V)$ instead allows entries in a vector space $V$. Read dimension labels $m,n$ from the stated matrix size or map domain and codomain.

### Summation conventions {id="summation-conventions"}

An explicit sum such as $\sum_{i=1}^n f_iM^i_j$ leaves $j$ fixed and sums over $i$. Where Einstein notation is used, an index repeated once above and once below is summed over its stated range. Thus

$$
f_iM^i_j=\sum_{i=1}^n f_iM^i_j,
  \qquad
  e_ja^j=\sum_{j=1}^m e_ja^j.
$$

An index that is not summed remains free. For instance, $j$ in $L(e_j)=f_iM^i_j$ identifies the basis vector whose image is being computed. These conventions are used in [§ 3.3](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#sec:linear-algebra-i:change-of-basis-for-functions-and-maps).

## A.3 Ordered bases and maps {id="sec:appendix:notation-bases-and-maps"}

An ordered basis is written as $E=(e_1,\ldots,e_m)$ or as the array $E=[e_1\ \cdots\ e_m]$. The expression $v=Ea$ means

$$
v=e_1a^1+\cdots+e_ma^m.
$$

The vector $v$ belongs to $V$, and the column $a\in\mathbb F^m$ contains its coordinates in $E$. Changing the basis changes the coordinate column while leaving the vector itself unchanged.

The equation $F=EM$ says that column $j$ of $M$ contains the $E$-coordinates of $f_j$. If $v=Ea=Fb$, then $a=Mb$, so $M$ converts $F$-coordinates to $E$-coordinates. See [§ 2.2](/notes/linear-algebra/linear-algebra-i/matrices-and-vector-coordinates/#sec:linear-algebra-i:change-of-basis-for-vectors).

For a linear map $L:V\to W$, with domain basis $E$ and codomain basis $F$, the notation

$$
L(E)=[L(e_1)\ \cdots\ L(e_m)]=FM
$$

means that $L$ is applied to each basis vector separately. Column $j$ of $M$ contains the $F$-coordinates of $L(e_j)$. If $\dim V=m$ and $\dim W=n$, this matrix has size $n\times m$. The representing matrix depends on $L$ and both ordered bases. [Table A.2](/notes/linear-algebra/appendices/notation/#tab:appendix:notation-maps) lists notation for maps.

:::::div{id="tab:appendix:notation-maps"}

::::tabular{widths="23,72"}

:::caption

Table A.2. Maps, identities, and inverses.

:::

| Symbol | Meaning |
|:---|:---|
| $L:V\to W$ | A map with domain $V$ and codomain $W$. |
| $v\mapsto L(v)$ | The rule assigning an output to an input. |
| $\mathcal L(V,W)$ | The vector space of linear maps from $V$ to $W$. |
| $I_V$ | The identity map on $V$. |
| $I_n$ | The $n$-by-$n$ identity matrix. |
| $L^{-1},M^{-1}$ | The inverse map and inverse matrix, respectively, when they exist. |

::::

:::::

Composition is read from right to left. In $L_2\circ L_1$, apply $L_1$ first and $L_2$ second. The representing matrix is $M_2M_1$ in compatible bases. A prime in $E'$, $F'$, or $M'$ labels a new basis or matrix, whereas $f'$ denotes the derivative of a function in the differentiation discussion.

## A.4 Kernel, image, and function spaces {id="sec:appendix:notation-kernel-and-image"}

:::::div{id="tab:appendix:notation-kernel-and-image"}

::::tabular{widths="23,72"}

:::caption

Table A.3. Kernel, image, rank, and nullity.

:::

| Symbol | Meaning |
|:---|:---|
| $\ker L$ | The subspace of inputs mapped to $0_W$. |
| $\operatorname{Null}(M)$ | The null space $\ker M$ of a matrix. |
| $\operatorname{im}L=L(V)$ | The subspace of outputs actually attained by $L$. |
| $\operatorname{nullity}L$ | The number $\dim\ker L$. |
| $\operatorname{rank}L$ | The number $\dim\operatorname{im}L$. |
| $v_0+\ker L$ | The set $\{v_0+k\mid k\in\ker L\}$. |

::::

:::::

[Table A.3](/notes/linear-algebra/appendices/notation/#tab:appendix:notation-kernel-and-image) lists kernel and image (subspaces) and nullity and rank (their dimensions). The codomain $W$ specifies the target space, while the image records which targets are reached. Writing $\ker M$ or $\operatorname{im}M$ treats the matrix as the linear map $x\mapsto Mx$. See [§ 4.1](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#sec:linear-algebra-i:kernel) through [§ 4.3](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#sec:linear-algebra-i:rank).

Both $C(\mathbb{R})$ and $C^0(\mathbb{R})$ denote continuous real-valued functions on $\mathbb{R}$. The notation $C^1(\mathbb{R})$ denotes continuously differentiable ones. These superscripts specify regularity. The space $\mathcal P$ contains real polynomials of arbitrary finite degree, while $\mathcal P_d(\mathbb{R})$ contains those of degree at most $d$, including the zero polynomial. These vector spaces consist of functions, as discussed in [§ 4.4](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#sec:linear-algebra-i:differentiation).

## A.5 Permutations and multilinear notation {id="sec:appendix:notation-permutations"}

:::::div{id="tab:appendix:notation-permutations"}

::::tabular{widths="23,72"}

:::caption

Table A.4. Permutations and their signs.

:::

| Symbol | Meaning |
|:---|:---|
| $S_n$ | Permutations of $\{1,\ldots,n\}$, with composition. |
| $T_n$ | All maps from $\{1,\ldots,n\}$ to itself. |
| $\iota$ | The identity permutation. |
| $\tau_{ij}$ | The transposition exchanging $i$ and $j$. |
| $\varepsilon(\sigma)$ | The sign of a permutation, equal to $1$ or $-1$. |
| $\varepsilon(\phi)$ | The extended sign on $T_n$, equal to $0$ for a map that is not a permutation. |

::::

:::::

[Table A.4](/notes/linear-algebra/appendices/notation/#tab:appendix:notation-permutations) uses $T_n$ for a set of maps, distinct from the transpose superscript $T$. As with maps, $\sigma_2\circ\sigma_1$ applies $\sigma_1$ first. The indices in $v_{\sigma(j)}$ and $b^{\sigma(j)}_j$ select a vector from the list and a row of column $j$, respectively. See [§ 5.2](/notes/linear-algebra/linear-algebra-i/determinants/#sec:linear-algebra-i:permutations) and [§ 5.4](/notes/linear-algebra/linear-algebra-i/determinants/#sec:linear-algebra-i:determinant).

### Symbols whose meaning depends on context {id="symbols-whose-meaning-depends-on-context"}

The symbol $A$ denotes a matrix in $Ax=b$, oriented area in $A(v,w)$, or an antisymmetric multilinear function in $A(v_1,\ldots,v_n)$. Its inputs and domain identify the meaning. The symbol $\mathcal V(a,b,c)$ denotes oriented volume. Ordinary area and volume are the absolute values of their oriented counterparts.

For differentiation, $D(f)=f'$. For determinants, $D$ is the normalized antisymmetric multilinear function, with $\det M=D(C_1,\ldots,C_n)$ for the columns $C_j$ of a square matrix. These column labels are distinct from the field $\mathbb{C}$ and the function spaces $C^0(\mathbb{R})$ and $C^1(\mathbb{R})$.

The symbols $P(v,w)$ and $P(a,b,c)$ denote a parallelogram and a parallelepiped, whereas $\mathcal P$ is a polynomial space.

## A.6 Forms and eigenvalues {id="sec:appendix:notation-forms-and-eigenvalues"}

[Table A.5](/notes/linear-algebra/appendices/notation/#tab:appendix:notation-forms-and-eigenvalues) collects the notation for the determinant of a map and its eigenspaces. In [Chapter 6](/notes/linear-algebra/linear-algebra-i/determinants-of-linear-maps/#ch:linear-algebra-i:determinants-of-linear-maps) and [Chapter 7](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#ch:linear-algebra-i:eigenvalues-and-diagonalization), the scalar field is $\mathbb{R}$ or $\mathbb{C}$, as stated locally.

:::::div{id="tab:appendix:notation-forms-and-eigenvalues"}

::::tabular{widths="23,72"}

:::caption

Table A.5. Forms, eigenvalues, and direct sums.

:::

| Symbol | Meaning |
|:---|:---|
| $V^*$ | The linear dual, consisting of linear scalar-valued functions on $V$. |
| $\Lambda^k V^*$ | The space of antisymmetric multilinear functions on $V$ with $k$ inputs. |
| $L^*A$ | The pullback of a form, obtained by applying $L$ to each input before evaluating $A$. |
| $\det L$ | For an endomorphism, the scalar by which pullback acts on top-degree forms. For maps between different equal-dimensional spaces, the pullback map itself. |
| $E_\lambda(L)$ | The eigenspace $\ker(L-\lambda I)$, including zero. Eigenvectors are its nonzero vectors. |
| $p_M(x)$ | The characteristic polynomial $\det(M-xI)$, with leading coefficient $(-1)^n$ for an $n$-by-$n$ matrix. The map version is $p_L(x)=\det(L-xI)$. |
| $\delta^i_j$ | The Kronecker delta, or identity-matrix entry, equal to $1$ when $i=j$ and $0$ otherwise. |
| $\bigoplus_j S_j$ | A direct sum, with a unique decomposition into vectors from the indicated subspaces. |

::::

:::::

In complex arithmetic, if $z=x+iy$, then $\overline z=x-iy$ is its conjugate and $|z|=\sqrt{x^2+y^2}$ is its modulus. The symbol $i$ here satisfies $i^2=-1$. It is distinct from an index named $i$ in a matrix entry. See [§ 7.4](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#sec:linear-algebra-i:complex-eigenvalues).

## A.7 Inner products and norms {id="sec:appendix:notation-inner-products-and-norms"}

The real inner-product notation of [Chapter 8](/notes/linear-algebra/linear-algebra-i/inner-products-and-norms/#ch:linear-algebra-i:inner-products-and-norms) is summarized in [Table A.6](/notes/linear-algebra/appendices/notation/#tab:appendix:notation-inner-products-and-norms). Here $V$ is a real vector space equipped with a chosen inner product $B:V\times V\to\mathbb{R}$. The pairing $(v,w)=B(v,w)$ is a real scalar. These parentheses do not denote an ordered pair. The pairing and its induced norm refer to the inner product currently specified, since a vector space does not itself determine that choice. See [§ 8.1](/notes/linear-algebra/linear-algebra-i/inner-products-and-norms/#sec:linear-algebra-i:real-inner-products) and [§ 8.5](/notes/linear-algebra/linear-algebra-i/inner-products-and-norms/#sec:linear-algebra-i:orthogonality-and-coordinate-products).

:::::div{id="tab:appendix:notation-inner-products-and-norms"}

::::tabular{widths="23,72"}

:::caption

Table A.6. Real inner products and induced norms.

:::

| Symbol | Meaning |
|:---|:---|
| $B(v,w)=(v,w)$ | A real scalar pairing that is positive definite, symmetric, and bilinear. |
| $v\cdot w$ | The ordinary dot product of real coordinate columns, equal to $w^Tv$. |
| $\mathcal T_n$ | Real trigonometric polynomials with frequencies from $0$ to $n$. This is distinct from the permutation chapter’s set $T_n$ of maps. |
| $\operatorname{tr}A$ | The trace, or sum of the diagonal entries of a square matrix. |
| $\lVert v\rVert$ | The induced norm $\sqrt{(v,v)}$. Its square is $\lVert v\rVert^2=(v,v)$. |
| $\lvert(v,w)\rvert$ | The absolute value of the real scalar $(v,w)$, as in the Cauchy–Schwarz inequality. |
| $\theta$ | The angle between nonzero vectors, with $0\le\theta\le\pi$ and $(v,w)=\lVert v\rVert\lVert w\rVert\cos\theta$. |
| $(v,w)=0$ | The condition that $v$ and $w$ are orthogonal. |
| $\delta_{ij}$ | The Kronecker delta, equal to $1$ for $i=j$ and $0$ otherwise. An orthonormal family satisfies $(v_i,v_j)=\delta_{ij}$. |
| $(v,w)_E$ | The inner product obtained by taking the dot product of the coordinate columns in the basis $E$. |

::::

:::::

Double bars $\lVert v\rVert$ denote a vector norm, whereas single bars $\lvert s\rvert$ denote the absolute value of a real scalar. In [Exercise 8.4.3](/notes/linear-algebra/linear-algebra-i/inner-products-and-norms/#ex:hw07:minimization-and-cauchy-schwarz), the original single-bar notation $\lvert v\rvert$ instead denotes the induced vector norm, as stated in [§ 8.4](/notes/linear-algebra/linear-algebra-i/inner-products-and-norms/#sec:linear-algebra-i:inner-product-norms-and-angles).
