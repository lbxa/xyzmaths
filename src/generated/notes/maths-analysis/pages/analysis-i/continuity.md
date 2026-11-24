---
title: "Continuity"
group: "Analysis I"
order: 10
part: "Part I · Analysis I"
page: "81"
outline: [{"id": "sec:analysis-i:continuity", "title": "5.1 Continuity", "level": 2}, {"id": "limits-and-continuity-at-a-point", "title": "Limits and continuity at a point", "level": 3}, {"id": "algebra-of-limits", "title": "Algebra of limits", "level": 3}, {"id": "testing-continuity-with-sequences", "title": "Testing continuity with sequences", "level": 3}, {"id": "examples-of-discontinuity", "title": "Examples of discontinuity", "level": 3}, {"id": "composition", "title": "Composition", "level": 3}, {"id": "sec:analysis-i:extreme-value-theorem", "title": "5.2 Maximum (extreme value theorem)", "level": 2}, {"id": "intermediate-value-theorem", "title": "Intermediate value theorem", "level": 2}, {"id": "roots-as-an-application", "title": "Roots as an application", "level": 3}, {"id": "continuity-of-an-inverse", "title": "Continuity of an inverse", "level": 3}, {"id": "sec:analysis-i:uniform-continuity", "title": "5.4 Uniform continuity", "level": 2}, {"id": "exercises-on-uniform-continuity", "title": "Exercises on uniform continuity", "level": 3}, {"id": "piecewise-linear-approximation", "title": "Piecewise linear approximation", "level": 3}]
---

# Chapter 5. Continuity {id="ch:analysis-i:continuity"}

Continuity turns small changes in an input into small changes in its output. We begin with this local condition, then use subsequences and completeness to prove that continuous functions attain extrema and intermediate values. On a closed bounded interval, uniform continuity also lets us approximate the whole graph by straight segments.

## 5.1 Continuity {id="sec:analysis-i:continuity"}

### Limits and continuity at a point {id="limits-and-continuity-at-a-point"}

Let $I\subseteq\mathbb{R}$ be an interval containing at least two points, and let $f:I\to\mathbb{R}$.

:::div{id="thm:analysis-i:function-limit" class="result definition"}

**Definition 5.1.1 (Limit of a function).** Suppose that $c$ can be approached by points of $I\setminus\{c\}$. We write

$$
\lim_{x\to c}f(x)=L
$$

if, for every $\varepsilon>0$, there is a $\delta>0$ such that

$$
x\in I,\quad 0<|x-c|<\delta
    \quad\Longrightarrow\quad |f(x)-L|<\varepsilon.
$$

:::

The condition $0<|x-c|$ excludes the point $c$ itself. The limit describes the values near $c$, so it does not depend on the value $f(c)$, or even require that $f(c)$ be defined.

The *left-hand limit* and *right-hand limit* are written

$$
\lim_{x\to c^-}f(x)=L_-,
  \qquad
  \lim_{x\to c^+}f(x)=L_+.
$$

Their definitions restrict the input condition to $0<c-x<\delta$ and $0<x-c<\delta$, respectively. When $c$ is an interior point of $I$, the two-sided limit exists exactly when both one-sided limits exist and have the same value.

::::div{id="web:sections/analysis-i/05-continuity/01-continuity:1111" class="result definition"}

**Definition 5.1.2 (Continuity).** [^33] :anchor[]{id="thm:analysis-i:continuity-at-a-point"} The function $f$ is *continuous at* $c\in I$ if

$$
\lim_{x\to c}f(x)=f(c).
$$

Equivalently, for every $\varepsilon>0$, there is a $\delta>0$ such that

$$
x\in I,\quad |x-c|<\delta
    \quad\Longrightarrow\quad |f(x)-f(c)|<\varepsilon.
$$

It is *continuous on* $I$ if it is continuous at every point of $I$.

:::notes{id="footnotes-32"}

[^33]: Cauchy described continuity through infinitesimal increments in 1821. Heine’s 1872 presentation gives the later quantified framework ([Cauchy 1821](/notes/maths-analysis/references/#ref-Cauchy1821), ch. II) ([Heine 1872](/notes/maths-analysis/references/#ref-Heine1872)). The modern epsilon–delta statement separates a point, an output tolerance, and a permitted input change. This precision made discontinuous functions and rigorous limiting arguments manageable.

:::

::::

For $c\in I$, *left continuity* and *right continuity* mean, respectively,

$$
\lim_{x\to c^-}f(x)=f(c),\qquad
  \lim_{x\to c^+}f(x)=f(c).
$$

Each condition is considered when $c$ can be approached from that side through the domain. At an endpoint of $I$, only inputs belonging to $I$ are considered. Thus continuity on $[a,b]$ means ordinary continuity in $(a,b)$, right continuity at $a$, and left continuity at $b$. [Figure 5.1](/notes/maths-analysis/analysis-i/continuity/#fig:analysis-i:continuity-basic-neighbourhood) shows how an input neighbourhood is chosen to fit a prescribed output neighbourhood.

:::::div{class="margin-figure"}

::::figure{id="fig:analysis-i:continuity-basic-neighbourhood"}

[![ A schematic continuous graph. Inputs within \\delta of c have outputs within \\varepsilon of f(c). The graph over the shaded input strip lies inside the horizontal output band. The arrows measure 2\\delta and 2\\varepsilon.](/notes/maths-analysis/figures/continuity-basic-neighbourhood.svg){.tikz-diagram}](/notes/maths-analysis/figures/continuity-basic-neighbourhood.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.1. A schematic continuous graph. Inputs within $\delta$ of $c$ have outputs within $\varepsilon$ of $f(c)$. The graph over the shaded input strip lies inside the horizontal output band. The arrows measure $2\delta$ and $2\varepsilon$.

:::

::::

:::::

### Algebra of limits {id="algebra-of-limits"}

:::div{id="thm:analysis-i:function-limit-laws" class="result proposition"}

**Proposition 5.1.3 (Limit laws).** Suppose that

$$
\lim_{x\to c}f(x)=F,
    \qquad
    \lim_{x\to c}g(x)=G,
$$

where $F,G\in\mathbb{R}$. For every $k\in\mathbb{R}$,

$$
\begin{aligned}
    \lim_{x\to c}k f(x)&=kF,\\
    \lim_{x\to c}\bigl(f(x)+g(x)\bigr)&=F+G,\\
    \lim_{x\to c}\bigl(f(x)-g(x)\bigr)&=F-G,\\
    \lim_{x\to c}f(x)g(x)&=FG.
  
\end{aligned}
$$

Also,

$$
\lim_{x\to c}\frac{f(x)}{g(x)}=\frac{F}{G}
    \qquad\text{provided }G\ne0.
$$

:::

:::div{class="proof"}

*Proof.* Fix $\varepsilon>0$. For the sum, choose input neighbourhoods in which $|f(x)-F|<\varepsilon/2$ and $|g(x)-G|<\varepsilon/2$. Taking the smaller of their two radii ensures both estimates whenever $x\in I$ and $0<|x-c|$ is smaller than that radius. Then

$$
|f(x)+g(x)-(F+G)|
      \le |f(x)-F|+|g(x)-G|<\varepsilon.
$$

If $k=0$, the scalar-multiple rule is immediate. If $k\ne0$, choose a neighbourhood in which $|f(x)-F|<\varepsilon/|k|$. Then $|kf(x)-kF|<\varepsilon$. The difference rule follows by applying the sum rule to $f$ and $-g$.

For the product, first restrict the neighbourhood so that $|f(x)-F|<1$, which gives $|f(x)|\le |F|+1$. Shrink it further so that both

$$
|g(x)-G|<\frac{\varepsilon}{2(|F|+1)},\qquad
    |f(x)-F|<\frac{\varepsilon}{2(|G|+1)}
$$

hold. Such a common neighbourhood exists by the two assumed limits. Within it,

$$
\begin{aligned}
    |f(x)g(x)-FG|
      &\le |f(x)|\,|g(x)-G|+|G|\,|f(x)-F|\\
      &\le (|F|+1)|g(x)-G|+|G|\,|f(x)-F|\\
      &<\varepsilon.
  
\end{aligned}
$$

Finally, suppose $G\ne0$. Choose a neighbourhood in which $|g(x)-G|<|G|/2$. The reverse triangle inequality gives $|g(x)|>|G|/2>0$ there, and hence

$$
\left|\frac1{g(x)}-\frac1G\right|
      =\frac{|g(x)-G|}{|g(x)|\,|G|}
      \le\frac{2|g(x)-G|}{|G|^2}.
$$

Shrinking the neighbourhood to also require $|g(x)-G|<\varepsilon|G|^2/2$ makes this error smaller than $\varepsilon$. Thus $1/g(x)\to1/G$. Apply the product rule to $f$ and $1/g$ to obtain $f(x)/g(x)\to F/G$. ◻

:::

The last condition ensures that $g(x)$ is nonzero sufficiently near $c$. These laws show that sums, scalar multiples, and products of continuous functions are continuous. A quotient is continuous wherever its denominator is nonzero. In particular, constant functions and $x\mapsto x$ are continuous, so every polynomial is continuous.

::statement{key="hw05:absolute-value-continuity"}

### Testing continuity with sequences {id="testing-continuity-with-sequences"}

The following characterization connects the definition above with the sequence methods already developed. The sequences approach $c$ through the domain of the function, including from only one side at an endpoint.

:::div{id="thm:analysis-i:sequential-continuity" class="result theorem"}

**Theorem 5.1.5 (Sequential characterization of continuity).** Let $f:I\to\mathbb{R}$ and $c\in I$. Then $f$ is continuous at $c$ if and only if every sequence $(x_n)$ in $I$ satisfies

$$
x_n\to c\quad\Longrightarrow\quad f(x_n)\to f(c).
$$

:::

:::div{class="proof"}

*Proof.* Suppose first that $f$ is continuous at $c$ and that $x_n\to c$. Given $\varepsilon>0$, continuity provides a $\delta>0$ such that $|f(x)-f(c)|<\varepsilon$ whenever $x\in I$ and $|x-c|<\delta$. Since $x_n\to c$, this input condition holds for all sufficiently large $n$. Hence $f(x_n)\to f(c)$.

Conversely, suppose that $f$ is not continuous at $c$. There is then an $\varepsilon_0>0$ such that, for every $n\in\mathbb{N}$, we can choose $x_n\in I$ with

$$
|x_n-c|<\frac1n,
    \qquad |f(x_n)-f(c)|\ge\varepsilon_0.
$$

Thus $x_n\to c$, while $f(x_n)$ does not tend to $f(c)$. This contradicts the stated sequence property and proves the converse. ◻

:::

::statement{key="hw05:continuous-additive-function"}

### Examples of discontinuity {id="examples-of-discontinuity"}

:::div{id="thm:analysis-i:indicator-function" class="result definition"}

**Definition 5.1.7 (Indicator function).** For a set $S\subseteq\mathbb{R}$, its *indicator function* is

$$
\mathbf{1}_S(x)=
    \begin{cases}
      0,&x\notin S,\\
      1,&x\in S.
    \end{cases}
$$

:::

:::div{id="thm:analysis-i:step-discontinuity" class="result example"}

**Example 5.1.8 (A jump at one point).** Fix $a\in\mathbb{R}$ and define

$$
H(x)=
    \begin{cases}
      0,&x\le a,\\
      1,&x>a.
    \end{cases}
$$

Its one-sided limits at $a$ are different, since

$$
\lim_{x\to a^-}H(x)=0,
    \qquad \lim_{x\to a^+}H(x)=1.
$$

Consequently $H$ is discontinuous at $a$, although it is constant near every other point and hence continuous there.

:::

::::div{id="web:sections/analysis-i/05-continuity/01-continuity:7589" class="result example"}

**Example 5.1.9 (The Dirichlet function).** [^34] :anchor[]{id="thm:analysis-i:dirichlet-function"} The *Dirichlet function* is

$$
D(x)=\mathbf{1}_{\mathbb{Q}}(x)=
    \begin{cases}
      0,&x\notin\mathbb{Q},\\
      1,&x\in\mathbb{Q}.
    \end{cases}
$$

This function is nowhere continuous.

:::notes{id="footnotes-33"}

[^34]: Dirichlet’s 1829 discussion of trigonometric representation includes the rational/irrational distinction  ([Dirichlet 1829](/notes/maths-analysis/references/#ref-Dirichlet1829)). Such examples force a broader concept of function than a single familiar analytic formula. This one shows how dense interwoven sets can prevent continuity everywhere.

:::

Every neighbourhood of a real number contains both rational and irrational numbers. Thus, however small the neighbourhood, the function takes both values $0$ and $1$. Taking $\varepsilon=1/2$ in the definition rules out continuity at every point.

::::

::::::div{id="web:sections/analysis-i/05-continuity/01-continuity:8452" class="result example"}

**Example 5.1.10 (Thomae’s function).** [^35]

:::notes{id="footnotes-34"}

[^35]: Thomae’s 1875 book on definite integrals uses a rational-denominator example to investigate discontinuity  ([Thomae 1875](/notes/maths-analysis/references/#ref-Thomae1875)). Its values become small as denominators grow. This separates the density of the discontinuity set from its effect on continuity at an irrational point, and motivates finer integrability criteria. See [Figure 5.2](/notes/maths-analysis/analysis-i/continuity/#fig:portrait:dirichlet-thomae).

:::

:::::div{class="margin-figure"}

::::figure{id="fig:portrait:dirichlet-thomae"}

![Lejeune Dirichlet](/notes/maths-analysis/figures/dirichlet.jpg) ![Johannes Thomae](/notes/maths-analysis/figures/thomae.jpg)

:::figcaption

Figure 5.2. Lejeune Dirichlet (left) and Johannes Thomae (right). Portrait sources ([MacTutor History of Mathematics n.d.x](/notes/maths-analysis/references/#ref-PortraitDirichlet), [n.d.r](/notes/maths-analysis/references/#ref-PortraitThomae); [Bookofproofs contributors, n.d.](/notes/maths-analysis/references/#ref-BookofproofsPortraits)).

:::

::::

:::::

:anchor[]{id="thm:analysis-i:thomae-function"} *Thomae’s function*, also called the *popcorn function*, is

$$
T(x)=
    \begin{cases}
      0,&x\notin\mathbb{Q},\\
      \dfrac1q,&x=\dfrac pq\in\mathbb{Q}.
    \end{cases}
$$

In the rational case, the fraction is written in lowest terms, with $p\in\mathbb{Z}$, $q\in\mathbb{N}$, and $q>0$. In particular, $T(0)=1$.

The function $T$ is discontinuous at every rational point. Indeed, if $c=p/q$ is rational in lowest terms, then $T(c)=1/q>0$. Choose irrational numbers $x_n\to c$. Since $T(x_n)=0$ for every $n$, the sequential characterization rules out continuity at $c$.

The function $T$ is continuous at every irrational point $c$. For a sequence of rational numbers $r_k=p_k/q_k\to c$, the denominators tend to infinity, giving

$$
T(r_k)=\frac1{q_k}\longrightarrow0=T(c).
$$

To justify the assertion about denominators, fix $M\in\mathbb{N}$. The convergent sequence $(r_k)$ eventually lies in $[c-1,c+1]$. Only finitely many reduced fractions in this interval have denominator at most $M$, since their numerators are also bounded. None equals the irrational number $c$, so a sufficiently small neighbourhood of $c$ avoids all of them. Eventually $q_k>M$, proving that $q_k\to\infty$.

Now take any sequence $x_n\to c$. Its irrational terms have $T(x_n)=0$, while the argument above makes the values at its rational terms arbitrarily small as well. Hence $T(x_n)\to0=T(c)$, and [Theorem 5.1.5](/notes/maths-analysis/analysis-i/continuity/#thm:analysis-i:sequential-continuity) proves continuity at $c$. [Figure 5.3](/notes/maths-analysis/analysis-i/continuity/#fig:analysis-i:continuity-basic-thomae) illustrates why only finitely many large values need to be avoided near $c$.

::::::

:::::div{class="margin-figure"}

::::figure{id="fig:analysis-i:continuity-basic-thomae"}

[![ Selected values of T on \[0,1\]. Dots show all reduced fractions with denominator at most 8. Larger denominators give smaller heights. Irrational inputs have value 0. The finite drawing shows only part of the graph.](/notes/maths-analysis/figures/continuity-basic-thomae.svg){.tikz-diagram}](/notes/maths-analysis/figures/continuity-basic-thomae.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.3. Selected values of $T$ on $[0,1]$. Dots show all reduced fractions with denominator at most $8$. Larger denominators give smaller heights. Irrational inputs have value $0$. The finite drawing shows only part of the graph.

:::

::::

:::::

### Composition {id="composition"}

:::div{id="thm:analysis-i:continuous-composition" class="result theorem"}

**Theorem 5.1.11 (Composition of continuous functions).** Let $f:I\to\mathbb{R}$ and $g:J\to\mathbb{R}$, where $f(I)\subseteq J$. If $f$ is continuous at $c$ and $g$ is continuous at $f(c)$, then $g\circ f$ is continuous at $c$, where

$$
(g\circ f)(x)=g(f(x)).
$$

:::

:::div{class="proof"}

*Proof.* If $x_n\to c$ with $x_n\in I$, continuity of $f$ gives $f(x_n)\to f(c)$. These values lie in $J$, so continuity of $g$ gives $g(f(x_n))\to g(f(c))$. Apply [Theorem 5.1.5](/notes/maths-analysis/analysis-i/continuity/#thm:analysis-i:sequential-continuity) to $g\circ f$. ◻

:::

::statement{key="hw05:composition-continuity"}

## 5.2 Maximum (extreme value theorem) {id="sec:analysis-i:extreme-value-theorem"}

:::div{id="thm:analysis-i:extreme-value" class="result theorem"}

**Theorem 5.2.1 (Extreme value theorem).** Let $a<b$ be real numbers and let $f:[a,b]\to\mathbb{R}$ be continuous. Then $f$ is bounded, and both its supremum and its infimum are attained. Thus there are $x_{\min},x_{\max}\in[a,b]$ such that

$$
\forall x\in[a,b]\quad
    f(x_{\min})\le f(x)\le f(x_{\max}).
$$

:::

Boundedness gives a finite supremum. Attainment says more. There must actually be a point of the domain at which the function has this value. [Figure 5.4](/notes/maths-analysis/analysis-i/continuity/#fig:continuity:attained-extrema) illustrates the distinction used in the proof.

:::::div{class="margin-figure"}

::::figure{id="fig:continuity:attained-extrema"}

[![Schematic graph on a closed interval. The maximum M and minimum m are values of the function. The gray points illustrate values approaching M.](/notes/maths-analysis/figures/attained-extrema.svg){.tikz-diagram}](/notes/maths-analysis/figures/attained-extrema.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.4. Schematic graph on a closed interval. The maximum $M$ and minimum $m$ are values of the function. The gray points illustrate values approaching $M$.

:::

::::

:::::

:::div{class="proof"}

*Proof.* Suppose first that $f$ is unbounded above. For each $n\in\mathbb{N}$, choose $x_n\in[a,b]$ such that $f(x_n)>n$. By [Theorem 3.3.1](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#thm:analysis-i:bolzano-weierstrass), the bounded sequence $(x_n)$ has a convergent subsequence $(x_{n_k})$ with $x_{n_k}\to x_0\in[a,b]$. Continuity and [Theorem 5.1.5](/notes/maths-analysis/analysis-i/continuity/#thm:analysis-i:sequential-continuity) give

$$
f(x_{n_k})\longrightarrow f(x_0).
$$

But $f(x_{n_k})>n_k\to\infty$, which is a contradiction. Hence $f$ is bounded above.

The function $-f$ is also continuous. The same argument shows that $-f$ is bounded above, so $f$ is bounded below as well.

Put $M=\sup\{f(x)\mid x\in[a,b]\}$. This is a finite real number. Since $M-1/n$ is not an upper bound, for each $n\in\mathbb{N}$ there is $x_n\in[a,b]$ such that

$$
M-\frac1n<f(x_n)\le M.
$$

Again take a convergent subsequence $x_{n_k}\to x_{\max}\in[a,b]$. Continuity gives

$$
f(x_{\max})=\lim_{k\to\infty}f(x_{n_k})\ge M.
$$

On the other hand, $f(x_{\max})\le M$ by the definition of the supremum. Therefore $f(x_{\max})=M$.

Apply the maximum argument to $-f$. There is $x_{\min}\in[a,b]$ such that $-f(x)\le-f(x_{\min})$ for every $x\in[a,b]$. Thus $f(x_{\min})$ is the minimum of $f$. ◻

:::

::statement{key="hw05:coercive-minimum"}

## Intermediate value theorem {id="intermediate-value-theorem"}

[^36] :anchor[]{id="sec:analysis-i:intermediate-value-theorem"}

:::notes{id="footnotes-35"}

[^36]: Bolzano’s 1817 title announces his aim of proving the existence of a real root between opposite-sign values by analysis, without relying on a drawn curve ([Bolzano 1817](/notes/maths-analysis/references/#ref-Bolzano1817)). The result therefore ties continuity to completeness. Today it underlies existence arguments and the bracketing step in numerical root finding.

:::

:::div{id="thm:analysis-i:intermediate-value" class="result theorem"}

**Theorem 5.3.1 (Intermediate value theorem).** Let $a<b$ be real numbers and let $f:[a,b]\to\mathbb{R}$ be continuous. Write

$$
m=\min_{x\in[a,b]}f(x),\qquad
    M=\max_{x\in[a,b]}f(x).
$$

For every $y_0\in[m,M]$, there is $x_0\in[a,b]$ such that $f(x_0)=y_0$. In other words, the image of $[a,b]$ is the interval

$$
f([a,b])=[m,M].
$$

:::

The extreme value theorem supplies the endpoints of the image. The intermediate value theorem says there are no gaps between them. [Figure 5.5](/notes/maths-analysis/analysis-i/continuity/#fig:continuity:intermediate-crossing) shows the central idea. Subtracting the desired value turns the problem into finding a zero.

:::::div{class="margin-figure"}

::::figure{id="fig:continuity:intermediate-crossing"}

[![Schematic continuous graph. A level y\_0 between the extreme values is reached at some x\_0. For g=f-y\_0, that point is a zero.](/notes/maths-analysis/figures/intermediate-crossing.svg){.tikz-diagram}](/notes/maths-analysis/figures/intermediate-crossing.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.5. Schematic continuous graph. A level $y_0$ between the extreme values is reached at some $x_0$. For $g=f-y_0$, that point is a zero.

:::

::::

:::::

:::div{class="proof"}

*Proof.* If $m=M$, the function is constant and the conclusion follows. The endpoint values $y_0=m$ and $y_0=M$ are already attained by [Theorem 5.2.1](/notes/maths-analysis/analysis-i/continuity/#thm:analysis-i:extreme-value). Suppose that $m<y_0<M$. Choose $a_1,b_1\in[a,b]$ with $f(a_1)=m$ and $f(b_1)=M$, and first suppose that $a_1<b_1$. The continuous function $g(x)=f(x)-y_0$ satisfies

$$
g(a_1)=m-y_0<0,\qquad g(b_1)=M-y_0>0.
$$

Let

$$
S=\{x\in[a_1,b_1]\mid g(x)<0\},\qquad c=\sup S.
$$

The set $S$ contains $a_1$ and is bounded above by $b_1$, so $c$ exists and lies in $[a_1,b_1]$. Continuity and the strict endpoint signs give $a_1<c<b_1$.

If $g(c)<0$, continuity gives points just to the right of $c$ at which $g$ remains negative. Such a point belongs to $S$, contradicting that $c$ is an upper bound. If $g(c)>0$, continuity gives $\eta>0$ such that $g(x)>0$ whenever $x\in(c-\eta,c+\eta)\cap[a_1,b_1]$. The definition of the supremum gives an element of $S$ greater than $c-\eta$, again a contradiction. Hence $g(c)=0$, so $f(c)=y_0$.

If $b_1<a_1$, apply the same argument to $-g$ on $[b_1,a_1]$. Its left endpoint value is negative and its right endpoint value is positive, and a zero of $-g$ is also a zero of $g$. ◻

:::

### Roots as an application {id="roots-as-an-application"}

:::div{id="ex:continuity:roots-by-intermediate-value" class="result example"}

**Example 5.3.2 (Reaching every nonnegative value with a power).** Let $n\in\mathbb{N}$ and consider $f(x)=x^n$ for $x\ge0$. This function is continuous and strictly increasing, with $f(0)=0$ and $f(x)\to\infty$ as $x\to\infty$. For any $c>0$, choose $A>0$ with $A^n>c$. On $[0,A]$, the function takes every value in $[0,A^n]$. Thus there is $b\in[0,A]$ with $b^n=c$, and $b=c^{1/n}$. Every nonnegative real number therefore has an $n$th root. Strict increase gives uniqueness. This is an alternative existence argument to [Theorem 1.11.1](/notes/maths-analysis/analysis-i/sets-and-foundations/#thm:analysis-i:positive-roots), whose earlier proof used completeness directly. The present argument uses continuity of $x^n$, without presupposing continuity of its inverse.

:::

::statement{key="hw05:interval-fixed-point"}

::statement{key="hw05:odd-polynomial-root"}

### Continuity of an inverse {id="continuity-of-an-inverse"}

:::div{id="thm:analysis-i:monotone-functions" class="result definition"}

**Definition 5.3.5 (Monotone functions).** A function $f:I\to\mathbb{R}$ is *nondecreasing* if $x<y$ implies $f(x)\le f(y)$, and *nonincreasing* if $x<y$ implies $f(x)\ge f(y)$. It is *monotone* if it has either property. Replacing these weak inequalities by strict inequalities defines *strictly increasing* and *strictly decreasing* functions. These two cases are called *strictly monotone*.

:::

:::div{id="thm:analysis-i:continuous-inverse" class="result theorem"}

**Theorem 5.3.6 (Continuity of an increasing inverse).** Let $a<b$ be real numbers and let $f:[a,b]\to\mathbb{R}$ be continuous and strictly increasing. Put $c=f(a)$ and $d=f(b)$. Then the inverse function

$$
g=f^{-1}:[c,d]\longrightarrow[a,b]
$$

is continuous.

:::

Strict increase makes $f$ injective, and [Theorem 5.3.1](/notes/maths-analysis/analysis-i/continuity/#thm:analysis-i:intermediate-value) shows that its image is exactly $[c,d]$. Together these facts justify the existence of $g$. The graphs of $f$ and $g$ interchange their coordinates, as [Figure 5.6](/notes/maths-analysis/analysis-i/continuity/#fig:continuity:inverse-reflection) illustrates.

:::::div{class="margin-figure"}

::::figure{id="fig:continuity:inverse-reflection"}

[![The graphs of y=x^2 and y=\\sqrt\{x\} for nonnegative inputs are reflections in y=x. A point (u,v) on one graph corresponds to (v,u) on the other.](/notes/maths-analysis/figures/inverse-reflection.svg){.tikz-diagram}](/notes/maths-analysis/figures/inverse-reflection.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.6. The graphs of $y=x^2$ and $y=\sqrt{x}$ for nonnegative inputs are reflections in $y=x$. A point $(u,v)$ on one graph corresponds to $(v,u)$ on the other.

:::

::::

:::::

:::div{class="proof"}

*Proof.* Suppose that $g$ is not continuous at $y_0\in[c,d]$, and put $x_0=g(y_0)$. By the failure of continuity, there are $\varepsilon_0>0$ and points $y_n\in[c,d]$ such that

$$
|y_n-y_0|<\frac1n,\qquad
      |g(y_n)-x_0|\ge\varepsilon_0.
$$

Set $x_n=g(y_n)$. Since $x_n\in[a,b]$, [Theorem 3.3.1](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#thm:analysis-i:bolzano-weierstrass) gives a subsequence $x_{n_k}\to x^*\in[a,b]$. Continuity of $f$ yields

$$
y_{n_k}=f(x_{n_k})\longrightarrow f(x^*).
$$

But $y_{n_k}\to y_0$, so uniqueness of limits gives $f(x^*)=y_0=f(x_0)$. Injectivity of $f$ then gives $x^*=x_0$. This contradicts $|x_{n_k}-x_0|\ge\varepsilon_0$ for every $k$, since $x_{n_k}\to x_0$. Therefore $g$ is continuous at $y_0$. ◻

:::

The inverse of a continuous strictly decreasing function is continuous as well. Apply the theorem to $-f$, which is strictly increasing, and compose its continuous inverse with $y\mapsto-y$. Strict monotonicity is essential for an inverse to exist. A merely monotone function can take the same value at several inputs.

:::div{id="ex:continuity:rational-powers" class="result example"}

**Example 5.3.7 (Continuity of roots and rational powers).** For $n\in\mathbb{N}$, the root function $x\mapsto x^{1/n}$ is continuous for $x\ge0$. Indeed, for every $A>0$ the power map is a continuous, strictly increasing bijection from $[0,A]$ onto $[0,A^n]$. Its inverse is continuous by [Theorem 5.3.6](/notes/maths-analysis/analysis-i/continuity/#thm:analysis-i:continuous-inverse). These intervals cover all nonnegative inputs, including relative continuity at zero.

For $m\in\mathbb{Z}$ and $n\in\mathbb{N}$, the rational power $x\mapsto x^{m/n}$ is also continuous on $(0,\infty)$. For positive $m$, it is continuous at zero as well. This follows by composing the root function with the integer power function, and taking a reciprocal when $m<0$.

:::

## 5.4 Uniform continuity {id="sec:analysis-i:uniform-continuity"}

For continuity at a single point $c$, the choice of $\delta$ may depend on $c$ as well as $\varepsilon$. Uniform continuity asks for one $\delta$ that works throughout the domain.

:::div{id="web:sections/analysis-i/05-continuity/04-uniform-continuity:281" class="result definition"}

**Definition 5.4.1 (Uniform continuity).** A function $f:I\to\mathbb{R}$ is *uniformly continuous* on $I$ if for every $\varepsilon>0$ there is a $\delta>0$ such that

$$
\text{for all }x,y\in I,\quad
    |x-y|<\delta\ \Longrightarrow\ |f(x)-f(y)|<\varepsilon.
$$

The same $\delta$ must work throughout $I$.

:::

[Figure 5.7](/notes/maths-analysis/analysis-i/continuity/#fig:continuity:uniform-versus-nonuniform) compares the square function on two domains, keeping the output tolerance fixed at $\varepsilon_0=1$.

::::figure{id="fig:continuity:uniform-versus-nonuniform"}

[![ The same parabola at identical coordinate scales. Every shaded window has width 1/4 and height 1. On \[0,2\], one input tolerance works throughout. Farther along \\mathbb\{R\}, input gaps 1/3 and 1/6 still give output gaps above 2.](/notes/maths-analysis/figures/uniform-versus-nonuniform.svg){.tikz-diagram}](/notes/maths-analysis/figures/uniform-versus-nonuniform.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.7. The same parabola at identical coordinate scales. Every shaded window has width $1/4$ and height $1$. On $[0,2]$, one input tolerance works throughout. Farther along $\mathbb{R}$, input gaps $1/3$ and $1/6$ still give output gaps above $2$.

:::

::::

For $f(x)=x^2$ on $[0,2]$,

$$
|x^2-y^2|=|x-y||x+y|\le4|x-y|,
$$

so the single choice $\delta=\varepsilon/4$ works for every pair of inputs. The shaded windows use $\varepsilon_0=1$ and $\delta=1/4$.

On $\mathbb{R}$, take $x_n=n$ and $y_n=n+1/n$. Then

$$
|x_n-y_n|=\frac1n\longrightarrow0,
  \qquad |x_n^2-y_n^2|=2+\frac1{n^2}>2.
$$

Keep $\varepsilon_0=1$ fixed. Whatever $\delta>0$ is chosen, taking $n>1/\delta$ gives inputs closer than $\delta$ whose outputs are more than $1$ apart. This is the failure of uniform continuity. Continuity at each point allows the input tolerance to shrink as the point moves.

:::div{id="thm:analysis-i:heine-cantor" class="result theorem"}

**Theorem 5.4.2 (Heine–Cantor).** Every continuous function on a closed bounded interval $[a,b]$ is uniformly continuous there.

:::

::::::div{class="proof"}

*Proof.* Suppose otherwise. Then there is some $\varepsilon_0>0$ such that for every $n\in\mathbb{N}$ we can choose $x_n,y_n\in[a,b]$ with

$$
|x_n-y_n|<\frac1n,
    \qquad |f(x_n)-f(y_n)|\ge\varepsilon_0.
$$

By [Theorem 3.3.1](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#thm:analysis-i:bolzano-weierstrass), $(x_n)$ has a convergent subsequence $(x_{n_k})$. Apply the theorem again to the bounded sequence $(y_{n_k})$ to obtain a convergent subsequence $(y_{n_{k_i}})$. With these same indices, $(x_{n_{k_i}})$ still converges. Write

$$
x_{n_{k_i}}\longrightarrow x_0,
    \qquad y_{n_{k_i}}\longrightarrow y_0.
$$

:::::div{class="margin-figure"}

::::figure{id="fig:continuity:paired-subsequences"}

[![Schematic pairs selected with common indices. Their separation tends to zero. Once both subsequences converge, their limits must coincide. The selection continues beyond the three pairs drawn.](/notes/maths-analysis/figures/paired-subsequences.svg){.tikz-diagram}](/notes/maths-analysis/figures/paired-subsequences.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.8. Schematic pairs selected with common indices. Their separation tends to zero. Once both subsequences converge, their limits must coincide. The selection continues beyond the three pairs drawn.

:::

::::

:::::

Both limits belong to $[a,b]$, since every selected term lies between $a$ and $b$. Moreover,

$$
|x_{n_{k_i}}-y_{n_{k_i}}|
    <\frac1{n_{k_i}}\longrightarrow0,
$$

so $x_0=y_0$. By continuity and [Theorem 5.1.5](/notes/maths-analysis/analysis-i/continuity/#thm:analysis-i:sequential-continuity),

$$
|f(x_{n_{k_i}})-f(y_{n_{k_i}})|
    \longrightarrow |f(x_0)-f(y_0)|=0.
$$

This contradicts the lower bound $\varepsilon_0$ on every one of these differences. ◻

::::::

[^37]

:::notes{id="footnotes-36"}

[^37]: Heine’s 1872 *Elemente der Functionenlehre* establishes uniform continuity on a closed interval  ([Heine 1872](/notes/maths-analysis/references/#ref-Heine1872)). The key advance is one input tolerance that works across the whole interval. This links local continuity with compactness and supports uniform approximation and integration. The paired name should not be read as a coauthored paper. See [Figure 5.9](/notes/maths-analysis/analysis-i/continuity/#fig:portrait:heine).

:::

:::::div{class="margin-figure"}

::::figure{id="fig:portrait:heine"}

![Eduard Heine](/notes/maths-analysis/figures/heine.jpg)

:::figcaption

Figure 5.9. Eduard Heine. ([MacTutor History of Mathematics n.d.f](/notes/maths-analysis/references/#ref-PortraitHeine); [Bookofproofs contributors, n.d.](/notes/maths-analysis/references/#ref-BookofproofsPortraits))

:::

::::

:::::

The indices in the proof matter. We first select a convergent subsequence of the $x_n$, then refine its indices to make the corresponding $y_n$ converge too. We never separate the pairs. Their shrinking distance then forces the same limit, as [Figure 5.8](/notes/maths-analysis/analysis-i/continuity/#fig:continuity:paired-subsequences) illustrates.

### Exercises on uniform continuity {id="exercises-on-uniform-continuity"}

::statement{key="hw05:uniform-continuity-boundedness"}

::statement{key="hw05:square-not-uniformly-continuous"}

[^38]

:::notes{id="footnotes-37"}

[^38]: Lipschitz’s 1864 study of trigonometric expansions uses a quantitative condition on changes in function values  ([Lipschitz 1864](/notes/maths-analysis/references/#ref-Lipschitz1864)). The linear bound in the following exercise is a particularly useful regularity condition. It supplies an explicit uniform-continuity estimate and later controls uniqueness and stability questions for differential equations. See [Figure 5.10](/notes/maths-analysis/analysis-i/continuity/#fig:portrait:lipschitz).

:::

:::::div{class="margin-figure"}

::::figure{id="fig:portrait:lipschitz"}

![Rudolf Lipschitz](/notes/maths-analysis/figures/lipschitz.jpg)

:::figcaption

Figure 5.10. Rudolf Lipschitz. ([MacTutor History of Mathematics n.d.z](/notes/maths-analysis/references/#ref-PortraitLipschitz); [Bookofproofs contributors, n.d.](/notes/maths-analysis/references/#ref-BookofproofsPortraits))

:::

::::

:::::

::statement{key="hw05:lipschitz-continuity"}

### Piecewise linear approximation {id="piecewise-linear-approximation"}

Partition $[a,b]$ into

$$
a=x_0<x_1<\cdots<x_n=b.
$$

The partition is equally spaced when $x_k-x_{k-1}=(b-a)/n$ for $k=1,\ldots,n$.

:::div{id="web:sections/analysis-i/05-continuity/04-uniform-continuity:5206" class="result definition"}

**Definition 5.4.6 (Piecewise linear function).** A function $g:[a,b]\to\mathbb{R}$ is *piecewise linear* if, on each interval $[x_{k-1},x_k]$, it agrees with an affine function $L_k(x)=\alpha_k+\beta_kx$.

:::

To approximate a continuous function $f$, join its successive values $(x_k,f(x_k))$ by straight segments. On $[x_{k-1},x_k]$ the slope is

$$
m_k=\frac{f(x_k)-f(x_{k-1})}{x_k-x_{k-1}},
$$

and the segment is given by

$$
g(x)=f(x_{k-1})
    +\frac{f(x_k)-f(x_{k-1})}{x_k-x_{k-1}}(x-x_{k-1}).
$$

The pieces agree at the partition points, since $g(x_k)=f(x_k)$. The curved graph and its straight interpolating segments are shown in [Figure 5.11](/notes/maths-analysis/analysis-i/continuity/#fig:continuity:polygonal-approximation).

:::::div{class="margin-figure"}

::::figure{id="fig:continuity:polygonal-approximation"}

[![The black curve is f(x)=1+x^2/4 on \[0,2\]. The two gray segments interpolate equally spaced values. Refining the partition makes the whole polygonal graph close to the curve.](/notes/maths-analysis/figures/polygonal-approximation.svg){.tikz-diagram}](/notes/maths-analysis/figures/polygonal-approximation.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 5.11. The black curve is $f(x)=1+x^2/4$ on $[0,2]$. The two gray segments interpolate equally spaced values. Refining the partition makes the whole polygonal graph close to the curve.

:::

::::

:::::

:::div{id="thm:analysis-i:polygonal-approximation" class="result proposition"}

**Proposition 5.4.7 (Piecewise linear approximation).** If $f:[a,b]\to\mathbb{R}$ is continuous, then for every $\varepsilon>0$ there is a piecewise linear function $g$ such that

$$
\text{for every }x\in[a,b],\quad |f(x)-g(x)|<\varepsilon.
$$

:::

:::div{class="proof"}

*Proof.* By [Theorem 5.4.2](/notes/maths-analysis/analysis-i/continuity/#thm:analysis-i:heine-cantor), choose $\delta>0$ so that points less than $\delta$ apart have function values less than $\varepsilon$ apart. Choose an equally spaced partition with $(b-a)/n<\delta$, and let $g$ be the interpolant above.

If $x\in[x_{k-1},x_k]$, put $t=(x-x_{k-1})/(x_k-x_{k-1})$. Then $0\le t\le1$ and

$$
g(x)=(1-t)f(x_{k-1})+tf(x_k).
$$

Both endpoints are less than $\delta$ from $x$, so

$$
\begin{aligned}
    |f(x)-g(x)|
      &\le (1-t)|f(x)-f(x_{k-1})|
        +t|f(x)-f(x_k)|\\
      &< (1-t)\varepsilon+t\varepsilon=\varepsilon.
  
\end{aligned}
$$

The same partition works for every $x\in[a,b]$, as required. ◻

:::

The construction also motivates integration. A piecewise linear function can be treated one segment at a time, turning its integral into a finite sum. We return to this idea in [Chapter 7](/notes/maths-analysis/analysis-i/riemann-integration/#ch:analysis-i:riemann-integration).
