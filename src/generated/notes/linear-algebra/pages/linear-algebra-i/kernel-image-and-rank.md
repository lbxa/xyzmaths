---
title: "Kernel, image, and rank"
group: "Linear Algebra I"
order: 10
part: "Part I · Linear Algebra I"
page: "49"
outline: [{"id": "sec:linear-algebra-i:kernel", "title": "4.1 Kernel", "level": 2}, {"id": "null-space-nullity-and-homogeneous-equations", "title": "Null space, nullity, and homogeneous equations", "level": 3}, {"id": "information-lost-by-the-map", "title": "Information lost by the map", "level": 3}, {"id": "injectivity", "title": "Injectivity", "level": 3}, {"id": "sec:linear-algebra-i:image", "title": "4.2 Image", "level": 2}, {"id": "sec:linear-algebra-i:rank", "title": "4.3 Rank", "level": 2}, {"id": "rank-of-a-matrix", "title": "Rank of a matrix", "level": 3}, {"id": "examples-in-euclidean-spaces", "title": "Examples in Euclidean spaces", "level": 3}, {"id": "adapted-bases-and-ranknullity", "title": "Adapted bases and rank–nullity", "level": 3}, {"id": "isomorphisms", "title": "Isomorphisms", "level": 3}, {"id": "a-matrix-adapted-to-the-kernel-and-image", "title": "A matrix adapted to the kernel and image", "level": 3}, {"id": "using-the-identity-lefm", "title": "Using the identity L(E)=FM", "level": 3}, {"id": "sec:linear-algebra-i:differentiation", "title": "4.4 Differentiation as a linear map", "level": 2}, {"id": "polynomial-differentiation", "title": "Polynomial differentiation", "level": 3}]
---

# Chapter 4. Kernel, image, and rank {id="ch:linear-algebra-i:kernel-image-and-rank"}

Two questions organize the study of a linear map. Which inputs have the same output, and which outputs can be reached? The kernel answers the first question through differences of inputs, and the image answers the second. Rank and nullity count the corresponding directions. Adapted bases make both visible in a matrix, and differentiation provides a function-space application of the same ideas.

## 4.1 Kernel {id="sec:linear-algebra-i:kernel"}

::::div{id="web:sections/linear-algebra-i/04-kernel-image-and-rank/01-kernel:54" class="result definition"}

**Definition 4.1.1.** Let $V$ and $W$ be vector spaces and $L:V\to W$ a linear map. Its kernel is[^1]

$$
\ker L=\{v\in V:L(v)=0_W\} \subseteq V.
$$

The kernel is a subspace of the domain $V$, consisting of the inputs mapped to the zero vector.

:::notes{id="footnotes"}

[^1]: *Kernel* comes from Old English *cyrnel*, meaning a seed or pip, related to *corn* with a diminutive ending. The word later acquired the figurative sense of a central core ([Harper n.d.](/notes/linear-algebra/references/#ref-EtymologyKernel)). Its technical meaning depends on the context.

:::

::::

:::div{class="pending-review"}

To verify the subspace assertion, linearity gives $L(0_V)=0_W$, so the kernel is nonempty. If $v_1,v_2\in\ker L$ and $a,b\in\mathbb F$, then

$$
L(av_1+bv_2)=aL(v_1)+bL(v_2)=0_W.
$$

Thus $av_1+bv_2\in\ker L$, proving closure under linear combinations.

:::

[Figure 4.1](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#fig:linear-algebra-i:kernel-to-zero) emphasizes the defining property of the kernel. Every input in this subspace has the same output, the zero vector $0_W$.

::::figure{id="fig:linear-algebra-i:kernel-to-zero"}

[![The kernel of L\:V\\to W, shown schematically. All vectors in the shaded region map to 0\_W. The circle indicates a set, not a bounded vector space. TikZ redrawing inspired by Wikipedia’s Kernel (linear algebra) page (Wikipedia contributors n.d.) and Pillsmarch’s illustration (Pillsmarch 2023), licensed under CC BY 4.0.](/notes/linear-algebra/figures/kernel-to-zero.svg){.tikz-diagram}](/notes/linear-algebra/figures/kernel-to-zero.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 4.1. The kernel of $L:V\to W$, shown schematically. All vectors in the shaded region map to $0_W$. The circle indicates a set, not a bounded vector space. TikZ redrawing inspired by Wikipedia’s *Kernel (linear algebra)* page ([Wikipedia contributors n.d.](/notes/linear-algebra/references/#ref-WikipediaKernel)) and Pillsmarch’s illustration ([Pillsmarch 2023](/notes/linear-algebra/references/#ref-PillsmarchKernelImage)), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

:::

::::

### Null space, nullity, and homogeneous equations {id="null-space-nullity-and-homogeneous-equations"}

The kernel is also called the *null space*. Here “null” refers to the zero output, while “space” refers to the subspace of inputs that produce it. A vector in the null space need not itself be zero.

The *nullity* of $L$ is the dimension of its null space,

$$
\operatorname{nullity}L=\dim\ker L.
$$

When the kernel is finite-dimensional, its nullity is the number of vectors in any basis of $\ker L$. The null space is a subspace of inputs. Nullity counts its independent directions.

In finite dimensions, nullity is therefore a nonnegative integer. If $\ker L=\{0_V\}$, its basis is empty, so its nullity is $0$. The zero vector is still in the kernel, but it contributes no independent direction. Since the kernel is a subspace of $V$, for finite-dimensional $V$ we have

$$
0\leq\operatorname{nullity}L\leq\dim V.
$$

For a matrix $A\in\mathbb F^{n\times m}$, the same definition becomes

$$
\operatorname{Null}(A)=\ker A
    =\{x\in\mathbb F^m:Ax=0\}.
$$

Thus finding the null space means solving a homogeneous system of linear equations ([Margalit and Rabinoff 2019b](/notes/linear-algebra/references/#ref-MargalitRabinoffSubspaces)), using the row operations of [§ 3.1](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#sec:linear-algebra-i:systems-of-linear-equations). The dimension of this solution space is $\operatorname{nullity}A$.

### Information lost by the map {id="information-lost-by-the-map"}

The kernel records changes to an input that leave its output unchanged. If $k\in\ker L$, then

$$
L(v+k)=L(v)+L(k)=L(v).
$$

Conversely, if $L(v_1)=L(v_2)$, linearity gives

$$
L(v_1-v_2)=L(v_1)-L(v_2)=0_W,
$$

so $v_1-v_2\in\ker L$. Two inputs are indistinguishable under $L$ exactly when their difference lies in its kernel.

This matters whenever a linear map models measurements. An input can change by any vector in the kernel without changing the observed data. [^2] Nullity therefore counts the independent directions of this ambiguity. [§ 4.3](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#sec:linear-algebra-i:rank) defines rank as the dimension of the image. For finite-dimensional $V$, the rank–nullity theorem ([Theorem 4.3.10](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#thm:linear-algebra-i:rank-nullity)) gives

$$
\operatorname{rank}L+\operatorname{nullity}L=\dim V.
$$

The independent output directions, counted by rank, and the input directions lost in the kernel, counted by nullity, together account for the dimension of the domain.

:::notes{id="footnotes-2"}

[^2]: In computer vision, a *kernel* usually means an array of weights used for convolution or correlation ([Huamán n.d.](/notes/linear-algebra/references/#ref-OpenCVLinearFilters)). The array defines a filter. For a linear filter, its linear-algebra kernel would instead be the subspace of images it maps to zero.

:::

More generally, suppose $v_0$ is one solution of $L(v)=w$. Then all solutions are precisely

$$
v_0+\ker L=\{v_0+k:k\in\ker L\}.
$$

Indeed, adding $k\in\ker L$ preserves the output, and any other solution differs from $v_0$ by a kernel vector. For a matrix equation $Ax=b$, this says that every solution is a particular solution plus a solution of $Ax=0$ ([Margalit and Rabinoff 2019a](/notes/linear-algebra/references/#ref-MargalitRabinoffSolutionSets)). The image determines whether a solution exists. The kernel determines whether an existing solution is unique.

### Injectivity {id="injectivity"}

The general definition of injectivity is recalled in [§ B.2](/notes/linear-algebra/appendices/assumed-knowledge/#sec:appendix:map-properties). The map $L$ is injective exactly when $\ker L=\{0_V\}$, or, in finite dimensions, when $\dim\ker L=0$. If $L$ is injective, $L(k)=0_W=L(0_V)$ forces $k=0_V$ for every $k\in\ker L$. Conversely, for a zero kernel, injectivity follows from the equivalences

$$
\begin{aligned}
    L(v_1)=L(v_2)
      &\iff L(v_2)-L(v_1)=0_W\\
      &\iff L(v_2-v_1)=0_W\\
      &\iff v_2-v_1\in\ker L=\{0_V\}\\
      &\iff v_2=v_1.
  \end{aligned}
$$

## 4.2 Image {id="sec:linear-algebra-i:image"}

:::div{id="web:sections/linear-algebra-i/04-kernel-image-and-rank/02-image:52" class="result definition"}

**Definition 4.2.1.** The image of $L:V\to W$ is the set of its possible outputs, given by

$$
\operatorname{im}L=L(V)=\{L(v):v\in V\}\subseteq W.
$$

It is a subspace of the codomain $W$.

:::

:::div{class="pending-review"}

The image contains $0_W=L(0_V)$. For any two of its elements, write $w_1=L(v_1)$ and $w_2=L(v_2)$. For scalars $a,b\in\mathbb F$, linearity gives

$$
aw_1+bw_2=aL(v_1)+bL(v_2)=L(av_1+bv_2)\in\operatorname{im}L.
$$

The image is therefore nonempty and closed under linear combinations, so it is a subspace of $W$.

:::

[Figure 4.2](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#fig:linear-algebra-i:kernel-image) shows the kernel and image inside $V$ and $W$. The map sends every vector of $V$ to a vector in $\operatorname{im}L\subseteq W$, and sends every vector of $\ker L\subseteq V$ to $0_W$. The codomain specifies the target space. The image consists of the outputs actually attained.

::::figure{id="fig:linear-algebra-i:kernel-image"}

[![Domain, kernel, image, and codomain of L\:V\\to W. The solid line sends v to L(v). The dashed line sends k\\in\\ker L to 0\_W. Circles show set containment schematically, not bounded vector spaces. TikZ redrawing inspired by Wikipedia’s Kernel (linear algebra) page (Wikipedia contributors n.d.) and Pillsmarch’s illustration (Pillsmarch 2023), licensed under CC BY 4.0.](/notes/linear-algebra/figures/kernel-image-linear-map.svg){.tikz-diagram}](/notes/linear-algebra/figures/kernel-image-linear-map.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 4.2. Domain, kernel, image, and codomain of $L:V\to W$. The solid line sends $v$ to $L(v)$. The dashed line sends $k\in\ker L$ to $0_W$. Circles show set containment schematically, not bounded vector spaces. TikZ redrawing inspired by Wikipedia’s *Kernel (linear algebra)* page ([Wikipedia contributors n.d.](/notes/linear-algebra/references/#ref-WikipediaKernel)) and Pillsmarch’s illustration ([Pillsmarch 2023](/notes/linear-algebra/references/#ref-PillsmarchKernelImage)), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

:::

::::

Recall surjectivity from [§ B.2](/notes/linear-algebra/appendices/assumed-knowledge/#sec:appendix:map-properties). The codomain need not equal the image. For example, a map into $\mathbb{R}$ need not take every real value. The map $L$ is surjective exactly when $\operatorname{im}L=W$. For finite-dimensional $W$, the subspace dimension criterion gives

$$
\dim\operatorname{im}L=\dim W
    \quad\Longleftrightarrow\quad
  \operatorname{im}L=W.
$$

## 4.3 Rank {id="sec:linear-algebra-i:rank"}

:::div{id="web:sections/linear-algebra-i/04-kernel-image-and-rank/03-rank:67" class="result definition"}

**Definition 4.3.1.** The rank of a linear map is the dimension of its image, so

$$
\operatorname{rank}L=\dim\operatorname{im}L.
$$

Its nullity, introduced in [§ 4.1](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#sec:linear-algebra-i:kernel), is $\operatorname{nullity}L=\dim\ker L$.

:::

### Rank of a matrix {id="rank-of-a-matrix"}

Let $M\in\mathbb F^{m\times n}$, with $m$ rows and $n$ columns. It represents the linear map $x\mapsto Mx$ from $\mathbb F^n$ to $\mathbb F^m$. If its columns are $c_1,\ldots,c_n$, then

$$
\operatorname{im}M=\{Mx:x\in\mathbb F^n\}
    =\operatorname{span}\{c_1,\ldots,c_n\}.
$$

Thus $\operatorname{rank}M$ is the maximum number of linearly independent columns of $M$. Since there are $n$ columns and each belongs to $\mathbb F^m$,

$$
0\leq\operatorname{rank}M\leq\min(m,n).
$$

Both rank and nullity are nonnegative integers because they are dimensions. The kernel of $M$ is a subspace of $\mathbb F^n$, so

$$
0\leq\operatorname{nullity}M\leq n.
$$

Here $n$ is the number of columns, the dimension of the domain. The rank–nullity theorem ([Theorem 4.3.10](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#thm:linear-algebra-i:rank-nullity)) gives

$$
\operatorname{nullity}M=n-\operatorname{rank}M.
$$

Combining this identity with the rank bound yields the sharper range

$$
\max(0,n-m)\leq\operatorname{nullity}M\leq n.
$$

Thus rank and nullity cannot be chosen independently. Their sum is $n$.

Rank measures the non-degeneracy of a system of linear equations $Mx=b$ by counting its independent output directions. The matrix has *full rank* when its rank equals $\min(m,n)$. A smaller rank reflects additional linear dependencies. The value of $b$ still determines whether the system is consistent, through the condition $b\in\operatorname{im}M$.

All columns of $M$ are independent precisely when $\operatorname{rank}M=n$, which requires $n\leq m$. If $n>m$, even a full-rank matrix has dependent columns, because its rank is at most $m<n$. Full rank means the largest rank permitted by the input and output dimensions.

::::::div{id="ex:linear-algebra-i:full-rank-dependent-columns" class="result example"}

**Example 4.3.2.** Consider the matrix

$$
A=\begin{bmatrix}1&0&1\\0&1&1\end{bmatrix},
    \qquad
    A\begin{bmatrix}x\\y\\z\end{bmatrix}
      =\begin{bmatrix}x+z\\y+z\end{bmatrix}.
$$

There are three input coordinates and two output coordinates, so this defines a linear map $\mathbb{R}^3\to\mathbb{R}^2$. Its columns are

$$
c_1=\begin{bmatrix}1\\0\end{bmatrix},\qquad
    c_2=\begin{bmatrix}0\\1\end{bmatrix},\qquad
    c_3=\begin{bmatrix}1\\1\end{bmatrix}=c_1+c_2.
$$

These are the images of the three standard basis vectors of $\mathbb{R}^3$. The first two span $\mathbb{R}^2$ and are independent, while the third lies in their span, as shown in [Figure 4.3](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#fig:linear-algebra-i:dependent-matrix-columns). Consequently,

$$
\operatorname{im}A=\mathbb{R}^2,
    \qquad \operatorname{rank}A=2=\min(2,3).
$$

Thus $A$ has full rank, although its three columns are dependent. The images of an input basis need not be an output basis.

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:dependent-matrix-columns"}

[![The three columns of A in the output plane. The first two form a basis of \\mathbb\{R\}^2. The third is their sum and contributes no additional independent direction.](/notes/linear-algebra/figures/dependent-matrix-columns.svg){.tikz-diagram}](/notes/linear-algebra/figures/dependent-matrix-columns.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 4.3. The three columns of $A$ in the output plane. The first two form a basis of $\mathbb{R}^2$. The third is their sum and contributes no additional independent direction.

:::

::::

:::::

The same column relation identifies a nonzero kernel vector, since

$$
A\begin{bmatrix}1\\1\\-1\end{bmatrix}=c_1+c_2-c_3=0.
$$

Every vector of $\mathbb{R}^2$ is reached, but some distinct inputs have the same output. The matrix therefore defines a surjective map with a nonzero kernel. This connects the columns’ spanning property to the image and their dependence to information lost by the map.

::::::

### Examples in Euclidean spaces {id="examples-in-euclidean-spaces"}

:::div{id="web:sections/linear-algebra-i/04-kernel-image-and-rank/03-rank:3968" class="result example"}

**Example 4.3.3.** The inclusion $Z:\mathbb{R}^2\to\mathbb{R}^3$, $Z(x,y)=(x,y,0)$, has matrix

$$
\begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix}.
$$

Its kernel is $\{0\}$, and its image is the plane $\{(x,y,0):x,y\in\mathbb{R}\}$, with basis $\{(1,0,0),(0,1,0)\}$. The zero kernel has the empty basis, so its nullity is $0$. The two-dimensional image gives rank $2$.

:::

:::div{id="web:sections/linear-algebra-i/04-kernel-image-and-rank/03-rank:4350" class="result example"}

**Example 4.3.4.** For $W:\mathbb{R}^2\to\mathbb{R}^3$, $W(x,y)=(y,0,0)$, the matrix is

$$
\begin{bmatrix}0&1\\0&0\\0&0\end{bmatrix}.
$$

The kernel is $\{(x,0):x\in\mathbb{R}\}$, with basis $\{(1,0)\}$. The image is $\{(y,0,0):y\in\mathbb{R}\}$, with basis $\{(1,0,0)\}$. Hence its nullity is $1$ and its rank is $1$.

:::

:::div{id="web:sections/linear-algebra-i/04-kernel-image-and-rank/03-rank:4680" class="result example"}

**Example 4.3.5.** The zero map $U:\mathbb{R}^2\to\mathbb{R}^3$ has matrix

$$
\begin{bmatrix}0&0\\0&0\\0&0\end{bmatrix},
$$

kernel $\mathbb{R}^2$, and image $\{(0,0,0)\}$. Its nullity is $2$ and its rank is $0$.

:::

:::div{id="web:sections/linear-algebra-i/04-kernel-image-and-rank/03-rank:4904" class="result example"}

**Example 4.3.6.** For $U:\mathbb{R}^3\to\mathbb{R}^2$, $U(x,y,z)=(y,z)$, the matrix is

$$
\begin{bmatrix}0&1&0\\0&0&1\end{bmatrix}.
$$

The kernel is $\{(x,0,0):x\in\mathbb{R}\}$, with basis $\{(1,0,0)\}$, and the image is $\mathbb{R}^2$. Its nullity is $1$ and its rank is $2$.

:::

:::div{id="web:sections/linear-algebra-i/04-kernel-image-and-rank/03-rank:5191" class="result example"}

**Example 4.3.7.** For $U:\mathbb{R}^3\to\mathbb{R}^2$, $U(x,y,z)=(z,0)$, the matrix is

$$
\begin{bmatrix}0&0&1\\0&0&0\end{bmatrix}.
$$

The kernel is $\{(x,y,0):x,y\in\mathbb{R}\}$, with basis $\{(1,0,0),(0,1,0)\}$. The image is $\{(z,0):z\in\mathbb{R}\}$, with basis $\{(1,0)\}$. Its nullity is $2$ and its rank is $1$.

:::

:::div{id="web:sections/linear-algebra-i/04-kernel-image-and-rank/03-rank:5524" class="result example"}

**Example 4.3.8.** The zero map $U:\mathbb{R}^3\to\mathbb{R}^2$ has matrix

$$
\begin{bmatrix}0&0&0\\0&0&0\end{bmatrix},
$$

kernel $\mathbb{R}^3$, and image $\{(0,0)\}$. Its nullity is $3$ and its rank is $0$.

:::

### Adapted bases and rank–nullity {id="adapted-bases-and-ranknullity"}

The following lemma supplies a basis adapted to the kernel and image.

:::div{id="thm:linear-algebra-i:adapted-basis" class="result lemma"}

**Lemma 4.3.9 (A basis adapted to the kernel and image).** Let $L:V\to W$ be a linear map between finite-dimensional vector spaces, with $\dim V=m$ and $\dim\ker L=k$. There is a basis

$$
(e_1,\ldots,e_k,e_{k+1},\ldots,e_m)
$$

of $V$ such that $(e_1,\ldots,e_k)$ is a basis of $\ker L$ and $(L(e_{k+1}),\ldots,L(e_m))$ is a basis of $\operatorname{im}L$. If $k=0$, the images of any basis of $V$ form a basis of the image.

:::

::::div{class="pending-review"}

:::div{class="proof"}

*Proof.* The kernel is a subspace of the finite-dimensional space $V$, so [Proposition 1.2.9](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:finite-dimensional-subspaces) gives a basis $(e_1,\ldots,e_k)$ of $\ker L$. By [Proposition 1.2.6](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:basis-extension), extend it to a basis $(e_1,\ldots,e_k,e_{k+1},\ldots,e_m)$ of $V$.

For any $v\in V$, write $v=\sum_{j=1}^m a_j e_j$. Since the first $k$ basis vectors lie in the kernel, linearity gives

$$
L(v)=\sum_{j=k+1}^m a_jL(e_j).
$$

Thus $L(e_{k+1}),\ldots,L(e_m)$ span $\operatorname{im}L$.

To prove independence, suppose $\sum_{j=k+1}^m a_jL(e_j)=0$. Then $u=\sum_{j=k+1}^m a_j e_j$ belongs to $\ker L$, so $u=\sum_{i=1}^k b_i e_i$ for some coefficients $b_i$. Subtracting these expressions for $u$ yields

$$
\sum_{j=k+1}^m a_j e_j-\sum_{i=1}^k b_i e_i=0.
$$

Independence of the full basis gives $a_j=0$ for every $j>k$. The surviving images are therefore independent and form a basis of $\operatorname{im}L$.

If $k=0$, the same spanning and independence arguments apply to any basis of $V$. If $k=m$, the surviving family is empty and is the basis of the zero image, so this case is included as well. ◻

:::

::::

:::div{id="thm:linear-algebra-i:rank-nullity" class="result theorem"}

**Theorem 4.3.10 (Rank–nullity).** For a linear map $L:V\to W$ between finite-dimensional vector spaces,

$$
\operatorname{rank}L+\operatorname{nullity}L=\dim V.
$$

:::

:::div{class="proof"}

*Proof.* Set $m=\dim V$ and $k=\dim\ker L$. By [Lemma 4.3.9](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#thm:linear-algebra-i:adapted-basis), the image has a basis consisting of $m-k$ vectors. Consequently,

$$
\dim\ker L+\operatorname{rank}L=k+(m-k)=m=\dim V.
$$

 ◻

:::

The following exercises apply these ideas.

::statement{key="hw04:kernel-image-and-rank"}

### Isomorphisms {id="isomorphisms"}

Recall the distinction between injectivity, surjectivity, and bijectivity in [§ B.2](/notes/linear-algebra/appendices/assumed-knowledge/#sec:appendix:map-properties). A linear map is an *isomorphism* if it is injective and surjective. The kernel and image criteria give

$$
L\text{ is an isomorphism}
    \quad\Longleftrightarrow\quad
  \dim\ker L=0\text{ and }\operatorname{rank}L=\dim W.
$$

Rank–nullity then implies $\dim V=\dim W$. Equivalently, $L$ is an isomorphism precisely when

$$
\dim V=\dim W=\operatorname{rank}L,\qquad \dim\ker L=0.
$$

Another equivalent criterion is

$$
L\text{ is bijective}
    \quad\Longleftrightarrow\quad
  \dim V=\dim W\text{ and }\dim\ker L=0.
$$

::statement{key="hw04:rank-nullity"}

[Figure 4.4](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#fig:linear-algebra-i:rank-map-criteria) summarizes the rank and nullity tests for a linear map between finite-dimensional spaces. The dimension inequalities are necessary consequences of these tests. The sizes of the domain and codomain alone do not decide injectivity or surjectivity. A bijective map satisfies both sets of criteria.

::::figure{id="fig:linear-algebra-i:rank-map-criteria"}

[![Finite-dimensional map criteria. Light gray shows the image. Dark gray shows a nonzero kernel. Dashed paths map to zero. The first two sketches illustrate non-bijective possibilities. Circle sizes do not encode dimensions.](/notes/linear-algebra/figures/rank-map-criteria.svg){.tikz-diagram}](/notes/linear-algebra/figures/rank-map-criteria.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 4.4. Finite-dimensional map criteria. Light gray shows the image. Dark gray shows a nonzero kernel. Dashed paths map to zero. The first two sketches illustrate non-bijective possibilities. Circle sizes do not encode dimensions.

:::

::::

### A matrix adapted to the kernel and image {id="a-matrix-adapted-to-the-kernel-and-image"}

The aim is to choose coordinates that make the kernel and image visible in the matrix.[^3] As in [§ 3.3](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#sec:linear-algebra-i:change-of-basis-for-functions-and-maps), each column records the image of one domain basis vector in the chosen codomain basis.

:::notes{id="footnotes-3"}

[^3]: *Adapted* means that the bases are chosen to fit the map. Changing coordinates preserves $L$, its kernel, and its image. It makes the lost input directions and the independent output directions easier to identify.

:::

For finite-dimensional $V$ and $W$, write $m=\dim V$, $n=\dim W$, $k=\dim\ker L$, and $r=m-k=\operatorname{rank}L$. Choose the basis $E$ of [Lemma 4.3.9](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#thm:linear-algebra-i:adapted-basis), with the $k$ kernel vectors first. The images of the remaining $r$ vectors form a basis of $\operatorname{im}L$. Choose a basis $F=[f_1,\ldots,f_n]$ of $W$ whose first $r$ vectors are

$$
f_j=L(e_{k+j}),\qquad 1\leq j\leq r.
$$

The remaining $n-r$ vectors complete the basis of $W$, as guaranteed by [Proposition 1.2.6](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:basis-extension). [^4]

:::notes{id="footnotes-4"}

[^4]: Here $m$ counts input coordinates and $n$ counts output coordinates, so $D$ has $n$ rows and $m$ columns. The domain basis begins with the kernel. The codomain basis begins with the image.

:::

Now $L(E)=[0,\ldots,0,f_1,\ldots,f_r]$. The first $k$ columns are zero because their basis vectors lie in the kernel. For the next $r$ columns, $L(e_{k+j})=f_j$ has coefficient $1$ in position $j$ and $0$ elsewhere, giving an identity block. Every output lies in the span of $f_1,\ldots,f_r$, so the last $n-r$ rows are zero. Thus the matrix in these bases is

:::div{id="eq:linear-algebra-i:kernel-first-normal-form" class="equation"}

$$
D=
  \begin{bmatrix}
    0_{r\times k}&I_r\\
    0_{(n-r)\times k}&0_{(n-r)\times r}
  \end{bmatrix}.\tag{4.1}
$$

:::

[Figure 4.5](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#fig:linear-algebra-i:adapted-basis-blocks) shows how the ordering of the two bases produces these four blocks.

::::figure{id="fig:linear-algebra-i:adapted-basis-blocks"}

[![Schematic of the adapted matrix D. The identity block carries the r surviving coordinates. Block sizes are indicated by the labels, not drawn to scale. A coordinate group disappears from D when its dimension is zero.](/notes/linear-algebra/figures/adapted-basis-block-matrix.svg){.tikz-diagram}](/notes/linear-algebra/figures/adapted-basis-block-matrix.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 4.5. Schematic of the adapted matrix $D$. The identity block carries the $r$ surviving coordinates. Block sizes are indicated by the labels, not drawn to scale. A coordinate group disappears from $D$ when its dimension is zero.

:::

::::

To see its action, split an input coordinate column into $u\in\mathbb F^k$ and $t\in\mathbb F^r$. Then

$$
a=\begin{bmatrix}u\\t\end{bmatrix},
  \qquad
  Da=\begin{bmatrix}t\\0\end{bmatrix},
  \qquad 0\in\mathbb F^{n-r}.
$$

In other words, if $v=Ea$, then $L(v)=\sum_{j=1}^r t^j f_j$. [^5] The $k$ kernel coordinates $u$ have no effect on the output. This makes nullity $k$ and rank $r$ directly visible.

:::notes{id="footnotes-5"}

[^5]: The identity block copies the surviving coefficients because $f_j$ was chosen to equal $L(e_{k+j})$. It does not assert that $L$ is the identity map on $V$.

:::

:::div{id="web:sections/linear-algebra-i/04-kernel-image-and-rank/03-rank:12826" class="result example"}

**Example 4.3.13.** For the standard bases of $\mathbb{R}^m$ and $\mathbb{R}^n$, the prescription

$$
L(e_1)=\cdots=L(e_k)=0,\qquad L(e_{k+j})=f_j\quad(1\leq j\leq r)
$$

gives the matrix $D$ in [Equation 4.1](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#eq:linear-algebra-i:kernel-first-normal-form). Here $r=m-k\leq n$. Its nullity is $k$ and its rank is $r$. It is injective when $k=0$, and surjective when $n-r=0$.

:::

::statement{key="hw04:prescribed-kernel-and-image"}

### Using the identity $L(E)=FM$ {id="using-the-identity-lefm"}

The identity $L(E)=FM$ is a recipe for finding the matrix of $L$ in the ordered bases $E=[e_1,\ldots,e_m]$ and $F=[f_1,\ldots,f_n]$. Here

$$
L(E)=[L(e_1),\ldots,L(e_m)]
$$

means applying $L$ to each basis vector and placing the images in columns. If $M_j$ is the $j$-th column of $M$, the corresponding column of $FM$ is

$$
FM_j=f_1M^1_j+\cdots+f_nM^n_j.
$$

Thus $L(E)=FM$ says that each column of $M$ contains the coefficients of $L(e_j)$ in the basis $F$.

To construct $M$, proceed one column at a time.

:::list

1.  **(1)** Compute $L(e_j)$, using the given formula for $L$.

2.  **(2)** Express this output as a linear combination of $f_1,\ldots,f_n$. Equivalently, solve $FM_j=L(e_j)$ for its coefficient column $M_j$. The coefficients are unique because $F$ is a basis.

3.  **(3)** Place that coefficient column in position $j$. Repeat in the order of $E$, giving $M=[M_1,\ldots,M_m]$.

:::

The resulting matrix has $n$ rows and $m$ columns. Multiplying $FM$ should reproduce all the computed images in $L(E)$. This is a direct check of the construction.

For a map between coordinate spaces, let $C$ be its standard-basis matrix, and write $E$ and $F$ as matrices whose columns are the basis vectors in standard coordinates. Then $L(E)=CE$, so

$$
CE=FM,\qquad M=F^{-1}CE.
$$

The matrix $F$ is invertible because its columns form a basis. In practice, one can compute $CE$ and solve $FM=CE$ column by column. The next example carries out the coefficient method directly.

::::div{id="ex:linear-algebra-i:adapted-basis-matrix" class="result example"}

**Example 4.3.15.** Consider $L:\mathbb{R}^3\to\mathbb{R}^2$ with standard-basis matrix

$$
C=\begin{bmatrix}1&2&3\\0&0&4\end{bmatrix}.
$$

Its kernel is

$$
\{(v^1,v^2,0):v^1+2v^2=0\},
$$

with basis $\{(-2,1,0)\}$. Choose the domain and codomain bases

$$
E=[(-2,1,0),(0,1,0),(0,0,1)],
    \qquad F=[(2,0),(3,4)].
$$

As matrices of standard coordinates, these are

$$
E=\begin{bmatrix}-2&0&0\\1&1&0\\0&0&1\end{bmatrix},
    \qquad F=\begin{bmatrix}2&3\\0&4\end{bmatrix}.
$$

Applying $C$ to the columns of $E$ gives[^6]

$$
\begin{aligned}
      L(e_1)&=(-2+2,0)=(0,0)=0f_1+0f_2,\\
      L(e_2)&=(2,0)=1f_1+0f_2,\\
      L(e_3)&=(3,4)=0f_1+1f_2.
    \end{aligned}
$$

The three coefficient columns are therefore

$$
M_1=\begin{bmatrix}0\\0\end{bmatrix},\qquad
    M_2=\begin{bmatrix}1\\0\end{bmatrix},\qquad
    M_3=\begin{bmatrix}0\\1\end{bmatrix}.
$$

Placing these columns in order gives[^7]

$$
M=[M_1,M_2,M_3]=\begin{bmatrix}0&1&0\\0&0&1\end{bmatrix}.
$$

To check $L(E)=FM$, multiply

$$
\begin{aligned}
      FM
        &=\begin{bmatrix}2&3\\0&4\end{bmatrix}
          \begin{bmatrix}0&1&0\\0&0&1\end{bmatrix}\\
        &=\begin{bmatrix}0&2&3\\0&0&4\end{bmatrix}
          =[L(e_1),L(e_2),L(e_3)]=L(E).
    \end{aligned}
$$

Thus, for $v=e_1a^1+e_2a^2+e_3a^3=Ea$,

$$
L(v)=f_1a^2+f_2a^3=FMa.
$$

:::notes{id="footnotes-6"}

[^6]: Although $L(e_2)=(2,0)$ in standard coordinates, it equals $f_1$. Its column in $M$ is therefore $(1,0)^T$, recording one copy of $f_1$ and zero copies of $f_2$.

[^7]: Here $k=1$ and $r=2$, so the adapted matrix has one zero column followed by $I_2$. Since $n=r=2$, there are no unused output coordinates and no lower block of zero rows.

:::

::::

::statement{key="hw04:adapted-bases"}

An alternative normal form places the identity block first.

:::div{id="thm:linear-algebra-i:image-first-normal-form" class="result proposition"}

**Proposition 4.3.17 (An image-first normal form).** If $C$ represents a map $\mathbb F^m\to\mathbb F^n$ of rank $r$, there are invertible matrices $A\in\mathbb F^{n\times n}$ and $B\in\mathbb F^{m\times m}$ such that

$$
C=A
    \begin{bmatrix}
      I_r&0_{r\times(m-r)}\\
      0_{(n-r)\times r}&0_{(n-r)\times(m-r)}
    \end{bmatrix}
    B^{-1}.
$$

:::

::::div{class="pending-review"}

:::div{class="proof"}

*Proof.* Let $L(x)=Cx$. Reorder the basis supplied by [Lemma 4.3.9](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#thm:linear-algebra-i:adapted-basis) so that the surviving vectors come first. This gives a basis $(u_1,\ldots,u_m)$ of $\mathbb F^m$. The images of its first $r$ vectors form a basis of the image, and its remaining vectors lie in the kernel. Set $f_j=L(u_j)$ for $1\leq j\leq r$, and extend these vectors to a basis $(f_1,\ldots,f_n)$ of $\mathbb F^n$ using [Proposition 1.2.6](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:basis-extension).

Let $B=[u_1,\ldots,u_m]$ and $A=[f_1,\ldots,f_n]$, with all columns in standard coordinates. Both matrices are invertible because their columns are bases. Let $J$ denote the displayed block matrix. The first $r$ columns of both $CB$ and $AJ$ are $f_1,\ldots,f_r$, and all their remaining columns are zero. Hence $CB=AJ$. Multiplying on the right by $B^{-1}$ gives $C=AJB^{-1}$, as required. ◻

:::

::::

The displayed block order differs from the kernel-first form in [Equation 4.1](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#eq:linear-algebra-i:kernel-first-normal-form).

::statement{key="hw03:kernel-image-and-adapted-bases"}

## 4.4 Differentiation as a linear map {id="sec:linear-algebra-i:differentiation"}

The elements of a vector space can be functions. The space $C^0(\mathbb{R})$ consists of continuous real-valued functions on $\mathbb{R}$, while $C^1(\mathbb{R})$ consists of differentiable real-valued functions $f$ for which both $f$ and $f'$ are continuous. Both are vector spaces over $\mathbb{R}$. In this example, no finite-dimensional assumption is imposed.

Differentiation gives a map between these spaces,

$$
D:C^1(\mathbb{R})\longrightarrow C^0(\mathbb{R}),\qquad D(f)=f'.
$$

It is linear by the sum and constant factor rules of differentiation. For $f_1,f_2,f\in C^1(\mathbb{R})$ and $r\in\mathbb{R}$,

$$
\begin{aligned}
    D(f_1+f_2)&=(f_1+f_2)'=f_1'+f_2'=D(f_1)+D(f_2),\\
    D(rf)&=(rf)'=rf'=rD(f).
  \end{aligned}
$$

Thus differentiation preserves addition and scalar multiplication. Its inputs and outputs are functions. [§ 1.2](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#sec:linear-algebra-i:linear-combinations-and-bases) discusses bases beyond finite dimension, including function spaces.

### Polynomial differentiation {id="polynomial-differentiation"}

The following exercises express differentiation in polynomial bases and examine its kernel, image, rank, and nullity.

::statement{key="hw03:polynomial-differentiation-powers"}

::statement{key="hw04:polynomial-differentiation"}

[Figure 4.6](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#fig:linear-algebra-i:polynomial-differentiation) shows how differentiation acts on the monomials in the given basis.

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:polynomial-differentiation"}

[![The basis images for D\:\\mathcal P\_3(\\mathbb\{R\})\\to\\mathcal P\_2(\\mathbb\{R\}). Constants go to zero. The other monomials lose one degree.](/notes/linear-algebra/figures/polynomial-differentiation.svg){.tikz-diagram}](/notes/linear-algebra/figures/polynomial-differentiation.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 4.6. The basis images for $D:\mathcal P_3(\mathbb{R})\to\mathcal P_2(\mathbb{R})$. Constants go to zero. The other monomials lose one degree.

:::

::::

:::::
