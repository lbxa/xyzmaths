---
title: "Multilinear algebra and determinants"
group: "Linear Algebra I"
order: 11
part: "Part I · Linear Algebra I"
page: "65"
outline: [{"id": "sec:linear-algebra-i:oriented-area-and-volume", "title": "5.1 Oriented area and volume", "level": 2}, {"id": "parallelograms-and-their-area", "title": "Parallelograms and their area", "level": 3}, {"id": "oriented-area-and-bilinearity", "title": "Oriented area and bilinearity", "level": 3}, {"id": "the-determinant-of-a-two-by-two-matrix", "title": "The determinant of a two-by-two matrix", "level": 3}, {"id": "oriented-volume", "title": "Oriented volume", "level": 3}, {"id": "sec:linear-algebra-i:permutations", "title": "5.2 Permutations", "level": 2}, {"id": "permutations-and-composition", "title": "Permutations and composition", "level": 3}, {"id": "parity-and-the-sign-function", "title": "Parity and the sign function", "level": 3}, {"id": "extending-the-sign-to-all-maps", "title": "Extending the sign to all maps", "level": 3}, {"id": "sec:linear-algebra-i:antisymmetric-multilinear-functions", "title": "5.3 Antisymmetric multilinear functions", "level": 2}, {"id": "multilinearity-and-antisymmetry", "title": "Multilinearity and antisymmetry", "level": 3}, {"id": "expansion-in-a-basis", "title": "Expansion in a basis", "level": 3}, {"id": "normalization-and-uniqueness", "title": "Normalization and uniqueness", "level": 3}, {"id": "sec:linear-algebra-i:determinant", "title": "5.4 Determinant", "level": 2}, {"id": "sec:linear-algebra-i:determinant-computation", "title": "Computation of determinant", "level": 3}, {"id": "sec:linear-algebra-i:determinant-properties", "title": "Determinant properties", "level": 3}, {"id": "sec:linear-algebra-i:permutation-matrices", "title": "Permutation matrices", "level": 3}]
---

# Chapter 5. Multilinear algebra and determinants {id="ch:linear-algebra-i:determinants"}

Oriented area and volume lead to the determinant. Their algebraic properties are described by antisymmetric multilinear functions, whose coordinate expansions use the signs of permutations.

## 5.1 Oriented area and volume {id="sec:linear-algebra-i:oriented-area-and-volume"}

### Parallelograms and their area {id="parallelograms-and-their-area"}

Let $V$ be a two-dimensional real vector space. The parallelogram spanned by $v_1,v_2\in V$ is

$$
P(v_1,v_2)=\{av_1+bv_2\mid 0\leq a,b\leq1\}.
$$

[Figure 5.1](/notes/linear-algebra/linear-algebra-i/determinants/#fig:linear-algebra-i:determinant-parallelogram) shows its two generating vectors and a point given by such a linear combination.

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:determinant-parallelogram"}

[![A parallelogram spanned by v\_1,v\_2, shown schematically. The interior point has the form av\_1+bv\_2.](/notes/linear-algebra/figures/determinant-parallelogram.svg){.tikz-diagram}](/notes/linear-algebra/figures/determinant-parallelogram.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.1. A parallelogram spanned by $v_1,v_2$, shown schematically. The interior point has the form $av_1+bv_2$.

:::

::::

:::::

Fix an ordered basis $E=(e_1,e_2)$ and normalize the area of $P(e_1,e_2)$ to be $1$. If

$$
v_1=ae_1+he_2,\qquad v_2=we_1,\qquad w>0,
$$

then $w$ and $h$ are width and signed-height coefficients in this basis. With area measured relative to the unit parallelogram, the ordinary area is

$$
\operatorname{area}P(v_1,v_2)=|h|w.
$$

For $h>0$, this is $hw$. For $h<0$, the parallelogram lies on the negative $e_2$-side of its base. Both configurations appear in [Figure 5.2](/notes/linear-algebra/linear-algebra-i/determinants/#fig:linear-algebra-i:determinant-signed-height).

::::figure{id="fig:linear-algebra-i:determinant-signed-height"}

[![Positive and negative height coefficients relative to the ordered basis, shown schematically. Ordinary area is \|h\|w. The oriented area A(v\_1,v\_2)=-hw changes sign.](/notes/linear-algebra/figures/determinant-signed-height.svg){.tikz-diagram}](/notes/linear-algebra/figures/determinant-signed-height.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.2. Positive and negative height coefficients relative to the ordered basis, shown schematically. Ordinary area is $|h|w$. The oriented area $A(v_1,v_2)=-hw$ changes sign.

:::

::::

### Oriented area and bilinearity {id="oriented-area-and-bilinearity"}

Choose the orientation for which $e_2$ lies counterclockwise of $e_1$, and normalize $A(e_1,e_2)=1$. Define the oriented area by

$$
A(v,w)=
  \begin{cases}
    \operatorname{area}P(v,w) & \text{if \((v,w)\) is positively oriented},\\
    -\operatorname{area}P(v,w) & \text{if \((v,w)\) is negatively oriented},\\
    0 & \text{if \(v,w\) are linearly dependent}.
  \end{cases}
$$

Thus $A(v,w)$ is positive when $w$ lies counterclockwise of $v$, and negative when $w$ lies clockwise of $v$.

Equal inputs are linearly dependent. The parallelogram $P(u,u)$ collapses to a line segment and has zero area, so $A(u,u)=0$ for every $u\in V$. In particular,

$$
A(v,v)=A(w,w)=0.
$$

In the signed-height configuration,

$$
A(v_1,v_2)=-hw.
$$

The ordinary area is $|A(v_1,v_2)|$. Under rescaling, ordinary area satisfies

$$
\begin{aligned}
    \operatorname{area}P(cv,w)&=|c|\operatorname{area}P(v,w),\\
    \operatorname{area}P(v,cw)&=|c|\operatorname{area}P(v,w).
  \end{aligned}
$$

:::div{id="thm:linear-algebra-i:bilinear-function" class="result definition"}

**Definition 5.1.1 (Bilinear function).** A function $B:V\times V\to\mathbb{R}$ is *bilinear* if it is linear in each input separately, with the other input fixed. Thus, for all $v,v_1,v_2,w,w_1,w_2\in V$ and $c\in\mathbb{R}$,

$$
\begin{aligned}
      B(v_1+v_2,w)&=B(v_1,w)+B(v_2,w),\\
      B(v,w_1+w_2)&=B(v,w_1)+B(v,w_2),\\
      B(cv,w)&=B(v,cw)=cB(v,w).
    \end{aligned}
$$

:::

The oriented area function $A$ is bilinear and satisfies these identities.

[Figure 5.3](/notes/linear-algebra/linear-algebra-i/determinants/#fig:linear-algebra-i:determinant-area-addition) illustrates addition with a common base. When the two vectors lie on opposite sides of the base, the same identity can be written as

$$
A(v_1,w)=A(v_1+v_2,w)-A(v_2,w).
$$

::::figure{id="fig:linear-algebra-i:determinant-area-addition"}

[![Addition with a common base w, shown schematically. The two input vectors lie on the same side of the base on the left, and on opposite sides on the right. Dashed sides represent v\_1+v\_2. The signed areas add in both cases.](/notes/linear-algebra/figures/determinant-area-addition.svg){.tikz-diagram}](/notes/linear-algebra/figures/determinant-area-addition.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.3. Addition with a common base $w$, shown schematically. The two input vectors lie on the same side of the base on the left, and on opposite sides on the right. Dashed sides represent $v_1+v_2$. The signed areas add in both cases.

:::

::::

Rescaling a vector multiplies the oriented area by the same scalar. In particular, replacing one vector by its negative reverses the sign. These operations appear in [Figure 5.4](/notes/linear-algebra/linear-algebra-i/determinants/#fig:linear-algebra-i:determinant-area-scaling). Linearity applies separately to each input. Doubling both inputs therefore multiplies the result by $2$ twice,

$$
A(2v,2w)=4A(v,w).
$$

::::figure{id="fig:linear-algebra-i:determinant-area-scaling"}

[![Rescaling and reflection of a parallelogram, shown schematically with c\>1. The identities are A(cv,w)=cA(v,w) and A(-v,w)=-A(v,w).](/notes/linear-algebra/figures/determinant-area-scaling.svg){.tikz-diagram}](/notes/linear-algebra/figures/determinant-area-scaling.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.4. Rescaling and reflection of a parallelogram, shown schematically with $c>1$. The identities are $A(cv,w)=cA(v,w)$ and $A(-v,w)=-A(v,w)$.

:::

::::

:::div{id="thm:linear-algebra-i:oriented-area-properties" class="result proposition"}

**Proposition 5.1.2 (Further properties of oriented area).** The oriented area function vanishes on equal inputs and is antisymmetric. For all $v,w\in V$,

$$
A(v,v)=0,\qquad A(w,v)=-A(v,w).
$$

:::

::::div{class="pending-review"}

:::div{class="proof"}

*Proof.* The parallelogram generated by $v,v$ collapses to a line segment, so $A(v,v)=0$ for every $v\in V$. The function $A$ is also bilinear. The [shared solution](/notes/linear-algebra/appendices/exercise-solutions/#sol:hw05:bilinear-antisymmetry) of [Exercise 5.1.3](/notes/linear-algebra/linear-algebra-i/determinants/#ex:hw05:bilinear-antisymmetry) proves that every real bilinear function vanishing on equal inputs is antisymmetric. Applying that argument to $A$ gives $A(w,v)=-A(v,w)$ for all $v,w\in V$, as required. ◻

:::

::::

These are additional properties of oriented area, rather than conditions in the definition of bilinearity. The area function is an antisymmetric bilinear tensor.

The following exercise asks for the antisymmetry argument.

::statement{key="hw05:bilinear-antisymmetry"}

### The determinant of a two-by-two matrix {id="the-determinant-of-a-two-by-two-matrix"}

Write $v=ae_1+ce_2$ and $w=be_1+de_2$. [Figure 5.5](/notes/linear-algebra/linear-algebra-i/determinants/#fig:linear-algebra-i:determinant-two-by-two-area) shows these coordinates and the parallelogram spanned by the two vectors.

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:determinant-two-by-two-area"}

[![Basis-coordinate schematic for v=ae\_1+ce\_2 and w=be\_1+de\_2. The shaded parallelogram has oriented area ad-bc, positive in the pictured configuration.](/notes/linear-algebra/figures/determinant-two-by-two-area.svg){.tikz-diagram}](/notes/linear-algebra/figures/determinant-two-by-two-area.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.5. Basis-coordinate schematic for $v=ae_1+ce_2$ and $w=be_1+de_2$. The shaded parallelogram has oriented area $ad-bc$, positive in the pictured configuration.

:::

::::

:::::

The equal-input property gives $A(e_1,e_1)=A(e_2,e_2)=0$. Bilinearity gives

$$
\begin{aligned}
    A(v,w)
      &=A(ae_1,be_1)+A(ce_2,be_1)\\
      &\quad+A(ae_1,de_2)+A(ce_2,de_2)\\
      &=abA(e_1,e_1)+bcA(e_2,e_1)\\
      &\quad+adA(e_1,e_2)+cdA(e_2,e_2)\\
      &=bcA(e_2,e_1)+adA(e_1,e_2)\\
      &=ad-bc.
  \end{aligned}
$$

The terms $abA(e_1,e_1)$ and $cdA(e_2,e_2)$ vanish because their inputs repeat. Antisymmetry gives $A(e_2,e_1)=-A(e_1,e_2)$, and the normalization is $A(e_1,e_2)=1$.

:::div{id="web:sections/linear-algebra-i/05-multilinear-algebra-and-determinants/01-oriented-area-and-volume:6834" class="result definition"}

**Definition 5.1.4.** The determinant of a two-by-two matrix is

$$
\det\begin{bmatrix}a&b\\c&d\end{bmatrix}=ad-bc.
$$

:::

In column notation,

$$
[v\ w]=[e_1\ e_2]\begin{bmatrix}a&b\\c&d\end{bmatrix}.
$$

Thus the determinant is the oriented area of the parallelogram whose generating vectors are the columns, measured in the normalized basis. Before imposing the normalization, the coordinate identity reads

$$
A(v,w)=A(e_1,e_2)(ad-bc).
$$

### Oriented volume {id="oriented-volume"}

Oriented volume extends the same idea from two inputs to three. In a three-dimensional real vector space, three independent vectors $a,b,c$ span the parallelepiped

$$
P(a,b,c)=\{sa+tb+uc\mid 0\leq s,t,u\leq1\}.
$$

Fix an ordered basis $(e_1,e_2,e_3)$ whose unit parallelepiped has volume $1$. Suppose $a,b$ lie in the plane spanned by $e_1,e_2$, and write

$$
c=ue_1+ve_2+he_3.
$$

Only the $e_3$-component takes $c$ off the base plane. Its coefficient $h$ is the height in these coordinates, as shown in [Figure 5.6](/notes/linear-algebra/linear-algebra-i/determinants/#fig:linear-algebra-i:determinant-parallelepiped). The ordinary volume is

$$
\operatorname{vol}P(a,b,c)=|h|\,|A(a,b)|.
$$

::::figure{id="fig:linear-algebra-i:determinant-parallelepiped"}

[![A parallelepiped with base spanned by a,b, shown schematically. The height coefficient is the e\_3-component of c. The drawing does not specify a Euclidean metric.](/notes/linear-algebra/figures/determinant-parallelepiped.svg){.tikz-diagram}](/notes/linear-algebra/figures/determinant-parallelepiped.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.6. A parallelepiped with base spanned by $a,b$, shown schematically. The height coefficient is the $e_3$-component of $c$. The drawing does not specify a Euclidean metric.

:::

::::

The oriented volume $\mathcal V(a,b,c)$ is normalized by

$$
\mathcal V(e_1,e_2,e_3)=1,
  \qquad |\mathcal V(a,b,c)|=\operatorname{vol}P(a,b,c).
$$

It is antisymmetric and linear in each of its three inputs. In the base-plane configuration,

$$
\mathcal V(a,b,c)=hA(a,b).
$$

This formula has no absolute values.

If $[v_1\ v_2\ v_3]=[e_1\ e_2\ e_3]M=EM$, then the determinant of the three-by-three matrix $M$ is characterized by

$$
\mathcal V(v_1,v_2,v_3)=\mathcal V(e_1,e_2,e_3)\det M.
$$

With the chosen normalization, $\det M=\mathcal V(v_1,v_2,v_3)$. The same algebraic construction extends to $n$ inputs through multilinear functions.

## 5.2 Permutations {id="sec:linear-algebra-i:permutations"}

### Permutations and composition {id="permutations-and-composition"}

Antisymmetry concerns the order of the inputs to an area or volume function. Permutations provide a way to describe every such reordering. Their signs will record the corresponding changes of orientation in the determinant formula.

::::div{id="web:sections/linear-algebra-i/05-multilinear-algebra-and-determinants/02-permutations:342" class="result definition"}

**Definition 5.2.1.** A permutation of $\{1,\ldots,n\}$ is a bijective map [^8]

$$
\sigma:\{1,\ldots,n\}\longrightarrow\{1,\ldots,n\}.
$$

Write $S_n$ for the set of all such permutations.

:::notes{id="footnotes-7"}

[^8]: **Permutations in combinatorics.** A permutation is an ordered arrangement of distinct objects, without repetition. The list $(\sigma(1),\ldots,\sigma(n))$ identifies a full arrangement with a bijection in $S_n$. There are $n$ choices for the first entry, $n-1$ for the next, and so on, giving $n!$ arrangements.
    
    For $0\le k\le n$, the binomial coefficient
    
    $$
    \binom{n}{k}=\frac{n!}{k!(n-k)!}
    $$
    
    counts unordered $k$-element subsets. Each subset has $k!$ orderings, so the number of ordered selections of $k$ distinct objects is
    
    $$
    k!\binom{n}{k}=\frac{n!}{(n-k)!},
    $$
    
    with $0!=1$. These same binomial coefficients appear in $(x+y)^n$. Choosing $k$ of the $n$ factors to contribute $y$ gives the term $\binom{n}{k}x^{n-k}y^k$.

:::

::::

Permutations reorder $n$ objects. Under composition, $S_n$ is a group. The identity permutation $\iota$ belongs to $S_n$, and the composition of two permutations is again a permutation. Every $\sigma\in S_n$ has an inverse satisfying

$$
\sigma\circ\sigma^{-1}=\sigma^{-1}\circ\sigma=\iota.
$$

Composition is associative.

:::div{id="web:sections/linear-algebra-i/05-multilinear-algebra-and-determinants/02-permutations:1753" class="result definition"}

**Definition 5.2.2.** A transposition switches two elements and leaves all the others unchanged. For $i\ne j$, the transposition $\tau_{ij}\in S_n$ is

$$
\tau_{ij}(k)=
    \begin{cases}
      j & \text{if \(k=i\)},\\
      i & \text{if \(k=j\)},\\
      k & \text{otherwise}.
    \end{cases}
$$

:::

:::div{id="web:sections/linear-algebra-i/05-multilinear-algebra-and-determinants/02-permutations:2079" class="result example"}

**Example 5.2.3.** The transposition $\tau_{24}\in S_4$ satisfies

$$
\tau_{24}(1)=1,\quad \tau_{24}(2)=4,\quad
    \tau_{24}(3)=3,\quad \tau_{24}(4)=2.
$$

:::

:::div{id="thm:linear-algebra-i:transposition-decomposition" class="result lemma"}

**Lemma 5.2.4 (Decomposition into transpositions).** Every permutation can be written as a composition of transpositions,

$$
\sigma=\tau_k\circ\cdots\circ\tau_1.
$$

The identity is the composition of zero transpositions.

:::

::::div{class="pending-review"}

:::div{class="proof"}

*Proof.* The identity already has the required empty decomposition. For a permutation $\sigma$ that is not the identity, choose $r$ with $\sigma(r)\ne r$, and put $s=\sigma(r)$. Compose on the left with $\tau_{rs}$. The new permutation fixes $r$, because

$$
(\tau_{rs}\circ\sigma)(r)=\tau_{rs}(s)=r.
$$

It also preserves every index previously fixed by $\sigma$. Such an index cannot be $r$, and it cannot be $s$, since $\sigma(s)=s=\sigma(r)$ would contradict injectivity. The transposition therefore leaves each previously fixed value unchanged.

Repeating this operation increases the number of fixed indices at each step, so after at most $n$ steps it produces the identity. Every transposition is its own inverse. Undoing these successive compositions consequently expresses the original $\sigma$ as a composition of transpositions. ◻

:::

::::

::::::div{id="web:sections/linear-algebra-i/05-multilinear-algebra-and-determinants/02-permutations:3514" class="result example"}

**Example 5.2.5.** The permutation $\sigma\in S_3$ given by

$$
\sigma(1)=2,\qquad \sigma(2)=3,\qquad \sigma(3)=1
$$

is $\sigma=\tau_{13}\circ\tau_{12}$. Here

$$
\begin{aligned}
      \tau_{12}(1)&=2,& \tau_{12}(2)&=1,& \tau_{12}(3)&=3,\\
      \tau_{13}(1)&=3,& \tau_{13}(2)&=2,& \tau_{13}(3)&=1.
    \end{aligned}
$$

The paths in [Figure 5.7](/notes/linear-algebra/linear-algebra-i/determinants/#fig:linear-algebra-i:permutation-composition) track each element through these two transpositions.

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:permutation-composition"}

[![Read from left to right, applying \\tau\_\{12\} first and \\tau\_\{13\} second. The resulting paths give 1\\mapsto2, 2\\mapsto3, and 3\\mapsto1.](/notes/linear-algebra/figures/permutation-composition.svg){.tikz-diagram}](/notes/linear-algebra/figures/permutation-composition.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.7. Read from left to right, applying $\tau_{12}$ first and $\tau_{13}$ second. The resulting paths give $1\mapsto2$, $2\mapsto3$, and $3\mapsto1$.

:::

::::

:::::

::::::

### Parity and the sign function {id="parity-and-the-sign-function"}

:::div{id="thm:linear-algebra-i:permutation-parity" class="result proposition"}

**Proposition 5.2.6 (Parity of a permutation).** A permutation cannot be both a composition of an even number of transpositions and a composition of an odd number of transpositions.

:::

::::div{class="pending-review"}

:::div{class="proof"}

*Proof.* For real numbers $a_1,\ldots,a_n$, define

$$
\Delta(a_1,\ldots,a_n)=\prod_{1\leq i<j\leq n}(a_j-a_i).
$$

An empty product is $1$. We first show that exchanging any two entries changes the sign of $\Delta$. Suppose their positions are $r<s$. The factor $a_s-a_r$ changes sign. For each index outside the interval from $r$ to $s$, the two factors involving that index and $r,s$ simply exchange places, leaving their product unchanged. For $r<j<s$, the two affected factors have product

$$
(a_j-a_r)(a_s-a_j).
$$

After the exchange, their product is

$$
(a_j-a_s)(a_r-a_j)=(a_s-a_j)(a_j-a_r),
$$

which is the same scalar. Every other factor is unchanged. Only the factor belonging to $r,s$ contributes a minus sign, proving the claim.

Now start with the list $(1,\ldots,n)$ and build $\sigma$ by composing transpositions on the left. At each stage, a transposition interchanges the two occurrences of its moved values in the current permutation list. The preceding calculation therefore shows that a decomposition with $k$ transpositions gives

$$
\Delta(\sigma(1),\ldots,\sigma(n))
      =(-1)^k\Delta(1,\ldots,n).
$$

The number $\Delta(1,\ldots,n)$ is nonzero, since every factor $j-i$ is positive. Thus $(-1)^k$ is determined by $\sigma$ itself. Any second decomposition must have the same parity, so an even decomposition and an odd decomposition cannot represent the same permutation. ◻

:::

::::

Consequently, the following definition does not depend on the chosen transposition decomposition. Different decompositions may have different lengths, but those lengths have the same parity.

:::div{id="web:sections/linear-algebra-i/05-multilinear-algebra-and-determinants/02-permutations:6403" class="result definition"}

**Definition 5.2.7.** The sign, or parity, of a permutation is the function $\varepsilon:S_n\to\{-1,1\}$. For a decomposition $\sigma=\tau_k\circ\cdots\circ\tau_1$ into transpositions,

$$
\varepsilon(\sigma)=
    \begin{cases}
      1 & \text{if \(k\) is even},\\
      -1 & \text{if \(k\) is odd}.
    \end{cases}
$$

:::

The sign function has the properties

$$
\begin{aligned}
    \varepsilon(\iota)&=1,\\
    \varepsilon(\tau)&=-1 &&\text{for every transposition \(\tau\)},\\
    \varepsilon(\sigma_2\circ\sigma_1)
      &=\varepsilon(\sigma_2)\varepsilon(\sigma_1),\\
    \varepsilon(\sigma^{-1})&=\varepsilon(\sigma).
  \end{aligned}
$$

::::div{class="pending-review"}

:::div{class="proof"}

*Verification of the first three identities.* The identity has a decomposition of length zero, so its sign is $1$. A transposition has a decomposition of length one, so its sign is $-1$. If $\sigma_1$ is a composition of $p$ transpositions and $\sigma_2$ is a composition of $q$ transpositions, concatenating the two decompositions expresses $\sigma_2\circ\sigma_1$ as a composition of $p+q$ transpositions. The definition of sign gives

$$
\varepsilon(\sigma_2\circ\sigma_1)
      =(-1)^{p+q}=(-1)^q(-1)^p
      =\varepsilon(\sigma_2)\varepsilon(\sigma_1).
$$

This proves the identity, transposition, and composition formulas. ◻

:::

::::

For the last property, reversing the order of the same transpositions gives the inverse,

$$
\sigma=\tau_1\circ\cdots\circ\tau_N
  \quad\Longrightarrow\quad
  \sigma^{-1}=\tau_N\circ\cdots\circ\tau_1.
$$

The sign function is uniquely determined by assigning sign $-1$ to every transposition and requiring multiplicativity under composition. Its existence depends on [Proposition 5.2.6](/notes/linear-algebra/linear-algebra-i/determinants/#thm:linear-algebra-i:permutation-parity).

### Extending the sign to all maps {id="extending-the-sign-to-all-maps"}

Let $T_n$ be the set of all maps

$$
\phi:\{1,\ldots,n\}\longrightarrow\{1,\ldots,n\}.
$$

Then $S_n\subseteq T_n$. Extend the sign function to $\varepsilon:T_n\to\{-1,0,1\}$ by keeping its existing values on $S_n$ and setting

$$
\varepsilon(\phi)=0\qquad\text{if \(\phi\notin S_n\)}.
$$

## 5.3 Antisymmetric multilinear functions {id="sec:linear-algebra-i:antisymmetric-multilinear-functions"}

Let $V$ be an $n$-dimensional real vector space. The oriented area and volume functions of [§ 5.1](/notes/linear-algebra/linear-algebra-i/determinants/#sec:linear-algebra-i:oriented-area-and-volume) share two properties. They are linear in each input separately, and reordering their inputs changes the value according to the sign of the permutation. We now formulate these properties for $n$ inputs and express them in a basis.

### Multilinearity and antisymmetry {id="multilinearity-and-antisymmetry"}

:::div{id="web:sections/linear-algebra-i/05-multilinear-algebra-and-determinants/03-antisymmetric-multilinear-functions:542" class="result definition"}

**Definition 5.3.1.** A function $A:V^n\to\mathbb{R}$ is multilinear if it is linear in each input while all other inputs are fixed. Thus, for each position $i$, vectors $t_1,\ldots,t_{i-1},t_{i+1},\ldots,t_n,v,w\in V$, and scalars $a,b\in\mathbb{R}$,

$$
\begin{aligned}
      &A(t_1,\ldots,t_{i-1},av+bw,t_{i+1},\ldots,t_n)\\
      &\quad=aA(t_1,\ldots,t_{i-1},v,t_{i+1},\ldots,t_n)\\
      &\qquad+bA(t_1,\ldots,t_{i-1},w,t_{i+1},\ldots,t_n).
    \end{aligned}
$$

:::

:::div{id="web:sections/linear-algebra-i/05-multilinear-algebra-and-determinants/03-antisymmetric-multilinear-functions:1031" class="result definition"}

**Definition 5.3.2.** A function $A:V^n\to\mathbb{R}$ is antisymmetric if interchanging any two inputs changes its sign. For the transposition $\tau_{ij}$,

$$
A(v_{\tau_{ij}(1)},\ldots,v_{\tau_{ij}(n)})
      =-A(v_1,\ldots,v_n).
$$

:::

If two inputs are equal, interchanging them leaves the input unchanged. Antisymmetry therefore gives

$$
A(v_1,\ldots,v_n)=-A(v_1,\ldots,v_n),
$$

so $A(v_1,\ldots,v_n)=0$.

For $\sigma=\tau_k\circ\cdots\circ\tau_1$, repeated antisymmetry gives

$$
\begin{aligned}
    A(v_{\sigma(1)},\ldots,v_{\sigma(n)})
      &=(-1)^kA(v_1,\ldots,v_n)\\
      &=\varepsilon(\sigma)A(v_1,\ldots,v_n).
  \end{aligned}
$$

If $\phi\in T_n\setminus S_n$, two of the indices $\phi(1),\ldots,\phi(n)$ agree, so the corresponding value of $A$ is zero. With the extended sign function, both cases are expressed by

:::div{id="eq:linear-algebra-i:antisymmetric-reindexing" class="equation"}

$$
A(v_{\phi(1)},\ldots,v_{\phi(n)})
    =\varepsilon(\phi)A(v_1,\ldots,v_n),\qquad \phi\in T_n.\tag{5.1}
$$

:::

:::div{id="thm:linear-algebra-i:alternating-antisymmetric" class="result proposition"}

**Proposition 5.3.3 (Alternating and antisymmetric multilinear functions).** A multilinear function on a real vector space is antisymmetric if and only if it vanishes whenever two inputs are equal. Such a multilinear function is also called alternating.

:::

::::div{class="pending-review"}

:::div{class="proof"}

*Proof.* If two inputs of an antisymmetric function agree, interchanging them leaves the value unchanged and also negates it. Over $\mathbb{R}$, the value must therefore be zero.

Conversely, suppose the multilinear function vanishes whenever two inputs agree. If it has at most one input, both conditions are vacuous. Otherwise, choose any two input positions and fix every other input. Let $B(u,v)$ denote the resulting bilinear function of the two remaining inputs. The vanishing hypothesis gives $B(u,u)=B(v,v)=B(u+v,u+v)=0$. Expanding the last expression,

$$
\begin{aligned}
      0=B(u+v,u+v)
        &=B(u,u)+B(u,v)+B(v,u)+B(v,v)\\
        &=B(u,v)+B(v,u).
    \end{aligned}
$$

Hence $B(v,u)=-B(u,v)$. The chosen positions and fixed inputs were arbitrary, so exchanging any two inputs negates the original function. It is antisymmetric. ◻

:::

::::

Antisymmetric multilinear functions with $n$ inputs give the algebraic description of oriented volume on an $n$-dimensional space.

### Expansion in a basis {id="expansion-in-a-basis"}

For a linear map, its values on a basis determine its values everywhere. Here multilinearity lets us expand every input in a basis. Antisymmetry then removes all terms that repeat a basis vector.

Let $E=(e_1,\ldots,e_n)$ be a basis of $V$. Write

$$
v_j=\sum_{i=1}^n b^i_j e_i,\qquad 1\leq j\leq n.
$$

Expanding the first input by linearity gives

$$
A(v_1,\ldots,v_n)=\sum_{k_1=1}^n b^{k_1}_1 A(e_{k_1},v_2,\ldots,v_n).
$$

Expanding each remaining input in turn yields

:::div{id="eq:linear-algebra-i:multilinear-basis-expansion" class="equation"}

$$
A(v_1,\ldots,v_n)
    =\sum_{k_1=1}^n\cdots\sum_{k_n=1}^n
      b^{k_1}_1\cdots b^{k_n}_n A(e_{k_1},\ldots,e_{k_n}).\tag{5.2}
$$

:::

Each tuple $(k_1,\ldots,k_n)$ determines a map $\phi\in T_n$ by $\phi(j)=k_j$. The same sum can therefore be written as

$$
A(v_1,\ldots,v_n)
    =\sum_{\phi\in T_n}b^{\phi(1)}_1\cdots b^{\phi(n)}_n
      A(e_{\phi(1)},\ldots,e_{\phi(n)}).
$$

Now assume $A$ is also antisymmetric. Terms with repeated indices vanish, and every remaining index tuple is a permutation of $(1,\ldots,n)$. Using [Equation 5.1](/notes/linear-algebra/linear-algebra-i/determinants/#eq:linear-algebra-i:antisymmetric-reindexing),

$$
A(e_{\phi(1)},\ldots,e_{\phi(n)})
    =\varepsilon(\phi)A(e_1,\ldots,e_n).
$$

Consequently,

:::div{id="eq:linear-algebra-i:antisymmetric-basis-expansion" class="equation"}

$$
\begin{aligned}
    A(v_1,\ldots,v_n)
      &=A(e_1,\ldots,e_n)
        \sum_{\phi\in T_n}\varepsilon(\phi)
          b^{\phi(1)}_1\cdots b^{\phi(n)}_n\\
      &=A(e_1,\ldots,e_n)
        \sum_{\sigma\in S_n}\varepsilon(\sigma)
          b^{\sigma(1)}_1\cdots b^{\sigma(n)}_n.
  \end{aligned}\tag{5.3}
$$

:::

The second equality uses $\varepsilon(\phi)=0$ outside $S_n$. Thus $A$ is determined by its value on the ordered basis.

### Normalization and uniqueness {id="normalization-and-uniqueness"}

:::div{id="thm:linear-algebra-i:normalized-volume-function" class="result theorem"}

**Theorem 5.3.4 (Normalized volume function).** For every $c\in\mathbb{R}$, there is a unique antisymmetric multilinear function $A:V^n\to\mathbb{R}$ satisfying

$$
A(e_1,\ldots,e_n)=c.
$$

:::

::::div{class="pending-review"}

:::div{class="proof"}

*Proof.* If $n=0$, there is only the empty input tuple. Assigning it the value $c$ gives the unique function, and multilinearity and antisymmetry have no input positions to check. Assume henceforth that $n\geq1$.

For each $v_j$, write its unique basis expansion as $v_j=\sum_{i=1}^n b^i_j e_i$, and define

$$
A(v_1,\ldots,v_n)
      =c\sum_{\sigma\in S_n}\varepsilon(\sigma)
        \prod_{j=1}^n b^{\sigma(j)}_j.
$$

The coordinate functions of $v_j$ are linear, because addition and scalar multiplication act on its basis coefficients. Every product in the sum contains exactly one coordinate from each input. With all other inputs fixed, that product is therefore linear in the remaining input. The finite sum is consequently multilinear.

To check antisymmetry, exchange input positions $r,s$, and let $\tau=\tau_{rs}$. The new coordinate array has entries $\widetilde b^i_j=b^i_{\tau(j)}$. Reordering the scalar factors gives

$$
\begin{aligned}
      \prod_{j=1}^n\widetilde b^{\sigma(j)}_j
        &=\prod_{j=1}^n b^{\sigma(j)}_{\tau(j)}\\
        &=\prod_{\ell=1}^n b^{(\sigma\circ\tau)(\ell)}_\ell.
    \end{aligned}
$$

The substitution $\rho=\sigma\circ\tau$ is a bijection of $S_n$, and the sign identities give $\varepsilon(\rho)=-\varepsilon(\sigma)$. Thus the sum defining the value on the exchanged inputs is $-A(v_1,\ldots,v_n)$. For $n=1$, there are no two positions to exchange, so this condition is vacuous.

On the input $(e_1,\ldots,e_n)$, the coordinate in row $i$, column $j$ is $1$ when $i=j$ and $0$ otherwise. All terms in the defining sum vanish except the identity permutation’s term, whose coordinate product and sign are both $1$. Hence $A(e_1,\ldots,e_n)=c$, proving existence.

Finally, [Equation 5.3](/notes/linear-algebra/linear-algebra-i/determinants/#eq:linear-algebra-i:antisymmetric-basis-expansion) shows that any antisymmetric multilinear function with this basis value must have exactly the displayed formula. The constructed function is therefore unique. ◻

:::

::::

In particular, there is a unique such function normalized by

$$
A(e_1,\ldots,e_n)=1.
$$

If $B$ is any other antisymmetric multilinear function with $n$ inputs, then

$$
B=cA,\qquad c=B(e_1,\ldots,e_n).
$$

## 5.4 Determinant {id="sec:linear-algebra-i:determinant"}

Let $(e_1,\ldots,e_n)$ be the standard basis of $\mathbb{R}^n$. By [Theorem 5.3.4](/notes/linear-algebra/linear-algebra-i/determinants/#thm:linear-algebra-i:normalized-volume-function), there is a unique antisymmetric multilinear function

$$
D:(\mathbb{R}^n)^n\longrightarrow\mathbb{R},\qquad D(e_1,\ldots,e_n)=1.
$$

For columns $v_j=(b^1_j,\ldots,b^n_j)^T$, its formula is

$$
\begin{aligned}
    D(v_1,\ldots,v_n)
      &=\sum_{\phi\in T_n}\varepsilon(\phi)
        b^{\phi(1)}_1\cdots b^{\phi(n)}_n\\
      &=\sum_{\sigma\in S_n}\varepsilon(\sigma)
        b^{\sigma(1)}_1\cdots b^{\sigma(n)}_n.
  \end{aligned}
$$

:::div{id="web:sections/linear-algebra-i/05-multilinear-algebra-and-determinants/04-determinant:608" class="result definition"}

**Definition 5.4.1.** Let $M$ be a real $n$-by-$n$ matrix with columns $C_1,\ldots,C_n$. Its determinant is

$$
\det M=D(C_1,\ldots,C_n).
$$

:::

Writing $M=(b^i_j)$, with upper index $i$ for the row and lower index $j$ for the column, gives the permutation formula

:::div{id="eq:linear-algebra-i:determinant-permutation-formula" class="equation"}

$$
\det M=\sum_{\sigma\in S_n}\varepsilon(\sigma)
    b^{\sigma(1)}_1\cdots b^{\sigma(n)}_n.\tag{5.4}
$$

:::

Each term selects one entry from every column. Since $\sigma$ is a permutation, the selected rows are also all distinct. The equivalent row-indexed expression is

$$
\det M=\sum_{\sigma\in S_n}\varepsilon(\sigma)
    b^1_{\sigma(1)}\cdots b^n_{\sigma(n)}.
$$

Replacing each permutation by its inverse matches the products in these two sums, and the sign is unchanged by taking inverses. For $n=2$, this agrees with the oriented-area formula $ad-bc$. For $n=3$, it agrees with the normalized oriented volume.

### Computation of determinant {id="sec:linear-algebra-i:determinant-computation"}

Each column of $M$ can be written in terms of the standard basis,

$$
c_k=e_1M^1_k+\cdots+e_nM^n_k.
$$

The determinant can be computed by applying the antisymmetric and multilinear properties of $D$ to

$$
\begin{aligned}
    \det(M)&=D(c_1,\ldots,c_n)\\
      &=D(e_1M^1_1+\cdots+e_nM^n_1,\ldots,
        e_1M^1_n+\cdots+e_nM^n_n).
  \end{aligned}
$$

The following exercises apply this column expansion.

::statement{key="hw05:two-by-two-determinant"}

::statement{key="hw05:three-by-three-triangular-determinant"}

::statement{key="hw05:upper-triangular-determinant"}

::statement{key="hw05:four-by-four-determinant"}

### Determinant properties {id="sec:linear-algebra-i:determinant-properties"}

The following exercises examine how the determinant changes when its columns are modified.

::statement{key="hw05:negating-a-matrix"}

::statement{key="hw05:column-addition"}

### Permutation matrices {id="sec:linear-algebra-i:permutation-matrices"}

::statement{key="hw05:permutation-matrices"}
