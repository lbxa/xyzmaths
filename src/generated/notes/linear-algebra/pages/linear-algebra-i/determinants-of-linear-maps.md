---
title: "Determinants of linear maps"
group: "Linear Algebra I"
order: 12
part: "Part I · Linear Algebra I"
page: "79"
outline: [{"id": "sec:linear-algebra-i:pullbacks-and-volume-functions", "title": "6.1 Pullbacks and volume functions", "level": 2}, {"id": "pullback-by-composition", "title": "Pullback by composition", "level": 3}, {"id": "the-space-of-top-degree-forms", "title": "The space of top-degree forms", "level": 3}, {"id": "sec:linear-algebra-i:determinants-of-endomorphisms", "title": "6.2 Determinants of endomorphisms", "level": 2}, {"id": "agreement-with-the-representing-matrix", "title": "Agreement with the representing matrix", "level": 3}, {"id": "computations-using-multilinearity", "title": "Computations using multilinearity", "level": 3}, {"id": "sec:linear-algebra-i:multiplicativity-and-singularity", "title": "6.3 Multiplicativity and singularity", "level": 2}, {"id": "composition-of-endomorphisms", "title": "Composition of endomorphisms", "level": 3}, {"id": "products-of-matrices", "title": "Products of matrices", "level": 3}, {"id": "invertibility-and-zero-determinant", "title": "Invertibility and zero determinant", "level": 3}, {"id": "sec:linear-algebra-i:transposes-and-linear-systems", "title": "6.4 Transposes and linear systems", "level": 2}, {"id": "transpose", "title": "Transpose", "level": 3}, {"id": "square-systems-of-equations", "title": "Square systems of equations", "level": 3}, {"id": "sec:linear-algebra-i:determinants-between-spaces", "title": "6.5 Maps between different spaces", "level": 2}]
---

# Chapter 6. Determinants of linear maps {id="ch:linear-algebra-i:determinants-of-linear-maps"}

The determinant of a matrix describes how its linear map acts on volume functions. Pullbacks make this description independent of a choice of basis and explain why determinants multiply under composition. The key fact is that top-degree volume functions form a one-dimensional vector space. An endomorphism therefore acts on that space by a single scalar.

Unless stated otherwise, the vector spaces in this chapter are finite dimensional over $\mathbb F=\mathbb{R}$ or $\mathbb{C}$. The coordinate expansions of [§ 5.3](/notes/linear-algebra/linear-algebra-i/determinants/#sec:linear-algebra-i:antisymmetric-multilinear-functions) apply over both fields.

## 6.1 Pullbacks and volume functions {id="sec:linear-algebra-i:pullbacks-and-volume-functions"}

### Pullback by composition {id="pullback-by-composition"}

Let $X,Y$ be sets and let $F:X\to Y$ be a map. Write $\mathcal F(X,\mathbb F)$ for the scalar-valued functions on $X$. Every function $f:Y\to\mathbb F$ gives a function on $X$ by composition,

$$
F^*f=f\circ F,\qquad (F^*f)(x)=f(F(x)).
$$

This construction is called pullback. Its direction is opposite to that of the original map,

$$
F:X\longrightarrow Y,\qquad
  F^*:\mathcal F(Y,\mathbb F)\longrightarrow\mathcal F(X,\mathbb F).
$$

[Figure 6.1](/notes/linear-algebra/linear-algebra-i/determinants-of-linear-maps/#fig:linear-algebra-i:pullback-composition) separates the path of an input from the direction in which a function is pulled back.

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:pullback-composition"}

[![In the triangle, start in X, apply F, then evaluate f. Below, F^\* takes the function f on Y back to the function F^\*f on X.](/notes/linear-algebra/figures/pullback-composition.svg){.tikz-diagram}](/notes/linear-algebra/figures/pullback-composition.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 6.1. In the triangle, start in $X$, apply $F$, then evaluate $f$. Below, $F^*$ takes the function $f$ on $Y$ back to the function $F^*f$ on $X$.

:::

::::

:::::

For a vector space $V$, its linear dual $V^*$ consists of the linear functions $V\to\mathbb F$. More generally, write $\Lambda^k V^*$ for the vector space of antisymmetric $k$-linear functions on $V$. Here $k$ is the number of inputs. It need not equal $\dim V$. The linear functionals of [§ 3.2](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#sec:linear-algebra-i:linear-functions-and-maps) are the one-input case.

:::div{id="web:sections/linear-algebra-i/06-determinants-of-linear-maps/01-pullbacks-and-volume-functions:1462" class="result definition"}

**Definition 6.1.1.** Let $L:V\to W$ be linear and let $A\in\Lambda^k W^*$. The pullback of $A$ by $L$ is the function

$$
(L^*A)(v_1,\ldots,v_k)
      =A(L(v_1),\ldots,L(v_k)).
$$

:::

Linearity of $L$ preserves multilinearity in each input, and interchanging two inputs interchanges the corresponding inputs of $A$. Thus $L^*A$ is again antisymmetric and multilinear. The induced map

$$
L^*:\Lambda^k W^*\longrightarrow\Lambda^k V^*
$$

is linear in $A$.

### The space of top-degree forms {id="the-space-of-top-degree-forms"}

Suppose $\dim V=n$. The functions in $\Lambda^n V^*$ are the top-degree forms on $V$. Over $\mathbb{R}$, a nonzero such function gives an oriented volume function.

:::div{id="thm:linear-algebra-i:top-degree-forms" class="result proposition"}

**Proposition 6.1.2 (The space of top-degree forms).** The space $\Lambda^n V^*$ has dimension one. If $A\in\Lambda^n V^*\setminus\{0\}$, then every $B\in\Lambda^n V^*$ is a unique scalar multiple of $A$. For any ordered basis $(e_1,\ldots,e_n)$, this scalar is

$$
B=bA,\qquad b=\frac{B(e_1,\ldots,e_n)}{A(e_1,\ldots,e_n)}.
$$

:::

:::div{class="proof"}

*Proof.* The normalized-volume construction supplies a nonzero top-degree form. The coordinate expansion in [Equation 5.3](/notes/linear-algebra/linear-algebra-i/determinants/#eq:linear-algebra-i:antisymmetric-basis-expansion) determines each top-degree form by its value on the ordered basis. Since $A\ne0$, its basis value cannot be zero. The displayed choice of $b$ makes $B$ and $bA$ agree on that basis, so the same expansion gives $B=bA$. Thus the single nonzero vector $A$ spans $\Lambda^n V^*$. Since it is nonzero, it is also independent, so $\{A\}$ is a basis and the dimension is one. ◻

:::

## 6.2 Determinants of endomorphisms {id="sec:linear-algebra-i:determinants-of-endomorphisms"}

An endomorphism is a linear map from a vector space to itself. If $U$ is one-dimensional, every linear map $F:U\to U$ is multiplication by a scalar. For $L:V\to V$, with $\dim V=n$, apply this fact to

$$
L^*:\Lambda^n V^*\longrightarrow\Lambda^n V^*.
$$

::::div{id="web:sections/linear-algebra-i/06-determinants-of-linear-maps/02-determinants-of-endomorphisms:365" class="result definition"}

**Definition 6.2.1.** The determinant of $L:V\to V$ is the unique scalar $\det L$ for which

:::div{id="eq:linear-algebra-i:determinant-pullback" class="equation"}

$$
L^*A=(\det L)A\qquad\text{for every \(A\in\Lambda^n V^*\)}.\tag{6.1}
$$

:::

::::

Equivalently, for all $v_1,\ldots,v_n\in V$,

$$
A(L(v_1),\ldots,L(v_n))=(\det L)A(v_1,\ldots,v_n).
$$

The real two-dimensional case is visualized in [Figure 6.2](/notes/linear-algebra/linear-algebra-i/determinants-of-linear-maps/#fig:linear-algebra-i:determinant-linear-map).

::::figure{id="fig:linear-algebra-i:determinant-linear-map"}

[![A real-plane schematic. Applying L to both edges multiplies their oriented area by \\det L. The drawing shows positive areas. A negative determinant reverses orientation.](/notes/linear-algebra/figures/determinant-linear-map.svg){.tikz-diagram}](/notes/linear-algebra/figures/determinant-linear-map.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 6.2. A real-plane schematic. Applying $L$ to both edges multiplies their oriented area by $\det L$. The drawing shows positive areas. A negative determinant reverses orientation.

:::

::::

Choose an ordered basis $E=(e_1,\ldots,e_n)$ and normalize $A$ so that

$$
A(e_1,\ldots,e_n)=1.
$$

Then

$$
\det L=A(L(e_1),\ldots,L(e_n)).
$$

For an unnormalized nonzero $A$, the formula is

$$
\det L=\frac{A(L(e_1),\ldots,L(e_n))}{A(e_1,\ldots,e_n)}.
$$

### Agreement with the representing matrix {id="agreement-with-the-representing-matrix"}

:::div{id="thm:linear-algebra-i:determinant-representing-matrix" class="result proposition"}

**Proposition 6.2.2 (Determinant of a representing matrix).** If $L(E)=EM$, then $\det L=\det M$.

:::

:::div{class="proof"}

*Proof.* Write $L(e_j)=\sum_{i=1}^n e_iM^i_j$, and normalize $A$ on $E$. Expanding each input gives

$$
\begin{aligned}
    \det L
      &=A(L(e_1),\ldots,L(e_n))\\
      &=\sum_{k_1=1}^n\cdots\sum_{k_n=1}^n
        M^{k_1}_1\cdots M^{k_n}_n A(e_{k_1},\ldots,e_{k_n})\\
      &=\sum_{\sigma\in S_n}\varepsilon(\sigma)
        M^{\sigma(1)}_1\cdots M^{\sigma(n)}_n\\
      &=\det M.
  
\end{aligned}
$$

Repeated indices vanish, and each remaining basis value is the sign of its permutation, since $A(e_1,\ldots,e_n)=1$. ◻

:::

The ordered basis in this argument was arbitrary. Each representing matrix therefore has the same determinant, even though its entries can change when the basis changes. The scalar $\det L$ belongs to the map itself.

### Computations using multilinearity {id="computations-using-multilinearity"}

:::div{id="ex:linear-algebra-i:triangular-endomorphism-determinant" class="result example"}

**Example 6.2.3.** Let $(e_1,e_2,e_3)$ be a basis and suppose

$$
\begin{aligned}
      L(e_1)&=2e_1+3e_2+4e_3,\\
      L(e_2)&=5e_2-6e_3,\\
      L(e_3)&=7e_3.
    \end{aligned}
$$

Choose $A$ with $A(e_1,e_2,e_3)=1$. Starting with the last input eliminates repeated basis vectors from the earlier inputs,

$$
\begin{aligned}
    \det L
      &=A(2e_1+3e_2+4e_3,5e_2-6e_3,7e_3)\\
      &=A(2e_1+3e_2,5e_2,7e_3)\\
      &=A(2e_1,5e_2,7e_3)\\
      &=2\cdot5\cdot7\,A(e_1,e_2,e_3)=70.
  
\end{aligned}
$$

For example, the discarded term from the second input is

$$
-6A(L(e_1),e_3,7e_3)=0.
$$

After it is removed, the $3e_2$ and $4e_3$ terms in the first input also give repeated inputs.

:::

:::div{id="ex:linear-algebra-i:sparse-determinant" class="result example"}

**Example 6.2.4.** Consider

$$
M=\begin{bmatrix}
      2&0&-1&0\\
      1&3&1&5\\
      0&0&3&0\\
      2&2&1&0
    \end{bmatrix}.
$$

Its columns are

$$
\begin{aligned}
      C_1&=2e_1+e_2+2e_4,& C_2&=3e_2+2e_4,\\
      C_3&=-e_1+e_2+3e_3+e_4,& C_4&=5e_2.
    \end{aligned}
$$

Let $D$ be normalized on the standard basis. The last input eliminates the $e_2$ terms, and the second input then eliminates the $e_4$ terms. Therefore,

$$
\begin{aligned}
    \det M
      &=D(C_1,C_2,C_3,C_4)\\
      &=D(2e_1+2e_4,2e_4,-e_1+3e_3+e_4,5e_2)\\
      &=D(2e_1,2e_4,-e_1+3e_3,5e_2)\\
      &=D(2e_1,2e_4,3e_3,5e_2)\\
      &=60D(e_1,e_4,e_3,e_2)\\
      &=-60D(e_1,e_2,e_3,e_4)=-60.
  
\end{aligned}
$$

The final sign comes from interchanging the second and fourth inputs.

If the entry in row $4$, column $2$ is instead $-2$, the same calculation gives

$$
-60D(e_1,e_4,e_3,e_2)=60.
$$

:::

## 6.3 Multiplicativity and singularity {id="sec:linear-algebra-i:multiplicativity-and-singularity"}

### Composition of endomorphisms {id="composition-of-endomorphisms"}

:::div{id="thm:linear-algebra-i:determinant-composition" class="result theorem"}

**Theorem 6.3.1 (Determinant of a composition).** For linear maps $L_1,L_2:V\to V$,

$$
\det(L_2\circ L_1)=(\det L_2)(\det L_1).
$$

:::

:::div{class="proof"}

*Proof.* Choose a basis $(e_1,\ldots,e_n)$ and a top-degree form $D$ normalized by $D(e_1,\ldots,e_n)=1$. Applying [Equation 6.1](/notes/linear-algebra/linear-algebra-i/determinants-of-linear-maps/#eq:linear-algebra-i:determinant-pullback) first to $L_2$ and then to $L_1$ gives

$$
\begin{aligned}
    \det(L_2\circ L_1)
      &=D(L_2(L_1(e_1)),\ldots,L_2(L_1(e_n)))\\
      &=(\det L_2)D(L_1(e_1),\ldots,L_1(e_n))\\
      &=(\det L_2)(\det L_1)D(e_1,\ldots,e_n)\\
      &=(\det L_2)(\det L_1).
  
\end{aligned}
$$

 ◻

:::

### Products of matrices {id="products-of-matrices"}

For matrices, composition acts on columns by successive multiplication. The determinant product rule can therefore be read directly from the effect on the normalized volume function.

:::div{id="thm:linear-algebra-i:determinant-product" class="result theorem"}

**Theorem 6.3.2 (Determinant of a matrix product).** If $A,B$ are $n$-by-$n$ matrices, then

$$
\det(AB)=(\det A)(\det B).
$$

:::

:::div{class="proof"}

*Proof.* For fixed $A$, define

$$
D_A(v_1,\ldots,v_n)=D(Av_1,\ldots,Av_n),
$$

where $D$ is the normalized determinant function on columns. Since multiplication by $A$ is linear, $D_A$ is antisymmetric and multilinear. The one-dimensionality of the space of top-degree forms gives

$$
D_A=D_A(e_1,\ldots,e_n)D=(\det A)D.
$$

Write the columns of $B$ as $C_1,\ldots,C_n$. The corresponding columns of $AB$ are $AC_1,\ldots,AC_n$. Hence

$$
\det(AB)=D_A(C_1,\ldots,C_n)=(\det A)(\det B).
$$

 ◻

:::

### Invertibility and zero determinant {id="invertibility-and-zero-determinant"}

An endomorphism is called *singular* when it is not invertible. The criteria in [§ 4.3](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#sec:linear-algebra-i:rank) identify this case with a nonzero kernel in finite dimensions.

:::div{id="thm:linear-algebra-i:determinant-invertibility" class="result theorem"}

**Theorem 6.3.3 (Determinant and invertibility).** An endomorphism $L:V\to V$ is singular if and only if $\det L=0$. If $L$ is invertible, then

$$
\det(L^{-1})=\frac{1}{\det L}.
$$

:::

:::div{class="proof"}

*Proof.* Suppose $L$ is singular. Choose $v\ne0$ in $\ker L$, set $e_1=v$, and extend this vector to a basis $(e_1,\ldots,e_n)$. Normalize $D$ on this basis. Then

$$
\det L=D(L(e_1),\ldots,L(e_n))
      =D(0,L(e_2),\ldots,L(e_n))=0.
$$

If $L$ is invertible, multiplicativity and $\det I=1$ give

$$
(\det L^{-1})(\det L)=\det(L^{-1}\circ L)=1.
$$

Thus $\det L\ne0$, and division gives the reciprocal formula. These two implications prove the equivalence. ◻

:::

For a square matrix $M$, this becomes

$$
\det M=0\quad\Longleftrightarrow\quad
  \operatorname{rank}M<n\quad\Longleftrightarrow\quad
  M\text{ is singular}.
$$

There is also a direct calculation using the adapted bases of [Equation 4.1](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#eq:linear-algebra-i:kernel-first-normal-form). Writing $r=\operatorname{rank}M$, place the domain basis vectors with independent nonzero images first. Suitable invertible basis matrices $E,F$ then satisfy

$$
ME=FJ_r,\qquad M=FJ_rE^{-1},
$$

where $J_r$ is $n$-by-$n$, with its first $r$ diagonal entries equal to $1$ and all other entries zero. Its determinant is zero for $r<n$ and is one for $r=n$. Since $\det F$ and $\det E^{-1}$ are nonzero, the product formula gives the same criterion.

## 6.4 Transposes and linear systems {id="sec:linear-algebra-i:transposes-and-linear-systems"}

### Transpose {id="transpose"}

:::div{id="web:sections/linear-algebra-i/06-determinants-of-linear-maps/04-transposes-and-linear-systems:124" class="result definition"}

**Definition 6.4.1.** If $M$ is an $m$-by-$n$ matrix, its transpose $M^T$ is the $n$-by-$m$ matrix obtained by interchanging rows and columns,

$$
(M^T)^j_i=M^i_j.
$$

:::

Transposition reverses the order of a matrix product. For $A\in\mathbb F^{k\times m}$ and $B\in\mathbb F^{m\times n}$,

$$
(AB)^T=B^TA^T\in\mathbb F^{n\times k}.
$$

:::div{id="thm:linear-algebra-i:determinant-transpose" class="result theorem"}

**Theorem 6.4.2 (Determinant of a transpose).** Every square matrix satisfies $\det(M^T)=\det M$.

:::

:::div{class="proof"}

*Proof.* The permutation formula gives

$$
\begin{aligned}
    \det M
      &=\sum_{\sigma\in S_n}\varepsilon(\sigma)
        M^{\sigma(1)}_1\cdots M^{\sigma(n)}_n\\
      &=\sum_{\sigma\in S_n}\varepsilon(\sigma)
        M^1_{\sigma^{-1}(1)}\cdots M^n_{\sigma^{-1}(n)}\\
      &=\sum_{\tau\in S_n}\varepsilon(\tau)
        M^1_{\tau(1)}\cdots M^n_{\tau(n)}\\
      &=\det(M^T).
  
\end{aligned}
$$

In the second line, the factors are reordered by their row indices. In the third, set $\tau=\sigma^{-1}$ and use $\varepsilon(\sigma^{-1})=\varepsilon(\sigma)$. ◻

:::

:::div{id="web:sections/linear-algebra-i/06-determinants-of-linear-maps/04-transposes-and-linear-systems:1248" class="result remark"}

**Remark 6.4.3.** For a factorization $M=PLU$, where $P$ is a permutation matrix, $L$ is lower triangular, and $U$ is upper triangular, the same determinant identity has the calculation

$$
\begin{aligned}
    \det(M^T)&=\det(U^TL^TP^T)\\
      &=(\det U)(\det L)(\det P)\\
      &=\det(PLU)=\det M.
  
\end{aligned}
$$

Transposition preserves the diagonal product of a triangular matrix and the determinant of a permutation matrix.

:::

### Square systems of equations {id="square-systems-of-equations"}

Consider $Ax=b$ with $A\in\mathbb{R}^{n\times n}$ and $b\in\mathbb{R}^n$. If $\det A\ne0$, the matrix is invertible and the unique solution is

$$
x=A^{-1}b.
$$

If $\det A=0$, then

$$
\dim\ker A>0,\qquad \dim\operatorname{im}A<n.
$$

A solution exists exactly when $b\in\operatorname{im}A$. If $x_0$ is one solution, every vector $x_0+v$, with $v\in\ker A$, is also a solution, since

$$
A(x_0+v)=Ax_0+Av=b.
$$

Thus a singular square system over $\mathbb{R}$ has either no solution or infinitely many solutions. Its full solution set, when nonempty, is $x_0+\ker A$, as in [§ 4.1](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#sec:linear-algebra-i:kernel). [Figure 6.3](/notes/linear-algebra/linear-algebra-i/determinants-of-linear-maps/#fig:linear-algebra-i:affine-solution-fiber) illustrates this translation when the kernel is a line in $\mathbb{R}^2$.

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:affine-solution-fiber"}

[![A real-plane schematic for a nonempty singular system. Moving from x\_0 by any kernel vector v gives another solution x\_0+v. The two lines are parallel.](/notes/linear-algebra/figures/affine-solution-fiber.svg){.tikz-diagram}](/notes/linear-algebra/figures/affine-solution-fiber.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 6.3. A real-plane schematic for a nonempty singular system. Moving from $x_0$ by any kernel vector $v$ gives another solution $x_0+v$. The two lines are parallel.

:::

::::

:::::

## 6.5 Maps between different spaces {id="sec:linear-algebra-i:determinants-between-spaces"}

For a linear map $L:V\to W$, pullback is defined even when the domain and codomain are different. If $\dim V=\dim W=n$, it gives a map between one-dimensional vector spaces,

$$
L^*:\Lambda^n W^*\longrightarrow\Lambda^n V^*.
$$

For an endomorphism, these two spaces coincide, so the map is multiplication by a well-defined scalar. When $V$ and $W$ are different, there is no canonical identification of their top-degree form spaces, and hence no canonical scalar for this map. A scalar description requires a choice of basis in each of these two one-dimensional spaces.

:::div{id="web:sections/linear-algebra-i/06-determinants-of-linear-maps/05-maps-between-different-spaces:678" class="result definition"}

**Definition 6.5.1.** For $L:V\to W$ with $\dim V=\dim W=n$, its determinant is the map

$$
\det(L)=L^*:\Lambda^n W^*\longrightarrow\Lambda^n V^*.
$$

:::

The determinant in this setting is therefore a linear map between two lines. It acts on a form $A$ by the same formula

$$
(L^*A)(v_1,\ldots,v_n)=A(L(v_1),\ldots,L(v_n)).
$$
