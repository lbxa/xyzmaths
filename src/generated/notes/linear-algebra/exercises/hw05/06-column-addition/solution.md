:::div{class="proof"}

*Solution.* Let $D$ be the determinant function on columns. Only column $j$ changes, and $c'_j=c_j+ac_k$. By linearity in the $j$-th input,

$$
\begin{aligned}
  \det M'
    &=D(c_1,\ldots,c_{j-1},c_j+ac_k,c_{j+1},\ldots,c_n)\\
    &=D(c_1,\ldots,c_n)\\
    &\quad+aD(c_1,\ldots,c_{j-1},c_k,c_{j+1},\ldots,c_n).
\end{aligned}
$$

Since $j\ne k$, the second determinant-function value contains $c_k$ in both positions $j$ and $k$. It vanishes because its inputs repeat. Hence $\det M'=D(c_1,\ldots,c_n)=\det M$. ◻

:::
