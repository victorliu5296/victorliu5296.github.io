---
title: 'Chapter 1'
date: 2025-02-28T23:26:59-05:00
summary: "Notes on the preface of the book Solving Mathematical Problems by Terence Tao."
math: katex
categories:
  - Competitive Math
tags:
  - Problems
  - Solving Mathematical Problems
  - Terence Tao
weight: 100
draft: false
---

### Problem

Show that the perpendicular bisectors of a triangle are concurrent.

#### Solution 1. Vectors

Let $\vec A$, $\vec B$, $\vec C$ be the vertices of the triangle.

A point $\vec{x}$ lies on the perpendicular bisector of $\vec{AB}$ if and only if it satisfies:

$$\|\vec{x}-\vec{A}\|=\|\vec{x}-\vec{B}\|$$

In other words, the intersection point $\vec{x}$ of the perpendicular bisector of $\vec{AB}$ with that of $\vec{BC}$ must satisfy:

$$\|\vec{x}-\vec{A}\|=\|\vec{x}-\vec{B}\|=\|\vec{x}-\vec{C}\|$$

Clearly, it then lies on the perpendicular bisector of $\vec{CA}$. $\blacksquare$

Incidentally, this neat proof generalizes to $\mathbb{R}^n$. If you have $n+1$ affinely independent points (i.e. they do not lie in a $n-1$-dimensional subspace), then the perpendicular bisectors are $n-1$-dimensional hyperplanes, and the intersection is the circumcenter of the points.

#### Solution 2. Cartesian Coordinate Bash

Let $A(a_1, a_2)$, $B(b_1, b_2)$, $C(c_1, c_2)$ be the vertices of the triangle. Then the midpoints are $M_{AB}(\frac{a_1+b_1}{2}, \frac{a_2+b_2}{2})$, $M_{BC}(\frac{c_1+b_1}{2}, \frac{c_2+b_2}{2})$, $M_{AC}(\frac{c_1+a_1}{2}, \frac{c_2+a_2}{2})$.

The slope of the lines are $m_{AB}=\frac{a_2-b_2}{a_1-b_1}$, $m_{BC}=\frac{c_2-b_2}{c_1-b_1}$, $m_{AC}=\frac{c_2-a_2}{c_1-a_1}$. Let the slops of the perpendicular bisectors be $L_{AB}=\frac{-1}{m_{AB}}=\frac{b_1-a_1}{a_2-b_2}$, $L_{BC}=\frac{b_1-c_1}{c_2-b_2}$, $L_{AC}=\frac{a_1-c_1}{c_2-a_2}$.

Then, the equations of the perpendicular bisectors are:

$$
\begin{cases}
\begin{aligned}
y-\frac{a_2+b_2}{2}&=\frac{b_1-a_1}{a_2-b_2} \cdot \left(x-\frac{a_1+b_1}{2} \right) \\
y-\frac{c_2+b_2}{2}&=\frac{b_1-c_1}{c_2-b_2} \cdot \left(x-\frac{c_1+b_1}{2} \right) \\
y-\frac{c_2+a_2}{2}&=\frac{a_1-c_1}{c_2-a_2} \cdot \left(x-\frac{c_1+a_1}{2} \right)
\end{aligned}
\end{cases}
$$

Never mind, I give up. Maybe you can use a computer algebra system to solve this and check that it's consistent.

