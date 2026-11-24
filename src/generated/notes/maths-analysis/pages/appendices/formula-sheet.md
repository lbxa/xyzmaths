---
title: "Formula sheet"
group: "Appendices"
order: 19
page: "211"
outline: [{"id": "sec:appendix:formula-sheet-sets", "title": "D.1 Sets, numbers, and counting", "level": 2}, {"id": "sec:appendix:formula-sheet-bounds", "title": "D.2 Bounds, completeness, and algebra", "level": 2}, {"id": "sec:appendix:formula-sheet-sequences", "title": "D.3 Sequences", "level": 2}, {"id": "sec:appendix:formula-sheet-series", "title": "D.4 Infinite series", "level": 2}, {"id": "sec:appendix:formula-sheet-power-series", "title": "D.5 Power series", "level": 2}, {"id": "sec:appendix:formula-sheet-proof-moves", "title": "D.6 Common proof moves", "level": 2}]
---

# Appendix D. Formula sheet {id="ch:appendix:formula-sheet"}

Throughout, limits are taken as the index tends to infinity and $N$ is a positive integer. Here $\mathbb{N}=\{1,2,\ldots\}$. Conditions are part of each result.

## D.1 Sets, numbers, and counting {id="sec:appendix:formula-sheet-sets"}

**Membership and complements in $S$**

$$
\begin{aligned}
    x\in\bigcup_\gamma A_\gamma&\iff\exists\gamma\quad x\in A_\gamma,\\
    x\in\bigcap_\gamma A_\gamma&\iff\forall\gamma\quad x\in A_\gamma,\\
    \left(\bigcup_\gamma A_\gamma\right)^c&=\bigcap_\gamma A_\gamma^c,\qquad
    \left(\bigcap_\gamma A_\gamma\right)^c=\bigcup_\gamma A_\gamma^c.
  \end{aligned}
$$

Empty family in $S$: $\bigcup_\varnothing A_\gamma=\varnothing$, $\bigcap_\varnothing A_\gamma=S$.

**Maps and counting**

For $f:A\to B$, injective means $f(x)=f(y)\Rightarrow x=y$. Surjective means $f(A)=B$. Bijective means both.

$$
A\hookrightarrow B\Rightarrow |A|\le|B|,\qquad
  (A\hookrightarrow B,\ B\hookrightarrow A)\Rightarrow |A|=|B|.
$$

The second statement is Cantor–Bernstein. A countable union of countable sets, or a finite product of countable sets, is at most countable. An infinite subset establishes cardinality $\aleph_0$.

**Finite sums**

:anchor[]{id="sec:appendix:formula-sheet-finite-sums"}

$$
\sum\nolimits_{j=1}^{N}j=\frac{N(N+1)}2.
$$

$$
\begin{aligned}
    \sum\nolimits_{j=1}^{N}(a+(j-1)d)&=\frac N2(2a+(N-1)d),\\
    \sum\nolimits_{j=1}^{N}j^2&=\frac{N(N+1)(2N+1)}6,\\
    \sum\nolimits_{j=1}^{N}j^3&=\left(\frac{N(N+1)}2\right)^2.
  \end{aligned}
$$

**Lowest terms and Euclid’s lemma**

$d\mid a$ means $a=dm$ for an integer $m$. For prime $p$ and $k\in\mathbb{N}$,

$$
p\mid ab\Rightarrow(p\mid a\text{ or }p\mid b),\qquad
  p\mid a^k\Rightarrow p\mid a.
$$

Use $a/b$ with $b>0$ and $\gcd(a,b)=1$. A common prime divisor forces $\gcd(a,b)>1$.

**Power sets, algebraic numbers, and CH**

$$
\begin{gathered}
    \mathcal P(\varnothing)=\{\varnothing\},\quad
    \mathcal P(\{\varnothing\})=\{\varnothing,\{\varnothing\}\},\\
    |\mathcal P(A)|=2^{|A|}>|A|,\\
    |\mathbb{N}|=|\mathbb{Z}|=|\mathbb{Q}|=|\mathcal A|=\aleph_0,\\
    |\mathbb{R}|=|\mathbb{C}|=|\mathbb{R}^2|=|\mathcal T|=\mathfrak c=2^{\aleph_0}.
  \end{gathered}
$$

$\mathcal A$ consists of real roots of nonzero polynomials in $\mathbb{Q}[X]$ (equivalently $\mathbb{Z}[X]$). Put $\mathcal T=\mathbb{R}\setminus\mathcal A$. A nonzero degree-$d$ polynomial has at most $d$ roots. CH asserts $\mathfrak c=\aleph_1$. The displayed sizes do not need CH. Bare $\aleph$ in exercises means $\mathfrak c$.

**Interval maps worth having at hand**

For $a<b$, $t=(x-a)/(b-a)$ maps $(a,b)$ bijectively to $(0,1)$. For $(0,1)\leftrightarrow\mathbb{R}$,

$$
f(t)=\tan\left(\pi t-\frac\pi2\right),\qquad
  f^{-1}(y)=\frac12+\frac{\arctan y}{\pi}.
$$

A bijection $h:(0,1)\to[0,1]$, with $n\in\mathbb{N}$, is

$$
h(t)=
  \begin{cases}
    0,&t=1/2,\\
    1,&t=1/3,\\
    1/(n-2),&t=1/n,\quad n\ge4,\\
    t,&\text{otherwise}.
  \end{cases}
$$

For $(0,1)^2\hookrightarrow(0,1)$, interleave decimal digits $x_1y_1x_2y_2\cdots$ using expansions not eventually all $9$s. For the reverse injection use $t\mapsto(t,1/2)$.

## D.2 Bounds, completeness, and algebra {id="sec:appendix:formula-sheet-bounds"}

**Best bounds and complete real intervals**

For nonempty $E$, $s=\sup E$ iff $s$ bounds $E$ above and $\forall\varepsilon>0\ \exists x\in E$ with $s-\varepsilon<x$. Likewise, $\ell=\inf E$ iff $\ell$ bounds $E$ below and $\forall\varepsilon>0\ \exists x\in E$ with $x<\ell+\varepsilon$.

If bounded below, $\inf E=-\sup(-E)$.

For a Dedekind partition $L<U$ of $\mathbb{R}$, $c=\sup L=\inf U$. For nested nonempty bounded closed real intervals,

$$
\bigcap_{n\ge1}[a_n,b_n]=[\sup_n a_n,\inf_n b_n]\ne\varnothing.
$$

If $b_n-a_n\to0$, the intersection is a singleton.

**Floor, finite geometric sum, and factorials**

Archimedean choice: for every real $M$, some $N\in\mathbb{N}$ has $N>M$.

$$
\begin{gathered}
    \lfloor x\rfloor\le x<\lfloor x\rfloor+1,\quad
    0\le x-\frac{\lfloor Nx\rfloor}{N}<\frac1N,\\
    \sum\nolimits_{j=0}^{N}ar^j=a\frac{1-r^{N+1}}{1-r}\quad(r\ne1),\\
    \sum\nolimits_{k=n}^{m}r^k
      =\frac{r^n-r^{m+1}}{1-r}
      =r^n\frac{1-r^{m-n+1}}{1-r}.
  \end{gathered}
$$

For the shifted sum, take integers $0\le n\le m$ and $r\ne1$. For $r=1$, the respective sums are $a(N+1)$ and $m-n+1$. With $s_N=\sum_{j=0}^N1/j!$, we have $2\le s_N<3$ and

$$
e=\sum\nolimits_{j=0}^\infty\frac1{j!},\quad
  k!\ge2^{k-1}\ (k\ge1),\quad
  0<N!(e-s_N)<\frac1N.
$$

For interval radii $\varepsilon2^{-n}$, $n\ge0$, total length is $2\varepsilon\sum2^{-n}=4\varepsilon$.

**Algebra and roots ($k\in\mathbb{N}$)**

$$
\begin{gathered}
    |x+y|\le|x|+|y|,\qquad \bigl||x|-|y|\bigr|\le|x-y|,\\
    b^k-a^k=(b-a)\sum\nolimits_{j=0}^{k-1}b^{k-1-j}a^j,\\
    0<b^k-a^k\le k(b-a)b^{k-1}\quad(0\le a<b),\\
    \sqrt u-\sqrt v=\frac{u-v}{\sqrt u+\sqrt v}\quad
       (u,v\ge0,\ u+v>0).
  \end{gathered}
$$

For nonnegative bases, $m,n\in\mathbb{N}$, and positive rational $r,s$, $(xy)^{1/n}=x^{1/n}y^{1/n}$, $x^{m/n}=(x^m)^{1/n}=(x^{1/n})^m$, $(x^r)^s=x^{rs}$, and $x^{r+s}=x^rx^s$. Negative exponents need $x>0$. Nonnegative roots are unique. Odd power maps are increasing bijections on $\mathbb{R}$.

**Newton’s method and quadratic roots**

$$
\begin{gathered}
      x_{n+1}=x_n-\frac{F(x_n)}{F'(x_n)},\\
      Ax^2+Bx+C=0\Rightarrow x=\frac{-B\pm\sqrt{B^2-4AC}}{2A}.
    \end{gathered}
$$

Require $F'(x_n)\ne 0$, $A\ne 0$, and a nonnegative discriminant for real roots.

## D.3 Sequences {id="sec:appendix:formula-sheet-sequences"}

$x_n\to L$ means $\forall\varepsilon>0\ \exists N\ \forall n\ge N\quad |x_n-L|<\varepsilon$. If $x_n\to L$, $y_n\to M$, limit laws give

$$
\begin{gathered}
    ax_n+by_n\to aL+bM,\\
    x_ny_n\to LM,\qquad x_n/y_n\to L/M\ (M\ne0).
  \end{gathered}
$$

Squeeze: eventual $u_n\le x_n\le v_n$ and $u_n,v_n\to L$ imply $x_n\to L$.

**Binomial identity**

$$
\begin{gathered}
    (u+v)^n=\sum\nolimits_{j=0}^n\binom nj u^{n-j}v^j,\\
    \binom nj=\frac{n!}{j!(n-j)!}.
  \end{gathered}
$$

**Standard limits**

Bernoulli: $(1+t)^n\ge1+nt$ for $t\ge-1$. For fixed $c>0$, $a>1$, and $p>0$,

$$
\begin{gathered}
    n^{-p}\to0,\quad c^{1/n}\to1,\quad n^{1/n}\to1,\\
    n^{p/n}\to1,\quad n^p/a^n\to0,\\
    (a^n+n)^{1/n}\to\max\{1,a\}\quad(a\ge0),\\
    (1+1/n)^n\to e,\qquad (1+1/n)^{1/n}\to1.
  \end{gathered}
$$

$r^n\to0$ for $|r|<1$. For $r>1$, $r^n\to+\infty$. For a polynomial with positive leading coefficient, $P(n)^{1/n}\to1$.

**Monotonicity, AM–GM, and subsequences**

A bounded increasing sequence tends to $\sup\{x_n\}$ and has infimum $x_1$. A bounded decreasing one tends to $\inf\{x_n\}$ and has supremum $x_1$.

$$
(a_1\cdots a_k)^{1/k}\le\frac{a_1+\cdots+a_k}{k}
  \quad(a_i\ge0,\ k\in\mathbb{N}).
$$

Equality holds exactly when all $a_i$ agree. Bounded real sequences have convergent subsequences. Two distinct subsequence limits rule out convergence. For indices $n\equiv0,1,2\pmod3$, respectively, $\sin(2\pi n/3)=0,\sqrt3/2,-\sqrt3/2$.

**Tail bounds and Cauchy**

$$
\begin{aligned}
    \liminf x_n&=\lim_n\inf_{k\ge n}x_k,\qquad
    \limsup x_n=\lim_n\sup_{k\ge n}x_k,\\
    x_n\to L&\iff\liminf x_n=\limsup x_n=L.
  \end{aligned}
$$

For bounded sequences these are the extreme subsequence limits. In $\mathbb{R}$, convergence is equivalent to the Cauchy condition

$$
\forall\varepsilon>0\ \exists N\ \forall m,n\ge N\quad
  |x_m-x_n|<\varepsilon.
$$

For integers $m>n\ge1$ and $0\le L<1$,

$$
\sum\nolimits_{k=n}^{m-1}L^k
    =\frac{L^n-L^m}{1-L}\le\frac{L^n}{1-L}.
$$

The final bound no longer depends on $m$, and $L^n\to0$.

## D.4 Infinite series {id="sec:appendix:formula-sheet-series"}

**Partial sums, tails, and basic sums**

$S_N=\sum_{n=1}^N a_n$. The notation $\sum a_n=S$ means $S_N\to S$. Convergence requires $a_n\to0$. The converse fails. For $a_n\ge0$, convergence is equivalent to bounded partial sums. The Cauchy criterion is

$$
\forall\varepsilon>0\ \exists N\ \forall m>n\ge N\quad
    \left|\sum\nolimits_{k=n+1}^m a_k\right|<\varepsilon.
$$

$$
\begin{aligned}
    \sum\nolimits_{k=0}^\infty ar^k&=\frac a{1-r}\quad(|r|<1),\\
    \sum\nolimits_{k=n}^\infty r^k&=\frac{r^n}{1-r}\quad(|r|<1),\\
    \sum\nolimits_{k=n}^\infty ar^k&=\frac{ar^n}{1-r}\quad(|r|<1),\\
    \sum\nolimits_{n=1}^N(b_n-b_{n+1})&=b_1-b_{N+1},\\
    \sum\nolimits_{n=1}^\infty(b_n-b_{n+1})&=b_1-B\quad(b_n\to B).
  \end{aligned}
$$

For geometric tails, $n$ is a nonnegative integer. Factor out $r^n$ so the remaining sum starts at exponent zero. In particular, $\sum_{n=1}^\infty1/[n(n+1)]=1$.

**Comparison**

$\sum n^{-p}$ converges iff $p>1$. For nonnegative terms, eventual $a_n\le Cb_n$ transfers convergence from $\sum b_n$. Eventual $a_n\ge cb_n$ transfers divergence ($C,c>0$). For $a_n\ge0$, $b_n>0$,

$$
r=\liminf\frac{a_n}{b_n},\qquad R=\limsup\frac{a_n}{b_n}.
$$

If $r>0$, divergence of $\sum b_n$ implies divergence of $\sum a_n$. If $R<\infty$, convergence of $\sum b_n$ implies convergence of $\sum a_n$. For a real shift $a>0$,

$$
0<\frac1{\sqrt n}-\frac1{\sqrt{n+a}}<\frac{a}{2n^{3/2}}.
$$

**Ratio, root, and alternating tests**

For eventually nonzero terms, $q_n=|a_{n+1}/a_n|$. Absolute convergence follows if $\limsup q_n<1$. Divergence follows if $\liminf q_n>1$. For $\rho=\limsup|a_n|^{1/n}$, $\rho<1$ gives absolute convergence. $\rho>1$ gives divergence. A lower root limit $>1$ also gives divergence. Test value $1$ is inconclusive. If $a_n\downarrow0$, $\sum_{n=0}^\infty(-1)^n a_n$ converges and

$$
|S-S_N|\le a_{N+1},\qquad |S_m-S_n|\le a_{n+1}\quad(m>n).
$$

Absolute convergence implies convergence. Its failure does not imply divergence.

## D.5 Power series {id="sec:appendix:formula-sheet-power-series"}

For $\sum c_nx^n$,

$$
R=\frac1{\limsup|c_n|^{1/n}},\qquad
  1/0=+\infty,\quad1/(+\infty)=0.
$$

If defined with a limit, $R=\lim|c_n/c_{n+1}|$ also works. There is absolute convergence for $|x|<R$, divergence for $|x|>R$. Test $x=\pm R$ separately. At $x=0$ the series equals $c_0$. For $a>0$, $k\in\mathbb{Z}$,

$$
\left|\frac{x^n}{a^n n^k}\right|^{1/n}
     =\frac{|x|}{a(n^{1/n})^k}\longrightarrow\frac{|x|}{a}.
$$

Thus $R=a$, while $|x|/a$ is the test value, not the radius. At $x=\pm a$, absolute convergence holds iff $k>1$ by $\sum n^{-k}$. For $k=1$, $x=-a$ converges conditionally and $x=a$ diverges. For $k\le0$, endpoint terms do not tend to zero.

## D.6 Common proof moves {id="sec:appendix:formula-sheet-proof-moves"}

**Sets, bijections, and enumeration**

Chase an arbitrary element in both directions. Swap $\forall,\exists$ when negating. For a bijection, give an inverse or show disjoint image pieces cover the target. For countable unions, read diagonals of an array of enumerations and skip repeats.

**Irrationality and transcendence**

Assume a lowest-terms fraction. For $p^{1/k}$, $p$ prime, $k\ge2$, raise to the $k$th power and force $p$ to divide both numerator and denominator. For powers of transcendental $\tau$, clear denominators in a nontrivial rational relation to get a nonzero polynomial vanishing at $\tau$. Count algebraic numbers using bounded degree and coefficients. Then $\mathbb{R}=\mathcal A\cup\mathcal T$ forces $\mathcal T$ uncountable. Under CH, $\aleph_0<|\mathcal T|\le|\mathbb{R}|$ implies equality with $|\mathbb{R}|$.

**Best bounds, epsilon choices, and cuts**

Prove a bound first, then give witnesses within every $\varepsilon$. If $u>v$, take $\varepsilon=(u-v)/2$. If $|x_n-L|\le C/n^\alpha$ with $C,\alpha>0$, choose $N>(C/\varepsilon)^{1/\alpha}$. For two errors budget $\varepsilon/2$ each. Use $|x_m-x_n|\le|x_m-L|+|x_n-L|$ to obtain a Cauchy estimate. For a direct infimum cut, take $L$ as all lower bounds and $U=\mathbb{R}\setminus L$. Prove separation, then use $c\le s+\varepsilon$ for every $\varepsilon>0$ to obtain $c\le s$. Do not invoke LUBP if the question forbids it.

**Missing hypotheses and missing limits**

Use $(0,1/n)$ to drop closedness, $[n,\infty)$ to drop boundedness, and shrinking rational-ended intervals about an irrational to expose incompleteness of $\mathbb{Q}$. Rational decimals $q_n$ with $|q_n-\alpha|<10^{-n}$ are Cauchy but have no rational limit when $\alpha$ is irrational. Small covering length alone does not prove incompleteness.

**Root uniqueness and equality conditions**

For nonnegative expressions, raise to a common integer power and use uniqueness. For rational exponents use a common denominator. Even powers do not identify signed reals. $(\sqrt a-\sqrt b)^2=a+b-2\sqrt{ab}\ge0$ proves AM–GM, with equality exactly at $a=b$. For reverse triangle, write $x=(x-y)+y$, then swap $x,y$. Equality holds exactly when $xy\ge0$.

**Recurrences and fixed points**

Simplify sums first. Prove an invariant interval by induction and factor $g(x)-x$ to get monotonicity. Bounded monotonicity proves convergence. Only then solve $L=g(L)$, retaining roots compatible with the bounds. Positive terms alone do not imply $L>0$. For $g(x)=(\tfrac32x^2+2x)/(1+x^2)$,

$$
2-g(x)=\frac{(x-2)^2}{2(1+x^2)},\qquad
  g(x)-x=\frac{x(2-x)(2x+1)}{2(1+x^2)}.
$$

The general Newton map for $x-a-1/x$ is $(ax^2+2x)/(1+x^2)$. Its positive limiting fixed point is $(a+\sqrt{a^2+4})/2$. Fibonacci ratios satisfy $r_n=1+1/r_{n-1}$ for $n\ge3$ and $1\le r_n\le2$ for $n\ge2$. If convergent, their limit is $(1+\sqrt5)/2$.

**Integer remainder, oscillation, and $n$th roots**

If $e=p/q$, take $N\ge\max\{q,2\}$. Then $N!(e-s_N)$ is an integer in $(0,1)$. For periodic behaviour, split indices modulo the period. An infinite subsequence contains infinitely many indices in one class. For $n$th roots, factor the dominant term and squeeze using $\max\{u,v\}\le u+v\le2\max\{u,v\}$ and $c^{1/n},n^{1/n}\to1$.

**Finite tails, strict gaps, and last checks**

Telescope finite partial sums and keep the last term. For alternating tails, pair in both parities, retaining any unpaired term, to get the first-omitted-term bound. Rationalise arbitrary real shifts rather than assuming cancellation. Choose $\limsup t_n<r<1$ for an eventual upper bound or $1<r<\liminf t_n$ for a lower bound. Test value $1$ is inconclusive. Test power-series endpoints separately. Finite prefixes do not change convergence, but can change extrema and sums.
