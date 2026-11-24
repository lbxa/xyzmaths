::::::div{class="proof"}

*Solution.* Write $x=(x-y)+y$. The triangle inequality gives

$$
|x|\leq|x-y|+|y|,
$$

and therefore $|x|-|y|\leq|x-y|$. Interchanging $x$ and $y$ gives $|y|-|x|\leq|y-x|=|x-y|$. Combining the two inequalities, we obtain

$$
-|x-y|\leq|x|-|y|\leq|x-y|.
$$

This is exactly

$$
\bigl||x|-|y|\bigr|\leq|x-y|.
$$

For equality, first suppose $xy\geq0$. If both numbers are nonnegative, then

$$
\bigl||x|-|y|\bigr|=|x-y|.
$$

If both are nonpositive, then $|x|=-x$ and $|y|=-y$, so

$$
\bigl||x|-|y|\bigr|=|-x+y|=|x-y|.
$$

These cases also include either number being zero.

If $xy<0$, the numbers have opposite signs and neither is zero. Then $|x-y|=|x|+|y|$. Since both $|x|$ and $|y|$ are positive,

$$
\bigl||x|-|y|\bigr|<|x|+|y|=|x-y|.
$$

Thus equality holds exactly when $xy\geq0$. Taking absolute values can be pictured as folding the number line at zero. Points on the same side keep their separation, while points on opposite sides move closer together. [Figure C.13](/notes/maths-analysis/appendices/exercise-solutions/#fig:hw03:reverse-triangle-distance) illustrates this folding.

:::::div{class="margin-figure"}

::::figure{id="fig:hw03:reverse-triangle-distance"}

[![Schematic folding by t\\mapsto\|t\|. Both rows use the same scale. Here y\<0\<x\<\|y\|, and the gap shrinks from \|x-y\| to \\bigl\|\|x\|-\|y\|\\bigr\|. Points on the same half-line keep their separation.](/notes/maths-analysis/figures/reverse-triangle-distance.svg){.tikz-diagram}](/notes/maths-analysis/figures/reverse-triangle-distance.svg "Open original SVG"){.diagram-link data-astro-reload=""}

:::figcaption

Figure C.13. Schematic folding by $t\mapsto|t|$. Both rows use the same scale. Here $y<0<x<|y|$, and the gap shrinks from $|x-y|$ to $\bigl||x|-|y|\bigr|$. Points on the same half-line keep their separation.

:::

::::

:::::

 ◻

::::::
