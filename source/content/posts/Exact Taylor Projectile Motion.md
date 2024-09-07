---
title: 'Exact Taylor Projectile Motion'
date: 2024-09-07T09:24:44-04:00
math: katex
categories: [Physics]
tags: [Mathematics, Physics, Projectile Motion, Taylor Expansion, Vectors]
weight: 100
draft: true
---

I recently built a physics simulator without air resistance, modeling a body’s motion through a Taylor expansion based on its initial conditions:

\[
x(t) = x^{(0)} + t x^{(1)} + \frac{1}{2} t^2 x^{(2)} + \frac{1}{6} t^3 x^{(3)} + \cdots + \frac{t^k}{k!} x^{(k)}
\]

where \( x^{(k)} \) represents the \( k \)-th derivative of the position vector at time \( t = 0 \).

The project mainly focuses on ballistics, hence the name `web-ballistics-3d`. It allows the calculation of the unknown direction of one projectile’s initial derivative vector (for example, velocity, acceleration, or higher-order derivatives) when all other initial conditions are provided for two objects.

Here, I will discuss some problems that arise when trying to control the motion of a projectile to intersect a target (assuming they are both points for simplicity).

## Problems
### 1. Known Intersection Time, 1 Unknown Initial Vector

Given all initial conditions for two objects except the direction of one projectile vector, how do we find the unknown initial vector \( x_{\text{projectile}}^{(1)} \) so that the projectile intersects the target at a future time \( t > 0 \)?

The solution is derived by isolating the equation \( x_{\text{projectile}}(t) = x_{\text{target}}(t) \). This assumes the objects are not already on the same trajectory throughout.

\[
x_{\text{projectile}}^{(i)} = x_{\text{target}}^{(i)} - \frac{i!}{t^i}\sum_{\substack{k=0 \\ k \neq i}}^{n} \frac{t^k}{k!} \left( x_{\text{target}}^{(k)} - x_{\text{projectile}}^{(k)} \right)
\]

where \( n \) is the highest order of non-zero derivatives.

### 2. Undetermined Intersection Time, Known Initial Vector Magnitude

Now, suppose only the magnitude \( \| x_{\text{projectile}}^{(i)} \| \) is known. How do we find the initial vector’s direction to guarantee intersection at a future time \( t > 0 \)?

Taking the norm of both sides of the earlier equation:

\[
\left\| x_{\text{projectile}}^{(i)} \right\| = \left\| x_{\text{target}}^{(i)} - \frac{i!}{t^i}\sum_{\substack{k=0 \\ k \neq i}}^{n} \frac{t^k}{k!} \left( x_{\text{target}}^{(k)} - x_{\text{projectile}}^{(k)} \right) \right\|
\]

This results in an equation for \( t \), whose solutions correspond to intersection times. These times allow us to compute the desired vector \( x_{\text{projectile}}^{(i)} \).

#### Converting to a Polynomial Equation

To simplify, we define a new variable:

\[
s^{(k)}:=
\begin{cases}
x_{\text{target}}^{(k)} - x_{\text{projectile}}^{(k)} & \text{if } k \neq i \\
x_{\text{target}}^{(i)} & \text{if } k = i
\end{cases}
\]

The equation becomes:

\[
\frac{t^i}{i!} \left\| x_{\text{projectile}}^{(i)} \right\| = \left\| \sum_{k=0}^{n} \frac{t^k}{k!} s^{(k)} \right\|
\]

Squaring both sides and converting the norm into a dot product, we obtain:

\[
\frac{t^{2i}}{(i!)^2} \left\| x_{\text{projectile}}^{(i)} \right\|^2 = \sum_{k=0}^{n} \sum_{l=0}^{n} \frac{t^{k+l}}{k!l!} \left( s^{(k)} \cdot s^{(l)} \right)
\]

Rewriting this as a polynomial in \( t \):

\[
\sum_{m=0}^{2n} t^m \left( \sum_{k=0}^{m} \frac{1}{k!(m-k)!} \left( s^{(k)} \cdot s^{(m-k)} \right) \right)
\]

#### Solving the Polynomial

The equation is now a polynomial in \( t \) of degree \( 2n \):

\[
a_{2n} t^{2n} + a_{2n-1} t^{2n-1} + \cdots + a_1 t + a_0 = 0
\]

The coefficients \( a_m \) are given by:

\[
a_m=
\begin{cases}
-\left( \frac{\left\| x_{\text{projectile}}^{(i)} \right\|}{i!} \right)^2 + \sum_{k=0}^{i} \frac{1}{k!(i-k)!} \left( s^{(k)} \cdot s^{(i-k)} \right) & \text{if } m = 2i \\
\sum_{k=0}^{m} \frac{1}{k!(m-k)!} \left( s^{(k)} \cdot s^{(m-k)} \right) & \text{if } m \neq 2i
\end{cases}
\]

To solve for \( t \), standard polynomial real root-finding methods like bisection (e.g. Vincent-Collins-Akritas) or continued fractions (e.g. Vincent-Akritas-Strzebonski) can be used. Once the roots are found, we can compute \( x_{\text{projectile}}^{(i)} \) for each intersection time \( t \).

Please note that there are not always real roots and therefore possible intersections given the initial conditions. For instance, this could happen if the target is moving away in the same direction as the projectile at a greater or equal rate than the projectile at any given time. In this case, the solution is undefined.

### 3. Minimizing the Magnitude of the Initial Vector

A somewhat more challenging task arises when we seek to minimize the magnitude \( \| x_{\text{projectile}}^{(i)} \| \) under the given initial conditions. Under what conditions does such a minimum exist, and how do we calculate it?

We need to analyze the problem using calculus. We wish to minimize the function:

\[
\left\| x_{\text{projectile}}^{(i)} \right\|(t) := \frac{i!}{t^i} \left\| \sum_{k=0}^{n} \frac{t^k}{k!} s^{(k)} \right\| 
\]

The norm is convex and nonnegative, and squaring preserves convexity. Also, scaling by a nonnegative constant does not affecth the minimum either, so we'll drop the $(i!)^2$. Therefore, we minimize the following rational function, which is more specifically a Laurent polynomial in \( t \):

\[
\begin{aligned}
 L(t) :=& \frac{1}{t^{2i}} \left\| \sum_{k=0}^{n} \frac{t^k}{k!} s^{(k)} \right\|^2 \\
 \\
 =&\sum_{m=0}^{2n} c_m t^{m-2i}
\end{aligned}
\]

where \( c_m \) is a constant for each \( m \) derived similarly in the previous section:

\[
c_m := \sum_{k=0}^{m} \frac{1}{k!(m-k)!} \left( s^{(k)} \cdot s^{(m-k)} \right)
\]

It is now easier to use calculus to find the minimum. A Laurent polynomial is nicer to work with because it is easier to differentiate. During the coding process, we can separate in 3 cases: the power of \( t \) being negative, zero, or positive.

Now, the tricky thing about this problem is that the behavior of the function is not nearly as nice compared to the other cases. We can have discontinuities, and even poles shooting off to infinity in either direction. These cases must be taken into account. 

Nevertheless, we push on and differentiate \( L(t) \) with respect to \( t \) and set it equal to zero to find critical points.

\[

\]