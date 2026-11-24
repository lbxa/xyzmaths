---
title: "Disc Game Prize Fund"
description: "Compute the maximum fair prize fund for a 15-turn disc game using probability DP."
date: "2026-07-08"
source: "https://projecteuler.net/problem=121"
sourceLabel: "Project Euler 121"
topic: "Dynamic Programming / Probability"
difficulty: 5
estimatedTime: 35
statement: |
  A player stakes £1 on 15 draws from a bag. The bag starts with two discs, one
  of each colour, red and blue. On each turn the player chooses a disc
  uniformly at random, records its colour, returns it to the bag, and adds
  one more red disc.

  The player wins if blue appears strictly more often than red. A winner
  receives a whole-number prize in pounds that includes the original £1
  stake. A losing player receives nothing. How large can the prize be if
  the banker must avoid an expected loss?
solution: |
  **The maximum prize is £2,269**, including the player's £1 stake.

  The player needs at least eight blue draws to win. On turn $i$ the bag
  holds one blue disc and $i$ red discs,
  whatever was drawn earlier. Encode the red choices by $i$ and the blue
  choice by $x$. In the product

  $$
  P(x)=(1+x)(2+x)\cdots(15+x),
  $$

  each choice of $x$ records one blue. The coefficient of $x^k$ counts
  the draw sequences with $k$ blues, with the individual red discs counted
  separately. The program below builds the coefficients one factor at a
  time. Multiplying by $i+x$ gives the new coefficient of $x^k$ as $i$
  times its old coefficient plus the old coefficient of $x^{k-1}$, taking
  missing coefficients as zero. There are $2\cdot3\cdots16=16!$ equally
  likely sequences. Adding the coefficients from $x^8$ through $x^{15}$
  and dividing by $16!$ gives the winning probability

  $$
  p=\frac{9\,219\,406\,943}{20\,922\,789\,888\,000}.
  $$

  The banker collects £1 and pays $F$ pounds with probability $p$, so the
  prize must satisfy $F\leq 1/p$. Dividing the denominator of $p$ by its
  numerator gives a quotient of 2269 and a remainder of 3,955,534,333.
  Paying £2,270 would cost more than £1 per play on average.
---

## The prize and the probability of winning

The banker collects £1 on every play and pays the prize only on a win. If
the prize is $F$ pounds and the probability of winning is $p$, the expected
payout is $pF$ pounds. The banker's expected profit is therefore $1-pF$.
Requiring $1-pF\geq 0$ gives the largest whole-pound prize

$$
F_{\max}=\left\lfloor\frac{1}{p}\right\rfloor.
$$

In $n$ draws, a player who sees blue $k$ times sees red $n-k$ times.
Winning requires $k>n-k$, so for 15 turns we need the probability of
drawing at least eight blues.

## Count the blues after each turn

Returning the disc makes the bag on the next turn predictable. Whatever the
previous colours were, on turn $i$ the bag holds one blue disc and $i$ red
discs. To decide whether the player has won, the only part of the history
we need to keep is the number of blues drawn so far.

Let $A_i(k)$ be the probability of exactly $k$ blues after $i$ turns.
A red disc on the last turn leaves the count at $k$, so it contributes
$A_{i-1}(k)\,i/(i+1)$. A blue disc brings the count up from $k-1$ and
contributes $A_{i-1}(k-1)/(i+1)$. Every history ending with $k$ blues
falls into exactly one of these cases. Adding them gives

$$
A_i(k)=\frac{i A_{i-1}(k)+A_{i-1}(k-1)}{i+1}.
$$

Initially $A_0(0)=1$. A count outside $0\leq k\leq i$ has probability
zero, which also covers the boundary cases of the recurrence.

To take the floor of $1/p$ exactly, keep the numerators as integers. Every
history through turn $i$ has the same denominator
$D_i=2\cdot3\cdots(i+1)=(i+1)!$, with $D_0=1$. Set
$W_i(k)=D_iA_i(k)$. Since $D_i=(i+1)D_{i-1}$, the recurrence becomes

$$
W_i(k)=iW_{i-1}(k)+W_{i-1}(k-1),\qquad W_0(0)=1.
$$

## Four turns by hand

With four draws the player needs at least three blues. Four blues have
weight $1$. If there is exactly one red, its turn determines the weight,
since red on turn $j$ contributes a factor of $j$ and every blue contributes
a factor of $1$. The winning weight is therefore $1+(1+2+3+4)=11$.
The denominator is $5!=120$, so the maximum prize is
$\lfloor 120/11\rfloor=10$ pounds. A winner keeps £9 after accounting for
the stake.

For 15 turns the recurrence gives $\sum_{k=8}^{15}W_{15}(k)=9\,219\,406\,943$.
The denominator is $16!=20\,922\,789\,888\,000$, so the largest prize is
**£2,269**.

## Time and space

The table has one row per turn and one column per possible blue count.
Filling it takes $O(n^2)$ arithmetic operations and $O(n^2)$ storage for
$n$ turns. Through turn 15 every row sums to at most $16!$, so all the
weights and the final denominator fit in an `unsigned long long`.
