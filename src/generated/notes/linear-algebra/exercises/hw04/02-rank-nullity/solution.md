:::div{class="proof"}

*Solution.* **(a)** By the rank–nullity theorem,

$$
\operatorname{rank}L
        =\dim V-\dim\ker L=7-3=4.
$$

The map $L$ is not injective because $\operatorname{nullity}L=3\ne0$. It is not surjective because $\operatorname{rank}L=4<5=\dim W$.

**(b)** Suppose $T\colon\mathbb{R}^4\to\mathbb{R}^4$ is injective. Then $\operatorname{nullity}T=0$, and the rank–nullity theorem gives

$$
\operatorname{rank}T=4-0=4.
$$

This equals the dimension of the codomain, so $T$ is surjective. Since $T$ is linear, injective, and surjective, it is an isomorphism.

**(c)** Suppose $L\colon\mathbb{R}^6\to\mathbb{R}^4$ were injective. Its nullity would be zero, so the rank–nullity theorem would give

$$
\operatorname{rank}L=6.
$$

However, $\operatorname{im}L\subseteq\mathbb{R}^4$, so $\operatorname{rank}L\le4$. This is a contradiction. Thus no such linear map can be injective.

**(d)** Suppose $L\colon\mathbb{R}^3\to\mathbb{R}^5$ were surjective. Then $\operatorname{rank}L=5$, and rank–nullity would imply

$$
\operatorname{nullity}L
        =3-5=-2.
$$

Nullity is a dimension and is therefore nonnegative. This contradiction shows that no such linear map can be surjective. [^13] ◻

:::

:::notes{id="footnotes-12"}

[^13]: A negative value of nullity contradicts its meaning as the dimension of the kernel.

:::
