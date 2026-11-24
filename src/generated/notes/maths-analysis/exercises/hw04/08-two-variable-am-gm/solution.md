:::div{class="proof"}

*Solution.* From the hint, we have

$$
(\sqrt a-\sqrt b)^2=a-2\sqrt{ab}+b.
$$

Since a square is nonnegative,

$$
\begin{aligned}
    (\sqrt a-\sqrt b)^2&\ge0,\\
    a-2\sqrt{ab}+b&\ge0,\\
    a+b&\ge2\sqrt{ab},\\
    \frac{a+b}{2}&\ge\sqrt{ab}.
  
\end{aligned}
$$

Each rearrangement is reversible. Thus

$$
\begin{aligned}
    \frac{a+b}{2}>\sqrt{ab}\quad
      &\Longleftrightarrow\quad
        (\sqrt a-\sqrt b)^2>0\\
      &\Longleftrightarrow\quad \sqrt a\ne\sqrt b\\
      &\Longleftrightarrow\quad a\ne b.
  
\end{aligned}
$$

Therefore the inequality is strict if and only if $a\ne b$. Equality holds exactly when $a=b$, including $a=b=0$. ◻

:::
