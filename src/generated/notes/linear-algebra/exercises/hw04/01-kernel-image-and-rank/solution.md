:::div{class="proof"}

*Solution.* **(a)** The kernel consists of the solutions of $Ax=0$. Subtracting the first row from the third, and then the second row from the third, gives

$$
A\sim
      \begin{pmatrix}
        1&2&0&1\\
        0&1&1&1\\
        0&0&0&0
      \end{pmatrix}.
$$

Thus the equations are

$$
x_1+2x_2+x_4=0,
      \qquad
      x_2+x_3+x_4=0.
$$

Taking $x_3$ and $x_4$ as free variables, we obtain $x_2=-x_3-x_4$ and $x_1=2x_3+x_4$. Consequently,

$$
x=
      x_3\begin{pmatrix}2\\-1\\1\\0\end{pmatrix}
      +x_4\begin{pmatrix}1\\-1\\0\\1\end{pmatrix},
$$

and

$$
\ker T=
      \operatorname{span}\left\{
        \begin{pmatrix}2\\-1\\1\\0\end{pmatrix},
        \begin{pmatrix}1\\-1\\0\\1\end{pmatrix}
      \right\}.
$$

These two vectors span the kernel. The third and fourth coordinates of a linear combination are its two coefficients, so a combination equal to zero forces both coefficients to be zero. Hence the vectors are linearly independent and form a basis of $\ker T$.

**(b)** Let $c_1,c_2,c_3,c_4$ denote the columns of $A$. They satisfy

$$
c_2=2c_1+c_3,
      \qquad
      c_4=c_2-c_1=c_1+c_3.
$$

For every $x\in\mathbb{R}^4$,

$$
\begin{aligned}
      Ax
        &=x_1c_1+x_2c_2+x_3c_3+x_4c_4\\
        &=(x_1+2x_2+x_4)c_1+(x_2+x_3+x_4)c_3.
    
\end{aligned}
$$

Therefore $\operatorname{im}T\subseteq
    \operatorname{span}\{c_1,c_3\}$.

Conversely, if $y=ac_1+bc_3$, choose $x=(a,0,b,0)^T$. Then $Ax=y$, so $\operatorname{span}\{c_1,c_3\}\subseteq\operatorname{im}T$. We conclude that

$$
\operatorname{im}T=
      \operatorname{span}\left\{
        \begin{pmatrix}1\\0\\1\end{pmatrix},
        \begin{pmatrix}0\\1\\1\end{pmatrix}
      \right\}.
$$

To check linear independence, suppose $ac_1+bc_3=0$. Then

$$
a\begin{pmatrix}1\\0\\1\end{pmatrix}
      +b\begin{pmatrix}0\\1\\1\end{pmatrix}
      =\begin{pmatrix}a\\b\\a+b\end{pmatrix}=0,
$$

which gives $a=b=0$. Thus $(c_1,c_3)$ is a basis of $\operatorname{im}T$. [^12]

**(c)** Both bases have two vectors, so

$$
\operatorname{nullity}T=2,
      \qquad
      \operatorname{rank}T=2.
$$

The rank–nullity identity is verified by

$$
\operatorname{rank}T+\operatorname{nullity}T
        =2+2=4=\dim\mathbb{R}^4.
$$

**(d)** The map $T$ is not injective, since its nullity is $2$. It is not surjective, since $\operatorname{rank}T=2<3=\dim\mathbb{R}^3$. ◻

:::

:::notes{id="footnotes-11"}

[^12]: To identify a span with the image, prove both inclusions. Then check linear independence to obtain a basis.

:::
