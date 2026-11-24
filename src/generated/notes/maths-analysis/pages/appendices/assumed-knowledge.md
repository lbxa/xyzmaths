---
title: "Assumed knowledge"
group: "Appendices"
order: 17
page: "147"
outline: [{"id": "sec:appendix:map-properties", "title": "B.1 Injective, surjective, and bijective maps", "level": 2}, {"id": "functions-domains-and-codomains", "title": "Functions, domains, and codomains", "level": 3}, {"id": "surjectivity", "title": "Surjectivity", "level": 3}, {"id": "injectivity", "title": "Injectivity", "level": 3}, {"id": "bijectivity", "title": "Bijectivity", "level": 3}, {"id": "examples-in-euclidean-spaces", "title": "Examples in Euclidean spaces", "level": 3}, {"id": "an-injective-inclusion-of-a-plane.", "title": "An injective inclusion of a plane.", "level": 5}, {"id": "a-surjective-coordinate-projection.", "title": "A surjective coordinate projection.", "level": 5}, {"id": "a-bijective-coordinate-swap.", "title": "A bijective coordinate swap.", "level": 5}, {"id": "sec:appendix:divisibility", "title": "B.2 Divisibility, primes, and greatest common divisors", "level": 2}, {"id": "divisibility-and-multiples", "title": "Divisibility and multiples", "level": 3}, {"id": "greatest-common-divisors-and-lowest-terms", "title": "Greatest common divisors and lowest terms", "level": 3}, {"id": "prime-divisors-and-euclids-lemma", "title": "Prime divisors and Euclid’s lemma", "level": 3}, {"id": "how-the-prime-root-contradiction-uses-gcd", "title": "How the prime-root contradiction uses GCD", "level": 3}]
---

# Appendix B. Assumed knowledge {id="ch:appendix:assumed-knowledge"}

This appendix recalls elementary ideas used throughout the notes. The main text states the definitions it needs before using them. The explanations and examples here provide a fuller reminder.

## B.1 Injective, surjective, and bijective maps {id="sec:appendix:map-properties"}

### Functions, domains, and codomains {id="functions-domains-and-codomains"}

Let $f:A\to B$ be a function, also called a map. The set $A$ is its *domain*, and $B$ is its *codomain*. Every element of $A$ has exactly one output in $B$. This requirement alone does not say whether every element of $B$ is reached or whether two different inputs can have the same output.

The *image* of $f$ consists of the outputs that are actually reached,

$$
f(A)=\{f(a)\mid a\in A\}\subseteq B.
$$

If $b=f(a)$, we call $a$ a *preimage* of $b$. An element of the codomain may have no preimage, one preimage, or several preimages. The domain and codomain are part of the function, so they must be specified when deciding whether a map has any of the following properties. :span[]{id="index:function:2"}:span[]{id="index:image-of-a-function:1"}:span[]{id="index:preimage:1"}

### Surjectivity {id="surjectivity"}

The map $f$ is *surjective*, or *onto*, if every element of the codomain is the output of at least one input. Equivalently,

$$
\forall b\in B\quad \exists a\in A\quad f(a)=b.
$$

In terms of the image, this says $f(A)=B$. Different inputs may have the same output. In the middle panel of [Figure B.1](/notes/maths-analysis/appendices/assumed-knowledge/#fig:recall:map-properties), every codomain element receives an arrow, and two inputs share an output. :span[]{id="index:surjective-map:1"}

### Injectivity {id="injectivity"}

The map $f$ is *injective*, or *one-to-one*, if distinct inputs have distinct outputs. Equivalently, for any $a_1,a_2\in A$,

$$
f(a_1)=f(a_2)\quad\Longrightarrow\quad a_1=a_2.
$$

[^56] Each codomain element has at most one input mapping to it. Some codomain elements may have no such input, as the left panel of [Figure B.1](/notes/maths-analysis/appendices/assumed-knowledge/#fig:recall:map-properties) shows. :span[]{id="index:injective-map:1"}

:::notes{id="footnotes-55"}

[^56]: As a mnemonic, think of the *in* in *injective* as a reminder to check the *inputs*. Different inputs must remain distinguishable through their outputs.

:::

### Bijectivity {id="bijectivity"}

The map $f$ is *bijective* if it is both injective and surjective. Every codomain element then has exactly one input mapping to it. This gives a one-to-one correspondence between the entire domain and codomain, as in the right panel of [Figure B.1](/notes/maths-analysis/appendices/assumed-knowledge/#fig:recall:map-properties). Bijectivity imposes both conditions, so it is stronger than either condition alone. For a bijection, the *inverse function* $f^{-1}:B\to A$ sends each $b\in B$ to its unique preimage. Thus

$$
f^{-1}(f(a))=a\quad(a\in A),\qquad
  f(f^{-1}(b))=b\quad(b\in B).
$$

:span[]{id="index:bijective-map:1"}:span[]{id="index:inverse-function:1"}

::::figure{id="fig:recall:map-properties"}

[![Three maps between finite sets. Each dot is an element. The left map is injective and leaves an output unused. The middle map is surjective, but two inputs share an output. The right map is bijective and reaches every output exactly once. The ellipses enclose the elements of each set. Arrows show the function f, and gray shading marks its image f(A). The comparisons give the relative cardinalities of the domain and codomain.](/notes/maths-analysis/figures/function-cardinality.svg){.tikz-diagram}](/notes/maths-analysis/figures/function-cardinality.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure B.1. Three maps between finite sets. Each dot is an element. The left map is injective and leaves an output unused. The middle map is surjective, but two inputs share an output. The right map is bijective and reaches every output exactly once. The ellipses enclose the elements of each set. Arrows show the function $f$, and gray shading marks its image $f(A)$. The comparisons give the relative cardinalities of the domain and codomain.

:::

::::

### Examples in Euclidean spaces {id="examples-in-euclidean-spaces"}

The same definitions apply to maps between spaces such as $\mathbb{R}^2$ and $\mathbb{R}^3$. The domain and codomain are part of each example.

##### An injective inclusion of a plane. {id="an-injective-inclusion-of-a-plane."}

Consider

$$
Z:\mathbb{R}^2\to\mathbb{R}^3,\qquad Z(x,y)=(x,y,0).
$$

Different pairs retain their distinct first two coordinates, so $Z$ is injective. Its image is the $xy$-plane. It is not surjective onto $\mathbb{R}^3$, since an output with a nonzero third coordinate is never reached. [Figure B.2](/notes/maths-analysis/appendices/assumed-knowledge/#fig:recall:plane-inclusion) shows a pair and its image in that plane. If we instead took the codomain to be the $xy$-plane itself, the same assignment would be bijective. This is why the codomain matters.

::::figure{id="fig:recall:plane-inclusion"}

[![Schematic inclusion Z\:\\mathbb\{R\}^2\\to\\mathbb\{R\}^3. The shaded region depicts part of the xy-plane, which continues beyond the drawing. The marked input maps to a point in this plane. Distinct input coordinates remain distinct after inclusion.](/notes/maths-analysis/figures/map-plane-inclusion.svg){.tikz-diagram}](/notes/maths-analysis/figures/map-plane-inclusion.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure B.2. Schematic inclusion $Z:\mathbb{R}^2\to\mathbb{R}^3$. The shaded region depicts part of the $xy$-plane, which continues beyond the drawing. The marked input maps to a point in this plane. Distinct input coordinates remain distinct after inclusion.

:::

::::

##### A surjective coordinate projection. {id="a-surjective-coordinate-projection."}

Consider

$$
U:\mathbb{R}^3\to\mathbb{R}^2,\qquad U(x,y,z)=(y,z).
$$

Every pair $(y,z)$ is attained, for instance from $(0,y,z)$, so $U$ is surjective. It is not injective, since changing $x$ leaves the output unchanged. [Figure B.3](/notes/maths-analysis/appendices/assumed-knowledge/#fig:recall:coordinate-projection) shows inputs differing in the $x$-direction sharing an output.

::::figure{id="fig:recall:coordinate-projection"}

[![Schematic projection U\:\\mathbb\{R\}^3\\to\\mathbb\{R\}^2. The marked inputs lie on a line parallel to the x-axis and have the same y,z coordinates. They map to the same pair. Every pair in the codomain is attained.](/notes/maths-analysis/figures/map-coordinate-projection.svg){.tikz-diagram}](/notes/maths-analysis/figures/map-coordinate-projection.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure B.3. Schematic projection $U:\mathbb{R}^3\to\mathbb{R}^2$. The marked inputs lie on a line parallel to the $x$-axis and have the same $y,z$ coordinates. They map to the same pair. Every pair in the codomain is attained.

:::

::::

##### A bijective coordinate swap. {id="a-bijective-coordinate-swap."}

Consider

$$
B:\mathbb{R}^2\to\mathbb{R}^2,\qquad B(x,y)=(y,x).
$$

Each output $(a,b)$ has exactly one preimage, namely $(b,a)$. Thus $B$ is bijective. Swapping coordinates again recovers the original input. [Figure B.4](/notes/maths-analysis/appendices/assumed-knowledge/#fig:recall:coordinate-swap) shows the reflection across the line $x=y$.

::::figure{id="fig:recall:coordinate-swap"}

[![Schematic coordinate swap in \\mathbb\{R\}^2. The dashed diagonal in each coordinate system is x=y. The marked point and its image have exchanged coordinates. Each output has exactly one input.](/notes/maths-analysis/figures/map-coordinate-swap.svg){.tikz-diagram}](/notes/maths-analysis/figures/map-coordinate-swap.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure B.4. Schematic coordinate swap in $\mathbb{R}^2$. The dashed diagonal in each coordinate system is $x=y$. The marked point and its image have exchanged coordinates. Each output has exactly one input.

:::

::::

## B.2 Divisibility, primes, and greatest common divisors {id="sec:appendix:divisibility"}

### Divisibility and multiples {id="divisibility-and-multiples"}

For integers $d\ne0$ and $a$, the notation $d\mid a$, read “$d$ divides $a$,” means

$$
a=md\quad\text{for some }m\in\mathbb{Z}.
$$

When $d>0$ and $a\ge0$, this says that $m$ groups of size $d$ make up $a$. For example, $3\mid12$ because $12=4\cdot3$. The multiplier $m$ may also be zero or negative. In particular, $3\mid0$ because $0=0\cdot3$, and $3\mid-12$ because $-12=(-4)\cdot3$.

For $a\ne0$, we can rearrange the defining equation as $d=a/m$ with a nonzero integer $m$. The product form $a=md$ also handles $a=0$, when $m=0$. The notation $d\nmid a$ means that there is no integer multiplier. Thus $3\nmid10$, since $10/3\notin\mathbb{Z}$. :span[]{id="index:divisibility:1"}:span[]{id="index:multiple:1"}

### Greatest common divisors and lowest terms {id="greatest-common-divisors-and-lowest-terms"}

For integers $a,b$ that are not both zero, their *greatest common divisor*, written $\gcd(a,b)$, is the largest positive integer dividing both of them. For example, the positive common divisors of $12$ and $18$ are $1,2,3,6$, so

$$
\gcd(12,18)=6.
$$

The integers $a,b$ are *coprime*, or *relatively prime*, when $\gcd(a,b)=1$. If a prime $p$ divides both $a$ and $b$, it is a positive common divisor, so

$$
\gcd(a,b)\ge p>1.
$$

Every rational number can be written as $a/b$ with $a,b\in\mathbb{Z}$, $b>0$, and $\gcd(a,b)=1$. This is a representation in *lowest terms*, obtained by dividing numerator and denominator by their GCD. Being rational, or even being a prime integer, does not make every representation reduced. For example,

$$
3=\frac31=\frac62,\qquad
  \gcd(3,1)=1,\quad\gcd(6,2)=2.
$$

We choose a lowest-terms representation when an argument needs coprime numerator and denominator. :span[]{id="index:greatest-common-divisor:1"}:span[]{id="index:coprime-integers:1"}:span[]{id="index:lowest-terms:1"}

### Prime divisors and Euclid’s lemma {id="prime-divisors-and-euclids-lemma"}

A *prime* is an integer $p>1$ whose only positive divisors are $1$ and $p$. Euclid’s lemma, proved in [Lemma 1.2.2](/notes/maths-analysis/analysis-i/sets-and-foundations/#thm:analysis-i:euclid-prime-divisors), states that for $a,b\in\mathbb{Z}$,

$$
p\mid ab\quad\Longrightarrow\quad
  p\mid a\quad\text{or}\quad p\mid b.
$$

In particular, $p\mid a^2$ implies $p\mid a$, since $a^2=a\cdot a$. Repeated application gives $p\mid a^k\Longrightarrow p\mid a$ for every positive integer $k$. The prime hypothesis is essential. For instance, $6\mid2\cdot3$, but $6$ divides neither $2$ nor $3$. :span[]{id="index:prime-number:1"}:span[]{id="index:euclid-s-lemma:1"}

### How the prime-root contradiction uses GCD {id="how-the-prime-root-contradiction-uses-gcd"}

In [Exercise 1.11.2](/notes/maths-analysis/analysis-i/sets-and-foundations/#ex:hw01:prime-roots), $p$ is prime and we suppose for a contradiction that $\sqrt p$ has a lowest-terms representation,

$$
\sqrt p=\frac ab,\qquad
  a,b\in\mathbb{Z},\quad b>0,\quad\gcd(a,b)=1.
$$

The [full solution](/notes/maths-analysis/appendices/exercise-solutions/#sol:hw01:prime-roots) uses Euclid’s lemma to establish both $p\mid a$ and $p\mid b$. These conclusions force

$$
\gcd(a,b)\ge p>1,
$$

contradicting the choice $\gcd(a,b)=1$. Rationality would have allowed a lowest-terms representation, so this contradiction proves that $\sqrt p$ is irrational. Throughout the argument, $p$ is prime. The rationality of $\sqrt p$ is the assumption being contradicted.
