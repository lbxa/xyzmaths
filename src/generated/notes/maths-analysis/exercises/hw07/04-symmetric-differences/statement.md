---
key: "hw07:symmetric-differences"
source: "problems/hw07/04-symmetric-differences/problem"
title: "Exercise"
number: "6.5.4"
assignment: "hw07"
question: 4
statement-page: "analysis-i/differentiation-and-applications"
solution-page: "appendices/exercise-solutions"
---

Let $f(x)$ be differentiable twice such that $f''(x)$ is also continuous.

:::list

1.  **(i)** Prove that

    $$
    f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x-h)}{2h}.
    $$

2.  **(ii)** Prove that

    $$
    f''(x)=\lim_{h\to0}
              \frac{f(x+h)+f(x-h)-2f(x)}{h^2}.
    $$

:::

(These formulas are very useful in numerical analysis. Hint: Are the limits of $0/0$ type?)
