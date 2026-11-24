---
title: "Eigenvalues and diagonalization"
group: "Linear Algebra I"
order: 13
part: "Part I · Linear Algebra I"
page: "87"
outline: [{"id": "sec:linear-algebra-i:eigenvalues-and-eigenspaces", "title": "7.1 Eigenvalues and eigenspaces", "level": 2}, {"id": "matrices-and-coordinates", "title": "Matrices and coordinates", "level": 3}, {"id": "a-motivating-quotient", "title": "A motivating quotient", "level": 3}, {"id": "sec:linear-algebra-i:characteristic-polynomials-and-similarity", "title": "7.2 Characteristic polynomials and similarity", "level": 2}, {"id": "characteristic-polynomials", "title": "Characteristic polynomials", "level": 3}, {"id": "changing-the-basis", "title": "Changing the basis", "level": 3}, {"id": "sec:linear-algebra-i:computing-eigenspaces", "title": "7.3 Computing eigenvalues and eigenspaces", "level": 2}, {"id": "diagonal-and-triangular-matrices", "title": "Diagonal and triangular matrices", "level": 3}, {"id": "a-matrix-that-interchanges-coordinates", "title": "A matrix that interchanges coordinates", "level": 3}, {"id": "a-matrix-with-no-real-eigenvalue", "title": "A matrix with no real eigenvalue", "level": 3}, {"id": "sec:linear-algebra-i:complex-eigenvalues", "title": "7.4 Complex eigenvalues", "level": 2}, {"id": "complex-arithmetic", "title": "Complex arithmetic", "level": 3}, {"id": "returning-to-the-rotation-example", "title": "Returning to the rotation example", "level": 3}, {"id": "roots-and-multiplicities", "title": "Roots and multiplicities", "level": 3}, {"id": "sec:linear-algebra-i:diagonalization", "title": "7.5 Diagonalization", "level": 2}, {"id": "failure-of-diagonalization", "title": "Failure of diagonalization", "level": 3}, {"id": "sec:linear-algebra-i:direct-sums", "title": "7.6 Direct sums and diagonalization criteria", "level": 2}, {"id": "transversal-subspaces", "title": "Transversal subspaces", "level": 3}, {"id": "combining-bases", "title": "Combining bases", "level": 3}, {"id": "transversality-of-distinct-eigenspaces", "title": "Transversality of distinct eigenspaces", "level": 3}, {"id": "criteria-for-an-eigenbasis", "title": "Criteria for an eigenbasis", "level": 3}, {"id": "approximation-by-diagonalizable-matrices", "title": "Approximation by diagonalizable matrices", "level": 3}]
---

# Chapter 7. Eigenvalues and diagonalization {id="ch:linear-algebra-i:eigenvalues-and-diagonalization"}

An eigenvector is a nonzero vector that a linear map sends to a scalar multiple of itself. The characteristic polynomial detects the possible scalars. When eigenvectors form a basis, the map has a diagonal matrix in that basis.

Throughout this chapter, $V$ is finite-dimensional and $\mathbb F$ is $\mathbb{R}$ or $\mathbb{C}$. The choice of scalar field matters both for the existence of eigenvalues and for diagonalization.

## 7.1 Eigenvalues and eigenspaces {id="sec:linear-algebra-i:eigenvalues-and-eigenspaces"}

The determinant detects when an endomorphism loses an input direction. To find directions on which $L$ acts by scalar multiplication, we apply that test to $L-\lambda I$. Its kernel will collect the vectors satisfying the eigenvector equation.

:::div{id="web:sections/linear-algebra-i/07-eigenvalues-and-diagonalization/01-eigenvalues-and-eigenspaces:345" class="result definition"}

**Definition 7.1.1.** Let $L:V\to V$ be linear. A scalar $\lambda\in\mathbb F$ is an eigenvalue of $L$ if there exists $v\in V\setminus\{0\}$ such that

$$
L(v)=\lambda v.
$$

Such a nonzero vector $v$ is an eigenvector for $\lambda$.

:::

The identity map $I$ allows us to subtract scalar multiplication from $L$. Since $(\lambda I)(v)=\lambda v$,

$$
\begin{aligned}
    L(v)=\lambda v
      &\Longleftrightarrow L(v)-\lambda v=0\\
      &\Longleftrightarrow (L-\lambda I)(v)=0\\
      &\Longleftrightarrow v\in\ker(L-\lambda I).
  \end{aligned}
$$

The requirement $v\ne0$ forces $L-\lambda I$ to be singular, meaning that it has no inverse.

:::div{class="proof"}

*Proof.* Let $v\ne0$ satisfy $(L-\lambda I)(v)=0$. Suppose, for a contradiction, that $L-\lambda I$ is not singular. It then has an inverse, with

$$
(L-\lambda I)^{-1}\circ(L-\lambda I)=I.
$$

Applying this inverse to $(L-\lambda I)(v)=0$ gives

$$
\begin{aligned}
      v&=(L-\lambda I)^{-1}\bigl((L-\lambda I)(v)\bigr)\\
        &=(L-\lambda I)^{-1}(0)=0.
    \end{aligned}
$$

The inverse is linear by [Proposition 3.3.6](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#thm:linear-algebra-i:inverse-linearity), so it sends the zero vector to the zero vector. This contradicts $v\ne0$. Therefore $L-\lambda I$ is singular. ◻

:::

Conversely, if $L-\lambda I$ is singular, the finite-dimensional endomorphism criteria in [§ 4.3](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#sec:linear-algebra-i:rank) give a nonzero vector in its kernel. The displayed equivalences then show that this vector is an eigenvector of $L$ with eigenvalue $\lambda$.

Thus [Theorem 6.3.3](/notes/linear-algebra/linear-algebra-i/determinants-of-linear-maps/#thm:linear-algebra-i:determinant-invertibility) gives

:::div{id="eq:linear-algebra-i:eigenvalue-determinant-criterion" class="equation"}

$$
\lambda\text{ is an eigenvalue of }L
  \quad\Longleftrightarrow\quad \det(L-\lambda I)=0.\tag{7.1}
$$

:::

:::div{id="web:sections/linear-algebra-i/07-eigenvalues-and-diagonalization/01-eigenvalues-and-eigenspaces:2194" class="result definition"}

**Definition 7.1.2.** The eigenspace associated with $\lambda$ is

$$
E_\lambda(L)=\ker(L-\lambda I)
      =\{v\in V\mid L(v)=\lambda v\}.
$$

:::

An eigenspace includes the zero vector, while an eigenvector must be nonzero. In particular, $E_0(L)=\ker L$. A nonzero scalar multiple of an eigenvector is another eigenvector for the same eigenvalue.

:::div{id="thm:linear-algebra-i:eigenspaces-are-subspaces" class="result proposition"}

**Proposition 7.1.3 (Eigenspaces are subspaces).** Every eigenspace is a subspace of $V$. If $\lambda$ is an eigenvalue, then $\dim E_\lambda(L)>0$.

:::

:::div{class="proof"}

*Proof.* The zero vector belongs to $E_\lambda(L)$. For $v_1,v_2\in E_\lambda(L)$ and $a_1,a_2\in\mathbb F$,

$$
\begin{aligned}
    L(a_1v_1+a_2v_2)
      &=a_1L(v_1)+a_2L(v_2)\\
      &=a_1\lambda v_1+a_2\lambda v_2\\
      &=\lambda(a_1v_1+a_2v_2).
  
\end{aligned}
$$

Hence $a_1v_1+a_2v_2\in E_\lambda(L)$. For an eigenvalue, the eigenspace contains a nonzero vector, so its dimension is positive. ◻

:::

:::div{id="thm:linear-algebra-i:distinct-eigenspaces-intersection" class="result proposition"}

**Proposition 7.1.4 (Intersection of distinct eigenspaces).** If $\lambda_1,\lambda_2$ are distinct eigenvalues of $L$, then

$$
E_{\lambda_1}(L)\cap E_{\lambda_2}(L)=\{0\}.
$$

:::

:::div{class="proof"}

*Proof.* If $v$ belongs to both eigenspaces, then $L(v)=\lambda_1v$ and $L(v)=\lambda_2v$. Subtracting gives $(\lambda_1-\lambda_2)v=0$. Since the scalar is nonzero, $v=0$. ◻

:::

::statement{key="hw06:sums-of-eigenvectors"}

### Matrices and coordinates {id="matrices-and-coordinates"}

For $M\in\mathbb F^{n\times n}$, a nonzero column $a\in\mathbb F^n$ is an eigenvector with eigenvalue $\lambda$ if $Ma=\lambda a$. The eigenspace is $E_\lambda(M)=\ker(M-\lambda I)$, and the eigenvalue criterion is $\det(M-\lambda I)=0$.

Let $E=(e_1,\ldots,e_n)$ be an ordered basis and let $L(E)=EM$. For $v=Ea=\sum_{j=1}^n e_ja^j$,

$$
\begin{aligned}
  L(v)&=\sum_{j=1}^n a^jL(e_j)\\
    &=\sum_{j=1}^n a^j\sum_{i=1}^n e_iM^i_j\\
    &=\sum_{i=1}^n e_i\left(\sum_{j=1}^n M^i_ja^j\right)
      =E(Ma).
\end{aligned}
$$

On the other hand, $\lambda v=E(\lambda a)$. Uniqueness of coordinates therefore gives

$$
L(v)=\lambda v\quad\Longleftrightarrow\quad Ma=\lambda a.
$$

Thus a nonzero vector is an eigenvector of $L$ precisely when its coordinate column is an eigenvector of the representing matrix.

### A motivating quotient {id="a-motivating-quotient"}

For a real matrix $M$ and a nonzero vector $v\in\mathbb{R}^n$, the quotient

$$
\frac{v\cdot Mv}{v\cdot v}
    =\frac{\displaystyle\sum_{j,k=1}^n v^jM^j_kv^k}
      {\displaystyle\sum_{j=1}^n(v^j)^2}
$$

compares a quadratic expression with the squared length of $v$. The associated optimization problem is to consider

$$
E(M)=\sup_{v\in\mathbb{R}^n\setminus\{0\}}
    \frac{v\cdot Mv}{v\cdot v}.
$$

## 7.2 Characteristic polynomials and similarity {id="sec:linear-algebra-i:characteristic-polynomials-and-similarity"}

### Characteristic polynomials {id="characteristic-polynomials"}

:::div{id="web:sections/linear-algebra-i/07-eigenvalues-and-diagonalization/02-characteristic-polynomials-and-similarity:165" class="result definition"}

**Definition 7.2.1.** The characteristic polynomial of $M\in\mathbb F^{n\times n}$ is

$$
p_M(x)=\det(M-xI).
$$

For an endomorphism $L:V\to V$, its characteristic polynomial is $p_L(x)=\det(L-xI)$.

:::

Let $\delta^i_j$ denote the entry in row $i$, column $j$ of the identity matrix,

$$
\delta^i_j=\begin{cases}1&\text{if }i=j,\\0&\text{if }i\ne j.\end{cases}
$$

The permutation formula gives

$$
p_M(x)=\sum_{\sigma\in S_n}\varepsilon(\sigma)
    \prod_{j=1}^n\bigl(M^{\sigma(j)}_j-x\delta^{\sigma(j)}_j\bigr).
$$

The term of degree $n$ is obtained by selecting $-x$ from every diagonal position. Thus this is a polynomial of degree $n$ with leading term $(-x)^n$. Setting $x=0$ gives its constant term, $\det M$. Its roots in the scalar field are exactly the eigenvalues of $M$.

There is also a direct expansion for $L$. Normalize a top-degree form $D$ on a basis $(e_1,\ldots,e_n)$. Then

$$
\begin{aligned}
  p_L(x)
    &=D((L-xI)e_1,\ldots,(L-xI)e_n)\\
    &=D(L(e_1)-xe_1,\ldots,L(e_n)-xe_n).
\end{aligned}
$$

For $n\ge2$, multilinearity gives the expansion

$$
\begin{aligned}
    p_L(x)&=D(L(e_1),\ldots,L(e_n))\\
      &\quad-x\sum_{j=1}^n
        D(L(e_1),\ldots,e_j,\ldots,L(e_n))\\
      &\quad+\cdots+(-x)^nD(e_1,\ldots,e_n).
  \end{aligned}
$$

In the sum displayed here, only the $j$-th input is replaced by $e_j$. The coefficient of $(-x)^{n-1}$ is

$$
\sum_{j=1}^n D(e_1,\ldots,L(e_j),\ldots,e_n),
$$

where only the $j$-th input is acted on by $L$. Since $D(e_1,\ldots,e_n)=1$, the leading coefficient is $(-1)^n$. Thus

$$
p_L(x)=(-x)^n+c_{n-1}(-x)^{n-1}+\cdots+c_1(-x)+c_0,
  \qquad c_0=\det L.
$$

If $L(E)=EM$, then $(L-xI)(E)=E(M-xI)$, so [Proposition 6.2.2](/notes/linear-algebra/linear-algebra-i/determinants-of-linear-maps/#thm:linear-algebra-i:determinant-representing-matrix) gives

$$
p_L(x)=\det(L-xI)=\det(M-xI)=p_M(x).
$$

### Changing the basis {id="changing-the-basis"}

Changing coordinates changes the entries of a representing matrix, but the equation $L(v)=\lambda v$ concerns the map and vector themselves. The change-of-basis formula identifies how this equation is expressed in two coordinate systems.

Suppose $E,F$ are bases with $F=EH$, and write $L(E)=EM$, $L(F)=FN$. Then

$$
FN=L(F)=L(EH)=EMH=FH^{-1}MH,
$$

and hence $N=H^{-1}MH$. For $v=Ea=Fb$, the coordinate columns satisfy $a=Hb$ and $b=H^{-1}a$.

:::div{id="web:sections/linear-algebra-i/07-eigenvalues-and-diagonalization/02-characteristic-polynomials-and-similarity:2508" class="result definition"}

**Definition 7.2.2.** Two square matrices $M,N$ are similar if there exists an invertible matrix $H$ such that

$$
N=H^{-1}MH.
$$

:::

:::div{id="thm:linear-algebra-i:similarity-invariants" class="result proposition"}

**Proposition 7.2.3 (Invariants under similarity).** Similar matrices have the same determinant and characteristic polynomial. If $N=H^{-1}MH$, then $a$ is an eigenvector of $M$ for $\lambda$ if and only if $H^{-1}a$ is an eigenvector of $N$ for $\lambda$.

:::

:::div{class="proof"}

*Proof.* Multiplicativity gives

$$
\det N=(\det H^{-1})(\det M)(\det H)=\det M.
$$

Also $N-xI=H^{-1}(M-xI)H$, so

$$
p_N(x)=(\det H^{-1})\det(M-xI)(\det H)=p_M(x).
$$

Finally, $NH^{-1}=H^{-1}M$ gives

$$
Ma=\lambda a
    \quad\Longleftrightarrow\quad
    N(H^{-1}a)=\lambda H^{-1}a.
$$

Since $H$ is invertible, $a\ne0$ if and only if $H^{-1}a\ne0$. ◻

:::

For $\lambda=0$, this gives an isomorphism of kernels. Its two directions are shown in [Figure 7.1](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#fig:linear-algebra-i:similar-matrix-kernels),

$$
\ker M\longrightarrow\ker N,\quad a\longmapsto H^{-1}a,
  \qquad b\longmapsto Hb\text{ in the reverse direction}.
$$

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:similar-matrix-kernels"}

[![For N=H^\{-1\}MH, the changes of coordinates restrict to inverse isomorphisms of kernels.](/notes/linear-algebra/figures/similar-matrix-kernels.svg){.tikz-diagram}](/notes/linear-algebra/figures/similar-matrix-kernels.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 7.1. For $N=H^{-1}MH$, the changes of coordinates restrict to inverse isomorphisms of kernels.

:::

::::

:::::

:::div{id="ex:linear-algebra-i:same-polynomial-not-similar" class="result example"}

**Example 7.2.4.** The converse to characteristic-polynomial invariance fails. Let

$$
A=\begin{bmatrix}0&0\\0&0\end{bmatrix},\qquad
    N=\begin{bmatrix}0&1\\0&0\end{bmatrix}.
$$

Both characteristic polynomials are $x^2$, but

$$
\ker A=\mathbb F^2,\qquad
    \ker N=\left\{\begin{bmatrix}t\\0\end{bmatrix}\;\middle|\;t\in\mathbb F\right\}.
$$

Their kernels have different dimensions, so they cannot be similar.

:::

## 7.3 Computing eigenvalues and eigenspaces {id="sec:linear-algebra-i:computing-eigenspaces"}

The calculation has two stages. First solve $\det(M-\lambda I)=0$ for the eigenvalues in the chosen scalar field. For each such value, solve the homogeneous system $(M-\lambda I)v=0$. Its full solution space is the eigenspace, and its nonzero solutions are the eigenvectors.

### Diagonal and triangular matrices {id="diagonal-and-triangular-matrices"}

:::div{id="web:sections/linear-algebra-i/07-eigenvalues-and-diagonalization/03-computing-eigenspaces:427" class="result example"}

**Example 7.3.1.** For

$$
D=\begin{bmatrix}a&0&0\\0&b&0\\0&0&c\end{bmatrix},
$$

the standard basis vectors satisfy $De_1=ae_1$, $De_2=be_2$, and $De_3=ce_3$. The characteristic polynomial is

$$
p_D(x)=\det\begin{bmatrix}
      a-x&0&0\\0&b-x&0\\0&0&c-x
    \end{bmatrix}=(a-x)(b-x)(c-x).
$$

Thus the eigenvalues are the diagonal entries.

:::

A triangular matrix also has its diagonal entries as eigenvalues, since subtracting $xI$ preserves triangularity. For instance,

$$
T=\begin{bmatrix}a&0&0\\b&c&0\\d&e&f\end{bmatrix}
  \quad\Longrightarrow\quad
  p_T(x)=(a-x)(c-x)(f-x).
$$

Here $Te_3=fe_3$, so $e_3$ is an eigenvector for $f$. Finding eigenvectors for $a$ and $c$ requires solving the corresponding kernel equations. In general, for triangular $T=(T^i_j)$,

$$
\det T=T^1_1\cdots T^n_n,\qquad
  p_T(x)=\prod_{j=1}^n(T^j_j-x).
$$

::statement{key="hw06:triangular-matrix-eigenvectors"}

::statement{key="hw06:eigenvectors-in-a-basis"}

### A matrix that interchanges coordinates {id="a-matrix-that-interchanges-coordinates"}

::::::div{id="ex:linear-algebra-i:coordinate-swap-eigenspaces" class="result example"}

**Example 7.3.4.** Let

$$
A=\begin{bmatrix}0&1\\1&0\end{bmatrix}.
$$

Its characteristic polynomial is $p_A(x)=x^2-1=(x-1)(x+1)$. Row reduction gives

$$
A-\lambda I=
    \begin{bmatrix}-\lambda&1\\1&-\lambda\end{bmatrix}
    \sim\begin{bmatrix}1&-\lambda\\-\lambda&1\end{bmatrix}
    \sim\begin{bmatrix}1&-\lambda\\0&1-\lambda^2\end{bmatrix}.
$$

If $1-\lambda^2\ne0$, the matrix reduces to the identity and its kernel is zero. If $\lambda=1$, the kernel equation is $v^1-v^2=0$, giving

$$
E_1(A)=\left\{\begin{bmatrix}t\\t\end{bmatrix}\;\middle|\;t\in\mathbb F\right\}
      =\operatorname{span}\left\{\begin{bmatrix}1\\1\end{bmatrix}\right\}.
$$

If $\lambda=-1$, the equation is $v^1+v^2=0$, giving

$$
E_{-1}(A)=\left\{\begin{bmatrix}t\\-t\end{bmatrix}\;\middle|\;t\in\mathbb F\right\}
      =\operatorname{span}\left\{\begin{bmatrix}1\\-1\end{bmatrix}\right\}.
$$

The nonzero vectors in these spaces are the eigenvectors. Over $\mathbb{R}$, their two directions appear in [Figure 7.2](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#fig:linear-algebra-i:swap-eigendirections).

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:swap-eigendirections"}

[![The map A(x,y)=(y,x) fixes the line E\_1 and reverses vectors on E\_\{-1\}. Here v=(1,1), w=(1,-1), and Aw=-w.](/notes/linear-algebra/figures/swap-eigendirections.svg){.tikz-diagram}](/notes/linear-algebra/figures/swap-eigendirections.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 7.2. The map $A(x,y)=(y,x)$ fixes the line $E_1$ and reverses vectors on $E_{-1}$. Here $v=(1,1)$, $w=(1,-1)$, and $Aw=-w$.

:::

::::

:::::

::::::

### A matrix with no real eigenvalue {id="a-matrix-with-no-real-eigenvalue"}

::::::div{id="ex:linear-algebra-i:rotation-no-real-eigenvalue" class="result example"}

**Example 7.3.5.** Consider

$$
B=\begin{bmatrix}0&-1\\1&0\end{bmatrix},\qquad
    B\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}-y\\x\end{bmatrix}.
$$

Its characteristic polynomial is $p_B(x)=x^2+1$, and

$$
B-\lambda I=
    \begin{bmatrix}-\lambda&-1\\1&-\lambda\end{bmatrix}
    \sim\begin{bmatrix}1&-\lambda\\-\lambda&-1\end{bmatrix}
    \sim\begin{bmatrix}1&-\lambda\\0&-1-\lambda^2\end{bmatrix}.
$$

For real $\lambda$, the last diagonal entry is strictly negative, so the kernel is zero. Thus $B$ has no real eigenvalues. Over $\mathbb{C}$, the roots of $x^2+1$ are $i$ and $-i$. Geometrically, $B$ makes a counterclockwise quarter-turn in the real plane, as in [Figure 7.3](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#fig:linear-algebra-i:rotation-no-real-eigendirection).

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:rotation-no-real-eigendirection"}

[![For every real nonzero v, the vector Bv is perpendicular to v, so it cannot be a real scalar multiple of v.](/notes/linear-algebra/figures/rotation-no-real-eigendirection.svg){.tikz-diagram}](/notes/linear-algebra/figures/rotation-no-real-eigendirection.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 7.3. For every real nonzero $v$, the vector $Bv$ is perpendicular to $v$, so it cannot be a real scalar multiple of $v$.

:::

::::

:::::

::::::

## 7.4 Complex eigenvalues {id="sec:linear-algebra-i:complex-eigenvalues"}

### Complex arithmetic {id="complex-arithmetic"}

The quarter-turn has no eigenvalue over $\mathbb{R}$, but its characteristic polynomial has roots over $\mathbb{C}$. We recall the arithmetic needed to solve its kernel equations with complex coordinates.

A complex number has the form $z=x+iy$, with $x,y\in\mathbb{R}$ and $i^2=-1$. Its real and imaginary parts are $x$ and $y$, respectively.

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:complex-conjugation"}

[![A schematic for x,y\>0. Conjugation reflects a point across the real axis. The distance from zero is \\lvert z\\rvert=\\sqrt\{x^2+y^2\} for both points.](/notes/linear-algebra/figures/complex-conjugation.svg){.tikz-diagram}](/notes/linear-algebra/figures/complex-conjugation.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 7.4. A schematic for $x,y>0$. Conjugation reflects a point across the real axis. The distance from zero is $\lvert z\rvert=\sqrt{x^2+y^2}$ for both points.

:::

::::

:::::

Powers of $i$ repeat with period four,

$$
i^2=-1,\qquad i^3=-i,\qquad i^4=1,\qquad i^5=i,\qquad i^6=-1.
$$

The conjugate of $z$ is $\overline z=x-iy$, and its modulus is the nonnegative number satisfying

$$
|z|^2=z\overline z=x^2+y^2.
$$

For $z\ne0$,

$$
\frac1z=\frac{\overline z}{|z|^2}=\frac{x-iy}{x^2+y^2}.
$$

More generally, division by $w\ne0$ can be written as $z/w=z\overline w/|w|^2$.

[Figure 7.4](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#fig:linear-algebra-i:complex-conjugation) identifies $z$ with the point $(x,y)$ and its conjugate with $(x,-y)$.

### Returning to the rotation example {id="returning-to-the-rotation-example"}

Regard the real matrix $B$ from [Example 7.3.5](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#ex:linear-algebra-i:rotation-no-real-eigenvalue) as a matrix acting on $\mathbb{C}^2$. For $\lambda=i$, its kernel equations give

$$
v^1-iv^2=0\quad\Longleftrightarrow\quad v^2=-iv^1.
$$

For $\lambda=-i$, they give $v^1+iv^2=0$. Consequently,

$$
\begin{aligned}
    E_i(B)&=\left\{\begin{bmatrix}t\\-it\end{bmatrix}\;\middle|\;t\in\mathbb{C}\right\},\\
    E_{-i}(B)&=\left\{\begin{bmatrix}t\\it\end{bmatrix}\;\middle|\;t\in\mathbb{C}\right\}.
  \end{aligned}
$$

In each case, the eigenvectors are obtained by taking $t\ne0$.

::statement{key="hw06:rotation-eigenvalues"}

### Roots and multiplicities {id="roots-and-multiplicities"}

:::div{id="thm:linear-algebra-i:fundamental-theorem-of-algebra" class="result theorem"}

**Theorem 7.4.2 (Fundamental theorem of algebra).** Every complex polynomial of degree $n\ge1$,

$$
p(z)=a_nz^n+\cdots+a_0,\qquad a_n\ne0,
$$

factors as

$$
p(z)=a_n(z-\lambda_1)\cdots(z-\lambda_n),
$$

where $\lambda_1,\ldots,\lambda_n\in\mathbb{C}$, with repetitions allowed.

:::

::::div{class="pending-review"}

The proof uses elementary real-analysis facts. Polynomials and their moduli are continuous, and a continuous real-valued function on a closed bounded disc in $\mathbb{R}^2$ attains its minimum. We also use the polar description of a nonzero complex number and the trigonometric angle-addition formulas.

:::div{class="proof"}

*Proof.* We first prove that every nonconstant complex polynomial has a root. Write $C=\sum_{j=0}^{n-1}|a_j|$. For $|z|\ge1$, the triangle inequality gives

$$
|p(z)|\ge |a_n||z|^n-C|z|^{n-1}.
$$

If also $|z|\ge 2C/|a_n|$, then

$$
|p(z)|\ge \tfrac12|a_n||z|^n.
$$

Consequently, $|p(z)|$ tends to infinity as $|z|$ tends to infinity. Choose $R$ large enough that $|p(z)|>|p(0)|$ whenever $|z|>R$. On the closed disc $|z|\le R$, continuity gives a point $z_0$ where $|p|$ attains its minimum. This minimum is at most $|p(0)|$, so no point outside the disc has a smaller value. Thus $z_0$ is a global minimum of $|p|$.

Suppose $c=p(z_0)\ne0$. Expanding the polynomial around $z_0$ and dividing by $c$, write

$$
\frac{p(z_0+w)}{c}
      =1+d_kw^k+d_{k+1}w^{k+1}+\cdots+d_nw^n,
$$

where $k\ge1$ is the first index with $d_k\ne0$. Such an index exists because $p$ is not constant. Set $\alpha=|d_k|>0$, and write $d_k=\alpha(\cos\theta+i\sin\theta)$. The unit complex number

$$
u=\cos\frac{\pi-\theta}{k}
        +i\sin\frac{\pi-\theta}{k}
$$

satisfies $d_ku^k=-\alpha$. Indeed, repeated multiplication and the angle-addition formulas give $u^k=\cos(\pi-\theta)+i\sin(\pi-\theta)$.

Put $K=\sum_{j=k+1}^n|d_j|$, taking $K=0$ if the sum is empty. For $0<t\le1$, the remaining terms satisfy

$$
\left|\sum_{j=k+1}^n d_j(tu)^j\right|
      \le Kt^{k+1}.
$$

Choose $t>0$ so small that $t\le1$, $\alpha t^k<1$, and $Kt\le\alpha/2$. These conditions can be met because $\alpha>0$ and $K$ is a fixed nonnegative number. The first nonconstant term is now a negative real number, and the remainder is too small to cancel its decrease. More precisely,

$$
\begin{aligned}
      \left|\frac{p(z_0+tu)}{c}\right|
        &\le |1-\alpha t^k|+Kt^{k+1}\\
        &=1-\alpha t^k+Kt^{k+1}\\
        &\le1-\tfrac12\alpha t^k<1.
    \end{aligned}
$$

Hence $|p(z_0+tu)|<|c|=|p(z_0)|$, contradicting the global minimality of $z_0$. Therefore $p(z_0)=0$, proving that a root exists.

Let $\lambda_1$ be a root. The identity

$$
z^j-\lambda_1^j
      =(z-\lambda_1)
        (z^{j-1}+z^{j-2}\lambda_1+\cdots+\lambda_1^{j-1})
$$

shows that $p(z)=p(z)-p(\lambda_1)$ is divisible by $z-\lambda_1$. The quotient has degree $n-1$ and leading coefficient $a_n$. If it is nonconstant, apply the root argument to the quotient and factor again. Repeating reduces the degree by one at each step and leaves the constant $a_n$. This gives

$$
p(z)=a_n(z-\lambda_1)\cdots(z-\lambda_n).
$$

The same root may occur at more than one step, so repetitions are allowed. ◻

:::

::::

The characteristic polynomial of an $n$-by-$n$ complex matrix therefore has $n$ roots counted with multiplicity. The multiplicity of $\lambda$ is the number of factors equal to $(z-\lambda)$. The $n$ eigenvalues need not be distinct. Since the convention here is $p_M(z)=\det(M-zI)$, its factorization has leading coefficient $(-1)^n$.

:::div{id="web:sections/linear-algebra-i/07-eigenvalues-and-diagonalization/04-complex-eigenvalues:5858" class="result example"}

**Example 7.4.3.** For the identity matrix on $\mathbb F^2$,

$$
p_I(x)=(1-x)^2,\qquad E_1(I)=\mathbb F^2.
$$

Its only eigenvalue is $1$, with multiplicity two, and every nonzero vector is an eigenvector.

In contrast, let

$$
J=\begin{bmatrix}1&1\\0&1\end{bmatrix}.
$$

It has the same characteristic polynomial, but

$$
(J-I)\begin{bmatrix}v^1\\v^2\end{bmatrix}
      =\begin{bmatrix}v^2\\0\end{bmatrix}.
$$

Hence

$$
E_1(J)=\left\{\begin{bmatrix}t\\0\end{bmatrix}\;\middle|\;t\in\mathbb F\right\},
$$

which has dimension one.

:::

The different actions of $I$ and $J$ over $\mathbb{R}$ are pictured in [Figure 7.5](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#fig:linear-algebra-i:identity-and-shear-eigenspaces). The matrix $J$ is the shear studied in [§ 2.1](/notes/linear-algebra/linear-algebra-i/matrices-and-vector-coordinates/#sec:linear-algebra-i:matrix-multiplication). Its columns describe the whole grid transformation, while its eigenspace identifies the vectors that the shear fixes.

::::figure{id="fig:linear-algebra-i:identity-and-shear-eigenspaces"}

[![The identity fixes every vector. The shear J fixes only the horizontal axis, although both characteristic polynomials are (1-x)^2. The dashed unit square on the right shows the shape before applying J. The shaded parallelogram is its image.](/notes/linear-algebra/figures/identity-and-shear-eigenspaces.svg){.tikz-diagram}](/notes/linear-algebra/figures/identity-and-shear-eigenspaces.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 7.5. The identity fixes every vector. The shear $J$ fixes only the horizontal axis, although both characteristic polynomials are $(1-x)^2$. The dashed unit square on the right shows the shape before applying $J$. The shaded parallelogram is its image.

:::

::::

:::div{id="thm:linear-algebra-i:eigenspace-multiplicity" class="result proposition"}

**Proposition 7.4.4 (Eigenspace dimension and root multiplicity).** If $\lambda$ is an eigenvalue of a complex matrix and has multiplicity $m_\lambda$ in its characteristic polynomial, then

$$
1\le\dim E_\lambda\le m_\lambda.
$$

:::

::::div{class="pending-review"}

:::div{class="proof"}

*Proof.* Let $M$ be the given $n$-by-$n$ matrix, and write $r=\dim E_\lambda(M)$. Since $\lambda$ is an eigenvalue, its eigenspace contains a nonzero vector, so $r\ge1$. Choose a basis $(v_1,\ldots,v_r)$ of this eigenspace and extend it to a basis of $\mathbb{C}^n$, using [Proposition 1.2.6](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:basis-extension). The matrix in this new basis has the same characteristic polynomial as $M$, since similarity preserves characteristic polynomials.

If $r=n$, every vector of this basis is multiplied by $\lambda$. The representing matrix is $\lambda I_n$, so its characteristic polynomial is $(\lambda-x)^n$. Thus $m_\lambda=n=r$.

Suppose $r<n$. Since $Mv_j=\lambda v_j$ for $j\le r$, the matrix in the extended basis has the form

$$
T=\begin{bmatrix}\lambda I_r&B\\0&C\end{bmatrix},
    \qquad C\in\mathrm M_{(n-r)\times(n-r)}(\mathbb{C}).
$$

In the permutation expansion of $\det(T-xI)$ from [Equation 5.4](/notes/linear-algebra/linear-algebra-i/determinants/#eq:linear-algebra-i:determinant-permutation-formula), column $j\le r$ has only one possibly nonzero entry, in row $j$. Every contributing permutation must therefore fix those first $r$ indices. The remaining factors select one entry from each row and column of $C-xI$. Their permutation has the same sign as the full permutation, since a decomposition into transpositions of the last $n-r$ indices also decomposes the full permutation. Consequently,

$$
p_M(x)=p_T(x)=(\lambda-x)^r\det(C-xI).
$$

The factor $(\lambda-x)^r=(-1)^r(x-\lambda)^r$ shows that $\lambda$ has root multiplicity at least $r$. Hence $1\le\dim E_\lambda(M)\le m_\lambda$, as claimed. ◻

:::

::::

::statement{key="hw06:eigenvalue-true-or-false"}

## 7.5 Diagonalization {id="sec:linear-algebra-i:diagonalization"}

An eigenvector provides one direction on which a map acts by scaling. If enough such vectors form a basis, every input can be assembled from these directions, and the action becomes a separate scalar multiplication on each coordinate. Diagonalization expresses this choice of coordinates.

:::div{id="web:sections/linear-algebra-i/07-eigenvalues-and-diagonalization/05-diagonalization:362" class="result definition"}

**Definition 7.5.1.** A square matrix $M$ is diagonalizable over $\mathbb F$ if it is similar to a diagonal matrix. Equivalently, there exist an invertible matrix $S$ and a diagonal matrix $D$ such that

$$
M=SDS^{-1}.
$$

:::

:::div{id="thm:linear-algebra-i:diagonalization-eigenbasis" class="result theorem"}

**Theorem 7.5.2 (Diagonalization and eigenbases).** A matrix $M\in\mathbb F^{n\times n}$ is diagonalizable if and only if $\mathbb F^n$ has a basis of eigenvectors of $M$.

:::

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:diagonalization-coordinates"}

[![The top row acts in eigenbasis coordinates. The bottom acts in the original coordinates. Both routes give MSc=SDc.](/notes/linear-algebra/figures/diagonalization-coordinates.svg){.tikz-diagram}](/notes/linear-algebra/figures/diagonalization-coordinates.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 7.6. The top row acts in eigenbasis coordinates. The bottom acts in the original coordinates. Both routes give $MSc=SDc$.

:::

::::

:::::

:::div{class="proof"}

*Proof.* Suppose $M=SDS^{-1}$, where $D$ has diagonal entries $\lambda_1,\ldots,\lambda_n$. Let $c_k=Se_k$ be column $k$ of $S$. Since $S$ is invertible, its columns form a basis, and

$$
\begin{aligned}
    Mc_k&=MSe_k=SDS^{-1}Se_k\\
      &=SDe_k=S(\lambda_ke_k)=\lambda_kc_k.
  
\end{aligned}
$$

Thus each column is an eigenvector.

Conversely, suppose $(b_1,\ldots,b_n)$ is a basis of eigenvectors, with $Mb_k=\lambda_kb_k$. Let $S$ have these basis vectors as columns, and let $D$ have the corresponding eigenvalues on its diagonal. The column equations say $MS=SD$. Since $S$ is invertible, $M=SDS^{-1}$. ◻

:::

The identity $MS=SD$ is visualized in [Figure 7.6](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#fig:linear-algebra-i:diagonalization-coordinates). If $c$ is an eigenbasis coordinate column, $S$ reconstructs the vector $Sc$, while $D$ multiplies each coordinate by its eigenvalue.

:::div{id="web:sections/linear-algebra-i/07-eigenvalues-and-diagonalization/05-diagonalization:2115" class="result definition"}

**Definition 7.5.3.** An endomorphism $L:V\to V$ is diagonalizable if $V$ has a basis $(e_1,\ldots,e_n)$ of eigenvectors of $L$.

:::

For such a basis,

$$
L(e_k)=\lambda_ke_k,\qquad
  L(E)=E\begin{bmatrix}
    \lambda_1&0&\cdots&0\\
    0&\lambda_2&\cdots&0\\
    \vdots&\vdots&\ddots&\vdots\\
    0&0&\cdots&\lambda_n
  \end{bmatrix}.
$$

Equivalently, the matrix representing $L$ in any basis is similar to a diagonal matrix.

### Failure of diagonalization {id="failure-of-diagonalization"}

:::div{id="web:sections/linear-algebra-i/07-eigenvalues-and-diagonalization/05-diagonalization:2610" class="result example"}

**Example 7.5.4.** Let $(e_1,e_2)$ be a basis of $V$, and define

$$
L(e_1)=e_2,\qquad L(e_2)=0.
$$

For $v=ae_1+be_2$, $L(v)=ae_2$. The eigenvector equation is

$$
ae_2=\lambda(ae_1+be_2).
$$

If $\lambda\ne0$, comparison of coefficients gives $a=0$ and then $b=0$, so there is no nonzero eigenvector. For $\lambda=0$, it gives $a=0$. Thus the only eigenvalue is zero and its eigenspace is $\operatorname{span}\{e_2\}$. It cannot provide a basis of $V$, so $L$ is not diagonalizable.

:::

The nonzero matrix $N$ in [Example 7.2.4](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#ex:linear-algebra-i:same-polynomial-not-similar) similarly has only the eigenvalue zero and a one-dimensional eigenspace, so it is not diagonalizable. The rotation matrix in [Example 7.3.5](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#ex:linear-algebra-i:rotation-no-real-eigenvalue) is not diagonalizable over $\mathbb{R}$, since it has no real eigenvectors.

::statement{key="hw06:nilpotent-eigenvalues"}

## 7.6 Direct sums and diagonalization criteria {id="sec:linear-algebra-i:direct-sums"}

### Transversal subspaces {id="transversal-subspaces"}

To assemble an eigenbasis, we must combine vectors from several eigenspaces without introducing a dependence. Direct sums express the corresponding idea for subspaces, requiring every vector to have a unique decomposition into components from the summands.

Suppose $S,T$ are subspaces of $V$ and $S\cap T=\{0\}$. If $s\in S$, $t\in T$, and $s-t=0$, then $s=t\in S\cap T$, so both vectors are zero.

::statement{key="hw07:disjoint-subspaces-independence"}

For a family $S_1,\ldots,S_k$, write

$$
S_1+\cdots+S_k
    =\{s_1+\cdots+s_k\mid s_j\in S_j\}.
$$

This is the span of the subspaces together.

:::div{id="web:sections/linear-algebra-i/07-eigenvalues-and-diagonalization/06-direct-sums:756" class="result definition"}

**Definition 7.6.2.** A family of subspaces $S_1,\ldots,S_k$ is transversal if

$$
S_j\cap\sum_{i\ne j}S_i=\{0\}\qquad\text{for every }j.
$$

:::

The coordinate axes are transversal. In contrast, three distinct lines through zero in a plane are not transversal, as illustrated in [Figure 7.7](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#fig:linear-algebra-i:three-lines-not-transversal).

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:three-lines-not-transversal"}

[![A real-plane schematic. Each pair of distinct lines meets only at zero, but any two span the plane. Thus S\_3\\cap(S\_1+S\_2)=S\_3\\ne\\\{0\\\}.](/notes/linear-algebra/figures/three-lines-not-transversal.svg){.tikz-diagram}](/notes/linear-algebra/figures/three-lines-not-transversal.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 7.7. A real-plane schematic. Each pair of distinct lines meets only at zero, but any two span the plane. Thus $S_3\cap(S_1+S_2)=S_3\ne\{0\}$.

:::

::::

:::::

:::div{id="thm:linear-algebra-i:transversal-unique-components" class="result proposition"}

**Proposition 7.6.3 (Uniqueness of components).** Let $S_1,\ldots,S_k$ be transversal, with $s_j\in S_j$. If $s_1+\cdots+s_k=0$, then every $s_j=0$. Consequently, if also $t_j\in S_j$ and $s_1+\cdots+s_k=t_1+\cdots+t_k$, then $s_j=t_j$ for every $j$.

:::

:::div{class="proof"}

*Proof.* Isolate the last component in the zero relation. It satisfies

$$
s_k=-\sum_{j=1}^{k-1}s_j
      \in S_k\cap(S_1+\cdots+S_{k-1})=\{0\}.
$$

Hence $s_k=0$. Repeating with the remaining components gives $s_1=\cdots=s_k=0$.

For two equal sums, subtract them. Each $s_j-t_j$ belongs to $S_j$, and their sum is zero. The first conclusion gives $s_j-t_j=0$ for every $j$. ◻

:::

:::div{id="web:sections/linear-algebra-i/07-eigenvalues-and-diagonalization/06-direct-sums:2259" class="result definition"}

**Definition 7.6.4.** If $S_1,\ldots,S_k$ are transversal and $S_1+\cdots+S_k=V$, then $V$ is their direct sum, written

$$
V=S_1\oplus\cdots\oplus S_k=\bigoplus_{j=1}^k S_j.
$$

:::

The spanning condition guarantees that each vector has a decomposition, and transversality guarantees that its components are unique. These are the existence and uniqueness roles played by spanning and independence for basis coordinates in [§ 1.2](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#sec:linear-algebra-i:linear-combinations-and-bases).

### Combining bases {id="combining-bases"}

For two complementary lines in $\mathbb{R}^2$, each vector has one component on each line, as in [Figure 7.8](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#fig:linear-algebra-i:direct-sum-components).

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:direct-sum-components"}

[![A real-plane schematic of V=S\\oplus T. The decomposition v=s+t, with s\\in S and t\\in T, is unique. The summands need not be perpendicular.](/notes/linear-algebra/figures/direct-sum-components.svg){.tikz-diagram}](/notes/linear-algebra/figures/direct-sum-components.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 7.8. A real-plane schematic of $V=S\oplus T$. The decomposition $v=s+t$, with $s\in S$ and $t\in T$, is unique. The summands need not be perpendicular.

:::

::::

:::::

:::div{id="thm:linear-algebra-i:direct-sum-bases" class="result proposition"}

**Proposition 7.6.5 (Bases of a direct sum).** If $V=S_1\oplus\cdots\oplus S_k$, concatenating a basis of each $S_j$ gives a basis of $V$. In particular,

$$
\dim V=\sum_{j=1}^k\dim S_j.
$$

:::

:::div{class="proof"}

*Proof.* Let $(e_{j,1},\ldots,e_{j,n_j})$ be a basis of $S_j$. Suppose a linear combination of all these vectors is zero,

$$
\sum_{j=1}^k\sum_{\ell=1}^{n_j}a_{j,\ell}e_{j,\ell}=0.
$$

Group the terms into vectors $s_j=\sum_{\ell=1}^{n_j}a_{j,\ell}e_{j,\ell}\in S_j$. Transversality gives $s_1=\cdots=s_k=0$. Since each group is a linear combination of a basis of $S_j$, all its coefficients $a_{j,\ell}$ are zero. Thus the concatenated list is independent.

The subspaces together span $V$, and the basis vectors in each group span its subspace. Hence the concatenated list spans $V$. It is therefore a basis, with $n_1+\cdots+n_k$ vectors. ◻

:::

### Transversality of distinct eigenspaces {id="transversality-of-distinct-eigenspaces"}

:::div{id="thm:linear-algebra-i:distinct-eigenspaces-transversal" class="result theorem"}

**Theorem 7.6.6 (Transversal eigenspaces).** Let $\lambda_1,\ldots,\lambda_k$ be distinct eigenvalues of $L:V\to V$. Their eigenspaces $E_{\lambda_1}(L),\ldots,E_{\lambda_k}(L)$ are transversal.

:::

:::div{class="proof"}

*Proof.* We show that a relation

$$
v_1+\cdots+v_k=0,\qquad v_j\in E_{\lambda_j}(L),
$$

forces every $v_j=0$. The argument proceeds by induction on the number of eigenspaces. For one eigenspace, the relation already says $v_1=0$.

Suppose the result holds for $k-1$ distinct eigenspaces. Apply $L$ to the relation and subtract $\lambda_k$ times the original relation. Since $L(v_j)=\lambda_jv_j$, this gives

$$
\sum_{j=1}^{k-1}(\lambda_j-\lambda_k)v_j=0.
$$

The $k$-th term has disappeared. Each remaining vector $(\lambda_j-\lambda_k)v_j$ still belongs to $E_{\lambda_j}(L)$. By the induction hypothesis, all these vectors are zero. The scalars $\lambda_j-\lambda_k$ are nonzero, so $v_j=0$ for $j<k$. The original relation now gives $v_k=0$.

A vector in one eigenspace that is a sum of vectors in the others produces such a zero relation by moving all terms to one side. The result just proved forces that vector to be zero. This is transversality. ◻

:::

### Criteria for an eigenbasis {id="criteria-for-an-eigenbasis"}

:::div{id="thm:linear-algebra-i:spanning-eigenspaces-diagonalizable" class="result theorem"}

**Theorem 7.6.7 (Spanning eigenspaces and diagonalization).** If $\lambda_1,\ldots,\lambda_k$ are eigenvalues of $L:V\to V$ and

$$
E_{\lambda_1}(L)+\cdots+E_{\lambda_k}(L)=V,
$$

then $L$ is diagonalizable.

:::

:::div{class="proof"}

*Proof.* Keep one copy of each distinct eigenspace in the sum. By [Theorem 7.6.6](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#thm:linear-algebra-i:distinct-eigenspaces-transversal), these eigenspaces are transversal, so the spanning hypothesis gives a direct-sum decomposition of $V$. Choose a basis in each eigenspace. By [Proposition 7.6.5](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#thm:linear-algebra-i:direct-sum-bases), their concatenation is a basis of $V$. Every vector in this basis is an eigenvector. Thus $L$ is diagonalizable. ◻

:::

The converse also holds. An endomorphism is diagonalizable exactly when its eigenspaces span $V$.

::::div{class="pending-review"}

:::div{class="proof"}

*Proof of the converse.* Suppose $L$ is diagonalizable, and choose an eigenbasis $(e_1,\ldots,e_n)$ of $V$. Each $e_j$ belongs to the eigenspace of its eigenvalue. Every vector in $V$ is a linear combination of these basis vectors, so every vector belongs to the sum of those eigenspaces. The eigenspaces therefore span $V$. ◻

:::

::::

:::div{id="thm:linear-algebra-i:distinct-eigenvalues-diagonalizable" class="result corollary"}

**Corollary 7.6.8 (Distinct eigenvalues and diagonalization).** If $\dim V=n$ and $L:V\to V$ has $n$ distinct eigenvalues in $\mathbb F$, then $L$ is diagonalizable over $\mathbb F$. In particular, a two-by-two matrix with two distinct eigenvalues in $\mathbb F$ is diagonalizable over $\mathbb F$.

:::

::::div{class="pending-review"}

:::div{class="proof"}

*Proof.* If $n=0$, the empty basis is already an eigenbasis. Suppose $n\ge1$, and let $\lambda_1,\ldots,\lambda_n$ be the distinct eigenvalues. Choose $v_j\ne0$ in each $E_{\lambda_j}(L)$. If

$$
a_1v_1+\cdots+a_nv_n=0,
$$

then $a_jv_j\in E_{\lambda_j}(L)$ for every $j$. By [Theorem 7.6.6](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#thm:linear-algebra-i:distinct-eigenspaces-transversal) and [Proposition 7.6.3](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#thm:linear-algebra-i:transversal-unique-components), every $a_jv_j=0$. Since $v_j\ne0$, every $a_j=0$. Thus $(v_1,\ldots,v_n)$ is independent.

By [Proposition 1.2.6](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:basis-extension), this list extends to a basis of $V$. A basis of the $n$-dimensional space has $n$ vectors, so no additional vectors are needed. The chosen list is an eigenbasis, and $L$ is diagonalizable over $\mathbb F$. Taking $n=2$ gives the two-by-two conclusion. ◻

:::

::::

The criterion does not require computing the dimensions of the individual eigenspaces. When the eigenspaces do not span the whole space, there is no eigenbasis. The nonzero nilpotent matrix in [Example 7.2.4](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#ex:linear-algebra-i:same-polynomial-not-similar) is an example.

### Approximation by diagonalizable matrices {id="approximation-by-diagonalizable-matrices"}

:::div{id="thm:linear-algebra-i:density-of-diagonalizable-complex-matrices" class="result proposition"}

**Proposition 7.6.9 (Density of diagonalizable complex matrices).** The matrices diagonalizable over $\mathbb{C}$ are dense in $\mathrm M_{n\times n}(\mathbb{C})$.

:::

Here density means that every complex matrix can be approximated arbitrarily closely, entry by entry, by matrices diagonalizable over $\mathbb{C}$.

::::div{class="pending-review"}

:::div{class="proof"}

*Proof.* The case $n=0$ has only the empty matrix, which is already diagonal. Suppose $n\ge1$. We first show by induction that every complex $n$-by-$n$ matrix is similar to an upper triangular matrix. The claim holds for $n=1$. For $n>1$, the characteristic polynomial has a root by [Theorem 7.4.2](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#thm:linear-algebra-i:fundamental-theorem-of-algebra), so $M$ has an eigenvalue $\lambda$ and a nonzero eigenvector $v_1$. Extend $v_1$ to a basis by [Proposition 1.2.6](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:basis-extension), and let $P$ be its basis matrix. The first column of $P^{-1}MP$ is $(\lambda,0,\ldots,0)^T$, giving

$$
P^{-1}MP=\begin{bmatrix}\lambda&b\\0&C\end{bmatrix}.
$$

The induction hypothesis gives an invertible $Q$ such that $Q^{-1}CQ=U$ is upper triangular. Set

$$
H=P\begin{bmatrix}1&0\\0&Q\end{bmatrix}.
$$

Both factors are invertible, and block multiplication gives

$$
T=H^{-1}MH=\begin{bmatrix}\lambda&bQ\\0&U\end{bmatrix}.
$$

This matrix is upper triangular, completing the induction.

Fix $M=HTH^{-1}$ in this form, and let $\varepsilon>0$ be an arbitrary prescribed error in each entry. The number

$$
K=\max_{1\le i,j\le n}
      \sum_{k=1}^n |H^i_k|\,|(H^{-1})^k_j|
$$

is finite and nonnegative. Put $\delta=\varepsilon/(K+1)>0$. Write the diagonal entries of $T$ as $\mu_1,\ldots,\mu_n$. Choose real numbers $\eta_1,\ldots,\eta_n$, each with $0<\eta_j<\delta$, so that the numbers $\mu_j+\eta_j$ are all distinct. This can be done successively. At step $j$, equality with one of the previous $j-1$ values forbids at most $j-1$ choices for $\eta_j$. The $n$ candidates

$$
\frac{\delta}{n+1},\frac{2\delta}{n+1},\ldots,
      \frac{n\delta}{n+1}
$$

all lie in $(0,\delta)$, so at least one candidate is permitted.

Define

$$
\Delta=\operatorname{diag}(\eta_1,\ldots,\eta_n),
    \qquad T_\delta=T+\Delta.
$$

This is upper triangular with distinct diagonal entries. In the permutation expansion of $\det(T_\delta-xI)$, a nonzero term requires $\sigma(j)\le j$ for every column $j$. This forces $\sigma(1)=1$, then $\sigma(2)=2$, and successively $\sigma(j)=j$ for all $j$. Thus only the identity permutation contributes, and the characteristic polynomial is $\prod_{j=1}^n(\mu_j+\eta_j-x)$. Thus $T_\delta$ has $n$ distinct eigenvalues. By [Corollary 7.6.8](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#thm:linear-algebra-i:distinct-eigenvalues-diagonalizable), $T_\delta$ is diagonalizable. Therefore $N=HT_\delta H^{-1}$ is also diagonalizable. Indeed, if $T_\delta=SDS^{-1}$, then $N=(HS)D(HS)^{-1}$.

Finally, $N-M=H\Delta H^{-1}$. For every pair of indices,

$$
\begin{aligned}
      |(N-M)^i_j|
        &=\left|\sum_{k=1}^n H^i_k\eta_k(H^{-1})^k_j\right|\\
        &\le\sum_{k=1}^n |H^i_k|\,|\eta_k|\,|(H^{-1})^k_j|\\
        &\le\delta K<\varepsilon.
    \end{aligned}
$$

Thus a diagonalizable complex matrix lies within every prescribed entrywise error of $M$. This proves density. ◻

:::

::::
