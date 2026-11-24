---
title: "Solutions to exercises"
group: "Appendices"
order: 18
page: "127"
outline: [{"id": "vector-spaces-and-bases", "title": "Vector spaces and bases", "level": 2}, {"id": "matrices-and-vector-coordinates", "title": "Matrices and vector coordinates", "level": 2}, {"id": "linear-equations-and-maps", "title": "Linear equations and maps", "level": 2}, {"id": "kernel-image-and-rank", "title": "Kernel, image, and rank", "level": 2}, {"id": "multilinear-algebra-and-determinants", "title": "Multilinear algebra and determinants", "level": 2}, {"id": "eigenvalues-and-diagonalization", "title": "Eigenvalues and diagonalization", "level": 2}, {"id": "inner-products-and-norms", "title": "Inner products and norms", "level": 2}]
---

# Appendix C. Solutions to exercises {id="ch:appendix:exercise-solutions"}

The exercises are restated in main-text order. Each exercise number links back to its original statement.

## Vector spaces and bases {id="vector-spaces-and-bases"}

::solution{key="hw01:axiom-consequences"}

::solution{key="hw01:positive-real-vector-space"}

::solution{key="hw01:span-and-containing-subspaces"}

::solution{key="hw01:parameter-dependent-span"}

::solution{key="hw01:affine-solution-set"}

::solution{key="hw01:polynomial-interpolation"}

::solution{key="hw01:recursive-sequences"}

::solution{key="hw01:intersections-and-sums"}

::solution{key="hw01:basis-extension"}

::solution{key="hw01:span-and-independence-assertions"}

::solution{key="hw03:modified-bases-and-dependence"}

::solution{key="hw03:continuous-functions-infinite-dimension"}

## Matrices and vector coordinates {id="matrices-and-vector-coordinates"}

::solution{key="hw02:matrix-product-entries"}

::solution{key="hw02:matrix-product-associativity"}

::solution{key="hw02:block-shear-inverses"}

::solution{key="hw02:characterizing-the-identity"}

::solution{key="hw02:matrix-commutation"}

::solution{key="hw02:zero-products"}

::solution{key="hw02:upper-triangular-subspace"}

::solution{key="hw02:two-by-two-matrix-identities"}

## Linear equations and maps {id="linear-equations-and-maps"}

::solution{key="hw02:inconsistent-system"}

::solution{key="hw02:matrix-product-bilinearity"}

::solution{key="hw03:shift-map-powers"}

::solution{key="hw03:prescribed-nilpotence-index"}

::solution{key="lec03:inverse-is-linear"}

::solution{key="hw02:inverse-uniqueness-and-products"}

::solution{key="hw02:one-sided-inverses"}

## Kernel, image, and rank {id="kernel-image-and-rank"}

::solution{key="hw04:kernel-image-and-rank"}

::solution{key="hw04:rank-nullity"}

::solution{key="hw04:prescribed-kernel-and-image"}

::solution{key="hw04:adapted-bases"}

::solution{key="hw03:kernel-image-and-adapted-bases"}

::solution{key="hw03:polynomial-differentiation-powers"}

::solution{key="hw04:polynomial-differentiation"}

## Multilinear algebra and determinants {id="multilinear-algebra-and-determinants"}

Let $M$ be an $n\times n$ matrix with columns $c_1,\ldots,c_n$, and let $D$ be the normalized determinant function from [§ 5.4](/notes/linear-algebra/linear-algebra-i/determinants/#sec:linear-algebra-i:determinant). The following column expansion is used in [Exercise 5.4.5](/notes/linear-algebra/linear-algebra-i/determinants/#ex:hw05:four-by-four-determinant). Each column of $M$ can be written in terms of the standard basis,

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

::solution{key="hw05:bilinear-antisymmetry"}

::solution{key="hw05:two-by-two-determinant"}

::solution{key="hw05:three-by-three-triangular-determinant"}

::solution{key="hw05:upper-triangular-determinant"}

::solution{key="hw05:four-by-four-determinant"}

::solution{key="hw05:negating-a-matrix"}

::solution{key="hw05:column-addition"}

::solution{key="hw05:permutation-matrices"}

## Eigenvalues and diagonalization {id="eigenvalues-and-diagonalization"}

::solution{key="hw06:sums-of-eigenvectors"}

::solution{key="hw06:triangular-matrix-eigenvectors"}

::solution{key="hw06:eigenvectors-in-a-basis"}

::solution{key="hw06:rotation-eigenvalues"}

::solution{key="hw06:eigenvalue-true-or-false"}

::solution{key="hw06:nilpotent-eigenvalues"}

::solution{key="hw07:disjoint-subspaces-independence"}

## Inner products and norms {id="inner-products-and-norms"}

::solution{key="hw07:coordinate-inner-products"}

::solution{key="hw07:tensor-inner-products"}

::solution{key="hw07:minimization-and-cauchy-schwarz"}

::solution{key="lec08:pythagorean-theorem"}
