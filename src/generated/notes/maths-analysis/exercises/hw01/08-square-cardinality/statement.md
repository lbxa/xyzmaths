---
key: "hw01:square-cardinality"
source: "problems/hw01/08-square-cardinality/problem"
title: "Exercise"
number: "1.3.10"
assignment: "hw01"
question: 8
statement-page: "analysis-i/sets-and-foundations"
solution-page: "appendices/exercise-solutions"
---

Show that

$$
|(0,1)\times(0,1)|=|(0,1)|=\aleph.
$$

(*Corrected hint.* For each number in $(0,1)$, choose the decimal expansion that is not eventually all $9$s. We can then write

$$
x\in(0,1),\quad x=0.x_1x_2\cdots,\quad
    x_i\in\{0,\ldots,9\},\quad i=1,2,\ldots.
$$

Then define a map from $(0,1)\times(0,1)$ to $(0,1)$ by

$$
(x,y)=(0.x_1x_2\cdots,0.y_1y_2\cdots)
    \mapsto (0.x_1y_1x_2y_2\ldots)=z\in(0,1).
$$

Show that this map is injective, then use injections in both directions.)
