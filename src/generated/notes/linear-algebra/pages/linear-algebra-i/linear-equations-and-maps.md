---
title: "Linear equations and maps"
group: "Linear Algebra I"
order: 9
part: "Part I · Linear Algebra I"
page: "33"
outline: [{"id": "sec:linear-algebra-i:systems-of-linear-equations", "title": "3.1 Systems of linear equations", "level": 2}, {"id": "matrix-form", "title": "Matrix form", "level": 3}, {"id": "augmented-matrices-and-row-operations", "title": "Augmented matrices and row operations", "level": 3}, {"id": "triangular-systems-and-factorization", "title": "Triangular systems and factorization", "level": 3}, {"id": "normalized-systems", "title": "Normalized systems", "level": 3}, {"id": "sec:linear-algebra-i:linear-functions-and-maps", "title": "3.2 Linear functions and maps", "level": 2}, {"id": "linearity-and-linear-functionals", "title": "Linearity and linear functionals", "level": 3}, {"id": "sec:linear-algebra-i:linear-map-grids", "title": "Why a linear map preserves grid structure", "level": 3}, {"id": "prescribing-a-map-on-a-basis", "title": "Prescribing a map on a basis", "level": 3}, {"id": "differentiation", "title": "Differentiation", "level": 3}, {"id": "the-vector-space-of-linear-maps", "title": "The vector space of linear maps", "level": 3}, {"id": "sec:linear-algebra-i:change-of-basis-for-functions-and-maps", "title": "3.3 Change of basis formula for functions and maps", "level": 2}, {"id": "matrices-in-standard-bases", "title": "Matrices in standard bases", "level": 3}, {"id": "matrices-in-arbitrary-bases", "title": "Matrices in arbitrary bases", "level": 3}, {"id": "composition", "title": "Composition", "level": 3}, {"id": "invertible-maps-and-inverse-matrices", "title": "Invertible maps and inverse matrices", "level": 3}, {"id": "changing-both-bases", "title": "Changing both bases", "level": 3}]
---

# Chapter 3. Linear equations and maps {id="ch:linear-algebra-i:linear-equations-and-maps"}

Matrix multiplication turns a system of linear equations into one equation $Ax=b$. We first use row operations to study that equation, then examine the linear map $x\mapsto Ax$ behind it. Choosing different bases changes the representing matrix, while composition and inversion of maps become matrix multiplication and inversion.

## 3.1 Systems of linear equations {id="sec:linear-algebra-i:systems-of-linear-equations"}

### Matrix form {id="matrix-form"}

A system of $n$ equations in $m$ unknowns has the form

$$
\sum_{j=1}^m a^i_jx^j=b^i,\qquad 1\leq i\leq n.
$$

Writing $A=(a^i_j)$, $x=(x^1,\ldots,x^m)^T$, and $b=(b^1,\ldots,b^n)^T$ gives

$$
Ax=b,\qquad
  A\in\mathbb F^{n\times m},\quad x\in\mathbb F^m,\quad b\in\mathbb F^n.
$$

The number of equations and the number of unknowns need not agree.

:::div{id="web:sections/linear-algebra-i/03-linear-equations-and-maps/01-systems-of-linear-equations:482" class="result example"}

**Example 3.1.1.** The system

$$
2x-3y=5,\qquad x+y=-1,\qquad 3x+5y=0
$$

can be written as

$$
\begin{bmatrix}2&-3\\1&1\\3&5\end{bmatrix}
    \begin{bmatrix}x\\y\end{bmatrix}
    =\begin{bmatrix}5\\-1\\0\end{bmatrix}.
$$

The equations $x+y+z=1$ and $3y-5z=2$ have matrix form

$$
\begin{bmatrix}1&1&1\\0&3&-5\end{bmatrix}
    \begin{bmatrix}x\\y\\z\end{bmatrix}
    =\begin{bmatrix}1\\2\end{bmatrix}.
$$

:::

Over $\mathbb{R}$, the equation $x=b$ has exactly one solution, whereas

$$
\begin{bmatrix}1&0\end{bmatrix}
  \begin{bmatrix}x\\y\end{bmatrix}=b
$$

has infinitely many, since $y$ is arbitrary. The equations $x=1$ and $x=0$ are inconsistent because no scalar satisfies both,

$$
\begin{bmatrix}1\\1\end{bmatrix}x=\begin{bmatrix}1\\0\end{bmatrix}.
$$

Two equations in two unknowns may have no solution, one solution, or infinitely many solutions. For example, $I_2(x,y)^T=(a,b)^T$ has the unique solution $x=a$, $y=b$.

The solution sets in these examples are visualized in [Figure 3.1](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#fig:linear-algebra-i:linear-system-solution-sets).

::::figure{id="fig:linear-algebra-i:linear-system-solution-sets"}

[![Real-plane schematics of the preceding systems. The equations x=a, y=b meet at one point. The equation x=b leaves a whole line of solutions, while x=0, x=1 have no common point. Arrows indicate that the lines continue.](/notes/linear-algebra/figures/linear-system-solution-sets.svg){.tikz-diagram}](/notes/linear-algebra/figures/linear-system-solution-sets.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 3.1. Real-plane schematics of the preceding systems. The equations $x=a$, $y=b$ meet at one point. The equation $x=b$ leaves a whole line of solutions, while $x=0$, $x=1$ have no common point. Arrows indicate that the lines continue.

:::

::::

### Augmented matrices and row operations {id="augmented-matrices-and-row-operations"}

To solve a system, we rewrite its equations in a form that exposes which variables are determined and which can be chosen freely. The augmented matrix keeps the coefficients and right-hand sides together throughout this calculation.

Appending the right-hand side produces the augmented matrix $[A\mid b]$. The equation $Ax=b$ is equivalent to

$$
[A\mid b]\begin{bmatrix}x\\-1\end{bmatrix}=0.
$$

The final coordinate here is fixed at $-1$.

The elementary row operations exchange two rows, multiply a row by a nonzero scalar, or add a multiple of one row to another. Apply an operation to the entire augmented row, including its right-hand side. Reordering variables corresponds to reordering the columns of $A$.

:::div{id="web:sections/linear-algebra-i/03-linear-equations-and-maps/01-systems-of-linear-equations:2796" class="result example"}

**Example 3.1.2.** Consider

$$
2x-4y+6z=12,\qquad 3x+12y+24z=36.
$$

Dividing the first equation by $2$ gives $x-2y+3z=6$. Subtracting three times this equation from the second gives $18y+15z=18$, or $y+\frac56z=1$. Adding twice this last equation to the first eliminates $y$, leaving

$$
x+\frac{14}{3}z=8,\qquad y+\frac56z=1.
$$

Thus all solutions are

$$
x=8-\frac{14}{3}z,\qquad y=1-\frac56z,\qquad z\in\mathbb{R}.
$$

:::

:::div{id="web:sections/linear-algebra-i/03-linear-equations-and-maps/01-systems-of-linear-equations:3265" class="result example"}

**Example 3.1.3.** The system

$$
\begin{aligned}
      x^1+2x^2+3x^3+5x^4+x^5&=1,\\
      x^3+5x^4&=2,\\
      -3x^5&=9
    \end{aligned}
$$

has augmented matrix

$$
\left[\begin{array}{rrrrr|r}
      1&2&3&5&1&1\\
      0&0&1&5&0&2\\
      0&0&0&0&-3&9
    \end{array}\right].
$$

Divide row $3$ by $-3$, subtract the new row $3$ from row $1$, and then subtract three times row $2$ from row $1$. The successive matrices are

$$
\left[\begin{array}{rrrrr|r}
      1&2&3&5&1&1\\0&0&1&5&0&2\\0&0&0&0&1&-3
    \end{array}\right],
    \qquad
    \left[\begin{array}{rrrrr|r}
      1&2&3&5&0&4\\0&0&1&5&0&2\\0&0&0&0&1&-3
    \end{array}\right],
$$

and finally

$$
\left[\begin{array}{rrrrr|r}
      1&2&0&-10&0&-2\\0&0&1&5&0&2\\0&0&0&0&1&-3
    \end{array}\right].
$$

:::

### Triangular systems and factorization {id="triangular-systems-and-factorization"}

:::div{id="web:sections/linear-algebra-i/03-linear-equations-and-maps/01-systems-of-linear-equations:4143" class="result example"}

**Example 3.1.4.** Consider the upper triangular system

$$
2x+y+z=3,\qquad y-3z=4,\qquad -z=2.
$$

We solve it from the last equation upward. In augmented form, dividing the last row by $-1$ and then eliminating $z$ from the first two rows gives

$$
\left[\begin{array}{rrr|r}
      2&1&1&3\\0&1&-3&4\\0&0&-1&2
    \end{array}\right]
    \longrightarrow
    \left[\begin{array}{rrr|r}
      2&1&1&3\\0&1&-3&4\\0&0&1&-2
    \end{array}\right]
    \longrightarrow
    \left[\begin{array}{rrr|r}
      2&1&0&5\\0&1&0&-2\\0&0&1&-2
    \end{array}\right].
$$

Subtracting row $2$ from row $1$ and then dividing row $1$ by $2$ gives

$$
\left[\begin{array}{rrr|r}
      2&0&0&7\\0&1&0&-2\\0&0&1&-2
    \end{array}\right]
    \longrightarrow
    \left[\begin{array}{rrr|r}
      1&0&0&7/2\\0&1&0&-2\\0&0&1&-2
    \end{array}\right].
$$

The solution is $x=\frac72$, $y=-2$, $z=-2$.

:::

For a square system $Ax=b$, an available factorization $A=LU$, with $L$ lower triangular and $U$ upper triangular, reduces the problem to

$$
Ly=b,\qquad Ux=y.
$$

One first solves $Ly=b$ for $y$, then solves $Ux=y$ for $x$. The resulting vector satisfies $Ax=LUx=Ly=b$. Sparse matrices have many zero entries. Their pattern of zeros can support more efficient solution strategies. Fast matrix multiplication is another topic in numerical linear algebra.

### Normalized systems {id="normalized-systems"}

The reduced equations reveal both the consistency conditions on the right-hand side and the freedom left in the unknowns. After row operations and a possible reordering of variables, consider the following four forms.

1.  For $I_mx=b'$, every variable is determined by $x^j=(b')^j$, where $1\leq j\leq m$.

2.  For

    $$
    [I_k\mid C]x=b',\qquad C\in\mathbb F^{k\times(m-k)},\quad k<m,
    $$

    the last $m-k$ variables are free. The first $k$ satisfy

    $$
    x^j+\sum_{\ell=1}^{m-k} c^j_\ell x^{k+\ell}=(b')^j,
          \qquad 1\leq j\leq k.
    $$

3.  For

    $$
    \begin{bmatrix}I_k\\0_{(n-k)\times k}\end{bmatrix}x=b',
    $$

    the unknown column has $k$ entries. The equations require $x^j=(b')^j$ for $1\leq j\leq k$ and $(b')^{k+1}=\cdots=(b')^n=0$. A nonzero entry among these last right-hand sides makes the system inconsistent.

4.  In the combined case,

    $$
    \begin{bmatrix}
            I_k&C\\
            0_{(n-k)\times k}&0_{(n-k)\times(m-k)}
          \end{bmatrix}x=b',
    $$

    there are free variables $x^{k+1},\ldots,x^m$, while the last $n-k$ equations require $(b')^{k+1}=\cdots=(b')^n=0$.

::statement{key="hw02:inconsistent-system"}

## 3.2 Linear functions and maps {id="sec:linear-algebra-i:linear-functions-and-maps"}

### Linearity and linear functionals {id="linearity-and-linear-functionals"}

The grid picture of [Subsection\* 1.2](/notes/linear-algebra/linear-algebra-i/vector-spaces-and-bases/#sec:linear-algebra-i:bases-to-transformations) is an instance of a general principle. A linear map respects addition and scaling in the domain, even when its inputs are functions or matrices rather than points of a plane. The following definition states that principle without depending on coordinates.

:::div{id="web:sections/linear-algebra-i/03-linear-equations-and-maps/02-linear-functions-and-maps:472" class="result definition"}

**Definition 3.2.1.** Let $V$ and $W$ be vector spaces over the same field $\mathbb F$. A map $L:V\to W$ is linear if the identities

$$
L(v+w)=L(v)+L(w),\qquad L(av)=aL(v)
$$

hold for $v,w\in V$ and $a\in\mathbb F$. These identities express preservation of addition and scalar multiplication. Equivalently,

$$
L(av+bw)=aL(v)+bL(w)
$$

for all $a,b\in\mathbb F$ and $v,w\in V$. When $W=\mathbb F$, a linear map is called a linear functional.

:::

In particular, $L(0_V)=0_W$. A function between vector spaces must satisfy the displayed identities to be linear. Its domain and codomain provide the vector-space operations with which this additional requirement is expressed.

The addition identity is pictured in [Figure 3.2](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#fig:linear-algebra-i:linearity-parallelograms).

::::figure{id="fig:linear-algebra-i:linearity-parallelograms"}

[![A real-plane schematic of L(v+w)=L(v)+L(w). The image of the diagonal is the sum of the images of the two sides.](/notes/linear-algebra/figures/linearity-parallelograms.svg){.tikz-diagram}](/notes/linear-algebra/figures/linearity-parallelograms.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 3.2. A real-plane schematic of $L(v+w)=L(v)+L(w)$. The image of the diagonal is the sum of the images of the two sides.

:::

::::

:::div{id="web:sections/linear-algebra-i/03-linear-equations-and-maps/02-linear-functions-and-maps:1611" class="result example"}

**Example 3.2.2.** If $E=(e_1,e_2)$ is a basis of $V$, write $a_1=L(e_1)$, $a_2=L(e_2)$ for a linear functional $L$. For $v=c_1e_1+c_2e_2$,

$$
L(v)=c_1L(e_1)+c_2L(e_2)=c_1a_1+c_2a_2.
$$

:::

### Why a linear map preserves grid structure {id="sec:linear-algebra-i:linear-map-grids"}

For a real vector space, a line with starting point $p$ and nonzero direction $d$ consists of vectors $p+td$, where $t\in\mathbb{R}$. Linearity gives

$$
L(p+td)=L(p)+tL(d).
$$

If $L(d)\ne0$, these images form a line with direction $L(d)$. Lines sharing the direction $d$ therefore have images sharing the direction $L(d)$, so the image lines are parallel or coincide. If $L(d)=0$, the entire line maps to the single point $L(p)$.

Equal spacing comes from the same identity. Consecutive inputs $p+kd$, for integer $k$, differ by $d$. Their images differ by the constant vector $L(d)$, since

$$
L(p+(k+1)d)-L(p+kd)=L(d).
$$

Every input step in this direction produces the same output step, wherever it is taken. In a two-dimensional grid generated by $e_1,e_2$, the two step vectors become $L(e_1),L(e_2)$. If these remain independent, the result is a parallelogram grid, with uniform spacing within each parallel family. The two spacings need not be equal to one another or to their original values. Angles and lengths may change.

Parallel lines alone do not capture this condition. [Figure 3.3](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#fig:linear-algebra-i:unequal-grid-steps) redraws a grid in which parallel lines survive but equal input steps have unequal image steps. Such an action cannot be linear. These pictures illustrate consequences of linearity. The definition still requires the identities for every vector and scalar, rather than just the finitely many points visible in a drawing.

::::figure{id="fig:linear-algebra-i:unequal-grid-steps"}

[![Schematic of a failure of linearity. The three marked input points are equally spaced on a line, but their three images are not. Parallel grid lines and a fixed origin do not repair the unequal steps.](/notes/linear-algebra/figures/unequal-grid-steps.svg){.tikz-diagram}](/notes/linear-algebra/figures/unequal-grid-steps.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 3.3. Schematic of a failure of linearity. The three marked input points are equally spaced on a line, but their three images are not. Parallel grid lines and a fixed origin do not repair the unequal steps.

:::

::::

The possibility of collapse is equally important. If the two image step vectors are dependent, a planar grid can collapse to a line, and if both are zero it collapses to the origin. These maps still preserve linear combinations. The kernel and image in [Chapter 4](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#ch:linear-algebra-i:kernel-image-and-rank) describe the lost directions and the output space that remains. For example, when $L(e_1)=u\ne0$ and $L(e_2)=0$,

$$
L(ae_1+be_2)=au.
$$

The output retains the first coefficient, while every change in the second coefficient gives the same output. This case is shown in [Figure 3.4](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#fig:linear-algebra-i:collapsed-grid).

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:collapsed-grid"}

[![Schematic with L(e\_1)=u\\ne0 and L(e\_2)=0. Each vertical input line collapses to one point. Equal horizontal steps still give equal steps along the image line.](/notes/linear-algebra/figures/collapsed-grid.svg){.tikz-diagram}](/notes/linear-algebra/figures/collapsed-grid.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 3.4. Schematic with $L(e_1)=u\ne0$ and $L(e_2)=0$. Each vertical input line collapses to one point. Equal horizontal steps still give equal steps along the image line.

:::

::::

:::::

### Prescribing a map on a basis {id="prescribing-a-map-on-a-basis"}

The grid discussion explains why it suffices to track basis vectors. Every other vector is assembled from them, and linearity retains its coefficients. The same argument applies in any vector space with a finite basis, without a geometric grid.

Let $(v_1,\ldots,v_m)$ be a basis of $V$. For each $j$, choose a vector $w_j\in W$. The prescription

$$
L(v_j)=w_j,\qquad 1\leq j\leq m,
$$

determines a linear map on all of $V$. For $v=a^1v_1+\cdots+a^mv_m$, its value is

$$
L(v)=a^1w_1+\cdots+a^mw_m.
$$

::::div{id="ex:linear-algebra-i:coordinate-rule-matrix-columns" class="result example"}

**Example 3.2.3 (Recovering matrix columns from a coordinate rule).** Define $L:\mathbb{R}^2\to\mathbb{R}^2$ by

$$
L(v^1,v^2)=(3v^1-2v^2,\;5v^1+6v^2).
$$

:::div{class="pending-review"}

Each output coordinate is a linear combination of the input coordinates. Coordinatewise addition and scalar multiplication therefore make $L$ linear. The images of the standard basis vectors are

$$
L(1,0)=(3,5),\qquad L(0,1)=(-2,6).
$$

Since $(v^1,v^2)=v^1(1,0)+v^2(0,1)$, linearity gives

$$
\begin{aligned}
      L(v)&=v^1(3,5)+v^2(-2,6)\\
        &=\begin{bmatrix}3&-2\\5&6\end{bmatrix}
          \begin{bmatrix}v^1\\v^2\end{bmatrix}.
    \end{aligned}
$$

Thus the first column is $L(1,0)$, and the second is $L(0,1)$. The same two images determine the value at every input. For instance,

$$
\begin{aligned}
      L(1,1)&=L(1,0)+L(0,1)\\
        &=(3-2,5+6)=(1,11),\\
      L(-2,3)&=-2L(1,0)+3L(0,1)\\
        &=(-6-6,-10+18)=(-12,8).
    \end{aligned}
$$

:::

::::

::::div{id="ex:linear-algebra-i:two-to-three-coordinate-map" class="result example"}

**Example 3.2.4 (Two input coordinates and three output coordinates).**

:::div{class="pending-review"}

The map $T:\mathbb{R}^2\to\mathbb{R}^3$ is given by

$$
T(v^1,v^2)=
      \begin{bmatrix}2v^1-v^2\\v^1+v^2\\-v^1+3v^2\end{bmatrix}.
$$

Setting one input coordinate to $1$ and the other to $0$ gives

$$
T(e_1)=\begin{bmatrix}2\\1\\-1\end{bmatrix},\qquad
    T(e_2)=\begin{bmatrix}-1\\1\\3\end{bmatrix}.
$$

For an arbitrary input, the component formula becomes

$$
\begin{aligned}
      T(v)&=v^1\begin{bmatrix}2\\1\\-1\end{bmatrix}
             +v^2\begin{bmatrix}-1\\1\\3\end{bmatrix}\\
        &=\begin{bmatrix}2&-1\\1&1\\-1&3\end{bmatrix}
          \begin{bmatrix}v^1\\v^2\end{bmatrix}.
    \end{aligned}
$$

The two input basis vectors supply two columns. Each image needs three output coordinates, so the matrix has three rows and two columns.

:::

::::

### Differentiation {id="differentiation"}

Differentiation is an example of a linear map whose inputs and outputs are functions. Its definition, linearity, and application to polynomial spaces are developed in [§ 4.4](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#sec:linear-algebra-i:differentiation).

### The vector space of linear maps {id="the-vector-space-of-linear-maps"}

The linear maps $V\to W$ form a vector space, denoted $\mathcal L(V,W)$, under the pointwise operations

$$
(L_1+L_2)(v)=L_1(v)+L_2(v),\qquad (aL)(v)=aL(v).
$$

If $\dim V=m$ and $\dim W=n$, choosing bases identifies this space with the space of $n$-by-$m$ matrices. The correspondence is developed in [§ 3.3](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#sec:linear-algebra-i:change-of-basis-for-functions-and-maps).

::statement{key="hw02:matrix-product-bilinearity"}

## 3.3 Change of basis formula for functions and maps {id="sec:linear-algebra-i:change-of-basis-for-functions-and-maps"}

### Matrices in standard bases {id="matrices-in-standard-bases"}

Let $L:\mathbb F^m\to\mathbb F^n$ be linear, and let $e_1,\ldots,e_m$ be the standard basis of $\mathbb F^m$. Write $A_j=L(e_j)$, and form the matrix $A$ whose columns are $A_1,\ldots,A_m$.

:::div{class="pending-review"}

For $v=v^1e_1+\cdots+v^me_m$, linearity gives

$$
\begin{aligned}
    L(v)&=L(v^1e_1+\cdots+v^me_m)\\
      &=v^1L(e_1)+\cdots+v^mL(e_m)\\
      &=v^1A_1+\cdots+v^mA_m\\
      &=\begin{bmatrix}A_1&\cdots&A_m\end{bmatrix}
        \begin{bmatrix}v^1\\\vdots\\v^m\end{bmatrix}=Av.
  \end{aligned}
$$

The last equality is precisely the column definition of matrix multiplication. Each input coordinate multiplies the image of its corresponding basis vector.

:::

Thus a linear map is represented by the matrix of its values on the standard basis. Conversely, an $n$-by-$m$ matrix $A$ defines the linear map $v\mapsto Av$.

::::div{id="ex:linear-algebra-i:two-basis-images-matrix" class="result example"}

**Example 3.3.1 (A map determined by two basis-vector images).**

:::div{class="pending-review"}

If the linear map $L:\mathbb F^2\to\mathbb F^3$ satisfies $L(e_1)=a=(a^1,a^2,a^3)^T$ and $L(e_2)=b=(b^1,b^2,b^3)^T$, then every input has the form $v=v^1e_1+v^2e_2$, and

$$
\begin{aligned}
      L(v)&=L(v^1e_1+v^2e_2)\\
        &=v^1L(e_1)+v^2L(e_2)\\
        &=v^1\begin{bmatrix}a^1\\a^2\\a^3\end{bmatrix}
          +v^2\begin{bmatrix}b^1\\b^2\\b^3\end{bmatrix}\\
        &=\begin{bmatrix}a^1&b^1\\a^2&b^2\\a^3&b^3\end{bmatrix}
          \begin{bmatrix}v^1\\v^2\end{bmatrix}.
    \end{aligned}
$$

There are two columns because the input has two basis vectors, and three rows because each image has three coordinates. No further values of $L$ need to be specified. Its values on $e_1,e_2$ already determine its value on every linear combination of them.

:::

::::

The correspondence $L\mapsto A$ is a bijective linear map

$$
\mathcal L(\mathbb F^m,\mathbb F^n)
    \longrightarrow \mathrm M_{n\times m}(\mathbb F).
$$

:::div{class="pending-review"}

It is one-to-one because equal matrices give equal basis-vector images and hence equal values at every input. Every matrix occurs, since multiplication by that matrix defines a linear map. Addition and scalar multiplication of maps act on each basis-vector image separately, so the correspondence also preserves these operations.

:::

### Matrices in arbitrary bases {id="matrices-in-arbitrary-bases"}

The standard-basis formula combines three ingredients already encountered. An input basis gives coefficients, the map determines the images of its basis vectors, and an output basis supplies coordinates for those images. The same construction works for abstract finite-dimensional vector spaces.

Choose ordered bases $E=[e_1,\ldots,e_m]$ of $V$ and $F=[f_1,\ldots,f_n]$ of $W$, and let $L:V\to W$ be linear. The basis $E$ assigns each vector in $V$ a unique coordinate column in $\mathbb F^m$, and $F$ does the same for $W$ in $\mathbb F^n$. These coordinate descriptions allow the vectors themselves to be functions, polynomials, or other vector-space objects. No containment of $V$ or $W$ in a Euclidean space is assumed.

::::div{class="pending-review"}

The row notation for a basis represents a linear combination. For scalar columns $a\in\mathbb F^m$ and $b\in\mathbb F^n$, it means

$$
\begin{aligned}
    Ea&=e_1a^1+\cdots+e_ma^m,\\
    Fb&=f_1b^1+\cdots+f_nb^n.
  \end{aligned}
$$

Thus $Ea$ is a vector in $V$, and $Fb$ is a vector in $W$. The basis vectors themselves may be functions or polynomials.

Since $F$ is a basis of $W$, each image $L(e_j)$ has a unique expansion in its vectors. Writing these expansions separately gives

$$
\begin{aligned}
    L(e_1)&=f_1M^1_1+\cdots+f_nM^n_1,\\
      &\ \vdots\\
    L(e_m)&=f_1M^1_m+\cdots+f_nM^n_m.
  \end{aligned}
$$

Place the coefficients of $L(e_j)$ in column $j$ of a matrix,

$$
M=\begin{bmatrix}
    M^1_1&\cdots&M^1_m\\
    \vdots&&\vdots\\
    M^n_1&\cdots&M^n_m
  \end{bmatrix}\in\mathbb F^{n\times m}.
$$

Column $j$ belongs to input basis vector $e_j$, and row $i$ records its image’s coefficient in output direction $f_i$. The $j$-th column $M_j$ therefore satisfies

$$
\begin{aligned}
    FM_j&=\begin{bmatrix}f_1&\cdots&f_n\end{bmatrix}
      \begin{bmatrix}M^1_j\\\vdots\\M^n_j\end{bmatrix}\\
      &=f_1M^1_j+\cdots+f_nM^n_j=L(e_j).
  \end{aligned}
$$

This equality holds for every $j$. By column-by-column multiplication, $FM$ is consequently the row of vectors $\begin{bmatrix}L(e_1)&\cdots&L(e_m)\end{bmatrix}$. We denote this row by $L(E)$, meaning that $L$ is applied to each basis vector separately. Thus

:::div{id="eq:linear-algebra-i:basis-image-matrix" class="equation"}

$$
L(E)=FM.\tag{3.1}
$$

:::

The matrix is unique because each basis-image expansion is unique.

::::

The images $L(e_j)$ may be zero or linearly dependent, so they need not form a basis of $W$. The matrix records their coordinates in $F$ in every case. Their span and dependencies are studied through image, rank, and kernel in [Chapter 4](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#ch:linear-algebra-i:kernel-image-and-rank). [Example 4.3.2](/notes/linear-algebra/linear-algebra-i/kernel-image-and-rank/#ex:linear-algebra-i:full-rank-dependent-columns) shows how dependent images can still span the entire codomain.

:::div{class="pending-review"}

[Equation 3.1](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#eq:linear-algebra-i:basis-image-matrix) records what happens to the basis vectors. Linearity explains why the same matrix computes the image of every input. Let

$$
v=Ea=e_1a^1+\cdots+e_ma^m.
$$

Applying $L$ and substituting the basis-image expansions gives

$$
\begin{aligned}
    L(v)&=L(e_1a^1+\cdots+e_ma^m)\\
      &=L(e_1)a^1+\cdots+L(e_m)a^m\\
      &=(f_1M^1_1+\cdots+f_nM^n_1)a^1\\
      &\quad+\cdots+(f_1M^1_m+\cdots+f_nM^n_m)a^m.
  \end{aligned}
$$

Regrouping by the output basis vectors produces

$$
\begin{aligned}
    L(v)&=f_1(M^1_1a^1+\cdots+M^1_ma^m)\\
      &\quad+\cdots+f_n(M^n_1a^1+\cdots+M^n_ma^m).
  \end{aligned}
$$

The coefficient of $f_i$ is the $i$-th entry of $Ma$. Consequently,

$$
L(v)=L(Ea)=L(E)a=(FM)a=F(Ma).
$$

The input-coordinate column is $a$, the output-coordinate column is $Ma$, and the output vector itself is $F(Ma)$. These expressions distinguish the coordinates from the vectors they represent. The matrix $M$ converts the $E$-coordinates of the input into the $F$-coordinates of its image. For a zero-dimensional space, the corresponding basis and coordinate column are empty, and the formulas use empty sums.

:::

Both routes through [Figure 3.5](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#fig:linear-algebra-i:linear-map-coordinates) give the same output vector, since $L(Ea)=F(Ma)$.

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:linear-map-coordinates"}

[![Across the top, M acts on coordinates. Across the bottom, L acts on vectors. The vertical arrows reconstruct vectors in the bases E and F.](/notes/linear-algebra/figures/linear-map-coordinates.svg){.tikz-diagram}](/notes/linear-algebra/figures/linear-map-coordinates.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 3.5. Across the top, $M$ acts on coordinates. Across the bottom, $L$ acts on vectors. The vertical arrows reconstruct vectors in the bases $E$ and $F$.

:::

::::

:::::

In Einstein notation, repeated upper and lower indices are summed over their ranges. With this convention, the expressions above become

$$
L(e_j)=f_iM^i_j,\qquad v=e_ja^j,\qquad L(v)=f_iM^i_ja^j.
$$

The matrix depends on the map and on both ordered bases. The map $L$ specifies what happens to a vector. Its matrix specifies how to compute the corresponding output coordinates from the chosen input coordinates. Changing either basis changes the coordinate descriptions used in this calculation. The identity $L(E)=FM$ keeps these roles separate and makes their connection explicit.

### Composition {id="composition"}

Suppose $L_1:V_0\to V_1$ and $L_2:V_1\to V_2$ have matrices $M_1$ and $M_2$ in compatible ordered bases, so that

$$
L_1(E_0)=E_1M_1,\qquad L_2(E_1)=E_2M_2.
$$

Then

$$
\begin{aligned}
    (L_2\circ L_1)(E_0)
      &=L_2(L_1(E_0))\\
      &=L_2(E_1M_1)=L_2(E_1)M_1\\
      &=E_2(M_2M_1).
  \end{aligned}
$$

The matrix of the composite is $M_2M_1$, in that order. For $v=E_0a$, this gives $(L_2\circ L_1)(v)=E_2M_2M_1a$.

:::div{id="web:sections/linear-algebra-i/03-linear-equations-and-maps/03-change-of-basis-for-functions-and-maps:8179" class="result example"}

**Example 3.3.2.** Rotate the real plane through $90^\circ$ counterclockwise and then apply the shear $S(x,y)=(x+y,y)$. In standard coordinates, the rotation and shear have matrices

$$
R=\begin{bmatrix}0&-1\\1&0\end{bmatrix},
    \qquad S=\begin{bmatrix}1&1\\0&1\end{bmatrix}.
$$

The rotation acts first, so the combined action is

$$
S(Rv)=(SR)v,
    \qquad
    SR=\begin{bmatrix}1&-1\\1&0\end{bmatrix}.
$$

Indeed, $(x,y)^T$ first becomes $(-y,x)^T$, which the shear sends to $(x-y,x)^T$. [Figure 3.6](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#fig:linear-algebra-i:rotation-shear-grid) follows the basis arrows and the grid through these two stages. The columns of $SR$ record their final images, so the product contains the complete combined transformation.

:::

::::figure{id="fig:linear-algebra-i:rotation-shear-grid"}

[![A real-plane grid under a counterclockwise quarter-turn R, followed by the shear S. The grid in the middle still consists of squares, but its basis arrows have rotated. The final step vectors are the columns of SR. The rightmost factor acts first.](/notes/linear-algebra/figures/rotation-shear-grid.svg){.tikz-diagram}](/notes/linear-algebra/figures/rotation-shear-grid.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 3.6. A real-plane grid under a counterclockwise quarter-turn $R$, followed by the shear $S$. The grid in the middle still consists of squares, but its basis arrows have rotated. The final step vectors are the columns of $SR$. The rightmost factor acts first.

:::

::::

::statement{key="hw03:shift-map-powers"}

::statement{key="hw03:prescribed-nilpotence-index"}

### Invertible maps and inverse matrices {id="invertible-maps-and-inverse-matrices"}

:::div{id="web:sections/linear-algebra-i/03-linear-equations-and-maps/03-change-of-basis-for-functions-and-maps:9569" class="result definition"}

**Definition 3.3.5.** A linear map $L:V\to W$ is invertible if every $w\in W$ is the image of exactly one $v\in V$. Equivalently, it is both injective and surjective. Its inverse $L^{-1}:W\to V$ satisfies

$$
L^{-1}\circ L=I_V,\qquad L\circ L^{-1}=I_W.
$$

:::

::::div{class="pending-review"}

:::div{id="thm:linear-algebra-i:inverse-linearity" class="result proposition"}

**Proposition 3.3.6 (The inverse of a linear map).** The inverse of an invertible linear map $L:V\to W$ is linear. If $E$ is a basis of $V$, then $L(E)$ is a basis of $W$. In particular, finite-dimensional $V$ and $W$ have equal dimension.

:::

:::div{class="proof"}

*Proof.* Let $w_1,w_2\in W$ and $a,b\in\mathbb F$. Put $v_1=L^{-1}(w_1)$ and $v_2=L^{-1}(w_2)$. Linearity gives

$$
L(av_1+bv_2)=aL(v_1)+bL(v_2)=aw_1+bw_2.
$$

Applying $L^{-1}$ yields

$$
L^{-1}(aw_1+bw_2)=aL^{-1}(w_1)+bL^{-1}(w_2),
$$

proving that the inverse is linear.

To prove the basis assertion, every $w\in W$ is $L(v)$ for some $v\in V$. Expanding $v$ in $E$ and applying $L$ expresses $w$ as a finite linear combination of the vectors in $L(E)$. Thus $L(E)$ spans $W$. If distinct $e_1,\ldots,e_q\in E$ satisfy $\sum_{j=1}^q a_jL(e_j)=0$, then $L(\sum_{j=1}^q a_je_j)=0=L(0)$. Injectivity gives $\sum_{j=1}^q a_je_j=0$, and independence of $E$ forces every $a_j=0$. The images are independent and form a basis. Since injectivity also keeps distinct basis vectors distinct, the two bases have the same size, giving the dimension assertion. ◻

:::

::::

::statement{key="lec03:inverse-is-linear"}

Let $E$ and $F$ be bases of $V$ and $W$, and write

$$
L(E)=FM,\qquad L^{-1}(F)=EN.
$$

Using [Proposition 3.3.6](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#thm:linear-algebra-i:inverse-linearity) gives

$$
\begin{aligned}
    F&=L(L^{-1}(F))=L(EN)=L(E)N=FMN,\\
    E&=L^{-1}(L(E))=L^{-1}(FM)=L^{-1}(F)M=ENM.
  \end{aligned}
$$

Since $E$ and $F$ are bases, $MN=NM=I$, hence $N=M^{-1}$. The inverse map is represented by the inverse matrix.

::statement{key="hw02:inverse-uniqueness-and-products"}

::statement{key="hw02:one-sided-inverses"}

### Changing both bases {id="changing-both-bases"}

Let $E'=EA$ and $F'=FB$ be new ordered bases, with invertible change-of-basis matrices $A$ and $B$. If $L(E)=FM$, then

$$
\begin{aligned}
    L(E')&=L(EA)=L(E)A\\
      &=FMA=F'B^{-1}MA.
  \end{aligned}
$$

Therefore, the matrix $M'$ satisfying $L(E')=F'M'$ is

:::div{id="eq:linear-algebra-i:change-of-basis-for-maps" class="equation"}

$$
M'=B^{-1}MA.\tag{3.2}
$$

:::

[Figure 3.7](/notes/linear-algebra/linear-algebra-i/linear-equations-and-maps/#fig:linear-algebra-i:change-both-bases) tracks the conversions. Following either route gives $BM'a'=MAa'$, hence $M'=B^{-1}MA$.

:::::div{class="margin-figure"}

::::figure{id="fig:linear-algebra-i:change-both-bases"}

[![The top row uses the new bases E',F'. The bottom uses E,F. The downward arrows convert new coordinates to old ones.](/notes/linear-algebra/figures/change-both-bases.svg){.tikz-diagram}](/notes/linear-algebra/figures/change-both-bases.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure 3.7. The top row uses the new bases $E',F'$. The bottom uses $E,F$. The downward arrows convert new coordinates to old ones.

:::

::::

:::::
