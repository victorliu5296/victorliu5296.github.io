---
title: 'Sequences in Triangles'
date: 2025-01-27T17:18:19-05:00
summary: "Some problems involving sequences in triangles"
math: katex
categories:
  - Competitive Math
  - Geometry
tags:
  - Triangle Geometry
  - Sequences
  - Arithmetic Sequence
  - Arithmetic Progression
  - Geometric Sequence
  - Geometric Progression
weight: 100
draft: false
---

Tricks to consider: since there are 3 values (sides or angles), it is often useful to write the sequence symmetrically, i.e. $a-d, a, a+d$ rather than $a,a+d,a+2d$. This helps with cancellation, and for angles, you avoid having double angles.

Notice that the sum of the angles is $180^\circ$ in a triangle. This implies that $(a-d)+a+(a+d)=3a=180^\circ$, so that $a=60^\circ$. Hence, the middle term for angles is always $60^\circ$, and you can write the sequence as $60^\circ-d, 60^\circ, 60^\circ+d$.

The largest side is opposite the largest angle and the smallest side is opposite the smallest angle.

---

#### 2013 AMC 12A Problems/Problem 12
The angles in a particular triangle are in arithmetic progression, and the side lengths are $4,5,x$. The sum of the possible values of $x$ equals $a+\sqrt{b}+\sqrt{c}$ where $a, b$, and $c$ are positive integers. What is $a+b+c$?

**Solution**:

Let the angles be $60^\circ-d, 60^\circ, 60^\circ+d$. We notice that we have one angle and have to relate all sides, so this is a [hint]({{< relref "blog/math-blog/competitive-math/strategies/math-patterns/geometry/Sine Law vs Cosine Law/index.md" >}}) to use the cosine law. Since the cosine law is symmetric in the two legs, we apply casework on $x$.

Cases on $x$:
1. $x$ is the hypotenuse.
2. $x$ is a leg.

Pre-computations:
$\cos 60^\circ = \frac{1}{2}$.

Case 1: $x$ is the hypotenuse.
$x^2 = 4^2 + 5^2 - 2\cdot4\cdot5\cdot\cos 60^\circ$
$x = \sqrt{21}$.

Case 2: $x$ is a leg.
$5^2 = 4^2 + x^2 - 2\cdot4\cdot x\cdot\cos 60^\circ$
$0 = x^2 - 4x - 9$
$13 = x^2-4x+4=(x-2)^2$
$x=2+\sqrt{13}$.

Hence the total sum is $2+\sqrt{13}+\sqrt{21}$, giving $2+13+21=\boxed{36}$.

---

#### 2023 AMC 12B Problems/Problem 17
Triangle $ABC$ has side lengths in arithmetic progression, and the smallest side has length $6$. If the triangle has an angle of $120^\circ$, what is the area of $ABC$?

Again, 3 sides and 1 angle, hinting toward cosine law. Let the sides be $6,6+d,6+2d$. By the cosine law with $\cos 120^\circ=-\frac{1}{2}$:

$$(6+2d)^2=6^2+(6+d)^2-2\cdot6\cdot(6+d)\cdot\cos 120^\circ$$

$$36+24d+4d^2=36+(36+12d+d^2)+(36+6d)$$

$$3d^2+6d-72=0$$

$$d^2+2d-24=0$$

$$(d+6)(d-4)=0$$

Hence $d=4$. Since $120^\circ \ge 90^\circ$, it must be opposite to the hypotenuse $6+2d$, so the angle is included between the legs. By the sine area formula, we have $\text{Area} = \frac{1}{2}6\cdot(6+4)\sin 120^\circ=30 \cdot \frac{\sqrt{3}}{2}=\boxed{15\sqrt{3}}$.

---

#### 2022 Euclid Problem 8(b)
Consider the following statement:

There is a triangle that is not equilateral whose side lengths form
a geometric sequence, and the measures of whose angles form an
arithmetic sequence.

Show that this statement is true by finding such a triangle or prove that it is false by demonstrating that there cannot be such a triangle.

**Solution**:

Some potential paths involve showing that if the triangle is not equilateral, then the triangle inequality is violated, or some sides are negative.

Let the angles be $60^\circ-d<60^\circ<60^\circ+d$.
Let the side lengths be $\frac{1}{a}<1<a$. (We can scale to a similar triangle.)

We have information about all sides and angles, and we want to relate them all. This is a hint to use the sine law.

$$\frac{1}{a\sin{60^\circ-d}}=\frac{1}{\sin{60^\circ}}=\frac{a}{\sin{60^\circ+d}}$$

We can isolate $a$ in the above equations to eliminate it:

$$a = \frac{\sin{60^\circ}}{\sin{60^\circ-d}}$$

and 

$$a=\frac{\sin{60^\circ+d}}{\sin{60^\circ}}$$

Equating the two:

$$\sin(60^\circ-d)\sin(60^\circ+d)=\sin^2{60^\circ}=\frac{3}{4}$$

Using the addition formulas:

$$\sin{60^\circ-d}=\sin{60^\circ}\cos{d}-\cos{60^\circ}\sin{d}$$

$$=\frac{\sqrt{3}}{2}\cos d - \frac{1}{2}\sin{d}$$

$$\sin{60^\circ+d}=\frac{\sqrt{3}}{2}\cos d + \frac{1}{2}\sin{d}$$

Hence:

$$\frac{3}{4}\cos^2 d - \frac{1}{4}\sin^2{d}=\frac{3}{4}$$

$$3\cos^2 d - \sin^2{d}=3$$

Substitute $\sin^2{d}=1-\cos^2{d}$:

$$3\cos^2 d - 1+\cos^2{d}=3$$

$$\cos^2{d} = 1$$

$$\cos{d} = \pm 1$$

The only solutions are multiples of $180^\circ$, so the only valid case in triangles would be $d=0^\circ$, but that means it is equilateral. Proof complete.