---
title: "Vector spaces and bases"
group: "Linear Algebra I"
order: 7
part: "Part I · Linear Algebra I"
page: "17"
outline: [{"id": "sec:linear-algebra-i:vector-spaces", "title": "1.1 Vector spaces", "level": 2}, {"id": "sec:linear-algebra-i:linear-combinations-and-bases", "title": "1.2 Linear combinations and bases", "level": 2}, {"id": "linear-combinations-and-span", "title": "Linear combinations and span", "level": 3}, {"id": "linear-independence", "title": "Linear independence", "level": 3}, {"id": "bases-and-dimension", "title": "Bases and dimension", "level": 3}, {"id": "subspaces", "title": "Subspaces", "level": 3}, {"id": "sec:linear-algebra-i:zorns-lemma", "title": "Zorn’s lemma and infinite-dimensional bases", "level": 3}, {"id": "sec:linear-algebra-i:bases-to-transformations", "title": "From bases to linear transformations", "level": 3}, {"id": "exercises-on-span-bases-and-subspaces", "title": "Exercises on span, bases, and subspaces", "level": 3}]
---

::anchor{id="part:linear-algebra-i"}

# Chapter 1. Vector spaces and bases {id="ch:linear-algebra-i:vector-spaces-and-bases"}

Linear algebra begins with two operations, addition and scalar multiplication. Together they let us construct vectors by linear combinations. A span records which vectors can be constructed, while a basis gives each vector a unique description. These ideas also explain linear transformations. Such a transformation carries a linear combination to the same combination of the transformed vectors. Choosing bases turns that rule into a matrix calculation. This chapter develops the language behind that connection.

## 1.1 Vector spaces {id="sec:linear-algebra-i:vector-spaces"}

Let $\mathbb F$ be a field, such as $\mathbb{R}$ or $\mathbb{C}$.

::::div{id="web:sections/linear-algebra-i/01-vector-spaces-and-bases/01-vector-spaces:125" class="result definition"}

**Definition 1.1.1.** A vector space over $\mathbb F$ is a nonempty set $V$ with addition and scalar multiplication

$$
\begin{aligned}
      V\times V&\longrightarrow V,& (v,w)&\longmapsto v+w,\\
      \mathbb F\times V&\longrightarrow V,& (a,v)&\longmapsto av,
    \end{aligned}
$$

satisfying the following axioms for all $u,v,w\in V$ and $a,b\in\mathbb F$.

*Addition.*

:::list

1.  **(A1)** $(u+v)+w=u+(v+w)$ (associativity).

2.  **(A2)** $v+w=w+v$ (commutativity).

3.  **(A3)** There is a vector $0_V\in V$ such that $v+0_V=v$ for every $v\in V$.

4.  **(A4)** Each $v\in V$ has an inverse $-v\in V$ with $v+(-v)=0_V$.

:::

*Scalar multiplication.*

:::list

1.  **(S1)** $(ab)v=a(bv)$ (associativity).

2.  **(S2)** $(a+b)v=av+bv$ (distributivity over scalar addition).

3.  **(S3)** $a(v+w)=av+aw$ (distributivity over vector addition).

4.  **(S4)** $1v=v$ (scalar identity).

:::

::::

The elements of $V$ are vectors, and the elements of $\mathbb F$ are scalars. The vector $0_V$ is called the zero vector or the origin. We write it as $0$ when the vector space is clear from the context.

The word *vector* describes an object’s role under addition and scalar multiplication. Coordinate columns, functions, and matrices can all play this role. The axioms specify the common structure that allows us to work with these different objects in the same way.

In the real plane, vector addition can be drawn by completing a parallelogram, as in [Figure 1.1](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#fig:linear-algebra-i:vector-addition).

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:vector-addition"}

[![A real-plane schematic of v+w. The dashed sides are translated copies of v and w.](/notes/linear-algebra/figures/vector-addition.svg){.tikz-diagram}](/notes/linear-algebra/figures/vector-addition.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 1.1. A real-plane schematic of $v+w$. The dashed sides are translated copies of $v$ and $w$.

:::

::::

:::::

The parallelogram makes addition visible in the plane. In a function space or a matrix space, the same operation is performed on functions or matrices. The expression $av+bw$ therefore has a meaning beyond arrows in a drawing. It is a construction using the two vector-space operations, which we study next through linear combinations and span.

::statement{key="hw01:axiom-consequences"}

## 1.2 Linear combinations and bases {id="sec:linear-algebra-i:linear-combinations-and-bases"}

### Linear combinations and span {id="linear-combinations-and-span"}

A linear combination is one result of choosing vectors and coefficients. The span collects every result obtainable when those coefficients and the finite selection of vectors are allowed to vary.

:::div{id="web:sections/linear-algebra-i/01-vector-spaces-and-bases/02-linear-combinations-and-bases:340" class="result definition"}

**Definition 1.2.1.** A linear combination of $v_1,\ldots,v_n\in V$ is a vector of the form

$$
a_1v_1+\cdots+a_nv_n,\qquad a_1,\ldots,a_n\in\mathbb F.
$$

For $S\subseteq V$, its span, denoted $\operatorname{span}(S)$, is the set of all finite linear combinations of elements of $S$. Explicitly,

$$
\operatorname{span}(S)=
      \left\{\sum_{j=1}^n a_jv_j\;\middle|\;
        \begin{gathered}
          n\ge0,\quad a_1,\ldots,a_n\in\mathbb F,\\
          v_1,\ldots,v_n\in S
        \end{gathered}
      \right\},
$$

where $n$ ranges over the nonnegative integers. The subset $S$ need not be finite, but each linear combination uses finitely many of its vectors.

:::

The empty linear combination is the zero vector, so $\operatorname{span}(\varnothing)=\{0\}$. A vector space is *finite-dimensional* when it has a finite spanning set. Unless explicitly stated otherwise, the vector spaces in this book are finite-dimensional.

:span[Set equalities can be proved by checking both inclusions. The template in [Subsection\* B.1](/notes/linear-algebra/appendices/assumed-knowledge/#sec:linear-algebra-i:set-equality-proofs) recalls this method.]{class="pending-review"}

### Linear independence {id="linear-independence"}

:::div{id="web:sections/linear-algebra-i/01-vector-spaces-and-bases/02-linear-combinations-and-bases:1525" class="result definition"}

**Definition 1.2.2.** A subset $S\subseteq V$ is linearly independent if, for every finite selection of distinct vectors $v_1,\ldots,v_n\in S$,

$$
a_1v_1+\cdots+a_nv_n=0
    \quad\Longrightarrow\quad
    a_1=\cdots=a_n=0.
$$

The empty set is linearly independent.

:::

Equivalently, coefficients in a linear combination of distinct vectors from an independent set are unique. If

$$
a_1v_1+\cdots+a_nv_n=b_1v_1+\cdots+b_nv_n,
$$

then $a_j=b_j$ for each $j$. Thus independence answers a different question from spanning. Spanning asks whether a vector can be constructed from the chosen vectors. Independence asks whether two different coefficient choices can construct the same vector.

:::div{id="web:sections/linear-algebra-i/01-vector-spaces-and-bases/02-linear-combinations-and-bases:2245" class="result definition"}

**Definition 1.2.3.** A subset is linearly dependent if some finite selection of distinct vectors from it satisfies

$$
a_1v_1+\cdots+a_nv_n=0
$$

with at least one coefficient nonzero.

:::

[Figure 1.2](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#fig:linear-algebra-i:span-and-dependence) compares two-vector configurations in $\mathbb{R}^2$. A dependent pair lies on a line through zero. An independent pair supplies two directions in the plane.

::::figure{id="fig:linear-algebra-i:span-and-dependence"}

[![Real-plane schematics. On the left, independent vectors span the plane. On the right, the nonzero vectors are scalar multiples, so their span is one line.](/notes/linear-algebra/figures/span-and-dependence.svg){.tikz-diagram}](/notes/linear-algebra/figures/span-and-dependence.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 1.2. Real-plane schematics. On the left, independent vectors span the plane. On the right, the nonzero vectors are scalar multiples, so their span is one line.

:::

::::

### Bases and dimension {id="bases-and-dimension"}

:::div{id="web:sections/linear-algebra-i/01-vector-spaces-and-bases/02-linear-combinations-and-bases:3028" class="result definition"}

**Definition 1.2.4.** A basis of $V$ is a linearly independent subset that spans $V$. The dimension of a finite-dimensional vector space is the number of vectors in a basis.

:::

Every finite-dimensional vector space has a basis, as [Proposition 1.2.6](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:basis-extension) will show. The general existence result is proved in [Theorem 1.2.10](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:basis-existence). The zero vector space has the empty basis. The three standard coordinate vectors span $\mathbb{R}^3$ and are independent, so $\dim\mathbb{R}^3=3$.

More generally, a basis $\{v_1,\ldots,v_n\}$ of $\mathbb{R}^n$ allows every vector in $\mathbb{R}^n$ to be written uniquely as $a_1v_1+\cdots+a_nv_n$. The spanning property guarantees that the representation exists, and linear independence makes its coefficients unique.

An ordered basis makes these coefficients into coordinates. For example, with an ordered basis $E=(e_1,e_2)$ of a real two-dimensional space,

$$
v=xe_1+ye_2
$$

identifies $v$ by the coordinate column $(x,y)^T$. [Figure 1.3](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#fig:linear-algebra-i:basis-coordinate-grid) shows how repeated steps in the two basis directions build a coordinate grid. The lines need not meet at right angles. Uniqueness of the coefficients, rather than the angles in the drawing, makes this a coordinate system.

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:basis-coordinate-grid"}

[![A real-plane schematic in the ordered basis E=(e\_1,e\_2). The marked vector has coordinates (2,1)^T, since it is two steps in the e\_1 direction and one in the e\_2 direction. Only integer grid lines are drawn.](/notes/linear-algebra/figures/basis-coordinate-grid.svg){.tikz-diagram}](/notes/linear-algebra/figures/basis-coordinate-grid.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 1.3. A real-plane schematic in the ordered basis $E=(e_1,e_2)$. The marked vector has coordinates $(2,1)^T$, since it is two steps in the $e_1$ direction and one in the $e_2$ direction. Only integer grid lines are drawn.

:::

::::

:::::

:::div{id="thm:linear-algebra-i:comparison-independent-spanning" class="result theorem"}

**Theorem 1.2.5 (Comparison of independent and spanning sets).** Let $T$ be a finite spanning set of a vector space $V$. Every linearly independent subset $S\subseteq V$ is finite, and

$$
|S|\leq|T|.
$$

:::

::::div{class="pending-review"}

:::div{class="proof"}

*Proof.* Write $n=|T|$. If $n=0$, then $V=\{0\}$, whose only independent subset is empty. Suppose $n>0$ and that $S$ contains distinct vectors $u_1,\ldots,u_{n+1}$. We will replace the vectors of $T$, one at a time, by $u_1,\ldots,u_n$, preserving the spanning property.

At step $j$, write the current spanning list as

$$
u_1,\ldots,u_{j-1},w_j,\ldots,w_n.
$$

Its first $j-1$ entries are the vectors already chosen from $S$. Since the list spans $V$, there are coefficients such that

$$
u_j=\sum_{i=1}^{j-1}a_i u_i+\sum_{i=j}^n b_iw_i.
$$

At least one $b_i$ is nonzero. Otherwise $u_j$ would be a linear combination of $u_1,\ldots,u_{j-1}$, contradicting the independence of the chosen vectors from $S$. For an index $\ell$ with $b_\ell\ne0$, solve this equation for $w_\ell$. It expresses $w_\ell$ as a linear combination of $u_j$ and the other vectors in the current list. Replacing $w_\ell$ by $u_j$ therefore leaves a spanning list. Reorder the remaining $w_i$ to prepare the next step.

After $n$ steps, $u_1,\ldots,u_n$ span $V$. In particular, $u_{n+1}$ is a linear combination of them, again contradicting independence. Thus $S$ cannot contain $n+1$ distinct vectors. It is consequently finite and has at most $n=|T|$ elements. ◻

:::

::::

::::div{class="pending-review"}

:::div{id="thm:linear-algebra-i:basis-extension" class="result proposition"}

**Proposition 1.2.6 (Finite basis extension).** Every linearly independent subset of a finite-dimensional vector space $V$ is contained in a finite basis of $V$. In particular, $V$ has a finite basis.

:::

:::div{class="proof"}

*Proof.* Let $S\subseteq V$ be independent, and choose a finite spanning set $T=\{t_1,\ldots,t_n\}$ of $V$. By [Theorem 1.2.5](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:comparison-independent-spanning), $S$ is finite. Starting with $S$, consider $t_1,\ldots,t_n$ in order. Add $t_j$ to the current set precisely when it is outside its span.

Each addition preserves independence. Indeed, if the current independent set is $\{v_1,\ldots,v_q\}$ and

$$
a_1v_1+\cdots+a_qv_q+bt_j=0,
$$

a nonzero $b$ would express $t_j$ as a linear combination of the current vectors. Since $t_j$ was outside their span, $b=0$, and independence then gives $a_1=\cdots=a_q=0$.

The resulting set is finite, independent, and contains $S$. Every element of $T$ belongs to its span, whether it was added or was already in the span when considered. The resulting set therefore spans $V$ and is a basis. Taking $S=\varnothing$ gives the final assertion. ◻

:::

:::div{id="thm:linear-algebra-i:basis-cardinality" class="result corollary"}

**Corollary 1.2.7 (The size of a finite basis).** Any two bases of a finite-dimensional vector space have the same finite number of elements. Thus its dimension is well-defined.

:::

:::div{class="proof"}

*Proof.* Any basis is finite by [Theorem 1.2.5](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:comparison-independent-spanning), applied to a finite spanning set of the space. If $E$ and $F$ are two bases, the same theorem gives $|E|\leq|F|$, since $E$ is independent and $F$ spans. Interchanging $E$ and $F$ gives $|F|\leq|E|$. Hence $|E|=|F|$. ◻

:::

::::

### Subspaces {id="subspaces"}

:::div{id="web:sections/linear-algebra-i/01-vector-spaces-and-bases/02-linear-combinations-and-bases:8380" class="result definition"}

**Definition 1.2.8.** A nonempty subset $T\subseteq V$ is a subspace if it is closed under linear combinations. That is, for $v,w\in T$ and $a,b\in\mathbb F$,

$$
av+bw\in T.
$$

A subspace inherits addition and scalar multiplication from $V$.

:::

Equivalently, every finite linear combination of elements of $T$ lies in $T$. Every subspace contains the zero vector. Choose $v,w\in T$, which is possible because $T$ is nonempty. Taking $a=b=0$ in the closure condition gives $0v+0w=0_V\in T$.

::::div{class="pending-review"}

:::div{id="thm:linear-algebra-i:finite-dimensional-subspaces" class="result proposition"}

**Proposition 1.2.9 (Subspaces of a finite-dimensional space).** If $T$ is a subspace of a finite-dimensional vector space $V$, then $T$ is finite-dimensional, and every basis of $T$ extends to a basis of $V$. Moreover,

$$
\dim T\leq\dim V,
    \qquad
    \dim T=\dim V\quad\Longleftrightarrow\quad T=V.
$$

:::

:::div{class="proof"}

*Proof.* Put $n=\dim V$. Every independent subset of $T$ is independent in $V$, so its size is at most $n$ by [Theorem 1.2.5](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:comparison-independent-spanning). The possible sizes of independent subsets of $T$ form a nonempty subset of $\{0,\ldots,n\}$, since the empty set is independent. Choose an independent subset $B\subseteq T$ of largest possible size.

If $B$ did not span $T$, there would be a vector $t\in T$ outside its span. Adjoining $t$ would preserve independence, by the coefficient argument in the proof of [Proposition 1.2.6](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:basis-extension). This contradicts the choice of $B$. Thus $B$ is a finite basis of $T$.

Every basis of $T$ is an independent subset of $V$, so [Proposition 1.2.6](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:basis-extension) extends it to a basis of $V$. Consequently $\dim T\leq\dim V$. If these dimensions are equal, the extended basis has no additional vectors. The original basis of $T$ then spans $V$, giving $T=V$. Conversely, $T=V$ immediately gives equality of their dimensions. ◻

:::

::::

### Zorn’s lemma and infinite-dimensional bases {id="sec:linear-algebra-i:zorns-lemma"}

In infinite-dimensional spaces, a basis $S$ is still linearly independent, and each vector is a *finite* linear combination of elements of $S$.

::::div{class="pending-review"}

The finite basis-extension argument examines a finite spanning set one vector at a time. For a space with no finite spanning set, we instead use a set-theoretic principle that guarantees a maximal independent set.

Let $\mathcal F$ be a nonempty family of sets, ordered by inclusion. A *chain* in $\mathcal F$ is a subfamily $\mathcal C$ such that any two of its members are comparable by inclusion. An *upper bound* for this chain is a member $U\in\mathcal F$ containing every member of $\mathcal C$. A member $M\in\mathcal F$ is *maximal* if no member of $\mathcal F$ properly contains $M$. Maximality does not require $M$ to contain every other member.

**Zorn’s lemma ([Zorn 1935](/notes/linear-algebra/references/#ref-Zorn1935TransfiniteAlgebra)).** If every chain in a nonempty family $\mathcal F$ has an upper bound in $\mathcal F$, then $\mathcal F$ has a maximal member.

We use this inclusion-ordered form of Zorn’s lemma as a set-theoretic prerequisite. It is equivalent to the axiom of choice. The finite-dimensional arguments above do not require this principle. In the basis-existence proof, the sets are independent subsets of $V$, and the upper bound for a chain will be its union. Maximality then forces the resulting independent set to span $V$.

:::div{id="thm:linear-algebra-i:basis-existence" class="result theorem"}

**Theorem 1.2.10 (Existence of a basis).** Every vector space has a basis.

:::

:::div{class="proof"}

*Proof.* Let $\mathcal I$ be the family of all linearly independent subsets of $V$, ordered by inclusion. This family is nonempty because $\varnothing\in\mathcal I$. We first show that every chain in $\mathcal I$ has an upper bound in $\mathcal I$.

For a nonempty chain $\mathcal C$, let $U=\bigcup_{A\in\mathcal C}A$. Every finite selection of vectors from $U$ lies in a single member of $\mathcal C$. Indeed, choose a chain member containing each vector and take the largest of these finitely many members, using their comparability. Since that member is independent, any zero linear combination of the selected vectors has all coefficients zero. Thus $U$ is independent and is an upper bound for $\mathcal C$. The empty chain has the independent upper bound $\varnothing$.

Zorn’s lemma now gives an inclusion-maximal independent subset $B\subseteq V$. Suppose $v\in V$ were outside $\operatorname{span}(B)$. In any relation

$$
av+b_1e_1+\cdots+b_qe_q=0,
    \qquad e_1,\ldots,e_q\in B
$$

with the $e_i$ distinct, a nonzero $a$ would express $v$ as a finite linear combination of vectors from $B$. Hence $a=0$, and independence of $B$ gives $b_1=\cdots=b_q=0$. Therefore $B\cup\{v\}$ would be independent, contradicting maximality. It follows that $B$ spans $V$ and is a basis. ◻

:::

::::

::::div{id="web:sections/linear-algebra-i/01-vector-spaces-and-bases/02-linear-combinations-and-bases:13578" class="result example"}

**Example 1.2.11.** The vector space $\mathcal P$ of polynomials in $x$ with real coefficients has the basis

$$
\{1,x,x^2,\ldots\}.
$$

:::div{class="pending-review"}

Every polynomial is a finite linear combination of these monomials. Such a combination is the zero polynomial only when all its coefficients are zero, so the monomials are independent as well as spanning.

:::

::::

For the vector space $C(\mathbb{R})$ of continuous functions $\mathbb{R}\to\mathbb{R}$, [Theorem 1.2.10](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:basis-existence) guarantees a basis. No explicit basis is constructed here. This example motivates the study of topological vector spaces.

### From bases to linear transformations {id="sec:linear-algebra-i:bases-to-transformations"}

The same linear combinations connect vector spaces to maps between them. A *linear map*, also called a *linear transformation*, is a map $L:V\to W$ between vector spaces over the same field that satisfies, for every $a,b\in\mathbb F$ and $v,w\in V$,

$$
L(av+bw)=aL(v)+bL(w).
$$

It preserves the way a vector is assembled. If $v=ae_1+be_2$, then

$$
L(v)=aL(e_1)+bL(e_2).
$$

The coefficients $a,b$ are retained, while the building blocks $e_1,e_2$ are replaced by their images. Since a basis describes every input uniquely, specifying its images determines a linear map everywhere.

In the real plane, consider the shear $S(x,y)=(x+y,y)$, illustrated in [Figure 1.4](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#fig:linear-algebra-i:shear-grid-overview). Its action on two basis vectors determines the action on the entire grid. The origin stays fixed, and repeated equal steps in a basis direction become repeated equal steps in its image direction. This is the geometric content of preserving linear combinations.

::::figure{id="fig:linear-algebra-i:shear-grid-overview"}

[![Schematic of S(x,y)=(x+y,y). The square grid becomes a parallelogram grid. Within each family, lines remain parallel and equally spaced, although angles change. The two arrows show the images of the standard basis vectors.](/notes/linear-algebra/figures/linear-map-grid-overview.svg){.tikz-diagram}](/notes/linear-algebra/figures/linear-map-grid-overview.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 1.4. Schematic of $S(x,y)=(x+y,y)$. The square grid becomes a parallelogram grid. Within each family, lines remain parallel and equally spaced, although angles change. The two arrows show the images of the standard basis vectors.

:::

::::

To calculate such an action, we choose output coordinates and record the coordinates of the basis-vector images as columns of a matrix. Matrix multiplication then forms their linear combination using the input coefficients. This is the link between the basis language of this chapter and the column calculations in [§ 2.1](/notes/linear-algebra/linear-algebra-i/matrices-and-vector-coordinates/#sec:linear-algebra-i:matrix-multiplication). The general definition of linearity and its grid interpretation are developed in [§ 3.2](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#sec:linear-algebra-i:linear-functions-and-maps), and [§ 3.3](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#sec:linear-algebra-i:change-of-basis-for-functions-and-maps) explains how the matrix records a map in chosen input and output bases.

### Exercises on span, bases, and subspaces {id="exercises-on-span-bases-and-subspaces"}

The following exercises apply the definitions to coordinate vectors, polynomials, functions, and sequences. The basis-extension question uses [Theorem 1.2.5](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#thm:linear-algebra-i:comparison-independent-spanning).

::statement{key="hw01:positive-real-vector-space"}

::statement{key="hw01:span-and-containing-subspaces"}

::statement{key="hw01:parameter-dependent-span"}

::statement{key="hw01:affine-solution-set"}

::statement{key="hw01:polynomial-interpolation"}

::statement{key="hw01:recursive-sequences"}

::statement{key="hw01:intersections-and-sums"}

::statement{key="hw01:basis-extension"}

::statement{key="hw01:span-and-independence-assertions"}

::statement{key="hw03:modified-bases-and-dependence"}

::statement{key="hw03:continuous-functions-infinite-dimension"}
