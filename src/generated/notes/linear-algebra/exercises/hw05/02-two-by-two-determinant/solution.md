:::div{class="proof"}

*Solution.* Let $(e_1,e_2)$ be the standard ordered basis of $\mathbb{R}^2$. The column vectors of the matrix are

$$
v=ae_1+be_2,\qquad w=ce_1+de_2.
$$

Geometrically, $v$ and $w$ span the parallelogram

$$
P(v,w)=\{sv+tw\mid 0\le s,t\le1\}.
$$

Let $A$ be the oriented area function, normalized by $A(e_1,e_2)=1$. It is antisymmetric and bilinear. By uniqueness of the normalized antisymmetric bilinear function, the determinant on columns satisfies

$$
\det\begin{bmatrix}a&c\\b&d\end{bmatrix}=A(v,w).
$$

Thus the determinant is the signed area of this parallelogram, while its ordinary area is $|A(v,w)|$.

Bilinearity gives

$$
\begin{aligned}
  A(v,w)
    &=A(ae_1+be_2,ce_1+de_2)\\
    &=acA(e_1,e_1)+adA(e_1,e_2)\\
    &\quad+bcA(e_2,e_1)+bdA(e_2,e_2)\\
    &=adA(e_1,e_2)+bcA(e_2,e_1)\\
    &=(ad-bc)A(e_1,e_2)\\
    &=ad-bc.
\end{aligned}
$$

The terms with repeated basis vectors vanish because $A(e_1,e_1)=A(e_2,e_2)=0$. Antisymmetry gives $A(e_2,e_1)=-A(e_1,e_2)$, and the normalization gives the final equality. Consequently, the determinant is $ad-bc$. ◻

:::
