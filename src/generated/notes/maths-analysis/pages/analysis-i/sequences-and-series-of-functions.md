---
title: "Sequences and series of functions"
group: "Analysis I"
order: 13
part: "Part I · Analysis I"
page: "117"
outline: [{"id": "sec:analysis-i:sequences-of-functions", "title": "8.1 Sequences of functions", "level": 2}, {"id": "sec:analysis-i:series-of-functions", "title": "8.2 Series of functions", "level": 2}, {"id": "sec:analysis-i:uniform-convergence", "title": "8.3 Uniform convergence", "level": 2}, {"id": "the-normed-space-cab", "title": "The normed space C[a,b]", "level": 3}, {"id": "uniform-convergence-and-arithmetic-operations", "title": "Uniform convergence and arithmetic operations", "level": 3}, {"id": "a-further-moving-input-example", "title": "A further moving-input example", "level": 3}, {"id": "equicontinuity", "title": "Equicontinuity", "level": 3}, {"id": "sec:analysis-i:cauchy-criterion-for-uniform-convergence", "title": "8.4 Cauchy criterion for uniform convergence", "level": 2}, {"id": "the-criterion-for-a-series", "title": "The criterion for a series", "level": 3}, {"id": "the-weierstrass-majorant-test", "title": "The Weierstrass majorant test", "level": 3}, {"id": "sec:analysis-i:uniform-convergence-and-integration", "title": "8.5 Uniform convergence and integration", "level": 2}, {"id": "sec:analysis-i:power-series", "title": "8.6 Power series", "level": 2}, {"id": "computing-the-radius-and-controlling-interior-intervals", "title": "Computing the radius and controlling interior intervals", "level": 3}, {"id": "the-geometric-power-series", "title": "The geometric power series", "level": 3}, {"id": "algebraic-and-transcendental-functions", "title": "Algebraic and transcendental functions", "level": 3}, {"id": "the-exponential-series", "title": "The exponential series", "level": 3}, {"id": "exponential-and-logarithmic-properties", "title": "Exponential and logarithmic properties", "level": 3}, {"id": "exponential-and-logarithmic-limits", "title": "Exponential and logarithmic limits", "level": 3}, {"id": "a-family-with-different-endpoints", "title": "A family with different endpoints", "level": 3}, {"id": "sec:analysis-i:analytic-functions", "title": "Analytic functions and the multiplicity of a zero", "level": 3}, {"id": "sec:analysis-i:polynomial-approximation", "title": "Uniform polynomial approximation", "level": 3}]
---

# Chapter 8. Sequences and series of functions {id="ch:analysis-i:sequences-and-series-of-functions"}

Sequences and series of functions have values that depend on a variable. For each fixed input, the scalar convergence tools apply. The difference between pointwise and uniform convergence determines whether continuity passes from the functions to their limit. The power-series examples in [§ 8.6](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#sec:analysis-i:power-series) use the tests from [Chapter 4](/notes/maths-analysis/analysis-i/infinite-series-of-numbers/#ch:analysis-i:infinite-series-of-numbers).

## 8.1 Sequences of functions {id="sec:analysis-i:sequences-of-functions"}

Let $f_n:D\to\mathbb{R}$ be a function for each $n\in\mathbb{N}$. For a fixed $x\in D$, the values $f_n(x)$ form a sequence of real numbers. Its limit may depend on the input $x$.

:::div{id="thm:analysis-i:pointwise-convergence" class="result definition"}

**Definition 8.1.1 (Pointwise convergence).** The sequence $(f_n)$ converges *pointwise* to $f:D\to\mathbb{R}$ if $f_n(x)\to f(x)$ for every $x\in D$. Equivalently,

$$
\begin{gathered}
      \forall x\in D\quad\forall\varepsilon>0\quad\exists N\in\mathbb{N}\\
      \forall n\ge N\quad |f_n(x)-f(x)|<\varepsilon.
    \end{gathered}
$$

Here $N$ may depend on both $\varepsilon$ and $x$.

:::

:::div{id="ex:analysis-i:truncated-powers" class="result example"}

**Example 8.1.2 (A discontinuous limit of continuous functions).** On $[0,\infty)$, define

$$
f_n(x)=
    \begin{cases}
      x^n,&0\le x\le1,\\
      1,&x>1.
    \end{cases}
$$

Every $f_n$ is continuous. At a fixed $0\le x<1$, the geometric sequence $x^n$ tends to zero. At $x=1$ and at every $x>1$, the value is always one. Thus the pointwise limit is

$$
f(x)=
    \begin{cases}
      0,&0\le x<1,\\
      1,&x\ge1.
    \end{cases}
$$

This function is discontinuous at $1$. The continuous curves and their pointwise limit are shown in [Figure 8.1](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#fig:analysis-i:truncated-powers).

:::

:::::div{class="margin-figure"}

::::figure{id="fig:analysis-i:truncated-powers"}

[![Truncated powers for n=2 (gray) and n=16 (black). The dashed graph is the pointwise limit. Its value at 1 is one.](/notes/maths-analysis/figures/truncated-powers.svg){.tikz-diagram}](/notes/maths-analysis/figures/truncated-powers.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 8.1. Truncated powers for $n=2$ (gray) and $n=16$ (black). The dashed graph is the pointwise limit. Its value at $1$ is one.

:::

::::

:::::

:::div{id="ex:analysis-i:truncated-roots" class="result example"}

**Example 8.1.3 (Truncated roots).** On $(0,\infty)$, define

$$
g_n(x)=
    \begin{cases}
      x^{1/n},&0<x\le1,\\
      1,&x>1.
    \end{cases}
$$

For each fixed $0<x\le1$, the root sequence $x^{1/n}$ tends to one. For $x>1$, the value is already one. Hence $g_n(x)\to1$ for every $x>0$, as illustrated in [Figure 8.2](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#fig:analysis-i:truncated-roots).

:::

If we extend every $g_n$ continuously to $0$ by setting $g_n(0)=0$, the pointwise limit on $[0,\infty)$ becomes

$$
g(x)=
    \begin{cases}
      0,&x=0,\\
      1,&x>0.
    \end{cases}
$$

The extended limit is discontinuous at $0$, even though each extended $g_n$ is continuous there. The original domain $(0,\infty)$ excludes precisely this point.

:::::div{class="margin-figure"}

::::figure{id="fig:analysis-i:truncated-roots"}

[![Truncated roots for n=2 (gray) and n=16 (black), on the domain x\>0. The dashed line is the limit 1. The open origin is excluded from each graph.](/notes/maths-analysis/figures/truncated-roots.svg){.tikz-diagram}](/notes/maths-analysis/figures/truncated-roots.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 8.2. Truncated roots for $n=2$ (gray) and $n=16$ (black), on the domain $x>0$. The dashed line is the limit $1$. The open origin is excluded from each graph.

:::

::::

:::::

:::div{id="ex:analysis-i:reciprocal-powers" class="result example"}

**Example 8.1.4 (A transition at one).** On $[0,\infty)$, let

$$
h_n(x)=\frac{1}{1+x^n}.
$$

If $0\le x<1$, then $x^n\to0$, so $h_n(x)\to1$. At $x=1$, every term equals $1/2$. If $x>1$, then $x^n\to\infty$, so $h_n(x)\to0$. Consequently,

$$
h(x)=\lim_{n\to\infty}h_n(x)=
    \begin{cases}
      1,&0\le x<1,\\
      \dfrac12,&x=1,\\
      0,&x>1.
    \end{cases}
$$

The transition becomes increasingly sharp near $1$, as shown in [Figure 8.3](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#fig:analysis-i:reciprocal-powers).

:::

:::::div{class="margin-figure"}

::::figure{id="fig:analysis-i:reciprocal-powers"}

[![Reciprocal powers for n=2 (gray) and n=16 (black). The dashed graph is the pointwise limit. All curves pass through (1,1/2), which remains the limit’s value at 1.](/notes/maths-analysis/figures/reciprocal-powers.svg){.tikz-diagram}](/notes/maths-analysis/figures/reciprocal-powers.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 8.3. Reciprocal powers for $n=2$ (gray) and $n=16$ (black). The dashed graph is the pointwise limit. All curves pass through $(1,1/2)$, which remains the limit’s value at $1$.

:::

::::

:::::

## 8.2 Series of functions {id="sec:analysis-i:series-of-functions"}

A series of functions is studied through its partial sums, just as a series of numbers is. The input remains a variable throughout the argument.

:::div{id="thm:analysis-i:function-series" class="result definition"}

**Definition 8.2.1 (Series of functions).** Let $f_n:D\to\mathbb{R}$ for $n=0,1,2,\ldots$, and put

$$
S_N(x)=\sum_{n=0}^{N}f_n(x).
$$

The series $\sum_{n=0}^{\infty}f_n(x)$ converges *pointwise* on $D$ if $S_N(x)$ has a finite limit $S(x)$ for every $x\in D$. It converges *absolutely at $x$* if $\sum_{n=0}^{\infty}|f_n(x)|<\infty$.

:::

Uniform convergence of the series means uniform convergence of the sequence $(S_N)$, using the definition in [§ 8.3](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#sec:analysis-i:uniform-convergence). Its error is the entire remaining tail,

$$
S(x)-S_N(x)=\sum_{n=N+1}^{\infty}f_n(x).
$$

Uniform convergence of the individual terms $f_n$ to zero is necessary for uniform convergence of the series, but is insufficient by itself. Indeed, if $S_N\to S$ uniformly, then for $N\ge1$,

$$
|f_N(x)|\le |S_N(x)-S(x)|+|S_{N-1}(x)-S(x)|,
$$

and both errors become uniformly small. For example, the constant functions $f_n(x)=1/(n+1)$ tend uniformly to zero on every nonempty domain, whereas their series is harmonic and diverges at every input.

The uniform Cauchy criterion and the majorant test in [§ 8.4](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#sec:analysis-i:cauchy-criterion-for-uniform-convergence) will control these tails without requiring an explicit formula for $S$.

## 8.3 Uniform convergence {id="sec:analysis-i:uniform-convergence"}

[^52]

:::notes{id="footnotes-51"}

[^52]: Cauchy’s 1821 claim about sums of continuous functions needed stronger convergence hypotheses. He returned to the question in 1853 ([Cauchy 1821](/notes/maths-analysis/references/#ref-Cauchy1821), ch. VI)([Cauchy 1853](/notes/maths-analysis/references/#ref-Cauchy1853)). The modern uniform requirement supplies one error bound for every point, exactly what the continuity-preservation proof below needs. The majorant bound in [Theorem 8.4.3](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:weierstrass-m-test) gives a practical way to obtain that uniform control. This distinction also matters when exchanging limits and integration.

:::

In pointwise convergence, we choose $N$ after fixing both $x$ and $\varepsilon$. Uniform convergence requires one $N$ that works simultaneously for every input.

:::div{id="thm:analysis-i:uniform-convergence" class="result definition"}

**Definition 8.3.1 (Uniform convergence).** The sequence $f_n:D\to\mathbb{R}$ converges *uniformly* to $f:D\to\mathbb{R}$ if

$$
\begin{gathered}
      \forall\varepsilon>0\quad\exists N\in\mathbb{N}\quad\forall x\in D\\
      \forall n\ge N\quad |f_n(x)-f(x)|<\varepsilon.
    \end{gathered}
$$

Here $N$ may depend on $\varepsilon$, but it is independent of $x$.

:::

Uniform convergence implies pointwise convergence, since its single choice of $N$ works at any fixed $x$. The converse need not hold. For the truncated powers in [Example 8.1.2](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#ex:analysis-i:truncated-powers), take $x_n=2^{-1/n}<1$. Then

$$
|f_n(x_n)-f(x_n)|=x_n^n=\frac12
$$

for every $n$. These moving inputs prevent any one $N$ from giving an error below $1/2$ throughout the domain. Each fixed input still has the pointwise limit found earlier.

:::div{id="thm:analysis-i:uniform-limit-continuity" class="result theorem"}

**Theorem 8.3.2 (Uniform limits preserve continuity).** Let $f_n:[a,b]\to\mathbb{R}$ be continuous for every $n\in\mathbb{N}$. If $f_n\to f$ uniformly on $[a,b]$, then $f$ is continuous on $[a,b]$.

:::

:::div{class="proof"}

*Proof.* Let $\varepsilon>0$. Uniform convergence gives an $N\in\mathbb{N}$ such that

$$
\forall x\in[a,b]\quad
    |f_N(x)-f(x)|<\frac{\varepsilon}{3}.
$$

We now keep this index $N$ fixed. Fix $t\in[a,b]$. Since $f_N$ is continuous at $t$, there is a $\delta>0$ such that $|f_N(s)-f_N(t)|<\varepsilon/3$ whenever $s\in[a,b]$ and $|s-t|<\delta$. For such $s$, adding and subtracting the two values of $f_N$ gives

$$
\begin{aligned}
    |f(s)-f(t)|
      &=\bigl|f(s)-f_N(s)+f_N(s)-f_N(t)+f_N(t)-f(t)\bigr|\\
      &\le |f(s)-f_N(s)|
        \mathbin{+}|f_N(s)-f_N(t)|
        +|f_N(t)-f(t)|\\
      &<\frac{\varepsilon}{3}+\frac{\varepsilon}{3}
        +\frac{\varepsilon}{3}
       =\varepsilon.
  
\end{aligned}
$$

Thus $f$ is continuous at $t$. Since $t$ was arbitrary, $f$ is continuous on $[a,b]$. ◻

:::

::statement{key="hw05:pointwise-not-uniform"}

### The normed space $C[a,b]$ {id="the-normed-space-cab"}

The notation $C[a,b]$ denotes the continuous real-valued functions on $[a,b]$, where $a<b$. Pointwise addition and scalar multiplication,

$$
(f+g)(x)=f(x)+g(x),\qquad (cf)(x)=cf(x),
$$

make this a real vector space. Continuity is preserved by these operations.

:::div{id="thm:analysis-i:supremum-norm" class="result definition"}

**Definition 8.3.4 (Norm and supremum norm).** A *norm* on a real vector space assigns a number $\|v\|$ to each vector, with

$$
\begin{gathered}
      \|v\|\ge0,\qquad \|v\|=0\ \Longleftrightarrow\ v=0,\\
      \|cv\|=|c|\,\|v\|,\qquad
      \|u+v\|\le\|u\|+\|v\|.
    \end{gathered}
$$

A vector space equipped with a norm is a *normed space*. On $C[a,b]$ the *supremum norm* is

$$
\|h\|_\infty=\sup_{x\in[a,b]}|h(x)|
      =\max_{x\in[a,b]}|h(x)|.
$$

:::

The maximum exists and is finite by [Theorem 5.2.1](/notes/maths-analysis/analysis-i/continuity/#thm:analysis-i:extreme-value). Nonnegativity, definiteness, and homogeneity follow from the corresponding properties of absolute value. For the triangle inequality, every $x\in[a,b]$ satisfies

$$
|f(x)+g(x)|\le |f(x)|+|g(x)|
    \le\|f\|_\infty+\|g\|_\infty.
$$

Taking the maximum proves the remaining norm axiom.

The distance $\|f-g\|_\infty$ is the largest vertical separation of the two graphs at the same input. Thus

$$
f_n\longrightarrow f\text{ uniformly on }[a,b]
  \quad\Longleftrightarrow\quad
  \|f_n-f\|_\infty\longrightarrow0.
$$

For example, $f_n(x)=x/n$ on $[0,1]$ has distance $1/n$ from the zero function. One bound controls its error at every input.

### Uniform convergence and arithmetic operations {id="uniform-convergence-and-arithmetic-operations"}

In the next question, membership in $C[a,b]$ is essential in part (i). On the entire real line a continuous function need not be bounded.

::statement{key="hw06:uniform-algebra"}

### A further moving-input example {id="a-further-moving-input-example"}

The following question belongs to the pointwise/uniform distinction. Its prescribed hint deliberately refers forward to [Exercise 8.6.9](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#ex:hw06:arbitrary-base-exponential) and [Exercise 8.6.12](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#ex:hw06:exponential-dominates-powers) in [§ 8.6](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#sec:analysis-i:power-series). Return to that hint after the exponential exercises. The alternative maximum calculation uses [§ 6.1](/notes/maths-analysis/analysis-i/differentiation-and-applications/#sec:analysis-i:differentiation).

::statement{key="hw06:moving-peaks"}

### Equicontinuity {id="equicontinuity"}

:::div{id="thm:analysis-i:equicontinuity" class="result definition"}

**Definition 8.3.7 (Equicontinuity).** A family $(f_n)$ on $[a,b]$ is *equicontinuous* if, for each $t\in[a,b]$ and $\varepsilon>0$, there is a $\delta>0$ such that

$$
\forall n\in\mathbb{N}\quad\forall x\in[a,b]\quad
    |x-t|<\delta\ \Longrightarrow\ |f_n(x)-f_n(t)|<\varepsilon.
$$

The same $\delta$ works for every $n$, although it may depend on $t$ and $\varepsilon$.

:::

Individual continuity allows the choice of $\delta$ to change with $n$. Equicontinuity requires a shared choice. For example, the functions $f_n(x)=nx$ on $[0,1]$ are individually continuous but are not equicontinuous at zero. For any $\delta>0$, fix $0<x<\min\{\delta,1\}$ and then choose $n>1/x$. The input lies within $\delta$ of zero, but $|f_n(x)-f_n(0)|>1$.

:::div{id="thm:analysis-i:uniform-convergence-equicontinuity" class="result proposition"}

**Proposition 8.3.8 (Uniform convergence gives equicontinuity).** If a sequence in $C[a,b]$ converges uniformly, it is equicontinuous.

:::

:::div{class="proof"}

*Proof.* Its limit $f$ is continuous by [Theorem 8.3.2](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:uniform-limit-continuity). Fix $t\in[a,b]$ and $\varepsilon>0$. Choose $N$ so that $\|f_n-f\|_\infty<\varepsilon/3$ for $n\ge N$. Continuity of $f$ at $t$ gives a $\delta_0>0$ for which $|f(x)-f(t)|<\varepsilon/3$ when $|x-t|<\delta_0$. For each of the finitely many indices $n<N$, continuity of $f_n$ at $t$ supplies a $\delta_n>0$ with $|f_n(x)-f_n(t)|<\varepsilon$ when $|x-t|<\delta_n$. Take the minimum of these positive numbers. For the early indices the desired estimate is already valid. For $n\ge N$ it follows from

$$
|f_n(x)-f_n(t)|
      \le |f_n(x)-f(x)|+|f(x)-f(t)|+|f(t)-f_n(t)|
      <\varepsilon.
$$

 ◻

:::

The converse fails. The constant functions $f_n(x)=(-1)^n$ are equicontinuous with any $\delta>0$, but do not even converge pointwise.

:::div{id="thm:analysis-i:uniform-equicontinuity" class="result proposition"}

**Proposition 8.3.9 (A shared modulus on a closed interval).** If $(f_n)$ is equicontinuous on $[a,b]$, then for every $\varepsilon>0$ there is $\delta>0$ such that

$$
\begin{gathered}
      \forall n\in\mathbb{N}\quad\forall x,t\in[a,b]\\
      |x-t|<\delta\ \Longrightarrow\ |f_n(x)-f_n(t)|<\varepsilon.
    \end{gathered}
$$

Here $\delta$ is independent of both $n$ and the base point $t$.

:::

:::div{class="proof"}

*Proof.* Otherwise there are $\varepsilon_0>0$, indices $n_k$, and points $x_k,t_k\in[a,b]$ such that $|x_k-t_k|<1/k$ and $|f_{n_k}(x_k)-f_{n_k}(t_k)|\ge\varepsilon_0$. By [Theorem 3.3.1](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#thm:analysis-i:bolzano-weierstrass), a subsequence of $(t_k)$ converges to some $t\in[a,b]$. The corresponding $(x_k)$ also converges to $t$. Equicontinuity at $t$, with tolerance $\varepsilon_0/3$, makes both $|f_{n_k}(x_k)-f_{n_k}(t)|$ and $|f_{n_k}(t_k)-f_{n_k}(t)|$ smaller than $\varepsilon_0/3$ along the late part of that subsequence. The triangle inequality contradicts their separation by at least $\varepsilon_0$. ◻

:::

::statement{key="hw06:equicontinuous-boundedness"}

## 8.4 Cauchy criterion for uniform convergence {id="sec:analysis-i:cauchy-criterion-for-uniform-convergence"}

The Cauchy criterion tests convergence without first identifying the limit. For functions, the comparisons must hold at every input with the same index threshold.

:::div{id="thm:analysis-i:uniformly-cauchy" class="result definition"}

**Definition 8.4.1 (Uniformly Cauchy sequence).** A sequence $f_n:D\to\mathbb{R}$ is *uniformly Cauchy* if

$$
\begin{gathered}
      \forall\varepsilon>0\quad\exists N\in\mathbb{N}\\
      \forall m,n\ge N\quad\forall x\in D\quad
      |f_m(x)-f_n(x)|<\varepsilon.
    \end{gathered}
$$

:::

:::div{id="thm:analysis-i:uniform-cauchy-criterion" class="result theorem"}

**Theorem 8.4.2 (Uniform Cauchy criterion).** A sequence of real-valued functions on $D$ converges uniformly if and only if it is uniformly Cauchy.

:::

:::div{class="proof"}

*Proof.* If $f_n\to f$ uniformly, choose $N$ so that $|f_n(x)-f(x)|<\varepsilon/2$ for every $n\ge N$ and $x\in D$. Then the triangle inequality gives $|f_m(x)-f_n(x)|<\varepsilon$ for all $m,n\ge N$ and $x\in D$.

Conversely, suppose $(f_n)$ is uniformly Cauchy. At each fixed $x$, the sequence $(f_n(x))$ is Cauchy in $\mathbb{R}$, so completeness gives a finite limit $f(x)$. Given $\varepsilon>0$, choose $N$ from the uniform Cauchy property with tolerance $\varepsilon/2$. For fixed $n\ge N$ and $x\in D$, let $m\to\infty$ in that estimate to get

$$
|f(x)-f_n(x)|\le\frac{\varepsilon}{2}<\varepsilon.
$$

The index $N$ is independent of $x$, which proves uniform convergence. ◻

:::

For a sequence in $C[a,b]$, the condition is precisely that $\|f_m-f_n\|_\infty\to0$ as $m,n\to\infty$. The limit belongs to $C[a,b]$ by [Theorem 8.3.2](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:uniform-limit-continuity). Thus Cauchy sequences for the supremum norm have limits in this same normed space.

### The criterion for a series {id="the-criterion-for-a-series"}

Apply [Theorem 8.4.2](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:uniform-cauchy-criterion) to the partial sums in [Definition 8.2.1](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:function-series). The series $\sum_{n=0}^{\infty}f_n$ converges uniformly on $D$ exactly when

$$
\begin{gathered}
    \forall\varepsilon>0\quad\exists N\in\mathbb{N}\\
    \forall m>n\ge N\quad\forall x\in D\quad
    \left|\sum_{k=n+1}^{m}f_k(x)\right|<\varepsilon.
  \end{gathered}
$$

The small quantity is the sum of a whole tail, rather than just one term of the series.

### The Weierstrass majorant test {id="the-weierstrass-majorant-test"}

:::div{id="thm:analysis-i:weierstrass-m-test" class="result theorem"}

**Theorem 8.4.3 (Weierstrass $M$-test).** Suppose $f_n:D\to\mathbb{R}$ and there are numbers $M_n\ge0$ such that

$$
\forall x\in D\quad |f_n(x)|\le M_n,\qquad
    \sum_{n=0}^{\infty}M_n<\infty.
$$

Then both $\sum f_n$ and $\sum |f_n|$ converge uniformly on $D$. In particular, $\sum f_n(x)$ converges absolutely at every input. Writing $S=\sum f_n$ and $S_N=\sum_{n=0}^N f_n$, we have

$$
\forall x\in D\quad
    |S(x)-S_N(x)|\le\sum_{n=N+1}^{\infty}M_n.
$$

:::

:::div{class="proof"}

*Proof.* The convergent numerical series $\sum M_n$ has arbitrarily small tails. For $m>n$ and every $x\in D$,

$$
\left|\sum_{k=n+1}^{m}f_k(x)\right|
      \le\sum_{k=n+1}^{m}|f_k(x)|
      \le\sum_{k=n+1}^{m}M_k.
$$

The same estimate holds with $f_k$ replaced by $|f_k|$. The uniform Cauchy criterion therefore proves both uniform-convergence claims. Letting $m\to\infty$ in the estimate with $n=N$ gives the stated remainder bound. Absolute convergence at each input also follows from comparison with $\sum M_n$. ◻

:::

The majorant $M_n$ must be independent of $x$ on the whole domain under consideration. Once it is found, a numerical tail estimate controls all functional errors at once. If every $f_n$ is continuous on $[a,b]$, its partial sums are continuous. The sum is then continuous by [Theorem 8.3.2](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:uniform-limit-continuity).

:::div{id="web:sections/analysis-i/08-sequences-and-series-of-functions/04-cauchy-criterion-for-uniform-convergence:3789" class="result example"}

**Example 8.4.4 (A uniform geometric tail).** For $0<r<1$ and $x\in[-r,r]$, we have $|x^n|\le r^n$. The $M$-test proves absolute and uniform convergence of $\sum_{n=0}^{\infty}x^n$ there, with the explicit estimate

$$
\left|\frac1{1-x}-\sum_{n=0}^{N}x^n\right|
      \le\frac{r^{N+1}}{1-r}.
$$

On the larger interval $(-1,1)$ the series is pointwise absolutely convergent but is not uniformly convergent. Uniform convergence would force $x^n$ to tend uniformly to zero, whereas $\sup_{|x|<1}|x^n|=1$ for every $n$.

:::

## 8.5 Uniform convergence and integration {id="sec:analysis-i:uniform-convergence-and-integration"}

## 8.6 Power series {id="sec:analysis-i:power-series"}

A power series uses a variable as the base of each term. For each fixed value of that variable, it is an ordinary number series, so the tests from [§ 4.2](/notes/maths-analysis/analysis-i/infinite-series-of-numbers/#sec:analysis-i:comparison-tests) apply.

:::div{id="web:sections/analysis-i/08-sequences-and-series-of-functions/06-power-series:257" class="result definition"}

**Definition 8.6.1.** A *power series centred at zero* has the form

$$
\sum_{n=0}^{\infty}c_nx^n,
$$

where the coefficients $c_n$ are fixed real numbers. Its *radius of convergence* is a number $R\in[0,+\infty]$ such that the series converges absolutely for $|x|<R$ and diverges for $|x|>R$. The points $x=\pm R$, when $0<R<\infty$, must be examined separately.

:::

:::div{id="thm:analysis-i:power-series-radius" class="result proposition"}

**Proposition 8.6.2.** Every real power series centred at zero has a radius of convergence $R\in[0,+\infty]$ with the properties in the preceding definition.

:::

:::div{class="proof"}

*Proof.* At $x=0$ the constant term is $c_0$ and every other term vanishes, so the series converges there. Suppose it converges at some $x_0\ne0$. Its terms tend to zero by [Proposition 4.1.3](/notes/maths-analysis/analysis-i/infinite-series-of-numbers/#thm:analysis-i:series-term-test), so there is a number $B>0$ such that $|c_nx_0^n|\le B$ for every $n\ge0$. If $|x|<|x_0|$, then

$$
|c_nx^n|\le B\left(\frac{|x|}{|x_0|}\right)^n.
$$

The geometric majorant converges. Thus convergence at any nonzero point implies absolute convergence at every point closer to zero.

Let $S$ consist of the nonnegative values $r$ where the power series converges absolutely. This set contains $0$. If $S$ is bounded above, let $R=\sup S$. Otherwise let $R=+\infty$. If $|x|<R$, there is an $r\in S$ with $|x|<r$. The preceding comparison then proves absolute convergence at $x$. For $R=0$ this interior condition is empty, while convergence at zero remains.

If $R<\infty$ and the series converged at a point with $|x|>R$, choose $t$ with $R<t<|x|$. The same comparison would give absolute convergence at $t$, so $t\in S$, contradicting that $R$ is an upper bound. The series therefore diverges for $|x|>R$. This proves all the required properties. Boundary behaviour when $0<R<\infty$ still requires separate tests. ◻

:::

An infinite radius means absolute convergence for every real $x$.

### Computing the radius and controlling interior intervals {id="computing-the-radius-and-controlling-interior-intervals"}

For the series $\sum c_nx^n$, set

$$
L=\limsup_{n\to\infty}|c_n|^{1/n}.
$$

Then

$$
R=\frac1L,\qquad \frac10=+\infty,\qquad \frac1{+\infty}=0.
$$

Indeed, for $x\ne0$ the upper limit of the $n$th roots of the terms is $|x|L$. A value below $1$ gives absolute convergence by [Theorem 4.2.6](/notes/maths-analysis/analysis-i/infinite-series-of-numbers/#thm:analysis-i:root-test). A value above $1$ gives infinitely many terms whose absolute values exceed a fixed geometric sequence with ratio greater than $1$, so the terms fail to tend to zero. These arguments also cover $L=0$ and $L=+\infty$. If the coefficients are eventually nonzero and $|c_{n+1}/c_n|\to\ell$, the ratio test gives the alternative formula $R=1/\ell$, with the same conventions. Neither formula decides the finite endpoints.

:::div{id="thm:analysis-i:power-series-local-uniform" class="result proposition"}

**Proposition 8.6.3 (Uniform convergence inside the radius).** If a power series has radius $R>0$, it converges absolutely and uniformly on every $[-r,r]$ with $0\le r<R$. Its sum is continuous on $(-R,R)$.

:::

:::div{class="proof"}

*Proof.* For $0<r<R$, set $M_n=|c_n|r^n$. The numerical series $\sum M_n$ converges by the radius property, and $|c_nx^n|\le M_n$ for every $x\in[-r,r]$. Apply [Theorem 8.4.3](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:weierstrass-m-test). At $r=0$ only the constant term remains. Each partial sum is a polynomial, hence continuous, so [Theorem 8.3.2](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:uniform-limit-continuity) makes the sum continuous on every such interval. Every point of $(-R,R)$ lies in the interior of one of them. ◻

:::

Uniform convergence on each smaller closed interval need not mean uniform convergence on the whole open interval. The geometric-series example following [Theorem 8.4.3](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:weierstrass-m-test) shows this.

### The geometric power series {id="the-geometric-power-series"}

The series $\sum_{n=0}^{\infty}x^n$ has radius $R=1$, since [§ 4.1](/notes/maths-analysis/analysis-i/infinite-series-of-numbers/#sec:analysis-i:number-series) proves that it converges exactly for $|x|<1$. Neither endpoint is included. At $x=1$ every term is $1$. At $x=-1$ the terms alternate between $1$ and $-1$. In both cases the terms fail to tend to zero.

### Algebraic and transcendental functions {id="algebraic-and-transcendental-functions"}

:::div{id="thm:analysis-i:algebraic-function" class="result definition"}

**Definition 8.6.4 (Algebraic and transcendental functions).** A real-valued function $f$ on a nonempty open interval $I$ is *algebraic* if there is a nonzero polynomial $P(X,Y)$ with real coefficients such that

$$
\forall x\in I\quad P(x,f(x))=0.
$$

A function for which no such polynomial exists is *transcendental*.

:::

For a polynomial function $f(x)=p(x)$, take $P(X,Y)=Y-p(X)$. For $f(x)=p(x)/q(x)$ on an interval where $q$ never vanishes, take $P(X,Y)=q(X)Y-p(X)$. The root function $f(x)=\sqrt{x}$ on $(0,\infty)$ is algebraic because $f(x)^2-x=0$.

The classification concerns a polynomial relation between input and output. Here the coefficients may be arbitrary real numbers. Thus even the constant function $f(x)=\pi$ is algebraic, using $Y-\pi=0$, although $\pi$ is a transcendental number over $\mathbb{Q}$. The exponential and logarithm below are transcendental functions on their full real domains, as we will prove after constructing them.

### The exponential series {id="the-exponential-series"}

Consider the polynomials and their limiting series

$$
E_N(x)=\sum_{k=0}^{N}\frac{x^k}{k!},\qquad
  E(x)=\sum_{k=0}^{\infty}\frac{x^k}{k!}.
$$

For fixed $x\ne0$, the absolute successive-term ratio is

$$
\frac{|x|^{k+1}/(k+1)!}{|x|^k/k!}
  =\frac{|x|}{k+1}\longrightarrow0.
$$

The ratio test proves absolute convergence for every such $x$. At $x=0$, only the constant term remains, so $E(0)=1$. Thus this series has infinite radius of convergence and $E_N(x)\to E(x)$ for every fixed real $x$. We write $E(x)=e^x$. The remaining properties follow from uniform convergence and series multiplication, as shown below. At $x=1$ the sum is the earlier factorial-series definition of $e$.

### Exponential and logarithmic properties {id="exponential-and-logarithmic-properties"}

:::div{id="thm:analysis-i:exponential-properties" class="result theorem"}

**Theorem 8.6.5 (The exponential function).** The series $E(x)=\sum_{n=0}^{\infty}x^n/n!$ defines a continuous, strictly increasing bijection from $\mathbb{R}$ onto $(0,\infty)$. It satisfies

$$
E(0)=1,\qquad E(1)=e,\qquad E(x+y)=E(x)E(y),
$$

and

$$
E(-x)=\frac1{E(x)},\qquad
    \lim_{x\to\infty}E(x)=+\infty,\qquad
    \lim_{x\to-\infty}E(x)=0.
$$

:::

:::div{class="proof"}

*Proof.* On every $[-r,r]$, the bounds $|x^n/n!|\le r^n/n!$ have a convergent numerical sum by the ratio test. By [Theorem 8.4.3](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:weierstrass-m-test) and [Theorem 8.3.2](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:uniform-limit-continuity), $E$ is continuous there, hence on $\mathbb{R}$. Its values at zero and one follow directly from the series and the earlier definition of $e$.

Both exponential series converge absolutely. By [Theorem 4.4.4](/notes/maths-analysis/analysis-i/infinite-series-of-numbers/#thm:analysis-i:absolute-cauchy-product), their product is the series whose $n$th coefficient is

$$
\sum_{k=0}^{n}\frac{x^ky^{n-k}}{k!(n-k)!}
      =\frac1{n!}\sum_{k=0}^{n}\binom nk x^ky^{n-k}
      =\frac{(x+y)^n}{n!}.
$$

The finite binomial theorem therefore gives $E(x)E(y)=E(x+y)$. Taking $y=-x$ gives $E(x)E(-x)=1$, so neither factor is zero. Also $E(x)=E(x/2)^2>0$.

If $h>0$, the series gives $E(h)\ge1+h>1$. Hence $E(x+h)=E(x)E(h)>E(x)$, proving strict increase. For $x\ge0$, the same bound $E(x)\ge1+x$ gives divergence to $+\infty$. The reciprocal identity gives the limit zero at $-\infty$. Continuity and [Theorem 5.3.1](/notes/maths-analysis/analysis-i/continuity/#thm:analysis-i:intermediate-value) now show that every positive value is attained, and strict increase gives uniqueness. ◻

:::

:::div{id="thm:analysis-i:logarithm-real-powers" class="result definition"}

**Definition 8.6.6 (Natural logarithm and positive-base powers).** The *natural logarithm* is the inverse function $\ln:(0,\infty)\to\mathbb{R}$ of $E$. We write $e^x=E(x)$, and for a positive base $a$ and real exponent $r$ define

$$
a^r=E(r\ln a).
$$

:::

The inverse is continuous by [Theorem 5.3.6](/notes/maths-analysis/analysis-i/continuity/#thm:analysis-i:continuous-inverse), applied on closed subintervals of $\mathbb{R}$, and is strictly increasing. Its defining identities and endpoint limits are

$$
\begin{gathered}
    \ln(e^x)=x,\qquad e^{\ln t}=t\quad(t>0),\\
    \ln1=0,\qquad \ln e=1,\\
    \lim_{t\to0^+}\ln t=-\infty,\qquad
    \lim_{t\to\infty}\ln t=+\infty.
  \end{gathered}
$$

For the endpoint limits, compare $t$ with $E(A)$ for any fixed real $A$ and use the strict increase of the inverse.

For $u,v>0$, the addition law gives $E(\ln u+\ln v)=uv$. Applying the inverse, and then using the reciprocal identity, proves

$$
\ln(uv)=\ln u+\ln v,\qquad
  \ln(u/v)=\ln u-\ln v.
$$

The definition of powers consequently gives, for $a,b>0$ and $r,s\in\mathbb{R}$,

$$
\begin{gathered}
    a^0=1,\qquad a^{r+s}=a^ra^s,\qquad
    \ln(a^r)=r\ln a,\\
    (a^r)^s=a^{rs},\qquad (ab)^r=a^rb^r.
  \end{gathered}
$$

For rational $r=m/n$, the positive number $E(r\ln a)$ has $n$th power $a^m$, so uniqueness of positive roots identifies it with the earlier rational power. The real-exponent definition therefore extends that construction. Continuity of $E$ and $\ln$ makes $a^r$ continuous in each variable on its domain. As a function of $r$ it is strictly increasing for $a>1$, constant for $a=1$, and strictly decreasing for $0<a<1$, according to the sign of $\ln a$.

:::div{id="web:sections/analysis-i/08-sequences-and-series-of-functions/06-power-series:9557" class="result example"}

**Example 8.6.7 (Why the exponential and logarithm are transcendental).** Suppose a nonzero polynomial relation held for $E$ on $\mathbb{R}$. Write it as $\sum_{k=0}^{m}p_k(x)E(x)^k=0$, with $p_m$ a nonzero polynomial. A relation with $m=0$ would already make a nonzero polynomial vanish everywhere, which is impossible. For $m\ge1$, division by $E(x)^m$ gives

$$
p_m(x)=-\sum_{k=0}^{m-1}p_k(x)E(-(m-k)x).
$$

Each term on the right tends to zero as $x\to\infty$. Indeed, if $d$ is the degree of a nonzero $p_k$, choose an integer $N>d$. For $x\ge1$, there is a constant $C$ with $|p_k(x)|\le Cx^d$, while the positive-term series gives, for $c=m-k>0$,

$$
E(cx)\ge\frac{(cx)^N}{N!},\qquad
    |p_k(x)|E(-cx)\le\frac{CN!}{c^N}x^{d-N}\longrightarrow0.
$$

This would make $p_m(x)\to0$, which no nonzero polynomial can do as $x\to\infty$. Thus $E$ is transcendental on $\mathbb{R}$.

If a nonzero polynomial $P$ satisfied $P(t,\ln t)=0$ for all $t>0$, substituting $t=E(x)$ would give $P(E(x),x)=0$ for every real $x$. Interchanging the two polynomial variables produces a forbidden polynomial relation for $E$. Hence $\ln$ is transcendental on $(0,\infty)$ as well. This concerns the whole function. For example, its individual value $E(0)=1$ is rational.

:::

These properties supply the exponential and logarithmic background for the following exercises and for the derivative calculations in [§ 6.1](/notes/maths-analysis/analysis-i/differentiation-and-applications/#sec:analysis-i:differentiation).

::statement{key="hw06:exponential-continuity"}

::statement{key="hw06:arbitrary-base-exponential"}

::statement{key="hw06:exponential-scaling"}

::statement{key="hw06:logarithm-power-law"}

### Exponential and logarithmic limits {id="exponential-and-logarithmic-limits"}

::statement{key="hw06:exponential-dominates-powers"}

::statement{key="hw06:logarithmic-boundary-limit"}

### A family with different endpoints {id="a-family-with-different-endpoints"}

Let $s\ge0$ be a real number and consider

$$
F_s(x)=\sum_{n=1}^{\infty}\frac{x^n}{n^s}.
$$

As in the $p$-series example, real powers use their usual exponent and order laws. For $x\ne0$, the $n$th root of the absolute value of the $n$th term is

$$
\left|\frac{x^n}{n^s}\right|^{1/n}
  =\frac{|x|}{(n^{1/n})^s}\longrightarrow |x|.
$$

To justify the denominator’s limit using the sequence results already available, choose an integer $m\ge s$. Since $n^{1/n}\ge1$,

$$
1\le(n^{1/n})^s\le(n^{1/n})^m\longrightarrow1.
$$

The last limit follows from [Proposition 3.1.5](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#thm:analysis-i:root-sequence-limits) and the product rule, and the squeeze principle gives the desired limit.

For $|x|<1$, the root test proves absolute convergence, with $x=0$ immediate. For $|x|>1$, choose $1<r<|x|$. The root values eventually exceed $r$, so $|x^n/n^s|>r^n$ for every sufficiently large $n$. The terms do not tend to zero and the series diverges. Therefore $R=1$ for every $s\ge0$.

:::::div{class="margin-figure"}

::::figure{id="fig:power-series-endpoints"}

[![All three cases have radius 1. Open or filled endpoint markers record the separate tests at -1 and 1. The radius alone does not settle them.](/notes/maths-analysis/figures/power-series-endpoints.svg){.tikz-diagram}](/notes/maths-analysis/figures/power-series-endpoints.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 8.4. All three cases have radius $1$. Open or filled endpoint markers record the separate tests at $-1$ and $1$. The radius alone does not settle them.

:::

::::

:::::

At $x=1$, this is the $p$-series, which converges exactly when $s>1$. At $x=-1$, it is $\sum(-1)^n/n^s$, which converges for $s>0$ by [Example 4.4.2](/notes/maths-analysis/analysis-i/infinite-series-of-numbers/#ex:analysis-i:alternating-power-series). For $s=0$, the terms do not tend to zero. Accordingly the intervals of convergence are

$$
\begin{array}{c|c}
    s=0 & (-1,1)\\[3pt]
    0<s\le1 & [-1,1)\\[3pt]
    s>1 & [-1,1].
  \end{array}
$$

[Figure 8.4](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#fig:power-series-endpoints) keeps the three cases distinct.

The following exercise introduces a scale factor in the coefficients. Use the series tests for the interior and exterior, then examine absolute convergence at each endpoint separately.

::statement{key="hw04:scaled-power-series"}

The next question composes a power series with a rational function. Check the domain of that rational function as well as the convergence interval of the series in its own variable.

::statement{key="hw06:composed-power-series"}

### Analytic functions and the multiplicity of a zero {id="sec:analysis-i:analytic-functions"}

:::div{id="thm:analysis-i:analytic-function" class="result definition"}

**Definition 8.6.16 (Real analytic function).** A function is *analytic at $a$* if, on some neighbourhood of $a$, it equals a convergent power series

$$
f(x)=\sum_{k=0}^{\infty}b_k(x-a)^k.
$$

It is analytic on an open interval if this holds at every point.

:::

A convergent power series can be differentiated term by term at every point strictly inside its radius of convergence. We state this power-series differentiation theorem here without proof. Repeated application gives $b_k=f^{(k)}(a)/k!$, so an analytic function equals its Taylor series locally. Taylor’s theorem alone does not assert this equality. Its remainder must tend to zero.

Suppose $f(a)=0$ and its local series has a first nonzero coefficient $b_m$, where $m\ge1$. Factoring gives

$$
f(x)=(x-a)^m g(x),\qquad
  g(x)=\sum_{j=0}^{\infty}b_{m+j}(x-a)^j,\qquad g(a)=b_m\ne0.
$$

The shifted series converges on the same neighbourhood. Continuity makes $g$ nonzero sufficiently close to $a$, so $a$ is an isolated zero. The integer $m$ is its *multiplicity*. If every coefficient vanishes, the function is zero on a neighbourhood and this argument does not assign a finite multiplicity.

:::div{id="web:sections/analysis-i/08-sequences-and-series-of-functions/06-analytic-and-approximation:1337" class="result example"}

**Example 8.6.17 (A simple zero of an exponential difference).** The function $e^x$ never vanishes, but

$$
e^x-1=x\left(1+\frac{x}{2!}+\frac{x^2}{3!}+\cdots\right).
$$

The factor in parentheses is continuous and has value $1$ at zero. Thus zero is a root of multiplicity one of $e^x-1$.

:::

:::div{id="web:sections/analysis-i/08-sequences-and-series-of-functions/06-analytic-and-approximation:1648" class="result example"}

**Example 8.6.18 (Trigonometric series and Euler’s identity).** Taylor’s theorem gives

$$
\cos x=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n}}{(2n)!},\qquad
    \sin x=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+1}}{(2n+1)!}.
$$

Indeed, successive derivatives cycle through sine and cosine with signs, and have absolute value at most one. The remainder after degree $N$ is bounded by $|x|^{N+1}/(N+1)!$, which tends to zero for fixed $x$ by the ratio test.

Define $e^z=\sum_{k=0}^{\infty}z^k/k!$ for $z\in\mathbb{C}$. The ratio test applied to absolute values proves convergence. Its even and odd terms can therefore be separated. Since $i^{2n}=(-1)^n$ and $i^{2n+1}=i(-1)^n$, the two displayed series give

$$
e^{ix}=\cos x+i\sin x.
$$

In particular $e^{i\pi}+1=0$. No complex differentiation is used.

:::

### Uniform polynomial approximation {id="sec:analysis-i:polynomial-approximation"}

Taylor polynomials use derivatives at one point. Uniform polynomial approximation asks for small error on an entire interval and requires only continuity, even for a function with corners.

:::div{id="thm:analysis-i:weierstrass-approximation" class="result theorem"}

**Theorem 8.6.19 (Weierstrass approximation theorem).** If $f\in C[a,b]$ with $a<b$, then for every $\varepsilon>0$ there exists a polynomial $P$ such that

$$
\forall x\in[a,b]\quad |f(x)-P(x)|<\varepsilon.
$$

:::

[^53]

:::notes{id="footnotes-52"}

[^53]: Sergei Bernstein’s 1912 paper offers a proof of Weierstrass’s theorem based on probability ([Bernstein 1912](/notes/maths-analysis/references/#ref-Bernstein1912)). The weights below are binomial probabilities. They average nearby sampled values and concentrate around the input as $n$ grows. This connects uniform approximation to concentration of random averages. Sergei Bernstein is a different mathematician from Felix Bernstein of [Theorem 1.3.3](/notes/maths-analysis/analysis-i/sets-and-foundations/#thm:analysis-i:cantor-bernstein).

:::

:::div{class="proof"}

*Proof by Bernstein polynomials.* First suppose $[a,b]=[0,1]$. For $n\ge1$, define

$$
w_{n,k}(x)=\binom nk x^k(1-x)^{n-k},\qquad
    B_nf(x)=\sum_{k=0}^n w_{n,k}(x)f(k/n).
$$

Polynomial values at endpoints use the usual constant-power convention. The binomial theorem gives $w_{n,k}(x)\ge0$ and $\sum_{k=0}^n w_{n,k}(x)=1$ on $[0,1]$. The identities $k\binom nk=n\binom{n-1}{k-1}$ and $k(k-1)\binom nk=n(n-1)\binom{n-2}{k-2}$ give

$$
\sum_{k=0}^n\frac{k}{n}w_{n,k}(x)=x,\qquad
    \sum_{k=0}^n\left(\frac{k}{n}-x\right)^2w_{n,k}(x)
       =\frac{x(1-x)}n\le\frac1{4n}.
$$

For the second identity, first sum $k(k-1)$ and $k$ to obtain $\sum k^2w_{n,k}=n(n-1)x^2+nx$, and expand the square. For $n=1$ the $k(k-1)$ terms are all zero, so the same identity holds.

By the extreme value theorem, $|f|\le M$ for some $M>0$. By uniform continuity, choose $\delta>0$ such that $|f(u)-f(v)|<\varepsilon/2$ whenever $|u-v|<\delta$. Since the weights sum to one,

$$
|B_nf(x)-f(x)|
      \le\sum_{k=0}^n w_{n,k}(x)|f(k/n)-f(x)|.
$$

Split the sum according to whether $|k/n-x|<\delta$ or $|k/n-x|\ge\delta$. The first part is at most $\varepsilon/2$. For the second part, use $|f(k/n)-f(x)|\le2M$ and $1\le(k/n-x)^2/\delta^2$. Thus, for every $x\in[0,1]$,

$$
|B_nf(x)-f(x)|\le\frac{\varepsilon}{2}
      +\frac{2M}{\delta^2}\frac{x(1-x)}n
      \le\frac{\varepsilon}{2}+\frac{M}{2n\delta^2}.
$$

Taking $n>M/(\varepsilon\delta^2)$ makes the last expression strictly less than $\varepsilon$. The choice is independent of $x$, proving uniform convergence.

For a general interval, apply this construction to $g(t)=f(a+(b-a)t)$ on $[0,1]$. Substituting $t=(x-a)/(b-a)$ in an approximating polynomial gives a polynomial in $x$ with the same error bound on $[a,b]$. ◻

:::

The two mechanisms in the proof are different. Uniform continuity controls the error at nearby samples. The second-moment bound controls the total weight of distant samples. A corner can therefore be approximated without differentiating it, as in [Figure 8.5](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#fig:analysis-i:bernstein-approximation).

::::figure{id="fig:analysis-i:bernstein-approximation"}

[![ The function f(x)=\|2x-1\| (black) and its Bernstein polynomials of degrees 2 and 8 (grey). The smooth polynomials approach a function that is not differentiable at x=1/2. Only \[0,1\] is shown.](/notes/maths-analysis/figures/bernstein-approximation.svg){.tikz-diagram}](/notes/maths-analysis/figures/bernstein-approximation.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 8.5. The function $f(x)=|2x-1|$ (black) and its Bernstein polynomials of degrees $2$ and $8$ (grey). The smooth polynomials approach a function that is not differentiable at $x=1/2$. Only $[0,1]$ is shown.

:::

::::
