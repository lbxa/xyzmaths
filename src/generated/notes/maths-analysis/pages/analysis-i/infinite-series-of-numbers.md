---
title: "Infinite series of numbers"
group: "Analysis I"
order: 9
part: "Part I · Analysis I"
page: "73"
outline: [{"id": "sec:analysis-i:number-series", "title": "4.1 Number series", "level": 2}, {"id": "the-harmonic-series", "title": "The harmonic series", "level": 3}, {"id": "the-geometric-series", "title": "The geometric series", "level": 3}, {"id": "sec:analysis-i:comparison-tests", "title": "4.2 Comparison tests", "level": 2}, {"id": "the-p-series", "title": "The p-series", "level": 3}, {"id": "exercises-on-comparison", "title": "Exercises on comparison", "level": 3}, {"id": "the-ratio-test", "title": "The ratio test", "level": 3}, {"id": "the-root-test", "title": "The root test", "level": 3}, {"id": "sec:analysis-i:dirichlet-test", "title": "4.3 Dirichlet test", "level": 2}, {"id": "conditional-convergence", "title": "Conditional convergence", "level": 2}, {"id": "the-cauchy-product", "title": "The Cauchy product", "level": 3}]
---

# Chapter 4. Infinite series of numbers {id="ch:analysis-i:infinite-series-of-numbers"}

A series converges when its sequence of partial sums converges. We begin with this definition and its Cauchy criterion, then use geometric series to control more complicated sums. Absolute convergence provides that control even when the terms have different signs.

## 4.1 Number series {id="sec:analysis-i:number-series"}

An infinite sum is defined through finite sums. This lets us use the sequence tools from the preceding chapter.

:::div{id="web:sections/analysis-i/04-infinite-series-of-numbers/01-number-series:175" class="result definition"}

**Definition 4.1.1.** Given real numbers $a_1,a_2,\ldots$, their *partial sums* are $S_n=\sum_{k=1}^n a_k$. The series $\sum_{k=1}^{\infty}a_k$ *converges* to $S\in\mathbb{R}$ if $S_n\to S$. If the partial sums have no finite limit, the series *diverges*.

:::

:::div{id="thm:analysis-i:series-cauchy" class="result theorem"}

**Theorem 4.1.2 (Cauchy criterion for series).** The series $\sum_{k=1}^{\infty}a_k$ converges if and only if

$$
\forall\varepsilon>0\ \exists N\in\mathbb{N}\quad
    m>n\ge N\ \Longrightarrow\
    \left|\sum_{k=n+1}^{m}a_k\right|<\varepsilon.
$$

:::

:::div{class="proof"}

*Proof.* For $m>n$, split $S_m$ after its first $n$ terms and subtract $S_n$. Using the definition of the partial sums gives

$$
\begin{aligned}
    S_m-S_n
      &=\sum_{k=1}^{m}a_k-\sum_{k=1}^{n}a_k\\
      &=\left(\sum_{k=1}^{n}a_k+\sum_{k=n+1}^{m}a_k\right)
        -\sum_{k=1}^{n}a_k\\
      &=\sum_{k=n+1}^{m}a_k.
  
\end{aligned}
$$

The shared terms $a_1,\ldots,a_n$ cancel. The first remaining term is $a_{n+1}$ and the last is $a_m$, so the remaining sum has $m-n$ terms. In particular, when $m=n+1$, it contains just $a_{n+1}$. Taking absolute values therefore gives

$$
|S_m-S_n|=\left|\sum_{k=n+1}^{m}a_k\right|.
$$

Thus the expression in the criterion measures the distance between two partial sums, using precisely the terms added after the $n$th one.

The restriction $m>n$ simply orders the two partial sums. Exchanging the indices gives the same absolute difference, and equal indices give zero. Thus checking $m>n\ge N$ is equivalent to checking every pair $m,n\ge N$. The criterion therefore says exactly that $(S_n)$ is Cauchy. By [Theorem 3.5.2](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#thm:analysis-i:cauchy-completeness), this is equivalent to convergence of $(S_n)$ in $\mathbb{R}$, which is the definition of convergence of the series. ◻

:::

:::div{id="thm:analysis-i:series-term-test" class="result proposition"}

**Proposition 4.1.3.** If $\sum_{n=1}^{\infty}a_n$ converges, then $a_n\to0$.

:::

:::div{class="proof"}

*Proof.* If $S_n\to S$, then $S_{n-1}\to S$ as well. Thus $a_n=S_n-S_{n-1}\to S-S=0$ by the difference rule for limits. ◻

:::

This condition is necessary but is not sufficient. The harmonic series provides the basic counterexample.

### The harmonic series {id="the-harmonic-series"}

Let $H_n=\sum_{k=1}^n1/k$. Although $1/n\to0$, for every $N\ge1$ we have

$$
H_{2N}-H_N=\sum_{k=N+1}^{2N}\frac1k
  \ge N\frac{1}{2N}=\frac12.
$$

There are $N$ terms in this block, each at least $1/(2N)$. Hence $(H_n)$ fails the Cauchy condition with $\varepsilon=1/2$, so the harmonic series diverges. Its partial sums are increasing. If they were bounded above, the monotone bounded sequence theorem would force convergence. They are therefore unbounded and tend to $+\infty$. [Figure 4.1](/notes/maths-analysis/analysis-i/infinite-series-of-numbers/#fig:harmonic-blocks) shows why each doubling contributes at least another $1/2$.

::::figure{id="fig:harmonic-blocks"}

[![Lower bounds for four harmonic blocks. A block of N terms has N strips of height 1/(2N), hence area 1/2. The actual terms are at least these heights, so the block sums do not shrink.](/notes/maths-analysis/figures/harmonic-blocks.svg){.tikz-diagram}](/notes/maths-analysis/figures/harmonic-blocks.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 4.1. Lower bounds for four harmonic blocks. A block of $N$ terms has $N$ strips of height $1/(2N)$, hence area $1/2$. The actual terms are at least these heights, so the block sums do not shrink.

:::

::::

### The geometric series {id="the-geometric-series"}

For $x\ne1$, multiplying a finite sum by $1-x$ gives

$$
(1-x)\sum_{k=0}^N x^k=1-x^{N+1},\qquad
  \sum_{k=0}^N x^k=\frac{1-x^{N+1}}{1-x}.
$$

If $|x|<1$, then $|x|^{N+1}\to0$ by the geometric-sequence estimate in [§ 3.1](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#sec:analysis-i:convergent-sequences), with $x=0$ immediate. Consequently

$$
\sum_{k=0}^{\infty}x^k=\frac{1}{1-x}\qquad(|x|<1).
$$

If $|x|\ge1$, the terms $x^k$ do not tend to zero, so the series diverges by [Proposition 4.1.3](/notes/maths-analysis/analysis-i/infinite-series-of-numbers/#thm:analysis-i:series-term-test).

The Cauchy criterion can also establish convergence when the terms alternate in sign.

::statement{key="hw04:alternating-series"}

## 4.2 Comparison tests {id="sec:analysis-i:comparison-tests"}

:::div{id="web:sections/analysis-i/04-infinite-series-of-numbers/02-comparison-tests:68" class="result definition"}

**Definition 4.2.1.** A series $\sum a_n$ is *absolutely convergent* if $\sum |a_n|$ converges.

:::

:::div{id="thm:analysis-i:series-comparison" class="result theorem"}

**Theorem 4.2.2 (Comparison with a majorant).** Suppose $|a_n|\le M_n$ for all sufficiently large $n$, where $M_n\ge0$ and $\sum M_n$ converges. Then $\sum |a_n|$ and $\sum a_n$ both converge.

:::

:::div{class="proof"}

*Proof.* Let $T_n=\sum_{k=1}^n M_k$. For $m>n$ beyond the index where the comparison holds, the triangle inequality gives

$$
\left|\sum_{k=n+1}^{m}a_k\right|
    \le\sum_{k=n+1}^{m}|a_k|
    \le\sum_{k=n+1}^{m}M_k=T_m-T_n.
$$

Since $(T_n)$ converges, its Cauchy property makes the right-hand side smaller than any given $\varepsilon>0$ when $m>n$ are sufficiently large. The Cauchy criterion proves convergence of $\sum a_n$. Applying the same argument to $|a_n|$ proves absolute convergence as well. ◻

:::

In particular, absolute convergence implies convergence by taking $M_n=|a_n|$. A finite number of early terms has no effect on convergence, because it only adds a fixed constant to all later partial sums.

### The $p$-series {id="the-p-series"}

For a real exponent $s>1$, consider $\sum_{n=1}^{\infty}1/n^s$. We use real powers with their usual exponent and order laws. Their construction extends the rational powers developed earlier.

The construction in [§ 1.11](/notes/maths-analysis/analysis-i/sets-and-foundations/#sec:analysis-i:roots-and-powers) defines rational powers. For irrational $s$, the arguments here assume that $n^s$ exists and obeys those order and exponent laws. They do not construct it. The definition and its exponent laws are established in [Definition 8.6.6](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:logarithm-real-powers).

Group its terms into blocks between consecutive powers of $2$. The block $2^j<n\le2^{j+1}$ has $2^j$ terms, and

$$
\sum_{n=2^j+1}^{2^{j+1}}\frac{1}{n^s}
  \le 2^j\frac{1}{(2^j)^s}=2^{-j(s-1)}.
$$

Writing $q=2^{1-s}<1$, every partial sum is bounded by

$$
1+\frac{1}{2^s}+\sum_{j=1}^{\infty}q^j<\infty.
$$

The positive partial sums increase, so the monotone bounded sequence theorem proves convergence. When $s\le1$, we have $n^{-s}\ge1/n$ for $n\ge1$. Comparison with the harmonic partial sums proves divergence. Thus the $p$-series converges exactly when $s>1$.

Euler’s evaluation $\sum_{n=1}^{\infty}1/n^2=\pi^2/6$ is stated here without proof. The argument above proves convergence, not that evaluation. [^28]

:::notes{id="footnotes-27"}

[^28]: How does this relate to Gabriel’s horn? Keep this question in mind for integration, where volume and surface area can be compared.

:::

### Exercises on comparison {id="exercises-on-comparison"}

These exercises use estimates of positive terms and partial sums. For the second, recall the eventual bounds supplied by the lower and upper limits in [§ 3.4](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#sec:analysis-i:upper-and-lower-limits).

::statement{key="hw04:shifted-root-series"}

::statement{key="hw04:lower-upper-comparison"}

### The ratio test {id="the-ratio-test"}

[^29]

:::notes{id="footnotes-28"}

[^29]: Cauchy’s 1821 treatment places root and ratio estimates among systematic convergence tests ([Cauchy 1821](/notes/maths-analysis/references/#ref-Cauchy1821), ch. VI). Their practical purpose is to compare a series tail with a geometric series. These nineteenth-century formulations belong to the effort to justify infinite operations. The limsup versions stated here are modern refinements of those estimates.

:::

:::div{id="thm:analysis-i:ratio-test" class="result theorem"}

**Theorem 4.2.5 (Ratio test).** Suppose $a_n\ne0$ for all sufficiently large $n$, and set $R_n=|a_{n+1}/a_n|$ on that tail. If $\limsup R_n<1$, then $\sum a_n$ converges absolutely. If $\liminf R_n>1$, then $\sum a_n$ diverges.

:::

:::div{class="proof"}

*Proof.* First suppose $R_0=\limsup R_n<1$. Choose $\rho$ with $R_0<\rho<1$. By the eventual-bound property in [§ 3.4](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#sec:analysis-i:upper-and-lower-limits), some $N$ satisfies $R_n\le\rho$ for every $n\ge N$. Thus

$$
|a_{n+1}|\le\rho|a_n|\quad(n\ge N),\qquad
    |a_{N+k}|\le|a_N|\rho^k\quad(k\ge0),
$$

where the second inequality follows by induction. The geometric majorant $\sum_{k=0}^{\infty}|a_N|\rho^k$ converges, so [Theorem 4.2.2](/notes/maths-analysis/analysis-i/infinite-series-of-numbers/#thm:analysis-i:series-comparison) proves absolute convergence.

Now suppose $\liminf R_n>1$. Choose $\rho>1$ below that lower limit. For some $N$, all $n\ge N$ satisfy $R_n\ge\rho$, hence $|a_{N+k}|\ge|a_N|\rho^k$. Since $a_N\ne0$, these terms do not tend to zero. The series diverges by [Proposition 4.1.3](/notes/maths-analysis/analysis-i/infinite-series-of-numbers/#thm:analysis-i:series-term-test). ◻

:::

[Figure 4.2](/notes/maths-analysis/analysis-i/infinite-series-of-numbers/#fig:geometric-bound-choice) highlights the choice in the first part of the proof. The upper bound must exceed the limsup, while still being small enough to produce a convergent geometric series.

:::::div{class="margin-figure"}

::::figure{id="fig:geometric-bound-choice"}

[![Choose \\rho in the open interval between R\_0=\\limsup R\_n and 1. The tail ratios are eventually below \\rho, and \\sum\\rho^k converges.](/notes/maths-analysis/figures/geometric-bound-choice.svg){.tikz-diagram}](/notes/maths-analysis/figures/geometric-bound-choice.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 4.2. Choose $\rho$ in the open interval between $R_0=\limsup R_n$ and $1$. The tail ratios are eventually below $\rho$, and $\sum\rho^k$ converges.

:::

::::

:::::

For a geometric series with $x\ne0$, the ratios equal $|x|$. The ratio test recovers absolute convergence when $|x|<1$. The case $x=0$ is immediate without forming ratios.

### The root test {id="the-root-test"}

:::div{id="thm:analysis-i:root-test" class="result theorem"}

**Theorem 4.2.6 (Root test).** If $\limsup_{n\to\infty}|a_n|^{1/n}<1$, then $\sum a_n$ converges absolutely.

:::

:::div{class="proof"}

*Proof.* Choose $\rho$ strictly between the upper limit and $1$. All sufficiently late terms satisfy $|a_n|^{1/n}\le\rho$, so $|a_n|\le\rho^n$. The geometric majorant $\sum\rho^n$ converges, and comparison proves the claim. ◻

:::

A limiting value of $1$ does not decide convergence. For example, both $1/n$ and $1/n^2$ have successive-term ratios tending to $1$ and $n$th-root limits equal to $1$, but only the second series converges.

The next exercise focuses on the divergence implications, using a lower limit to bound the late terms away from zero.

::statement{key="hw04:divergence-tests"}

## 4.3 Dirichlet test {id="sec:analysis-i:dirichlet-test"}

[^30]

:::notes{id="footnotes-29"}

[^30]: Dirichlet’s 1829 paper sought conditions under which a trigonometric series really represents a function ([Dirichlet 1829](/notes/maths-analysis/references/#ref-Dirichlet1829)). Controlling cancellation, rather than absolute values alone, is the idea behind the test bearing his name. Its impact is especially clear in Fourier analysis. The general series-test statement is reserved for the later mathematical treatment.

:::

## Conditional convergence {id="conditional-convergence"}

[^31] :anchor[]{id="sec:analysis-i:conditional-convergence"}

:::notes{id="footnotes-30"}

[^31]: In his 1854 work on trigonometric series, Riemann examined how a conditionally convergent series changes when its terms are reordered ([Riemann 1867, sec. 3](/notes/maths-analysis/references/#ref-Riemann1867)). The work was published after his death. This made the order of summation a mathematical hypothesis, with consequences for Fourier series and the distinction between absolute and conditional convergence.

:::

:::div{id="web:sections/analysis-i/04-infinite-series-of-numbers/04-conditional-convergence:460" class="result definition"}

**Definition 4.4.1.** A series is *conditionally convergent* if it converges but does not converge absolutely.

:::

::::div{id="ex:analysis-i:alternating-power-series" class="result example"}

**Example 4.4.2 (Alternating power series).** For every real $s>0$, the series

$$
\sum_{n=1}^{\infty}\frac{(-1)^n}{n^s}
$$

converges. Its even and odd partial sums give a direct way to see why.

:::div{class="proof"}

*Proof.* Put $u_n=1/n^s$ and $S_n=\sum_{j=1}^n(-1)^ju_j$. The positive terms $u_n$ decrease to zero. Indeed, for any $\varepsilon>0$, choosing $n>\varepsilon^{-1/s}$ gives $u_n<\varepsilon$. Consecutive partial sums of the same parity satisfy

$$
\begin{aligned}
      S_{2k+2}-S_{2k}&=u_{2k+2}-u_{2k+1}\le0,\\
      S_{2k+1}-S_{2k-1}&=u_{2k}-u_{2k+1}\ge0.
    
\end{aligned}
$$

Thus the even partial sums decrease and the odd partial sums increase. They are bounded, since

$$
-u_1\le S_{2k-1}\le S_{2k}\le S_2.
$$

By [Theorem 3.2.1](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#thm:analysis-i:monotone-convergence), both subsequences converge. Their difference is $S_{2k}-S_{2k-1}=u_{2k}\to0$, so their limits agree. Every sufficiently late partial sum belongs to one of these two subsequences and is therefore close to their common limit. This proves convergence of the full sequence $(S_n)$. ◻

:::

The series of absolute values is $\sum 1/n^s$. The $p$-series test therefore gives conditional convergence for $0<s\le1$ and absolute convergence for $s>1$. At $s=0$, the terms alternate between $-1$ and $1$ and do not tend to zero, so the series diverges.

::::

In particular, taking $s=1$ gives the alternating harmonic series

$$
\sum_{n=1}^{\infty}\frac{(-1)^n}{n}
  =-1+\frac12-\frac13+\frac14-\cdots.
$$

It converges by [Example 4.4.2](/notes/maths-analysis/analysis-i/infinite-series-of-numbers/#ex:analysis-i:alternating-power-series), but its absolute values form the divergent harmonic series. It is therefore conditionally convergent.

### The Cauchy product {id="the-cauchy-product"}

[^32]

:::notes{id="footnotes-31"}

[^32]: Cauchy’s 1821 *Cours d’analyse* treats multiplication of series under convergence of their absolute values ([Cauchy 1821](/notes/maths-analysis/references/#ref-Cauchy1821), ch. VI). The problem is to justify collecting infinitely many pairwise products into a new single series. This supplies the coefficient rule used in power-series multiplication, including the exponential addition law.

:::

Multiplying finite sums pairs every term from one sum with every term from the other. For infinite sums we must also justify how the resulting terms are grouped.

:::div{id="thm:analysis-i:cauchy-product" class="result definition"}

**Definition 4.4.3 (Cauchy product).** The *Cauchy product* of $\sum_{n=0}^{\infty}a_n$ and $\sum_{n=0}^{\infty}b_n$ is $\sum_{n=0}^{\infty}c_n$, where

$$
c_n=\sum_{k=0}^{n}a_kb_{n-k}.
$$

:::

The coefficient $c_n$ collects all pairs whose indices add to $n$. The first terms are

$$
c_0=a_0b_0,\qquad c_1=a_0b_1+a_1b_0,\qquad
  c_2=a_0b_2+a_1b_1+a_2b_0.
$$

:::div{id="thm:analysis-i:absolute-cauchy-product" class="result theorem"}

**Theorem 4.4.4 (Product of absolutely convergent series).** If $\sum a_n=A$ and $\sum b_n=B$ converge absolutely, their Cauchy product converges absolutely and

$$
\sum_{n=0}^{\infty}\sum_{k=0}^{n}a_kb_{n-k}=AB.
$$

:::

:::div{class="proof"}

*Proof.* Put $U=\sum_{n=0}^{\infty}|a_n|$ and $V=\sum_{n=0}^{\infty}|b_n|$. For each $N$,

$$
\sum_{n=0}^{N}|c_n|
      \le\sum_{i+j\le N}|a_i|\,|b_j|\le UV.
$$

These absolute partial sums increase and are bounded, so they converge by [Theorem 3.2.1](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#thm:analysis-i:monotone-convergence).

Set $A_N=\sum_{i=0}^{N}a_i$, $B_N=\sum_{j=0}^{N}b_j$, and $C_N=\sum_{n=0}^{N}c_n$. The finite product $A_NB_N$ includes the square of index pairs $0\le i,j\le N$, whereas $C_N$ includes the triangle $i+j\le N$. Every pair in their difference has $i>N/2$ or $j>N/2$. Consequently,

$$
|A_NB_N-C_N|
      \le V\sum_{i>\lfloor N/2\rfloor}|a_i|
        +U\sum_{j>\lfloor N/2\rfloor}|b_j|
      \longrightarrow0.
$$

Since $A_NB_N\to AB$ by the product law for limits, $C_N\to AB$. ◻

:::

Convergence of both factors alone is insufficient. To see the danger, take $a_n=b_n=(-1)^n/\sqrt{n+1}$. Each series converges by [Example 4.4.2](/notes/maths-analysis/analysis-i/infinite-series-of-numbers/#ex:analysis-i:alternating-power-series), after changing the starting index and sign, but

$$
|c_n|=\sum_{k=0}^{n}\frac1{\sqrt{(k+1)(n-k+1)}}
    \ge\frac{2(n+1)}{n+2}\ge1.
$$

The estimate follows from $(k+1)(n-k+1)\le((n+2)/2)^2$. Thus the product terms do not tend to zero and the product series diverges. Absolute convergence is a sufficient hypothesis that makes the preceding multiplication safe.
