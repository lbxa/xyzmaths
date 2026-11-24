---
title: "Inner products and norms"
group: "Linear Algebra I"
order: 14
part: "Part I · Linear Algebra I"
page: "105"
outline: [{"id": "sec:linear-algebra-i:real-inner-products", "title": "8.1 Real inner products", "level": 2}, {"id": "the-dot-product", "title": "The dot product", "level": 3}, {"id": "the-abstract-definition", "title": "The abstract definition", "level": 3}, {"id": "why-the-real-field-matters", "title": "Why the real field matters", "level": 3}, {"id": "testing-the-defining-properties", "title": "Testing the defining properties", "level": 3}, {"id": "sec:linear-algebra-i:examples-of-inner-products", "title": "8.2 Examples of inner products", "level": 2}, {"id": "polynomials", "title": "Polynomials", "level": 3}, {"id": "trigonometric-polynomials", "title": "Trigonometric polynomials", "level": 3}, {"id": "matrices", "title": "Matrices", "level": 3}, {"id": "sec:linear-algebra-i:inner-product-nondegeneracy", "title": "8.3 Nondegeneracy", "level": 2}, {"id": "sec:linear-algebra-i:inner-product-norms-and-angles", "title": "8.4 Norms and angles", "level": 2}, {"id": "a-minimization-problem", "title": "A minimization problem", "level": 3}, {"id": "angles", "title": "Angles", "level": 3}, {"id": "sec:linear-algebra-i:orthogonality-and-coordinate-products", "title": "8.5 Orthogonality and coordinate inner products", "level": 2}, {"id": "an-inner-product-chosen-from-a-basis", "title": "An inner product chosen from a basis", "level": 3}]
---

# Chapter 8. Inner products and norms {id="ch:linear-algebra-i:inner-products-and-norms"}

An inner product gives a vector space additional structure. It allows us to measure lengths and angles and to speak of orthogonal vectors. The ordinary dot product is the prototype, but the same properties apply to spaces of polynomials, trigonometric polynomials, and matrices.

This chapter concerns real vector spaces and real inner products.

## 8.1 Real inner products {id="sec:linear-algebra-i:real-inner-products"}

### The dot product {id="the-dot-product"}

For columns $v,w\in\mathbb{R}^n$, the dot product sums the products of corresponding coordinates. Transposing a column gives a row, so

$$
v\cdot w=\sum_{j=1}^n v^jw^j=v^Tw=w^Tv=w\cdot v.
$$

The dot product is positive definite, symmetric, and linear in each input. These are the properties used to define an inner product on an abstract real vector space.

### The abstract definition {id="the-abstract-definition"}

[^9]

:::notes{id="footnotes-8"}

[^9]: Checking the properties in this order often makes proofs easier. Positive definiteness can rule out a candidate quickly. Once symmetry is established, linearity in the second argument implies linearity in the first. For real $a,b,c,d$ and $v_1,v_2\in V$, put $w=cv_1+dv_2$. Then
    
    $$
    \begin{aligned}
          &(av_1+bv_2,w)\\
          &\quad=(w,av_1+bv_2)\\
          &\quad=a(w,v_1)+b(w,v_2)\\
          &\quad=a(v_1,w)+b(v_2,w).
        \end{aligned}
    $$

:::

:::div{id="web:sections/linear-algebra-i/08-inner-products-and-norms/01-real-inner-products:974" class="result definition"}

**Definition 8.1.1.** An inner product on a real vector space $V$ is a function

$$
B:V\times V\longrightarrow\mathbb{R}
$$

with the following properties.

1.  It is positive definite, so

    $$
    B(v,v)\ge0,\qquad B(v,v)=0\quad\Longleftrightarrow\quad v=0.
    $$

2.  It is symmetric, so $B(v,w)=B(w,v)$.

3.  It is bilinear. For $a,b\in\mathbb{R}$ and $u,v,w\in V$,

    $$
    \begin{aligned}
              B(au+bv,w)&=aB(u,w)+bB(v,w),\\
              B(u,av+bw)&=aB(u,v)+bB(u,w).
            \end{aligned}
    $$

:::

We also write $(v,w)$ for $B(v,w)$. In this notation, parentheses denote an inner product when their value is a real scalar. The context distinguishes them from an ordered pair. In the multilinear terminology of [§ 5.3](/notes/linear-algebra/linear-algebra-i/determinants/#sec:linear-algebra-i:antisymmetric-multilinear-functions), an inner product is a tensor with two inputs. Both inner products and determinant functions are examples of multilinear functions.

### Why the real field matters {id="why-the-real-field-matters"}

For a nonzero vector, complex bilinearity conflicts with positive definiteness. If a complex bilinear function satisfied $(v,v)>0$ for a nonzero $v$, then

$$
(iv,iv)=i^2(v,v)=-(v,v)<0.
$$

Thus the real definition cannot be carried over unchanged to a nonzero complex vector space.

### Testing the defining properties {id="testing-the-defining-properties"}

::statement{key="hw07:coordinate-inner-products"}

::statement{key="hw07:tensor-inner-products"}

## 8.2 Examples of inner products {id="sec:linear-algebra-i:examples-of-inner-products"}

The dot product pairs coordinate columns by multiplying corresponding entries and adding the results. The following pairings use the same bilinear structure for functions and matrices.

### Polynomials {id="polynomials"}

:::div{id="web:sections/linear-algebra-i/08-inner-products-and-norms/02-examples-of-inner-products:306" class="result example"}

**Example 8.2.1.** Let $\mathcal P_n(\mathbb{R})$ be the real polynomials of degree at most $n$, including the zero polynomial. An inner product on this space is

$$
(p,q)=\int_{-1}^1 p(x)q(x)\,dx.
$$

In particular,

$$
(p,p)=\int_{-1}^1 p(x)^2\,dx\ge0,
    \qquad (p,p)=0\quad\Longleftrightarrow\quad p=0.
$$

:::

### Trigonometric polynomials {id="trigonometric-polynomials"}

:::div{id="web:sections/linear-algebra-i/08-inner-products-and-norms/02-examples-of-inner-products:684" class="result example"}

**Example 8.2.2.** Let $\mathcal T_n$ be the real trigonometric polynomials

$$
f(x)=\sum_{k=0}^n\bigl(a_k\cos(kx)+b_k\sin(kx)\bigr),
    \qquad a_k,b_k\in\mathbb{R}.
$$

On this space, use the inner product

$$
(f,g)=\int_0^{2\pi}f(x)g(x)\,dx.
$$

:::

Polynomial and trigonometric families are useful for approximating more general functions, with applications to partial differential equations. Inner products also play a role in analysis on infinite-dimensional function spaces.

### Matrices {id="matrices"}

:::div{id="web:sections/linear-algebra-i/08-inner-products-and-norms/02-examples-of-inner-products:1208" class="result definition"}

**Definition 8.2.3.** The trace of a matrix $A\in\mathrm M_{n\times n}(\mathbb{R})$ is the sum of its diagonal entries,

$$
\operatorname{tr}A=\sum_{i=1}^n A^i_i.
$$

:::

:::div{id="web:sections/linear-algebra-i/08-inner-products-and-norms/02-examples-of-inner-products:1394" class="result example"}

**Example 8.2.4.** On the vector space $\mathrm M_{n\times n}(\mathbb{R})$, an inner product is

$$
(A,B)=\operatorname{tr}(B^TA)
      =\sum_{i=1}^n\sum_{j=1}^n B^i_jA^i_j.
$$

Thus matrices are paired by summing the products of their corresponding entries.

:::

## 8.3 Nondegeneracy {id="sec:linear-algebra-i:inner-product-nondegeneracy"}

An inner product allows us to recognize a vector by its pairings with all other vectors.

:::div{id="thm:linear-algebra-i:inner-product-nondegeneracy" class="result proposition"}

**Proposition 8.3.1 (Nondegeneracy of an inner product).** For $v\in V$,

$$
(v,w)=0\text{ for every }w\in V
    \quad\Longleftrightarrow\quad v=0.
$$

:::

:::div{class="proof"}

*Proof.* If every pairing is zero, take $w=v$. Then $(v,v)=0$, so positive definiteness gives $v=0$. Conversely, bilinearity gives $(0,w)=0$ for every $w$. ◻

:::

:::div{id="thm:linear-algebra-i:inner-product-determines-vector" class="result proposition"}

**Proposition 8.3.2 (A vector is determined by its pairings).** If $v_1,v_2\in V$ satisfy

$$
(v_1,w)=(v_2,w)\qquad\text{for every }w\in V,
$$

then $v_1=v_2$.

:::

:::div{class="proof"}

*Proof.* Bilinearity gives $(v_1-v_2,w)=0$ for every $w\in V$. By [Proposition 8.3.1](/notes/linear-algebra/linear-algebra-i/inner-products-and-norms/#thm:linear-algebra-i:inner-product-nondegeneracy), $v_1-v_2=0$, hence $v_1=v_2$. ◻

:::

:::div{id="thm:linear-algebra-i:maps-determined-by-pairings" class="result corollary"}

**Corollary 8.3.3 (Maps determined by their pairings).** Let $W$ be a real inner-product space, and let $L_1,L_2:V\to W$ be maps. If

$$
(L_1(v),w)=(L_2(v),w)\qquad
    \text{for every }v\in V\text{ and }w\in W,
$$

then $L_1=L_2$.

:::

::::div{class="pending-review"}

:::div{class="proof"}

*Proof.* Fix an arbitrary $v\in V$. The hypothesis says that the two vectors $L_1(v),L_2(v)\in W$ have equal inner products with every $w\in W$. By [Proposition 8.3.2](/notes/linear-algebra/linear-algebra-i/inner-products-and-norms/#thm:linear-algebra-i:inner-product-determines-vector), they are equal. This holds for every input $v$, so the maps agree everywhere and $L_1=L_2$. ◻

:::

::::

Such comparisons are useful in the calculus of variations, where an identity can be tested by pairing with arbitrary vectors or functions.

## 8.4 Norms and angles {id="sec:linear-algebra-i:inner-product-norms-and-angles"}

:::div{id="web:sections/linear-algebra-i/08-inner-products-and-norms/04-norms-and-angles:88" class="result definition"}

**Definition 8.4.1.** The norm induced by a real inner product is the nonnegative number

$$
\lVert v\rVert=\sqrt{(v,v)}.
$$

:::

For the ordinary dot product on $\mathbb{R}^n$, this is the Euclidean magnitude. It is often convenient to work with its square,

$$
\lVert v\rVert^2=(v,v),\qquad
  \lVert v\rVert=0\quad\Longleftrightarrow\quad v=0.
$$

:::div{id="thm:linear-algebra-i:cauchy-schwarz" class="result theorem"}

**Theorem 8.4.2 (Cauchy–Schwarz inequality).** For any $v,w$ in a real inner-product space,

$$
\lvert(v,w)\rvert\le\lVert v\rVert\lVert w\rVert.
$$

Equality holds if and only if the pair $v,w$ is linearly dependent, including the cases in which either vector is zero.

:::

::::div{class="pending-review"}

:::div{class="proof"}

*Proof.* The minimization argument in [Exercise 8.4.3](/notes/linear-algebra/linear-algebra-i/inner-products-and-norms/#ex:hw07:minimization-and-cauchy-schwarz), proved in its solution on [the linked page](/notes/linear-algebra/appendices/exercise-solutions/#sol:hw07:minimization-and-cauchy-schwarz), uses only the inner-product axioms and establishes

$$
(v,w)^2\leq(v,v)(w,w)
$$

for all $v,w\in V$. It also proves that equality holds exactly when $v=sw$ or $w=sv$ for some real scalar $s$.

By the definition of the induced norm,

$$
\lvert(v,w)\rvert^2=(v,w)^2,
    \qquad
    \bigl(\lVert v\rVert\lVert w\rVert\bigr)^2=(v,v)(w,w).
$$

Both $\lvert(v,w)\rvert$ and $\lVert v\rVert\lVert w\rVert$ are nonnegative. Taking nonnegative square roots therefore gives the stated inequality and preserves equality.

To identify the equality condition, suppose the pair is dependent. Choose real $a,b$, not both zero, with $av+bw=0$. If $a\ne0$, then $v=-(b/a)w$. If $a=0$, then $b\ne0$ and $w=0=0v$. Conversely, $v=sw$ gives the nontrivial relation $v-sw=0$, and $w=sv$ gives $w-sv=0$. Thus the scalar-multiple alternatives are equivalent to linear dependence, including the zero-vector cases. This proves the full equality characterization. ◻

:::

::::

### A minimization problem {id="a-minimization-problem"}

Minimizing a squared norm leads to the Cauchy–Schwarz inequality in [Exercise 8.4.3](/notes/linear-algebra/linear-algebra-i/inner-products-and-norms/#ex:hw07:minimization-and-cauchy-schwarz). In this exercise, single bars denote the induced norm.

::statement{key="hw07:minimization-and-cauchy-schwarz"}

### Angles {id="angles"}

For nonzero $v,w$, the angle $\theta\in[0,\pi]$ is described by

$$
(v,w)=\lVert v\rVert\lVert w\rVert\cos\theta,
  \qquad
  \cos\theta=\frac{(v,w)}{\lVert v\rVert\lVert w\rVert}.
$$

The Cauchy–Schwarz inequality puts the displayed quotient in $[-1,1]$, so it determines an angle in $[0,\pi]$. This relation gives a notion of angle using the inner product, including when the vectors are functions or matrices. In the ordinary real plane, it has the geometric meaning shown in [Figure 8.1](/notes/linear-algebra/linear-algebra-i/inner-products-and-norms/#fig:linear-algebra-i:inner-product-angle).

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:inner-product-angle"}

[![A real-plane schematic with the ordinary dot product. The vectors have lengths \\lVert v\\rVert, \\lVert w\\rVert, and angle \\theta.](/notes/linear-algebra/figures/inner-product-angle.svg){.tikz-diagram}](/notes/linear-algebra/figures/inner-product-angle.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 8.1. A real-plane schematic with the ordinary dot product. The vectors have lengths $\lVert v\rVert$, $\lVert w\rVert$, and angle $\theta$.

:::

::::

:::::

## 8.5 Orthogonality and coordinate inner products {id="sec:linear-algebra-i:orthogonality-and-coordinate-products"}

:::div{id="web:sections/linear-algebra-i/08-inner-products-and-norms/05-orthogonality-and-coordinate-products:122" class="result definition"}

**Definition 8.5.1.** Vectors $v,w$ are orthogonal if $(v,w)=0$. A family $\{v_j\}$ is mutually orthogonal if

$$
(v_i,v_j)=0\qquad\text{whenever }i\ne j.
$$

It is orthonormal if it is mutually orthogonal and $(v_j,v_j)=1$ for every $j$.

:::

The Pythagorean identity can be expressed using only the properties of an inner product.

::statement{key="lec08:pythagorean-theorem"}

### An inner product chosen from a basis {id="an-inner-product-chosen-from-a-basis"}

A vector space does not come with a specified inner product. Fix an ordered basis $E=[e_1,\ldots,e_n]$. If $v=Ea$ and $w=Eb$, define

$$
(v,w)_E=a\cdot b=\sum_{j=1}^n a^jb^j.
$$

This makes $E$ an orthonormal basis for the chosen inner product,

$$
(e_i,e_j)_E=\delta_{ij}.
$$

Here $\delta_{ij}$ is the *Kronecker delta*, defined by

$$
\delta_{ij}=
  \begin{cases}
    1&\text{if }i=j,\\
    0&\text{if }i\ne j.
  \end{cases}
$$

The diagonal values $(e_i,e_i)_E=1$ say that the basis vectors have unit norm, while the off-diagonal values $(e_i,e_j)_E=0$ say that distinct basis vectors are orthogonal. Thus the single formula $(e_i,e_j)_E=\delta_{ij}$ records both parts of orthonormality. The matrix of these pairings is the identity matrix $I_n$, with the same $0$–$1$ pattern denoted by $\delta^i_j$ in [§ 7.2](/notes/linear-algebra/linear-algebra-i/eigenvalues-and-diagonalization/#sec:linear-algebra-i:characteristic-polynomials-and-similarity).

[^10]

:::notes{id="footnotes-9"}

[^10]: Leopold Kronecker’s paper on bilinear forms was read to the Berlin Academy on 15 October 1866. He describes discussions with Weierstrass about theta functions as the motivation for his algebraic investigation. In the paper, the delta expresses that a linear substitution followed by its inverse gives the identity. The same identity pattern appears here in orthonormal coordinates. ([Kronecker \[1866\] 1895, 145, 150](/notes/linear-algebra/references/#ref-Kronecker1895BilinearForms))

:::

Bilinearity makes the role of the delta explicit. For $v=Ea$ and $w=Eb$,

$$
\begin{aligned}
    (v,w)_E
      &=\sum_{i=1}^n\sum_{j=1}^n a^ib^j(e_i,e_j)_E\\
      &=\sum_{i=1}^n\sum_{j=1}^n a^ib^j\delta_{ij}\\
      &=\sum_{i=1}^n a^ib^i.
  \end{aligned}
$$

Only terms with equal indices survive. All cross terms vanish. Pairing with a single basis vector therefore reads off a coordinate,

$$
(v,e_i)_E=\sum_{j=1}^n a^j\delta_{ji}=a^i.
$$

Conversely, prescribing $(e_i,e_j)=\delta_{ij}$ determines the inner product by bilinearity. Choosing a basis therefore provides a way to equip the vector space with an inner product.
