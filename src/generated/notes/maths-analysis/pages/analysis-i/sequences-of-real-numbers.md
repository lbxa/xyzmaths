---
title: "Sequences of real numbers"
group: "Analysis I"
order: 8
part: "Part I · Analysis I"
page: "63"
outline: [{"id": "sec:analysis-i:convergent-sequences", "title": "3.1 Convergent sequences", "level": 2}, {"id": "rules-for-limits", "title": "Rules for limits", "level": 3}, {"id": "divergence-to-infinity", "title": "Divergence to infinity", "level": 3}, {"id": "geometric-sequences", "title": "Geometric sequences", "level": 3}, {"id": "taking-increasingly-high-roots", "title": "Taking increasingly high roots", "level": 3}, {"id": "exercises-on-root-limits", "title": "Exercises on root limits", "level": 3}, {"id": "sec:analysis-i:monotone-bounded-sequence-theorem", "title": "3.2 Monotone bounded sequence theorem", "level": 2}, {"id": "the-sequence-11nn", "title": "The sequence (1+1/n)^n", "level": 3}, {"id": "sec:analysis-i:bolzano-weierstrass-theorem", "title": "3.3 Bolzano–Weierstrass theorem", "level": 2}, {"id": "sec:analysis-i:upper-and-lower-limits", "title": "3.4 Upper and lower limits (lim sup and lim inf)", "level": 2}, {"id": "allowing-infinite-tail-bounds", "title": "Allowing infinite tail bounds", "level": 3}, {"id": "cauchy-sequences", "title": "Cauchy sequences", "level": 2}]
---

# Chapter 3. Sequences of real numbers {id="ch:analysis-i:sequences-of-real-numbers"}

The foundations chapter introduced limits as a tool for completeness and iteration. We now develop these ideas through sequence examples in more detail. Limit laws and the squeeze principle come first. Monotonicity then gives convergence when the limit is not yet known. The later sections recall the completeness results and tail bounds needed for series.

## 3.1 Convergent sequences {id="sec:analysis-i:convergent-sequences"}

A sequence is a list of real numbers indexed by the natural numbers. Convergence describes what happens to its terms after sufficiently many of them have been discarded. The first few terms do not decide its limit.

:::div{id="web:sections/analysis-i/03-sequences-of-real-numbers/01-convergent-sequences:292" class="result definition"}

**Definition 3.1.1.** A sequence $(a_n)$ *converges* to $L\in\mathbb{R}$ if

$$
\forall\varepsilon>0\ \exists N\in\mathbb{N}\quad
    n\ge N\ \Longrightarrow\ |a_n-L|<\varepsilon.
$$

We write $a_n\to L$ or $\lim_{n\to\infty}a_n=L$.

:::

The index $N$ may depend on $\varepsilon$. Once it has been chosen, *every* term with index at least $N$ must lie in $(L-\varepsilon,L+\varepsilon)$, as in [Figure 3.1](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#fig:sequence-convergence-band). Finding a few terms near $L$ would not be enough.

:::::div{class="margin-figure"}

::::figure{id="fig:sequence-convergence-band"}

[![For a\_n=1+(-1)^n/n, all terms from N=4 onward lie in the band 1-0.3\<a\_n\<1+0.3. A smaller band may require a later N.](/notes/maths-analysis/figures/convergence-band.svg){.tikz-diagram}](/notes/maths-analysis/figures/convergence-band.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 3.1. For $a_n=1+(-1)^n/n$, all terms from $N=4$ onward lie in the band $1-0.3<a_n<1+0.3$. A smaller band may require a later $N$.

:::

::::

:::::

### Rules for limits {id="rules-for-limits"}

If $a_n\to L$, $b_n\to M$, and $c\in\mathbb{R}$, then

$$
\begin{aligned}
  ca_n&\to cL, & a_n\pm b_n&\to L\pm M,\\
  a_nb_n&\to LM, & \frac{a_n}{b_n}&\to\frac{L}{M}\quad(M\ne0).
\end{aligned}
$$

In the quotient rule the denominator is nonzero for all sufficiently large $n$, because $b_n\to M\ne0$. These are the rules proved in [Proposition 1.4.3](/notes/maths-analysis/analysis-i/sets-and-foundations/#thm:analysis-i:limit-laws). The scalar rule follows from the product rule by using the constant sequence $c$.

:::div{id="ex:analysis-i:limit-law-bounds" class="result example"}

**Example 3.1.2 (Bounds in the product and quotient rules).** Suppose $a_n\to L$ and $b_n\to M$. Eventually $|a_n-L|<1$, so $|a_n|\le A$ with $A=|L|+1$. The product error satisfies

$$
|a_nb_n-LM|\le A|b_n-M|+|M||a_n-L|.
$$

Given $\varepsilon>0$, choose $N$ so that this bound on $|a_n|$ holds and the two errors are respectively less than $\varepsilon/(2A)$ and $\varepsilon/(2(|M|+1))$ for $n\ge N$. The right-hand side is then less than $\varepsilon$, proving $a_nb_n\to LM$ directly from the definition.

If $M\ne0$, eventually $|b_n-M|<|M|/2$, which gives $|b_n|\ge |M|-|b_n-M|>|M|/2$. Hence

$$
\left|\frac{a_n}{b_n}-\frac{L}{M}\right|
    \le\frac{2}{|M|}|a_n-L|
      +\frac{2|L|}{|M|^2}|b_n-M|.
$$

Choose $N$ so that the denominator bound holds and the two errors are respectively less than $\varepsilon|M|/4$ and $\varepsilon|M|^2/(4(|L|+1))$ for $n\ge N$. The displayed bound is then less than $\varepsilon$, proving the quotient rule.

:::

:::div{id="thm:analysis-i:squeeze" class="result theorem"}

**Theorem 3.1.3 (Squeeze principle).** Suppose that $a_n\le b_n\le c_n$ for all sufficiently large $n$. If $a_n\to L$ and $c_n\to L$, then $b_n\to L$.

:::

:::div{class="proof"}

*Proof.* Subtracting $L$ gives

$$
-|a_n-L|\le a_n-L\le b_n-L\le c_n-L\le |c_n-L|.
$$

Consequently $|b_n-L|\le |a_n-L|+|c_n-L|$. Given $\varepsilon>0$, choose an index after which the inequalities hold and both errors on the right are less than $\varepsilon/2$. Then $|b_n-L|<\varepsilon$ for every later term, which proves convergence. ◻

:::

The middle sequence may oscillate. What matters is that its available room shrinks to zero, as [Figure 3.2](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#fig:sequence-squeeze) shows. In particular, if $0\le a_n\le b_n$ and $b_n\to0$, then $a_n\to0$.

:::::div{class="margin-figure"}

::::figure{id="fig:sequence-squeeze"}

[![The terms b\_n=1+(-1)^n/(2n) are trapped between a\_n=1-1/n and c\_n=1+1/n. The gray curves guide the eye. The sequence terms are discrete. Both bounds tend to 1.](/notes/maths-analysis/figures/squeeze.svg){.tikz-diagram}](/notes/maths-analysis/figures/squeeze.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 3.2. The terms $b_n=1+(-1)^n/(2n)$ are trapped between $a_n=1-1/n$ and $c_n=1+1/n$. The gray curves guide the eye. The sequence terms are discrete. Both bounds tend to $1$.

:::

::::

:::::

### Divergence to infinity {id="divergence-to-infinity"}

:::div{id="web:sections/analysis-i/03-sequences-of-real-numbers/01-convergent-sequences:3791" class="result definition"}

**Definition 3.1.4.** We write $a_n\to+\infty$ if

$$
\forall M\in\mathbb{R}\ \exists N\in\mathbb{N}\quad n\ge N\ \Longrightarrow\ a_n>M.
$$

Similarly, $a_n\to-\infty$ means that for every $M\in\mathbb{R}$, all sufficiently late terms satisfy $a_n<M$.

:::

These sequences do not have a finite real limit. Divergence to $+\infty$ means eventually remaining above every prescribed level. Being unbounded alone does not imply this.

### Geometric sequences {id="geometric-sequences"}

For a positive number $a$, the behaviour of $a^n$ depends on whether $a$ is below, equal to, or above $1$.

$$
a^n\longrightarrow
  \begin{cases}
    0,&0<a<1,\\
    1,&a=1,\\
    +\infty,&a>1.
  \end{cases}
$$

The binomial identity provides a useful estimate. For $n\in\mathbb{N}$,

$$
(u+v)^n=\sum_{k=0}^n\binom nk u^{n-k}v^k,
  \qquad \binom nk=\frac{n!}{k!(n-k)!}.
$$

If $h>0$, all terms in the expansion of $(1+h)^n$ are nonnegative, so $(1+h)^n\ge1+nh$. [^24]

:::notes{id="footnotes-23"}

[^24]: This estimate is usually called Bernoulli’s inequality. Jakob Bernoulli used it in his 1689 work on infinite series  ([Bernoulli 1689](/notes/maths-analysis/references/#ref-Bernoulli1689)). He is Johann Bernoulli’s elder brother, not the Bernoulli in the L’Hôpital correspondence. Here its linear lower bound turns exponential growth into an elementary limit estimate. The modern version also includes negative increments down to $-1$. See [Figure 3.3](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#fig:portrait:bernoulli-jacob).

:::

:::::div{class="margin-figure"}

::::figure{id="fig:portrait:bernoulli-jacob"}

![Jakob Bernoulli](/notes/maths-analysis/figures/bernoulli-jacob.jpg)

:::figcaption

Figure 3.3. Jakob Bernoulli. ([MacTutor History of Mathematics n.d.p](/notes/maths-analysis/references/#ref-PortraitBernoulliJacob); [Bookofproofs contributors, n.d.](/notes/maths-analysis/references/#ref-BookofproofsPortraits))

:::

::::

:::::

For $0<a<1$, write $1/a=1+h$ with $h>0$. Then

$$
0<a^n=\frac{1}{(1+h)^n}\le\frac{1}{1+nh}\longrightarrow0.
$$

The squeeze principle gives the limit. If $a>1$, write $a=1+h$. Now $a^n\ge1+nh$, which eventually exceeds every $M\in\mathbb{R}$ by the Archimedean property. Thus $a^n\to+\infty$.

### Taking increasingly high roots {id="taking-increasingly-high-roots"}

:::div{id="thm:analysis-i:root-sequence-limits" class="result proposition"}

**Proposition 3.1.5.** We have $n^{1/n}\to1$ and, for every fixed $a>0$, $a^{1/n}\to1$.

:::

:::div{class="proof"}

*Proof.* Set $\delta_n=n^{1/n}-1\ge0$. For $n\ge2$, keeping just the quadratic term in the binomial expansion gives

$$
n=(1+\delta_n)^n\ge\binom n2\delta_n^2,
    \qquad 0\le\delta_n^2\le\frac{2}{n-1}.
$$

Given $\varepsilon>0$, the right-hand side is eventually smaller than $\varepsilon^2$, so $0\le\delta_n<\varepsilon$. Therefore $n^{1/n}\to1$.

If $a\ge1$, choose $n>a$. Monotonicity of positive $n$th roots gives $1\le a^{1/n}\le n^{1/n}$, so the squeeze principle gives $a^{1/n}\to1$. If $0<a<1$, apply this result to $1/a>1$ and use the quotient rule to obtain

$$
a^{1/n}=\frac{1}{(1/a)^{1/n}}\longrightarrow1.
$$

 ◻

:::

[Figure 3.4](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#fig:root-sequences) plots actual terms of two root sequences. The base in $n^{1/n}$ grows, yet taking the $n$th root brings the terms back towards $1$.

### Exercises on root limits {id="exercises-on-root-limits"}

The following exercises combine root limits with geometric growth and the squeeze principle.

::statement{key="hw04:polynomial-root-limit"}

::statement{key="hw04:exponential-root-limit"}

::::figure{id="fig:root-sequences"}

[![Terms of n^\{1/n\} and 2^\{1/n\} on Cartesian axes. Both sequences approach the horizontal line y=1. Only integer indices represent sequence terms.](/notes/maths-analysis/figures/root-sequences.svg){.tikz-diagram}](/notes/maths-analysis/figures/root-sequences.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 3.4. Terms of $n^{1/n}$ and $2^{1/n}$ on Cartesian axes. Both sequences approach the horizontal line $y=1$. Only integer indices represent sequence terms.

:::

::::

## 3.2 Monotone bounded sequence theorem {id="sec:analysis-i:monotone-bounded-sequence-theorem"}

:::div{id="thm:analysis-i:monotone-convergence" class="result theorem"}

**Theorem 3.2.1 (Monotone bounded sequence theorem).** An increasing sequence bounded above converges to the supremum of its terms. A decreasing sequence bounded below converges to their infimum.

:::

Here increasing and decreasing allow equality between consecutive terms. The proof was given in [§ 1.7](/notes/maths-analysis/analysis-i/sets-and-foundations/#sec:analysis-i:completeness-equivalences). For example, if $L=\sup\{a_n\mid n\in\mathbb{N}\}$ and $(a_n)$ is increasing, some $a_N$ exceeds $L-\varepsilon$. Every later term then satisfies $L-\varepsilon<a_N\le a_n\le L$.

### The sequence $(1+1/n)^n$ {id="the-sequence-11nn"}

Consider

$$
c_n=\left(1+\frac1n\right)^n.
$$

We first establish a finite limit by proving monotonicity and an upper bound. We then compare the binomial expansion with the factorial series to identify the limit as $e$.

::::div{id="web:sections/analysis-i/03-sequences-of-real-numbers/02-monotone-bounded-sequence-theorem:980" class="result proposition"}

**Proposition 3.2.2 (Arithmetic–geometric mean inequality).** [^25] :anchor[]{id="thm:analysis-i:am-gm"} For an integer $k\ge1$ and positive real numbers $a_1,\ldots,a_k$,

$$
(a_1\cdots a_k)^{1/k}\le\frac{a_1+\cdots+a_k}{k}.
$$

:::notes{id="footnotes-24"}

[^25]: Cauchy’s 1821 *Cours d’analyse* gives a general arithmetic–geometric mean argument in its note on means  ([Cauchy 1821, n. II](/notes/maths-analysis/references/#ref-Cauchy1821)). The two-variable inequality has a much older geometric background. Its use here is an estimate for a sequence. In optimisation it compares products under a fixed sum. This is not an attribution of the inequality’s first discovery to Cauchy.

:::

::::

:::div{class="proof"}

*Proof.* We prove the equivalent product inequality

$$
a_1\cdots a_k\le\left(\frac{a_1+\cdots+a_k}{k}\right)^k.
$$

The case $k=1$ is equality. For two positive numbers $u,v$, the inequality $(u-v)^2\ge0$ gives

$$
uv\le\left(\frac{u+v}{2}\right)^2.
$$

Suppose the product inequality holds for $n$ numbers. For $2n$ numbers, let $U$ and $V$ be the arithmetic means of the first and second groups of $n$ numbers. Apply the $n$-variable inequality to each group and then the two-variable inequality to $U,V$. This gives

$$
a_1\cdots a_{2n}\le U^nV^n
      \le\left(\frac{U+V}{2}\right)^{2n}.
$$

Since $(U+V)/2$ is the mean of all $2n$ numbers, induction proves the product inequality whenever the number of terms is a power of two.

Now let $k\ge1$ be arbitrary, and put $M=(a_1+\cdots+a_k)/k>0$. Choose a power of two $m\ge k$, and append $m-k$ copies of $M$ to the original list. The mean of these $m$ numbers is still $M$, so the case just proved gives

$$
(a_1\cdots a_k)M^{m-k}\le M^m.
$$

Divide by the positive number $M^{m-k}$ and take the increasing positive $k$th root to obtain the stated inequality. ◻

:::

We abbreviate this inequality as AM–GM.

:::div{id="ex:analysis-i:binomial-sequence-am-gm" class="result example"}

**Example 3.2.3 (Convergence using AM–GM).** Apply [Proposition 3.2.2](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#thm:analysis-i:am-gm) to $n+1$ positive numbers, one equal to $1$ and the other $n$ equal to $(n+1)/n$. Their arithmetic mean is $1+1/(n+1)$. Hence

$$
\left(\frac{n+1}{n}\right)^{n/(n+1)}
    \le1+\frac{1}{n+1}.
$$

Raising both sides to the power $n+1$ gives $c_n\le c_{n+1}$. Thus $(c_n)$ is increasing.

We still need an upper bound. It is convenient to bound $c_{2n}$ first. Put $b=1+1/(2n)$. Factoring the difference of powers gives

$$
\begin{aligned}
    b^n-1
      &=(b-1)\sum_{j=0}^{n-1}b^j\\
      &\le n(b-1)b^{n-1}
       =\frac12b^{n-1}<\frac12b^n.
  
\end{aligned}
$$

The sum has $n$ terms, each at most $b^{n-1}$, including when $n=1$. Thus $b^n<2$ and $c_{2n}=(b^n)^2<4$. Since the sequence is increasing, $c_n\le c_{2n}<4$ for every $n$. [Theorem 3.2.1](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#thm:analysis-i:monotone-convergence) now proves that $(c_n)$ converges to a finite limit.

:::

Convergence alone does not determine the value of the limit. To find it, we compare the binomial expansion with the factorial series defining $e$.

:::div{id="thm:analysis-i:binomial-limit" class="result proposition"}

**Proposition 3.2.4 (The binomial limit).**

$$
\lim_{n\to\infty}\left(1+\frac1n\right)^n=e.
$$

:::

:::div{class="proof"}

*Identification of the limit.* Let $L=\lim c_n$, whose existence has just been proved. The binomial expansion gives

$$
c_n=\sum_{k=0}^{n}\frac{1}{k!}
      \prod_{j=0}^{k-1}\left(1-\frac{j}{n}\right)
    \le\sum_{k=0}^{n}\frac{1}{k!}\le e.
$$

The product for $k=0$ is empty and equals $1$. Every other factor lies between $0$ and $1$. Taking limits gives $L\le e$, where $e$ is the factorial-series sum defined in [§ 1.9](/notes/maths-analysis/analysis-i/sets-and-foundations/#sec:analysis-i:denseness).

Now fix an integer $m\ge0$. For every $n\ge\max\{m,1\}$, positivity of the remaining terms gives

$$
c_n\ge\sum_{k=0}^{m}\frac{1}{k!}
      \prod_{j=0}^{k-1}\left(1-\frac{j}{n}\right).
$$

This sum has a fixed number of terms. Each factor tends to $1$ as $n\to\infty$, so the finite product and sum rules give $L\ge\sum_{k=0}^{m}1/k!$. These inequalities hold for every $m$. The factorial partial sums tend to $e$, hence $L\ge e$. Together with $L\le e$, this proves $L=e$ without exchanging a limit with an infinite sum. ◻

:::

There is also a direct proof of strict monotonicity using differences of powers.

:::div{id="ex:analysis-i:binomial-sequence-powers" class="result example"}

**Example 3.2.5 (Monotonicity by differences of powers).** If $0<a<b$ and $k\ge2$ is an integer, then

$$
\begin{aligned}
    b^k-a^k
      &=(b-a)\bigl(b^{k-1}+b^{k-2}a+\cdots+a^{k-1}\bigr)\\
      &<k(b-a)b^{k-1}.
  
\end{aligned}
$$

Each summand in the brackets is at most $b^{k-1}$, and at least one is strictly smaller. Substitute

$$
a=1+\frac{1}{n+1},\qquad b=1+\frac1n,\qquad k=n+1.
$$

Since $k(b-a)=1/n$, we obtain

$$
\left(1+\frac1n\right)c_n-c_{n+1}<\frac{c_n}{n},
$$

and therefore $c_n<c_{n+1}$.

:::

:::div{id="web:sections/analysis-i/03-sequences-of-real-numbers/02-monotone-bounded-sequence-theorem:5875" class="result remark"}

**Remark 3.2.6 (Changing the exponent).** The related expression with exponent $1/n$ has a different limit. Indeed,

$$
1\le\left(1+\frac1n\right)^{1/n}\le2^{1/n}\longrightarrow1,
$$

so it tends to $1$ by the squeeze principle.

:::

The two-variable case of AM–GM admits a direct proof that also allows zero inputs and determines when equality holds.

::statement{key="hw04:two-variable-am-gm"}

## 3.3 Bolzano–Weierstrass theorem {id="sec:analysis-i:bolzano-weierstrass-theorem"}

[^26]

:::notes{id="footnotes-25"}

[^26]: Bolzano’s 1817 search for an analytic proof of the intermediate value theorem led him to boundedness and limiting-point arguments ([Bolzano 1817](/notes/maths-analysis/references/#ref-Bolzano1817)). The familiar name also honours Weierstrass’s later development of rigorous analysis. The sequence form used here is modern. Its role is to extract a convergent subsequence, the mechanism behind many compactness arguments. See [Figure 3.5](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#fig:portrait:bolzano-weierstrass).

:::

:::::div{class="margin-figure"}

::::figure{id="fig:portrait:bolzano-weierstrass"}

![Bernard Bolzano](/notes/maths-analysis/figures/bolzano.jpg) ![Karl Weierstrass](/notes/maths-analysis/figures/weierstrass.jpg)

:::figcaption

Figure 3.5. Bernard Bolzano (left) and Karl Weierstrass (right). Portrait sources ([MacTutor History of Mathematics n.d.c](/notes/maths-analysis/references/#ref-PortraitBolzano), [n.d.u](/notes/maths-analysis/references/#ref-PortraitWeierstrass); [Bookofproofs contributors, n.d.](/notes/maths-analysis/references/#ref-BookofproofsPortraits)).

:::

::::

:::::

:::div{id="thm:analysis-i:bolzano-weierstrass" class="result theorem"}

**Theorem 3.3.1 (Bolzano–Weierstrass).** Every bounded real sequence has a convergent subsequence.

:::

:::::div{class="margin-figure"}

::::figure{id="fig:bolzano-weierstrass-selection"}

[![Schematic selection in nested intervals. Each I\_k contains infinitely many terms, so we can choose a\_\{n\_k\}\\in I\_k with n\_1\<n\_2\<\\cdots. The shrinking intervals share the point L. The construction continues beyond the rows shown.](/notes/maths-analysis/figures/bolzano-weierstrass-selection.svg){.tikz-diagram}](/notes/maths-analysis/figures/bolzano-weierstrass-selection.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 3.6. Schematic selection in nested intervals. Each $I_k$ contains infinitely many terms, so we can choose $a_{n_k}\in I_k$ with $n_1<n_2<\cdots$. The shrinking intervals share the point $L$. The construction continues beyond the rows shown.

:::

::::

:::::

A subsequence $(a_{n_k})$ uses strictly increasing indices $n_1<n_2<\cdots$. It keeps some terms in their original order. The nested-interval proof in [§ 1.7](/notes/maths-analysis/analysis-i/sets-and-foundations/#sec:analysis-i:completeness-equivalences) repeatedly retains a half-interval containing infinitely many terms, then chooses a term in each retained interval with index larger than the previous one. [Figure 3.6](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#fig:bolzano-weierstrass-selection) shows these choices. If $L$ is the common point of the retained intervals $I_k$, then

$$
|a_{n_k}-L|\le |I_k|\longrightarrow0,
$$

where $|I_k|$ denotes the length of $I_k$. Thus the shrinking intervals force the chosen subsequence to converge to $L$.

The theorem guarantees a convergent subsequence, rather than convergence of the original sequence. For instance, $(-1)^n$ is bounded and has constant subsequences with limits $1$ and $-1$, although the whole sequence does not converge. These subsequential limits are the limit points introduced in [§ 1.9](/notes/maths-analysis/analysis-i/sets-and-foundations/#sec:analysis-i:denseness).

## 3.4 Upper and lower limits (lim sup and lim inf) {id="sec:analysis-i:upper-and-lower-limits"}

For a bounded real sequence $(a_n)$, define its tail bounds by

$$
\alpha_n=\inf\{a_k\mid k\ge n\},\qquad
  \beta_n=\sup\{a_k\mid k\ge n\}.
$$

Removing early terms can only raise the infimum and lower the supremum. Thus $(\alpha_n)$ is increasing, $(\beta_n)$ is decreasing, and

$$
\liminf_{n\to\infty}a_n=\lim_{n\to\infty}\alpha_n,
  \qquad
  \limsup_{n\to\infty}a_n=\lim_{n\to\infty}\beta_n.
$$

By [Proposition 1.9.2](/notes/maths-analysis/analysis-i/sets-and-foundations/#thm:analysis-i:extreme-limit-points), these are respectively the smallest and largest limits of convergent subsequences. The full sequence converges exactly when these two numbers agree. The tail picture and its proof appear in [§ 1.9](/notes/maths-analysis/analysis-i/sets-and-foundations/#sec:analysis-i:denseness).

### Allowing infinite tail bounds {id="allowing-infinite-tail-bounds"}

The tests for series also use sequences that need not be bounded. We allow tail bounds to take values in $\mathbb{R}\cup\{-\infty,+\infty\}$. An unbounded-above tail has supremum $+\infty$, and an unbounded-below tail has infimum $-\infty$. The definitions become

$$
\liminf a_n=\sup_n\alpha_n,\qquad
  \limsup a_n=\inf_n\beta_n.
$$

For bounded sequences these agree with the preceding definitions. The infinite values describe unbounded tail behaviour. They are not additional real numbers.

:::::div{class="margin-figure"}

::::figure{id="fig:infinite-tail-bounds"}

[![For a\_n=n, every sufficiently late term stays above a chosen level r. Here r=5/2 and N=3. For b\_n=(-1)^n n, every tail reaches arbitrarily far in both directions. Dots are actual terms. Ellipses indicate continuation.](/notes/maths-analysis/figures/infinite-tail-bounds.svg){.tikz-diagram}](/notes/maths-analysis/figures/infinite-tail-bounds.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 3.7. For $a_n=n$, every sufficiently late term stays above a chosen level $r$. Here $r=5/2$ and $N=3$. For $b_n=(-1)^n n$, every tail reaches arbitrarily far in both directions. Dots are actual terms. Ellipses indicate continuation.

:::

::::

:::::

:::div{id="ex:analysis-i:infinite-tail-bounds" class="result example"}

**Example 3.4.1 (Two patterns of unbounded tails).** For $a_n=n$, the tail beginning at $N$ has $\alpha_N=N$ and $\beta_N=+\infty$. Hence both $\liminf a_n$ and $\limsup a_n$ equal $+\infty$, and $a_n\to+\infty$. For $b_n=(-1)^n n$, every tail is unbounded above and below, so $\alpha_N=-\infty$ and $\beta_N=+\infty$ for every $N$. Its lower and upper limits are different, and it does not tend to either infinity. [Figure 3.7](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#fig:infinite-tail-bounds) compares the two patterns. Infinite tail bounds describe the whole tail, even though each individual term is a finite real number.

:::

The feature we will need is an eventual bound. If $\limsup a_n<r$, then $\beta_N<r$ for some $N$, so $a_n<r$ for every $n\ge N$. Similarly, if $\liminf a_n>r$, then every sufficiently late term exceeds $r$. The strict gap between the limit bound and $r$ is essential.

:::div{id="web:sections/analysis-i/03-sequences-of-real-numbers/04-upper-and-lower-limits:2664" class="result proposition"}

**Proposition 3.4.2.** If $a_n\le b_n$ for every sufficiently large $n$, then $\liminf a_n\le\limsup b_n$.

:::

:::div{class="proof"}

*Proof.* For all sufficiently late tails, $\alpha_n^{a}\le a_k\le b_k
  \le\beta_n^{b}$ whenever $k\ge n$. Given any two tail indices $i,j$, choose $k$ at least as large as both and beyond the index where $a_k\le b_k$. Then $\alpha_i^{a}\le\beta_j^{b}$. Taking the supremum over $i$ and then the infimum over $j$ gives the claimed inequality, including when a bound is infinite. ◻

:::

## Cauchy sequences {id="cauchy-sequences"}

[^27]

:::notes{id="footnotes-26"}

[^27]: Cauchy’s *Cours d’analyse* (1821) tests series by comparing partial sums far out in the sequence ([Cauchy 1821](/notes/maths-analysis/references/#ref-Cauchy1821), ch. VI). The useful decision is to test convergence without first knowing its limit. The modern Cauchy-sequence definition extends that idea and is central to completing spaces. It needs completeness to guarantee that the limit belongs to the space. See [Figure 3.8](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#fig:portrait:cauchy).

:::

:::::div{class="margin-figure"}

::::figure{id="fig:portrait:cauchy"}

![Augustin-Louis Cauchy](/notes/maths-analysis/figures/cauchy.jpg)

:::figcaption

Figure 3.8. Augustin-Louis Cauchy. ([MacTutor History of Mathematics n.d.a](/notes/maths-analysis/references/#ref-PortraitCauchy); [Bookofproofs contributors, n.d.](/notes/maths-analysis/references/#ref-BookofproofsPortraits))

:::

::::

:::::

:anchor[]{id="sec:analysis-i:cauchy-sequences"}

:::div{id="web:sections/analysis-i/03-sequences-of-real-numbers/05-cauchy-sequences:554" class="result definition"}

**Definition 3.5.1.** A real sequence $(a_n)$ is *Cauchy* if

$$
\forall\varepsilon>0\ \exists N\in\mathbb{N}\quad
    \forall m,n\ge N\quad |a_m-a_n|<\varepsilon.
$$

:::

Here $m,n\ge N$ means $m\ge N$ and $n\ge N$, with both indices chosen independently from the same tail. We can equivalently require the inequality only for $m>n\ge N$. Indeed, exchanging the indices does not change the distance, since $|a_m-a_n|=|a_n-a_m|$, and the case $m=n$ gives $0<\varepsilon$. In either form, every pair of distinct tail terms must be close, however far apart their indices are.

:::::div{class="margin-figure"}

::::figure{id="fig:cauchy-tail-diameter"}

[![Schematic real-line views of two tails, with \\varepsilon\_2\<\\varepsilon\_1. Each shaded interval contains a whole tail and is narrower than its indicated tolerance, so every pair of terms in that tail is close. Dots show sample terms.](/notes/maths-analysis/figures/cauchy-tail-diameter.svg){.tikz-diagram}](/notes/maths-analysis/figures/cauchy-tail-diameter.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 3.9. Schematic real-line views of two tails, with $\varepsilon_2<\varepsilon_1$. Each shaded interval contains a whole tail and is narrower than its indicated tolerance, so every pair of terms in that tail is close. Dots show sample terms.

:::

::::

:::::

Convergence compares late terms with a proposed limit. The Cauchy condition compares late terms with one another, so it can be checked without knowing the limit in advance. [Figure 3.9](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#fig:cauchy-tail-diameter) shows the whole tail confined to a small interval. A smaller tolerance may require a larger starting index. The condition controls every pair of terms after that index.

:::div{id="thm:analysis-i:cauchy-completeness" class="result theorem"}

**Theorem 3.5.2 (Cauchy completeness of the real numbers).** A real sequence converges if and only if it is Cauchy.

:::

If $a_n\to L$, choose $N$ so that $|a_n-L|<\varepsilon/2$ for $n\ge N$. The triangle inequality then gives $|a_m-a_n|\le|a_m-L|+|a_n-L|<\varepsilon$. The converse uses completeness, as proved in [§ 1.7](/notes/maths-analysis/analysis-i/sets-and-foundations/#sec:analysis-i:completeness-equivalences). A Cauchy sequence is bounded, hence has a convergent subsequence. Its Cauchy property then forces every sufficiently late term towards the same limit. We will apply this theorem to partial sums of series.
