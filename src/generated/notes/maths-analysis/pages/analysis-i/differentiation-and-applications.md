---
title: "Differentiation and its applications"
group: "Analysis I"
order: 11
part: "Part I · Analysis I"
page: "93"
outline: [{"id": "sec:analysis-i:differentiation", "title": "6.1 Differentiation", "level": 2}, {"id": "difference-quotients-and-local-approximation", "title": "Difference quotients and local approximation", "level": 3}, {"id": "left-and-right-derivatives", "title": "Left and right derivatives", "level": 3}, {"id": "basic-differentiation-rules", "title": "Basic differentiation rules", "level": 3}, {"id": "exponential-logarithmic-and-real-power-derivatives", "title": "Exponential, logarithmic, and real-power derivatives", "level": 3}, {"id": "trigonometric-derivatives", "title": "Trigonometric derivatives", "level": 3}, {"id": "stationary-points-and-local-extrema", "title": "Stationary points and local extrema", "level": 3}, {"id": "sec:analysis-i:mean-value-theorems", "title": "6.2 Mean value theorems", "level": 2}, {"id": "an-average-slope-interpretation", "title": "An average-slope interpretation", "level": 3}, {"id": "derivative-signs-and-monotonicity", "title": "Derivative signs and monotonicity", "level": 3}, {"id": "why-logarithms-preserve-monotonicity", "title": "Why logarithms preserve monotonicity", "level": 3}, {"id": "the-extended-mean-value-theorem", "title": "The extended mean value theorem", "level": 3}, {"id": "sec:analysis-i:taylor-theorem", "title": "6.3 Taylor’s theorem", "level": 2}, {"id": "higher-derivatives", "title": "Higher derivatives", "level": 3}, {"id": "taylor-expansion-and-remainder", "title": "Taylor expansion and remainder", "level": 3}, {"id": "a-polynomial-approximation-with-an-error-bound", "title": "A polynomial approximation with an error bound", "level": 3}, {"id": "the-factorial-series-and-the-exponential-function", "title": "The factorial series and the exponential function", "level": 3}, {"id": "sec:analysis-i:convex-functions", "title": "6.4 Convex functions", "level": 2}, {"id": "curvature-chords-and-tangent-lines", "title": "Curvature, chords, and tangent lines", "level": 3}, {"id": "a-second-derivative-test-for-extrema", "title": "A second-derivative test for extrema", "level": 3}, {"id": "arithmeticgeometric-means-and-youngs-inequality", "title": "Arithmetic–geometric means and Young’s inequality", "level": 3}, {"id": "convexity-and-integral-averages", "title": "Convexity and integral averages", "level": 3}, {"id": "sec:analysis-i:lhopital-rules", "title": "6.5 L’Hôpital’s rules", "level": 2}, {"id": "logarithms-and-limits-of-variable-powers", "title": "Logarithms and limits of variable powers", "level": 3}, {"id": "exercises-on-difference-quotients-and-indeterminate-forms", "title": "Exercises on difference quotients and indeterminate forms", "level": 3}, {"id": "sec:analysis-i:inverse-function-theorem", "title": "6.6 Inverse function theorem", "level": 2}]
---

# Chapter 6. Differentiation and its applications {id="ch:analysis-i:differentiation-and-applications"}

## 6.1 Differentiation {id="sec:analysis-i:differentiation"}

Differentiation studies local change through the limiting slope of a secant line. [^39]

:::notes{id="footnotes-38"}

[^39]: Newton’s 1669 manuscript links infinite series with quadrature. Leibniz’s 1684 paper publishes rules for differentials and tangents ([Newton 1669](/notes/maths-analysis/references/#ref-Newton1669); [Leibniz 1684](/notes/maths-analysis/references/#ref-Leibniz1684)). Their approaches developed in the seventeenth-century study of motion, areas, and tangents. These primary texts document distinct contributions. The modern limit definition came later. Calculus transformed mechanics and differential equations. See [Figure 6.1](/notes/maths-analysis/analysis-i/differentiation-and-applications/#fig:portrait:leibniz).

:::

:::::div{class="margin-figure"}

::::figure{id="fig:portrait:leibniz"}

![Gottfried Wilhelm Leibniz](/notes/maths-analysis/figures/leibniz.jpg)

:::figcaption

Figure 6.1. Gottfried Wilhelm Leibniz. ([MacTutor History of Mathematics n.d.l](/notes/maths-analysis/references/#ref-PortraitLeibniz); [Bookofproofs contributors, n.d.](/notes/maths-analysis/references/#ref-BookofproofsPortraits))

:::

::::

:::::

### Difference quotients and local approximation {id="difference-quotients-and-local-approximation"}

:::div{id="thm:analysis-i:derivative" class="result definition"}

**Definition 6.1.1 (Derivative).** Let $f$ be defined on an open interval containing $x_0$. It is *differentiable at $x_0$* if the finite limit

$$
f'(x_0)=\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}
$$

exists. Equivalently, putting $h=x-x_0$,

$$
f'(x_0)=\lim_{h\to0}\frac{f(x_0+h)-f(x_0)}{h},\qquad h\ne0.
$$

:::

:::div{id="web:sections/analysis-i/06-differentiation-and-applications/01-differentiation:1120" class="result example"}

**Example 6.1.2 (A derivative from first principles).** Fix $P=(1,f(1))$ on the graph $f(x)=x^2/2$, and let $Q_h=(1+h,f(1+h))$ move towards it. The secant through these points has horizontal change $h$ and vertical change $\Delta f=f(1+h)-f(1)$, as shown in [Figure 6.2](/notes/maths-analysis/analysis-i/differentiation-and-applications/#fig:analysis-i:first-principles-derivative). For $h\ne0$,

$$
\frac{f(1+h)-f(1)}h
      =\frac{(1+h)^2-1}{2h}
      =\frac{2h+h^2}{2h}=1+\frac h2.
$$

Consequently,

$$
f'(1)=\lim_{h\to0}\left(1+\frac h2\right)=1.
$$

We cancel while $h$ is nonzero and then take the limit. The figure shows positive $h$ shrinking. The same limiting slope is obtained from negative $h$.

:::

[^40]

:::notes{id="footnotes-39"}

[^40]: In an entry dated 20 May 1665 in his *Waste Book*, Newton replaces $x$ by $x+o$, expands, and cancels a factor of $o$ before saying that $o$ “vanisheth into nothing” ([Newton 1665, fol. 47r](/notes/maths-analysis/references/#ref-NewtonWasteBook1665)). This is notebook evidence of working with vanishing increments while developing calculus. The limit definition used here is a later formulation.

:::

::::figure{id="fig:analysis-i:first-principles-derivative"}

[![Secants for f(x)=x^2/2. On the left, h=1. On the right, h=1,1/2,1/4. The grey secants approach the dashed tangent y=x-1/2 as Q\_h\\to P. Only x\\ge0 is shown.](/notes/maths-analysis/figures/first-principles-derivative.svg){.tikz-diagram}](/notes/maths-analysis/figures/first-principles-derivative.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 6.2. Secants for $f(x)=x^2/2$. On the left, $h=1$. On the right, $h=1,1/2,1/4$. The grey secants approach the dashed tangent $y=x-1/2$ as $Q_h\to P$. Only $x\ge0$ is shown.

:::

::::

For a fixed $x$ at which the derivative exists, write

$$
e(h)=\frac{f(x+h)-f(x)}{h}-f'(x).
$$

Then $e(h)\to0$ as $h\to0$, and rearranging gives

$$
f(x+h)-f(x)=h f'(x)+h e(h).
$$

The residual $r(h)=h e(h)$ satisfies $r(h)/h\to0$. Thus

$$
f(x+h)=f(x)+h f'(x)+o(h).
$$

The notation $o(h)$ expresses a smaller error than the first-order scale $h$. In particular the residual is also $O(h)$, but the stronger vanishing ratio is what characterises differentiability.

:::div{id="thm:analysis-i:differentiable-continuous" class="result proposition"}

**Proposition 6.1.3 (Differentiability implies continuity).** If $f$ is differentiable at $x_0$, then it is continuous at $x_0$.

:::

:::div{class="proof"}

*Proof.* The local approximation gives $f(x_0+h)-f(x_0)=h(f'(x_0)+e(h))$. The factor in parentheses has a finite limit and $h\to0$, so the difference tends to zero. ◻

:::

### Left and right derivatives {id="left-and-right-derivatives"}

:::div{id="thm:analysis-i:one-sided-derivatives" class="result definition"}

**Definition 6.1.4 (Left and right derivatives).** :span[]{id="index:derivative-left:1"}:span[]{id="index:derivative-right:1"} Let $f$ be a real-valued function defined at $c$. If $f$ is also defined on $(c,c+\eta)$ for some $\eta>0$, its *right derivative at $c$* is

$$
f'_+(c)=\lim_{h\to0^+}\frac{f(c+h)-f(c)}{h},
$$

provided this limit exists as a finite real number. If $f$ is defined on $(c-\eta,c)$ for some $\eta>0$, its *left derivative at $c$* is

$$
f'_-(c)=\lim_{h\to0^-}\frac{f(c+h)-f(c)}{h},
$$

provided this limit exists as a finite real number.

:::

In the right-hand limit, $h>0$, so $c+h$ approaches $c$ from the right. In the left-hand limit, $h<0$, so $c+h$ approaches $c$ from the left. The quotient keeps the signed increment $h$ in both cases.

At an interior point of the domain, the ordinary derivative exists exactly when both one-sided derivatives exist as finite numbers and are equal. Their common value is then

$$
f'(c)=f'_-(c)=f'_+(c).
$$

On a closed interval $[a,b]$ with $a<b$, these one-sided limits define the endpoint derivatives $f'_+(a)$ and $f'_-(b)$ when they exist, using only points in the interval.

:::div{id="ex:analysis-i:absolute-value-derivative" class="result example"}

**Example 6.1.5 (A corner and one-sided derivatives).** For $f(x)=|x|$, the difference quotient at zero is $|h|/h$. The definitions in [Definition 6.1.4](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:one-sided-derivatives) give

$$
f'_+(0)=\lim_{h\to0^+}\frac{|h|}{h}=1,\qquad
    f'_-(0)=\lim_{h\to0^-}\frac{|h|}{h}=-1.
$$

These unequal one-sided limits show that $f'(0)$ does not exist, although $f$ is continuous at zero.

:::

The next exercise combines the one-sided quotient definitions with the endpoint behaviour of the exponential. We use its positivity and limits from [Theorem 8.6.5](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:exponential-properties).

::statement{key="hw07:one-sided-derivatives"}

### Basic differentiation rules {id="basic-differentiation-rules"}

Suppose $f$ and $g$ are differentiable at the relevant input, and let $c\in\mathbb{R}$ be constant. The differentiation rules are

$$
\begin{aligned}
    (f\pm g)'&=f'\pm g',& (cf)'&=cf',\\
    (fg)'&=f'g+fg',& (1/g)'&=-g'/g^2\quad(g\ne0).
  \end{aligned}
$$

For a composition, if $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$, the chain rule is

$$
(f\circ g)'(x)=f'(g(x))g'(x).
$$

These rules are stated here without proof.

:::div{id="web:sections/analysis-i/06-differentiation-and-applications/01-differentiation:5857" class="result example"}

**Example 6.1.7 (Integer powers).** For $n=1,2,\ldots$, the derivative of $x^n$ is $nx^{n-1}$. Indeed, the difference-of-powers identity gives, for $h\ne0$,

$$
\frac{(x+h)^n-x^n}{h}
      =\sum_{j=0}^{n-1}(x+h)^{n-1-j}x^j.
$$

There are $n$ terms, each tending to $x^{n-1}$ as $h\to0$.

:::

:::div{id="web:sections/analysis-i/06-differentiation-and-applications/01-differentiation:6167" class="result example"}

**Example 6.1.8 (Roots and rational powers).** For $x>0$, the inverse derivative rule in [§ 6.6](/notes/maths-analysis/analysis-i/differentiation-and-applications/#sec:analysis-i:inverse-function-theorem) gives

$$
\frac{d}{dx}x^{1/n}=\frac1n x^{1/n-1}.
$$

In fact, if $y=t^n$ with $t>0$, then the inverse $t=y^{1/n}$ has derivative $1/(nt^{n-1})=y^{1/n-1}/n$. For $q=m/n\in\mathbb{Q}$, with $m\in\mathbb{Z}$ and $n\in\mathbb{N}$, the power and chain rules therefore give

$$
\frac{d}{dx}x^q
      =m(x^{1/n})^{m-1}\frac1n x^{1/n-1}
      =\frac mn x^{(m-1)/n+1/n-1}
      =q x^{q-1}.
$$

Negative integer powers use the reciprocal rule. The case $m=0$ is the constant function. The restriction $x>0$ avoids the zero endpoint, where a nontrivial root has no finite derivative.

:::

### Exponential, logarithmic, and real-power derivatives {id="exponential-logarithmic-and-real-power-derivatives"}

These calculations use the exponential series from [§ 8.6](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#sec:analysis-i:power-series), the addition law in [Theorem 8.6.5](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:exponential-properties), and its continuous inverse $\ln$ on $(0,\infty)$. The required series-and-inverse construction is developed in [§ 8.6](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#sec:analysis-i:power-series). We use those properties here.

:::div{id="web:sections/analysis-i/06-differentiation-and-applications/01-differentiation:7302" class="result example"}

**Example 6.1.9 (The derivative of the exponential).** Writing $E(x)=e^x$, the addition law gives

$$
\frac{e^{x+h}-e^x}{h}=e^x\frac{e^h-1}{h}
      =e^x\sum_{k=1}^{\infty}\frac{h^{k-1}}{k!}.
$$

For $0<|h|\le1$, absolute convergence yields

$$
\left|\frac{e^h-1}{h}-1\right|
       \le |h|\sum_{k=2}^{\infty}\frac1{k!}\longrightarrow0.
$$

This tail estimate justifies the limit of the series directly, without differentiating an infinite sum term by term. Hence $(e^x)'=e^x$.

:::

Applying the inverse derivative rule to $y=e^x$ gives

$$
(\ln y)'=\frac1{e^x}=\frac1y,\qquad y>0.
$$

For $a>0$, the representation $a^x=e^{x\ln a}$ and the chain rule show that $a^x$ is differentiable. Logarithmic differentiation therefore gives

$$
\ln(a^x)=x\ln a,\qquad
  \frac{(a^x)'}{a^x}=\ln a,\qquad
  (a^x)'=a^x\ln a.
$$

Similarly, for any $r\in\mathbb{R}$ and $x>0$, writing $x^r=e^{r\ln x}$ gives

$$
(x^r)'=e^{r\ln x}\frac r x=r x^{r-1}.
$$

This supplies a direct justification for real powers. Approximation of $r$ by rational numbers alone would not justify passing derivatives to a limit.

When both base and exponent vary, first express the positive function through its logarithm and use the chain rule.

::statement{key="hw07:self-power-derivative"}

### Trigonometric derivatives {id="trigonometric-derivatives"}

For angles in radians, the elementary small-angle limits are $\sin h/h\to1$ and $(\cos h-1)/h\to0$. Using these limits and the angle-addition identities in the difference quotients gives

$$
(\sin x)'=\cos x,\qquad (\cos x)'=-\sin x.
$$

The quotient rule consequently gives

$$
(\tan x)'=\frac1{\cos^2x}\qquad(\cos x\ne0).
$$

These calculations use the geometric trigonometric functions and their small-angle limits. Their power-series representations are given in [Subsection\* 8.6](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#sec:analysis-i:analytic-functions).

### Stationary points and local extrema {id="stationary-points-and-local-extrema"}

:::div{id="thm:analysis-i:stationary-point" class="result definition"}

**Definition 6.1.11 (Stationary point).** A point $c$ is stationary if $f$ is differentiable at $c$ and $f'(c)=0$.

:::

Here we use *stationary* for this precise condition. Some conventions also count points where the derivative is undefined as critical points. Differentiability alone does not imply $f'(c)=0$.

:::div{id="thm:analysis-i:interior-extremum" class="result proposition"}

**Proposition 6.1.12 (Interior extrema).** If $f$ has a local maximum or local minimum at an interior point $c$ of its domain and is differentiable there, then $f'(c)=0$.

:::

:::div{class="proof"}

*Proof.* At a local minimum, $f(c+h)-f(c)\ge0$ for all sufficiently small $h$. The quotient is nonnegative for $h>0$ and nonpositive for $h<0$. Since both one-sided limits equal $f'(c)$, that number must be zero. At a local maximum the signs reverse and the same conclusion follows. ◻

:::

The extrema in [Figure 6.3](/notes/maths-analysis/analysis-i/differentiation-and-applications/#fig:analysis-i:local-extrema) illustrate the interior-point condition.

::::figure{id="fig:analysis-i:local-extrema"}

[![Schematic differentiable local minimum and maximum. Each horizontal tangent has slope zero at the marked interior point c.](/notes/maths-analysis/figures/local-extrema.svg){.tikz-diagram}](/notes/maths-analysis/figures/local-extrema.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 6.3. Schematic differentiable local minimum and maximum. Each horizontal tangent has slope zero at the marked interior point $c$.

:::

::::

## 6.2 Mean value theorems {id="sec:analysis-i:mean-value-theorems"}

:::div{id="thm:analysis-i:rolle" class="result theorem"}

**Theorem 6.2.1 (Rolle’s theorem).** Let $f$ be continuous on $[a,b]$ and differentiable on $(a,b)$, where $a<b$. If $f(a)=f(b)$, then there exists $c\in(a,b)$ such that $f'(c)=0$.

:::

:::div{class="proof"}

*Proof.* If $f$ is constant, every interior point has derivative zero. Otherwise, by [Theorem 5.2.1](/notes/maths-analysis/analysis-i/continuity/#thm:analysis-i:extreme-value), $f$ attains a maximum and a minimum. Since the endpoint values agree and $f$ is nonconstant, at least one of these extrema is attained at an interior point $c$. Then [Proposition 6.1.12](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:interior-extremum) gives $f'(c)=0$. ◻

:::

[^41]

:::notes{id="footnotes-40"}

[^41]: Rolle’s 1691 *Démonstration* concerns solving polynomial equations ([Rolle 1691](/notes/maths-analysis/references/#ref-Rolle1691)). The formulation here is a modern statement for differentiable functions, not a verbatim seventeenth-century theorem. Equal endpoint heights force a stationary point, making this a useful bridge from extrema to mean-value arguments.

:::

The following polynomial question can be approached by constructing a polynomial whose derivative is $P$ and comparing its endpoint values. No integration theorem is required.

::statement{key="hw07:polynomial-rolle"}

:::div{id="thm:analysis-i:mean-value" class="result theorem"}

**Theorem 6.2.3 (Mean value theorem).** Let $a<b$. Suppose $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$. There exists $c\in(a,b)$ such that

$$
f'(c)=\frac{f(b)-f(a)}{b-a}.
$$

:::

[^42]

:::notes{id="footnotes-41"}

[^42]: Cauchy’s 1823 *Résumé des leçons* develops differential calculus through derivatives and finite increments ([Cauchy 1823](/notes/maths-analysis/references/#ref-Cauchy1823)). The mean-value method relates a finite change to a local slope, turning derivative information into bounds and monotonicity. This citation documents a historical treatment, without claiming sole discovery of the modern formulation.

:::

:::div{class="proof"}

*Proof.* Subtract the secant line by defining

$$
H(t)=f(t)-f(a)-\frac{f(b)-f(a)}{b-a}(t-a).
$$

This function is continuous on $[a,b]$, differentiable on $(a,b)$, and satisfies $H(a)=H(b)=0$. By [Theorem 6.2.1](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:rolle), some $c\in(a,b)$ satisfies $H'(c)=0$. Therefore

$$
0=f'(c)-\frac{f(b)-f(a)}{b-a},
$$

which is the required equality. ◻

:::

The geometry of both results is shown in [Figure 6.4](/notes/maths-analysis/analysis-i/differentiation-and-applications/#fig:analysis-i:mean-value-geometry).

::::figure{id="fig:analysis-i:mean-value-geometry"}

[![On the left, equal endpoint heights give a horizontal tangent. On the right, the tangent at c is parallel to the secant through the endpoints. These are schematic examples of the two theorems.](/notes/maths-analysis/figures/mean-value-geometry.svg){.tikz-diagram}](/notes/maths-analysis/figures/mean-value-geometry.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 6.4. On the left, equal endpoint heights give a horizontal tangent. On the right, the tangent at $c$ is parallel to the secant through the endpoints. These are schematic examples of the two theorems.

:::

::::

### An average-slope interpretation {id="an-average-slope-interpretation"}

If $f'$ is continuous on $[a,b]$, the fundamental theorem of calculus, assumed here and reserved for [§ 7.5](/notes/maths-analysis/analysis-i/riemann-integration/#sec:analysis-i:fundamental-theorem-of-calculus), gives

$$
\frac1{b-a}\int_a^b f'(x)\,dx=\frac{f(b)-f(a)}{b-a}.
$$

Thus the mean value theorem says that this average slope is attained at an interior point. The continuity of $f'$ is an additional hypothesis for this integral interpretation. The mean value theorem itself only requires differentiability on the open interval. A schematic illustration of average height appears in [Figure 6.5](/notes/maths-analysis/analysis-i/differentiation-and-applications/#fig:analysis-i:average-height).

:::::div{class="margin-figure"}

::::figure{id="fig:analysis-i:average-height"}

[![A schematic continuous function \\phi and its average height \\overline\\phi=(b-a)^\{-1\}\\int\_a^b\\phi(x)\\,dx (dashed).](/notes/maths-analysis/figures/average-height.svg){.tikz-diagram}](/notes/maths-analysis/figures/average-height.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 6.5. A schematic continuous function $\phi$ and its average height $\overline\phi=(b-a)^{-1}\int_a^b\phi(x)\,dx$ (dashed).

:::

::::

:::::

### Derivative signs and monotonicity {id="derivative-signs-and-monotonicity"}

:::div{id="thm:analysis-i:derivative-monotonicity" class="result corollary"}

**Corollary 6.2.4.** Let $f$ be differentiable on an open interval $I$. If $f'(x)\ge0$ for every $x\in I$, then $f$ is nondecreasing on $I$. If $f'(x)>0$ everywhere, it is strictly increasing. The analogous statements with reversed inequalities also hold.

:::

:::div{class="proof"}

*Proof.* For $x_1<x_2$ in $I$, differentiability implies continuity on $[x_1,x_2]$. [Theorem 6.2.3](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:mean-value) gives a $c\in(x_1,x_2)$ with $f(x_2)-f(x_1)=f'(c)(x_2-x_1)$. This difference is nonnegative when $f'\ge0$, and positive when $f'>0$. Apply the same argument to $-f$ for the reversed inequalities. ◻

:::

The next exercise links the mean value theorem to Lipschitz continuity from [§ 5.4](/notes/maths-analysis/analysis-i/continuity/#sec:analysis-i:uniform-continuity). Its iteration also uses geometric-series tail bounds and the completeness of $\mathbb{R}$ from [Figure 3.5](/notes/maths-analysis/analysis-i/sequences-of-real-numbers/#sec:analysis-i:cauchy-sequences).

::statement{key="hw07:contractive-fixed-point"}

Derivative signs can also identify a sharp global bound on a half-line. The next question asks for both the bound and the equality case.

::statement{key="hw07:rational-maximum"}

### Why logarithms preserve monotonicity {id="why-logarithms-preserve-monotonicity"}

For a positive function, taking a logarithm changes the heights of its graph while preserving the order of those heights. This is why its logarithm can serve as a proxy for studying increase and decrease. The essential property is that $\ln$ is strictly increasing on $(0,\infty)$. The exponential and logarithm used here are constructed in [Theorem 8.6.5](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:exponential-properties) and [Definition 8.6.6](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:logarithm-real-powers).

::::figure{id="fig:analysis-i:logarithm-monotonicity"}

[![Solid curves are f and dashed curves are \\ln f, on identical coordinate scales. Dotted guides mark y=1. The logarithm preserves increase, decrease, and the inputs at peaks and valleys. Values and curvature can change. Only a window of each graph is shown.](/notes/maths-analysis/figures/logarithm-monotonicity.svg){.tikz-diagram}](/notes/maths-analysis/figures/logarithm-monotonicity.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 6.6. Solid curves are $f$ and dashed curves are $\ln f$, on identical coordinate scales. Dotted guides mark $y=1$. The logarithm preserves increase, decrease, and the inputs at peaks and valleys. Values and curvature can change. Only a window of each graph is shown.

:::

::::

:::div{id="thm:analysis-i:logarithmic-monotonicity" class="result proposition"}

**Proposition 6.2.7 (Logarithms preserve order and monotonicity).** Let $f:I\to(0,\infty)$, where $I$ is an interval, and put $H(x)=\ln(f(x))$. For any $s,t\in I$,

$$
f(s)<f(t)\quad\Longleftrightarrow\quad H(s)<H(t).
$$

The same equivalence holds with $\le$ or $=$. Consequently, $f$ and $H$ are increasing or decreasing on exactly the same intervals, with the same strict or non-strict sense. They also attain local and global maxima and minima at the same inputs.

:::

:::div{class="proof"}

*Proof.* First take $0<a<b$. The logarithm is continuous on $[a,b]$ and differentiable on $(a,b)$. The mean value theorem gives some $\xi\in(a,b)$ with

$$
\ln b-\ln a=\frac{b-a}{\xi}>0.
$$

Thus $\ln$ preserves strict inequalities between positive values. Conversely, if $H(s)<H(t)$, strict increase of the exponential gives $f(s)=e^{H(s)}<e^{H(t)}=f(t)$. Its inverse identities also preserve equality, so the non-strict comparison follows.

Applying these comparisons to every pair $s<t$ proves the monotonicity statements. Applying them to the comparison of one value with all nearby values, or all values in $I$, proves the statements about extrema. ◻

:::

When $f$ is differentiable, the chain rule gives a second way to see the connection,

$$
H'(x)=\frac{f'(x)}{f(x)}.
$$

Since $f(x)>0$, the derivatives $H'(x)$ and $f'(x)$ have the same sign and vanish at the same inputs. A simpler formula for $H'$ can therefore settle the sign of $f'$ without differentiating a complicated power directly. For example, if $f(x)=g(x)^{h(x)}$ with $g(x)>0$, then

$$
H(x)=h(x)\ln g(x).
$$

The exponent has become a factor.

[Figure 6.6](/notes/maths-analysis/analysis-i/differentiation-and-applications/#fig:analysis-i:logarithm-monotonicity) compares four positive functions with their logarithms using matching axes and identical scales. Each point $(x,f(x))$ becomes $(x,\ln(f(x)))$. The input stays fixed while the vertical coordinate changes. The slope $1/y$ of the logarithm compresses differences between large positive outputs and magnifies differences between outputs close to zero. The increasing and decreasing examples retain their direction. The other two retain their peak and valley at $x=0$. The heights change, and curvature need not be preserved. In particular, $f(x)=1$ becomes $H(x)=0$, while $0<f(x)<1$ gives $H(x)<0$. A negative logarithm is allowed. It is the argument of the logarithm that must be positive throughout the interval.

:::::div{id="ex:analysis-i:increasing-euler-approximants" class="result example"}

**Example 6.2.8 (Increasing exponential approximants).** Consider $F(x)=(1+1/x)^x$ for $x\ge1$. We will show that $F$ is strictly increasing. Since $F>0$, [Proposition 6.2.7](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:logarithmic-monotonicity) lets us study its logarithm with exactly the same monotonicity. Taking the logarithm also turns the varying exponent into a product. Put

$$
H(x)=\ln F(x)=x\ln(1+1/x).
$$

The left panel of [Figure 6.7](/notes/maths-analysis/analysis-i/differentiation-and-applications/#fig:analysis-i:increasing-euler-approximants) shows the positive gap that will control the derivative. The right panel illustrates the resulting increase of $F$.

::::figure{id="fig:analysis-i:increasing-euler-approximants"}

[![ The shaded gap on the left is \\psi(u)=\\ln(1+u)-u/(1+u), with u\_0=4/5 marked. Its positivity gives H'(x)=\\psi(1/x)\>0. The right panel shows the actual graph of F, with selected integer inputs marked. The dashed level is e, whose role as the limit is proved in Example 6.5.3.](/notes/maths-analysis/figures/increasing-euler-approximants.svg){.tikz-diagram}](/notes/maths-analysis/figures/increasing-euler-approximants.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 6.7. The shaded gap on the left is $\psi(u)=\ln(1+u)-u/(1+u)$, with $u_0=4/5$ marked. Its positivity gives $H'(x)=\psi(1/x)>0$. The right panel shows the actual graph of $F$, with selected integer inputs marked. The dashed level is $e$, whose role as the limit is proved in [Example 6.5.3](/notes/maths-analysis/analysis-i/differentiation-and-applications/#ex:analysis-i:euler-approximant-limit).

:::

::::

:::div{class="proof"}

*Proof.* The product and chain rules give the first line below. The second uses $x/[x^2(1+1/x)]=1/(x+1)$.

$$
\begin{aligned}
      H'(x)&=\ln(1+1/x)
        +x\frac{1}{1+1/x}\left(-\frac1{x^2}\right)\\
        &=\ln(1+1/x)-\frac1{x+1}.
    \end{aligned}
$$

The sign depends on which of the two positive terms is larger. Write $u=1/x$, so $1/(x+1)=u/(1+u)$, and define

$$
\psi(u)=\ln(1+u)-\frac{u}{1+u},\qquad u\ge0.
$$

Thus $H'(x)=\psi(1/x)$. Geometrically, $\psi(u)$ is the vertical gap between the two curves in the left panel.

The gap is zero at $u=0$. For $u>0$, its derivative is

$$
\psi'(u)=\frac1{1+u}-\frac1{(1+u)^2}
      =\frac{u}{(1+u)^2}>0.
$$

To turn this derivative information into a strict inequality, fix $u>0$. The function $\psi$ is continuous on $[0,u]$ and differentiable on $(0,u)$. By [Theorem 6.2.3](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:mean-value), some $\xi\in(0,u)$ satisfies

$$
\psi(u)-\psi(0)=u\psi'(\xi)
      =\frac{u\xi}{(1+\xi)^2}>0.
$$

Thus $\psi(u)>0$ for $u>0$. Taking $u=1/x$ shows that $H'(x)=\psi(1/x)>0$ for $x>1$.

Finally, take $1\le s<t$. The function $H$ is continuous on $[s,t]$ and differentiable on $(s,t)$. The mean value theorem gives $H(t)-H(s)=H'(c)(t-s)>0$ for some $c\in(s,t)$. Since the exponential is strictly increasing, the following comparison proves that $F$ is strictly increasing on $[1,\infty)$.

$$
F(s)=e^{H(s)}<e^{H(t)}=F(t).
$$

 ◻

:::

:::::

The next question changes the exponent by one. The corresponding limit can be studied after [Example 6.5.3](/notes/maths-analysis/analysis-i/differentiation-and-applications/#ex:analysis-i:euler-approximant-limit), where the logarithmic quotient is evaluated. Its monotonicity can already be studied here.

::statement{key="hw07:decreasing-euler-approximants"}

### The extended mean value theorem {id="the-extended-mean-value-theorem"}

:::div{id="thm:analysis-i:cauchy-mean-value" class="result theorem"}

**Theorem 6.2.10 (Cauchy’s mean value theorem).** Let $a<b$, and suppose $f$ and $g$ are continuous on $[a,b]$ and differentiable on $(a,b)$. There exists $c\in(a,b)$ such that

$$
f'(c)\bigl(g(b)-g(a)\bigr)
      =g'(c)\bigl(f(b)-f(a)\bigr).
$$

:::

Applying the ordinary mean value theorem separately to $f$ and $g$ gives two possibly different points. It does not show that they coincide. The extended theorem asserts a single common point. Its proof uses one auxiliary function.

:::div{class="proof"}

*Proof.* Define

$$
H(t)=\bigl(g(b)-g(a)\bigr)\bigl(f(t)-f(a)\bigr)
      -\bigl(f(b)-f(a)\bigr)\bigl(g(t)-g(a)\bigr).
$$

By the hypotheses on $f$ and $g$, the function $H$ is continuous on $[a,b]$ and differentiable on $(a,b)$. Also, $H(a)=H(b)=0$. Therefore [Theorem 6.2.1](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:rolle) supplies a point $c\in(a,b)$ with $H'(c)=0$. Differentiating gives

$$
\bigl(g(b)-g(a)\bigr)f'(c)
      -\bigl(f(b)-f(a)\bigr)g'(c)=0,
$$

which is the required identity. No division by an endpoint difference is needed, so the argument also covers zero endpoint differences. ◻

:::

## 6.3 Taylor’s theorem {id="sec:analysis-i:taylor-theorem"}

[^44]

:::notes{id="footnotes-43"}

[^44]: Taylor’s *Methodus incrementorum* (1715) develops the expansion bearing his name ([Taylor 1715](/notes/maths-analysis/references/#ref-Taylor1715)). Lagrange’s later analysis makes the finite remainder central ([Lagrange 1797](/notes/maths-analysis/references/#ref-Lagrange1797)). The distinction matters: an approximating polynomial with a controlled error is useful even before any infinite expansion is justified. This is fundamental in approximation and numerical error estimates. See [Figure 6.8](/notes/maths-analysis/analysis-i/differentiation-and-applications/#fig:portrait:taylor-lagrange).

:::

:::::div{class="margin-figure"}

::::figure{id="fig:portrait:taylor-lagrange"}

![Brook Taylor](/notes/maths-analysis/figures/taylor.jpg) ![Joseph-Louis Lagrange](/notes/maths-analysis/figures/lagrange.jpg)

:::figcaption

Figure 6.8. Brook Taylor (left) and Joseph-Louis Lagrange (right). Portrait sources ([MacTutor History of Mathematics n.d.e](/notes/maths-analysis/references/#ref-PortraitTaylor), [n.d.t](/notes/maths-analysis/references/#ref-PortraitLagrange); [Bookofproofs contributors, n.d.](/notes/maths-analysis/references/#ref-BookofproofsPortraits)).

:::

::::

:::::

### Higher derivatives {id="higher-derivatives"}

Successive differentiation gives $f'$, $f''$, and more generally $f^{(n)}$. Write $f^{(0)}=f$. A function belongs to $C^n[a,b]$ when its derivatives through order $n$ exist in the interior and extend continuously to the endpoints. In particular, $C^0[a,b]=C[a,b]$.

### Taylor expansion and remainder {id="taylor-expansion-and-remainder"}

The following statement gives a polynomial approximation together with a finite error term.

:::div{id="thm:analysis-i:taylor-lagrange" class="result theorem"}

**Theorem 6.3.1 (Taylor’s theorem with Lagrange remainder).** Suppose $f$ has $n+1$ continuous derivatives on an interval containing the segment between $a$ and $x$, where $n\geq0$ and $x\ne a$. There is a point $\xi$ strictly between $a$ and $x$ such that

$$
f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k
      +\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}.
$$

:::

:::div{class="proof"}

*Proof.* Let

$$
P_n(t)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(t-a)^k,
    \qquad R=f(x)-P_n(x).
$$

Subtract a correction chosen to make the error vanish at $x$, by setting

$$
H(t)=f(t)-P_n(t)-R\frac{(t-a)^{n+1}}{(x-a)^{n+1}}.
$$

The denominator is nonzero because $x\ne a$. Differentiating the polynomials gives $P_n^{(j)}(a)=f^{(j)}(a)$ for $0\le j\le n$. The correction and its first $n$ derivatives vanish at $a$, so

$$
H(x)=0,\qquad H^{(j)}(a)=0\quad(0\le j\le n).
$$

Apply [Theorem 6.2.1](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:rolle) between $a$ and $x$ to obtain a point $c_1$ with $H'(c_1)=0$. If $n\ge1$, apply it to $H'$ between $a$ and $c_1$, using $H'(a)=0$, to obtain $c_2$ with $H''(c_2)=0$. Continuing in this way gives, after $n+1$ applications, a point $\xi$ strictly between $a$ and $x$ with $H^{(n+1)}(\xi)=0$. The assumed continuity of the derivatives and their differentiability in the interior justify each application. This reasoning works on either side of $a$ and includes $n=0$, when only one application is needed.

Since $P_n^{(n+1)}=0$, the final equality becomes

$$
0=f^{(n+1)}(\xi)-R\frac{(n+1)!}{(x-a)^{n+1}}.
$$

Solving for $R=f(x)-P_n(x)$ gives

$$
f(x)=P_n(x)+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1},
$$

as required. ◻

:::

:::div{class="proof"}

*A second proof using a moving centre.* Fix $x\ne a$ and define the Taylor error with variable centre $t$ by

$$
H(t)=f(x)-\sum_{k=0}^n\frac{f^{(k)}(t)}{k!}(x-t)^k.
$$

Differentiating each term produces two sums. Every term cancels except the one containing $f^{(n+1)}$, so

$$
H'(t)=-\frac{f^{(n+1)}(t)}{n!}(x-t)^n.
$$

Also $H(x)=0$. To make equal endpoint values, put

$$
G(t)=H(t)-H(a)\frac{(x-t)^{n+1}}{(x-a)^{n+1}}.
$$

The hypotheses of [Theorem 6.2.1](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:rolle) hold between $a$ and $x$, and $G(a)=G(x)=0$. Thus $G'(\xi)=0$ for some $\xi$ strictly between these endpoints. Substituting $H'$ gives

$$
0=-\frac{f^{(n+1)}(\xi)}{n!}(x-\xi)^n
      +H(a)\frac{(n+1)(x-\xi)^n}{(x-a)^{n+1}}.
$$

Since $\xi\ne x$, cancellation and rearrangement yield

$$
H(a)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}.
$$

The definition of $H(a)$ is exactly the required Taylor error. ◻

:::

### A polynomial approximation with an error bound {id="a-polynomial-approximation-with-an-error-bound"}

If $|f^{(n+1)}(t)|\le M$ on the segment from $a$ to $x$, then [Theorem 6.3.1](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:taylor-lagrange) gives

$$
|f(x)-P_n(x)|\le\frac{M|x-a|^{n+1}}{(n+1)!}.
$$

For $f(x)=e^x$ and $a=0$, the quadratic approximation is $P_2(x)=1+x+x^2/2$. On $[0,1]$, its error is at most $ex^3/6$. The vertical distance in [Figure 6.9](/notes/maths-analysis/analysis-i/differentiation-and-applications/#fig:analysis-i:taylor-error) is the error controlled by this bound.

::::figure{id="fig:analysis-i:taylor-error"}

[![ The exponential and its quadratic Taylor polynomial about zero. The grey vertical segment at x=1 is the remainder e-5/2. Curves are shown only on \[0,1\].](/notes/maths-analysis/figures/taylor-error.svg){.tikz-diagram}](/notes/maths-analysis/figures/taylor-error.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 6.9. The exponential and its quadratic Taylor polynomial about zero. The grey vertical segment at $x=1$ is the remainder $e-5/2$. Curves are shown only on $[0,1]$.

:::

::::

### The factorial series and the exponential function {id="the-factorial-series-and-the-exponential-function"}

[Exercise 1.9.10](/notes/maths-analysis/analysis-i/sets-and-foundations/#ex:hw02:factorial-sequence) identified the supremum of the factorial partial sums using their series definition of $e$. Once the exponential function is available, [Theorem 6.3.1](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:taylor-lagrange) gives another identification of the same limit.

The exponential function has value $1$ at zero, and each derivative equals the same continuous function. Apply [Theorem 6.3.1](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:taylor-lagrange) about $0$ and evaluate at $1$ to obtain

$$
\exp(1)=\sum_{k=0}^{n}\frac1{k!}
    +\frac{\exp(\xi_n)}{(n+1)!},\qquad 0<\xi_n<1.
$$

Since $\exp$ is increasing, the remainder satisfies

$$
0<\exp(1)-\sum_{k=0}^{n}\frac1{k!}
    \leq\frac{\exp(1)}{(n+1)!}\longrightarrow0.
$$

The factorials tend to infinity, for example because $(n+1)!\geq2^n$. Thus $\exp(1)=\sum_{k=0}^{\infty}1/k!=e$. This later calculus argument is independent of the elementary construction of the series limit in [§ 1.9](/notes/maths-analysis/analysis-i/sets-and-foundations/#sec:analysis-i:denseness).

## 6.4 Convex functions {id="sec:analysis-i:convex-functions"}

### Curvature, chords, and tangent lines {id="curvature-chords-and-tangent-lines"}

:::div{id="thm:analysis-i:convex-function" class="result definition"}

**Definition 6.4.1 (Convex and concave functions).** A function $f:I\to\mathbb{R}$ on an interval is *convex* if

$$
f(tx+(1-t)y)\le t f(x)+(1-t)f(y)
    \quad(x,y\in I,\ 0\le t\le1).
$$

It is *concave* when the inequality is reversed.

:::

The point $z=tx+(1-t)y$ lies between $x$ and $y$. Convexity says that the graph at $z$ lies below the chord joining the endpoint values. A tangent line, when it exists, lies below the graph instead. [Figure 6.10](/notes/maths-analysis/analysis-i/differentiation-and-applications/#fig:analysis-i:convex-chord-tangent) shows both comparisons.

::::figure{id="fig:analysis-i:convex-chord-tangent"}

[![ For f(x)=x^2, the chord from x=0 to x=2 lies above the graph, while the tangent at x=1 lies below it. The vertical guides compare all three heights at z=1/2.](/notes/maths-analysis/figures/convex-chord-tangent.svg){.tikz-diagram}](/notes/maths-analysis/figures/convex-chord-tangent.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 6.10. For $f(x)=x^2$, the chord from $x=0$ to $x=2$ lies above the graph, while the tangent at $x=1$ lies below it. The vertical guides compare all three heights at $z=1/2$.

:::

::::

:::div{id="thm:analysis-i:convex-second-derivative" class="result proposition"}

**Proposition 6.4.2 (The second-derivative criterion).** Let $f\in C^2(I)$ on an open interval. The following are equivalent.

1.  $f$ is convex.

2.  $f(x)\ge f(a)+f'(a)(x-a)$ for all $a,x\in I$.

3.  $f''(x)\ge0$ for every $x\in I$.

Reversing the inequalities gives the concave case.

:::

:::div{class="proof"}

*Proof.* Suppose first that $f''\ge0$. By [Corollary 6.2.4](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:derivative-monotonicity), $f'$ is nondecreasing. If $x>a$, the mean value theorem gives $f(x)-f(a)=f'(c)(x-a)\ge f'(a)(x-a)$ for some $c\in(a,x)$. If $x<a$, then $f'(c)\le f'(a)$, and multiplying by $x-a<0$ gives the same supporting-line inequality. Equality holds at $x=a$.

Suppose the supporting-line inequality holds and set $z=tx+(1-t)y$. Apply it at $a=z$ to both $x$ and $y$, multiply by $t$ and $1-t$, and add. The derivative terms cancel because $t(x-z)+(1-t)(y-z)=0$. This proves convexity.

Finally, suppose $f$ is convex. For $0<s<1$, its defining inequality gives

$$
\frac{f(a+s(x-a))-f(a)}s\le f(x)-f(a).
$$

Letting $s\to0^+$ yields the supporting-line inequality. Taylor’s theorem at $a$ then gives, for small nonzero $h$,

$$
0\le f(a+h)-f(a)-hf'(a)=\frac12 f''(\xi_h)h^2.
$$

Here $\xi_h$ lies between $a$ and $a+h$. Divide by $h^2/2$ and use continuity of $f''$ to obtain $f''(a)\ge0$. ◻

:::

### A second-derivative test for extrema {id="a-second-derivative-test-for-extrema"}

:::div{id="thm:analysis-i:second-derivative-extremum" class="result proposition"}

**Proposition 6.4.3 (The second-derivative test).** Suppose $f$ is twice continuously differentiable near $a$ and $f'(a)=0$. If $f''(a)>0$, then $a$ is a strict local minimum. If $f''(a)<0$, it is a strict local maximum.

:::

:::div{class="proof"}

*Proof.* When $f''(a)>0$, continuity makes $f''$ positive on a neighbourhood of $a$. By [Theorem 6.3.1](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:taylor-lagrange), every sufficiently close $x\ne a$ satisfies

$$
f(x)-f(a)=\frac12 f''(\xi)(x-a)^2>0.
$$

This proves the minimum assertion. Apply it to $-f$ for the maximum. ◻

:::

The condition $f''(a)=0$ does not decide the issue. At zero, $x^4$ has a minimum, $-x^4$ has a maximum, and $x^3$ has neither.

### Arithmetic–geometric means and Young’s inequality {id="arithmeticgeometric-means-and-youngs-inequality"}

For nonnegative $u,v$, the two-variable arithmetic–geometric mean inequality gives $\sqrt{uv}\le(u+v)/2$. Substituting $u=x^2$ and $v=y^2$ gives $xy\le(x^2+y^2)/2$ for $x,y\ge0$. Convexity of the exponential extends this to conjugate exponents.

:::div{id="thm:analysis-i:young-inequality" class="result proposition"}

**Proposition 6.4.4 (Young’s inequality).** Let $p,q>1$ satisfy $1/p+1/q=1$. For $x,y\ge0$,

$$
xy\le\frac{x^p}{p}+\frac{y^q}{q}.
$$

:::

:::div{class="proof"}

*Proof.* For $x,y>0$, the function $E(s)=e^s$ has $E''(s)>0$, so [Proposition 6.4.2](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:convex-second-derivative) makes it convex. Its defining inequality with weights $1/p$ and $1/q$ gives

$$
xy=\exp\!\left(\frac{\ln(x^p)}p+\frac{\ln(y^q)}q\right)
      \le\frac{\exp(\ln(x^p))}{p}
        +\frac{\exp(\ln(y^q))}{q}
      =\frac{x^p}{p}+\frac{y^q}{q}.
$$

If either variable is zero, the left side is zero and the right side is nonnegative. ◻

:::

### Convexity and integral averages {id="convexity-and-integral-averages"}

The next application uses the order and linearity properties of the Riemann integral, developed in [§ 7.1](/notes/maths-analysis/analysis-i/riemann-integration/#sec:analysis-i:integration). We assume these properties for this application. Its geometric content is that a convex function of an average is at most the average of the convex function.

:::div{id="thm:analysis-i:jensen-integral" class="result theorem"}

**Theorem 6.4.5 (Jensen’s inequality for integral averages).** Let $a<b$, let $f$ be continuous on $[a,b]$, and let $\phi\in C^2(I)$ on an open interval containing the range of $f$. Suppose $\phi''\ge0$ on $I$. Put

$$
\overline f=\frac1{b-a}\int_a^b f(x)\,dx.
$$

Then

$$
\phi(\overline f)\le\frac1{b-a}\int_a^b\phi(f(x))\,dx.
$$

:::

[^45]

:::notes{id="footnotes-44"}

[^45]: Johan Ludwig William Valdemar Jensen’s 1906 paper begins with Cauchy’s arithmetic–geometric mean argument and uses convexity to organise inequalities between means ([Jensen 1906, 175–76](/notes/maths-analysis/references/#ref-Jensen1906)). The historical definition starts with midpoint comparisons. The all-weight definition used here makes the averaging principle explicit, and does not require differentiability.

:::

:::div{class="proof"}

*Proof.* The extreme value theorem bounds $f$ between its minimum and maximum. Integrating these bounds shows that $\overline f$ lies in the same interval, hence in $I$. By [Proposition 6.4.2](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:convex-second-derivative),

$$
\phi(f(x))\ge\phi(\overline f)
      +\phi'(\overline f)(f(x)-\overline f).
$$

The functions are continuous, so these integrals exist. Integrate the inequality and divide by $b-a$. The last term vanishes because $\int_a^b(f(x)-\overline f)\,dx=0$, giving the result. ◻

:::

## 6.5 L’Hôpital’s rules {id="sec:analysis-i:lhopital-rules"}

L’Hôpital’s rules resolve certain indeterminate quotients by comparing derivatives. [^46]

:::notes{id="footnotes-45"}

[^46]: On 17 March 1694 the marquis de L’Hôpital offered Johann Bernoulli a retainer of 300 French livres and requested exclusive communication of discoveries ([L’Hôpital 1694](/notes/maths-analysis/references/#ref-LHopital1694Letter)). The correspondence, reviewed by Truesdell, supports Bernoulli’s mathematical contribution ([Truesdell 1958](/notes/maths-analysis/references/#ref-Truesdell1958)). Financial need is part of that historical interpretation, rather than a clause proving his motive. See [Figure 6.11](/notes/maths-analysis/analysis-i/differentiation-and-applications/#fig:portrait:lhopital-bernoulli).

:::

:::::div{class="margin-figure"}

::::figure{id="fig:portrait:lhopital-bernoulli"}

![Guillaume de L’Hôpital](/notes/maths-analysis/figures/de-lhopital.jpg) ![Johann Bernoulli](/notes/maths-analysis/figures/bernoulli-johann.jpg)

:::figcaption

Figure 6.11. Guillaume de L’Hôpital (left) and Johann Bernoulli (right). Portrait sources ([MacTutor History of Mathematics n.d.m](/notes/maths-analysis/references/#ref-PortraitDeLHopital), [n.d.q](/notes/maths-analysis/references/#ref-PortraitBernoulliJohann); [Bookofproofs contributors, n.d.](/notes/maths-analysis/references/#ref-BookofproofsPortraits)).

:::

::::

:::::

[^47]

:::notes{id="footnotes-46"}

[^47]: The rule supplied by Johann Bernoulli appeared in L’Hôpital’s 1696 textbook ([Truesdell 1958](/notes/maths-analysis/references/#ref-Truesdell1958)), section IX, article 163. Its preface acknowledges a special debt to Bernoulli ([L’Hôpital 1696](/notes/maths-analysis/references/#ref-LHopital1696)). Patronage and textbook publication help explain the familiar name. The episode distinguishes discovering mathematics from teaching and disseminating it. The rule became a standard tool for evaluating limits.

:::

We distinguish the forms $0/0$ and $\infty/\infty$. The first has the following mean-value proof.

:::div{id="thm:analysis-i:lhopital-zero" class="result theorem"}

**Theorem 6.5.1 (L’Hôpital’s rule for $0/0$).** Let $f$ and $g$ be differentiable on $(a,b)$, with $g'(x)\ne0$ throughout that interval. Suppose $f(x)\to0$ and $g(x)\to0$ as $x\to a^+$. If

$$
\lim_{x\to a^+}\frac{f'(x)}{g'(x)}=L\in\mathbb{R}\cup\{-\infty,+\infty\},
$$

then $g(x)\ne0$ on $(a,b)$ and

$$
\lim_{x\to a^+}\frac{f(x)}{g(x)}=L.
$$

A corresponding left-sided statement holds.

:::

:::div{class="proof"}

*Proof.* Define $f(a)=g(a)=0$, making both functions continuous at $a$. If $g(x)=0$ at some $x\in(a,b)$, [Theorem 6.2.1](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:rolle) on $[a,x]$ would give a zero of $g'$, a contradiction. For any $x\in(a,b)$, [Theorem 6.2.10](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:cauchy-mean-value) supplies a point $z\in(a,x)$ for which

$$
\frac{f(x)}{g(x)}
      =\frac{f(x)-f(a)}{g(x)-g(a)}
      =\frac{f'(z)}{g'(z)}.
$$

As $x\to a^+$, the inequalities $a<z<x$ force $z\to a^+$. The assumed derivative-ratio limit therefore gives the asserted quotient limit, also when $L$ is infinite. ◻

:::

For the $\infty/\infty$ form, suppose instead that both $f(x)$ and $g(x)$ tend to $+\infty$, with the same differentiability and nonzero denominator-derivative assumptions. If $f'(x)/g'(x)$ has a limit $L$, the corresponding rule gives $f(x)/g(x)\to L$. This version is stated without proof here. Writing

$$
\frac{f(x)}{g(x)}=\frac{1/g(x)}{1/f(x)}
$$

does turn the expression into $0/0$, but it does not by itself prove the rule, since differentiating these reciprocals introduces additional factors of $f$ and $g$.

### Logarithms and limits of variable powers {id="logarithms-and-limits-of-variable-powers"}

Taking a logarithm turns a power into a product. To recover the original limit, we use continuity of the exponential. The required continuity and positive-base power identities are developed in [Theorem 8.6.5](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:exponential-properties) and [Definition 8.6.6](/notes/maths-analysis/analysis-i/sequences-and-series-of-functions/#thm:analysis-i:logarithm-real-powers).

First distinguish the two directions of this argument. If $u(x)>0$ near $a$ and $u(x)\to A>0$, continuity of $\ln$ on $(0,\infty)$ gives

$$
\lim_{x\to a}\ln u(x)
    =\ln\left(\lim_{x\to a}u(x)\right)=\ln A.
$$

The condition $A>0$ matters because $\ln0$ is not a real number. When the original limit is unknown, the useful direction starts by finding the logarithmic limit and then applying the exponential.

:::div{id="thm:analysis-i:logarithmic-power-limits" class="result proposition"}

**Proposition 6.5.2 (Logarithmic method for power limits).** Let $g$ and $h$ be real-valued functions defined near $a$, possibly excluding $a$ itself, with $g(x)>0$ there. If

$$
\lim_{x\to a}h(x)\ln g(x)=L\in\mathbb{R},
$$

then

$$
\lim_{x\to a}g(x)^{h(x)}=e^L.
$$

:::

:::div{class="proof"}

*Proof.* For each $x$ under consideration, positivity of the base gives

$$
g(x)^{h(x)}=e^{h(x)\ln g(x)}.
$$

The exponent tends to the finite real number $L$. Since the exponential is continuous at $L$, we obtain

$$
\lim_{x\to a}g(x)^{h(x)}
      =\exp\left(\lim_{x\to a}h(x)\ln g(x)\right)=e^L.
$$

Thus convergence of the logarithmic expression establishes convergence of the original power. ◻

:::

This method replaces a variable exponent by multiplication. The product $h(x)\ln g(x)$ can often be rewritten as a quotient and evaluated with limit laws or L’Hôpital’s rule, after checking the rule’s hypotheses. The same continuity argument applies to one-sided limits and limits at infinity.

For sequences, positivity is needed only for all sufficiently large indices. If $u_n>0$ eventually and $v_n\ln u_n\to L\in\mathbb{R}$, then

$$
u_n^{v_n}=\exp(v_n\ln u_n)\longrightarrow e^L.
$$

Finitely many initial terms do not affect the limit. We first establish the limit of the exponent and then use continuity to pass that limit inside the exponential.

:::div{id="ex:analysis-i:euler-approximant-limit" class="result example"}

**Example 6.5.3 (The limit of the exponential approximants).** For $x>0$, put $t=1/x$. The logarithm of $(1+1/x)^x$ is

$$
x\ln(1+1/x)=\frac{\ln(1+t)}{t}.
$$

As $t\to0^+$, numerator and denominator tend to zero. Applying [Theorem 6.5.1](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:lhopital-zero) gives

$$
\lim_{t\to0^+}\frac{\ln(1+t)}{t}
      =\lim_{t\to0^+}\frac{1/(1+t)}{1}=1.
$$

Applying [Proposition 6.5.2](/notes/maths-analysis/analysis-i/differentiation-and-applications/#thm:analysis-i:logarithmic-power-limits) to this logarithmic limit therefore yields

$$
\lim_{x\to+\infty}(1+1/x)^x=e.
$$

The monotonicity of these approximants was established in [Example 6.2.8](/notes/maths-analysis/analysis-i/differentiation-and-applications/#ex:analysis-i:increasing-euler-approximants).

:::

### Exercises on difference quotients and indeterminate forms {id="exercises-on-difference-quotients-and-indeterminate-forms"}

Symmetric differences use values on both sides of the input. The following question can be approached using the zero-quotient rule, with differentiation performed with respect to $h$ while $x$ is fixed. Taylor’s theorem supplies another route.

::statement{key="hw07:symmetric-differences"}

The elementary derivative formulas in [§ 6.1](/notes/maths-analysis/analysis-i/differentiation-and-applications/#sec:analysis-i:differentiation) provide the trigonometric and logarithmic tools needed for the next limits.

::statement{key="hw07:trigonometric-logarithmic-limits"}

::statement{key="hw07:power-sequence-limits"}

<span class="smallcaps">Check your understanding.</span> Fix $x\in\mathbb{R}$ and denote the first sequence in [Exercise 6.5.6](/notes/maths-analysis/analysis-i/differentiation-and-applications/#ex:hw07:power-sequence-limits) by $(y_n)$. For all sufficiently large $n$, what product do you obtain for $\ln y_n$? Rewrite it as a quotient suitable for a real-variable limit. Which continuity property will recover the limit of $y_n$ from the limit of $\ln y_n$?

::statement{key="hw07:self-power-limit"}

## 6.6 Inverse function theorem {id="sec:analysis-i:inverse-function-theorem"}

The inverse differentiation rule used for roots and logarithms is a one-dimensional statement. Continuity of a strictly monotone inverse was established in [Theorem 5.3.6](/notes/maths-analysis/analysis-i/continuity/#thm:analysis-i:continuous-inverse).

:::div{id="thm:analysis-i:inverse-derivative" class="result theorem"}

**Theorem 6.6.1 (Derivative of an inverse).** Let $f:I\to J$ be a continuous strictly monotone bijection between open intervals, and let $g=f^{-1}$. If $f$ is differentiable at $x\in I$ and $f'(x)\ne0$, then $g$ is differentiable at $y=f(x)$ and

$$
g'(y)=\frac1{f'(x)}=\frac1{f'(g(y))}.
$$

:::

:::div{class="proof"}

*Proof.* Restrict $f$ to a closed subinterval of $I$ containing $x$ in its interior. By [Theorem 5.3.6](/notes/maths-analysis/analysis-i/continuity/#thm:analysis-i:continuous-inverse) and its decreasing analogue, its inverse, and hence $g$, is continuous near $y$. For $k\ne0$ sufficiently small, set $h=g(y+k)-g(y)$. Injectivity gives $h\ne0$, and continuity of $g$ gives $h\to0$ as $k\to0$. Also $k=f(x+h)-f(x)$, so

$$
\frac{g(y+k)-g(y)}{k}
      =\frac1{\bigl(f(x+h)-f(x)\bigr)/h}
      \longrightarrow\frac1{f'(x)}.
$$

 ◻

:::

This difference-quotient argument establishes that the inverse derivative exists before applying the chain rule.

Differentiating $g(f(x))=x$ now gives the identity

$$
g'(f(x))f'(x)=1.
$$
