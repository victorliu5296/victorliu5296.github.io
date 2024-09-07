---
title: 'Exact Taylor Projectile Motion'
date: 2024-09-07T09:24:44-04:00
math: katex
categories: [Physics]
tags: [Mathematics, Physics, Projectile Motion, Taylor Expansion, Vectors]
weight: 100
draft: true
---

I recently made a physics simulator with no air resistance where I model a body’s motion through a Taylor expansion based on its initial conditions:

\[
x(t) = x^{(0)} + t x^{(1)} + \frac{1}{2} t^2 x^{(2)} + \frac{1}{6} t^3 x^{(3)} + \cdots + \frac{t^k}{k!} x^{(k)}
\]

where \( x^{(k)} \) denotes the \( k \)-th position derivative vector at time 0.

The main focus of the project was ballistics, hence the name `web-ballistics-3d`. I have integrated logic for the following: all initial conditions of two objects are given except the direction of one projectile vector (for instance, I could have all the vectors \( x_{\text{target}}^{(k)} \) and all the vectors \( x_{\text{projectile}}^{(k)} \) except the direction of the initial velocity vector \( x_{\text{projectile}}^{(1)} \)).

What solution for the initial vector \( x_{\text{projectile}}^{(i)} \) ensures an intersection with the target at time \( t > 0\)? The solution is given by isolating the equation \( x_{\text{projectile}}(t) = x_{\text{target}}(t) \):

\[
x_{\text{projectile}}^{(i)} = x_{\text{target}}^{(i)} - \frac{i!}{t^i}\sum_{\substack{k=0 \\ k \neq i}}^{n} \frac{t^k}{k!} \left( x_{\text{target}}^{(k)} - x_{\text{projectile}}^{(k)} \right)
\]
where \( n \) is the order of the highest non-zero initial position derivative vector.

Similarly, if you are instead given only the magnitude of the unknown position derivative vector \( \| x_{\text{projectile}}^{(i)} \| \), how do you find all initial values of the vector that will guarantee an intersection with the target?

Taking the norm on both sides of our previously derived equation, we get:

\[
\|x_{\text{projectile}}^{(i)}\| = \left\| x_{\text{target}}^{(i)} - \frac{i!}{t^i}\sum_{\substack{k=0 \\ k \neq i}}^{n} \frac{t^k}{k!} \left( x_{\text{target}}^{(k)} - x_{\text{projectile}}^{(k)} \right) \right\|
\]

All values are known except the intersection time \( t \). Therefore, this is an equation in terms of \( t \), whose solutions give the intersection times. These can be used to find the desired initial values of the position derivative vector \( x_{\text{projectile}}^{(i)} \).

If we expand further, it is possible to convert this into a polynomial equation.

For the sake of practicality, let's introduce a new variable
\[
s^{(k)}:=
\begin{cases}
x_{\text{target}}^{(k)} - x_{\text{projectile}}^{(k)} & \text{if } k \neq i \\
x_{\text{target}}^{(i)} & \text{if } k = i
\end{cases}
\]

Then we can rewrite the equation as:

\[
\frac{t^i}{i!} \|x_{\text{projectile}}^{(i)}\| = \left\| \sum_{k=0}^{n} \frac{t^k}{k!} s^{(k)} \right\|
\]

Squaring both sides and converting the squared norm into a dot product, we get:

\[
\frac{t^{2i}}{(i!)^2} \|x_{\text{projectile}}^{(i)}\|^2 = \sum_{k=0}^{n} \sum_{l=0}^{n} \frac{t^{k+l}}{k!l!} \left( s^{(k)} \cdot s^{(l)} \right)
\]

This is a polynomial equation in terms of \( t \) and known \( s^{(k)} \). We can rewrite the double summation to group the terms of the same power:

Let \( m = k + l \). The double summation becomes:

\[
\sum_{m=0}^{2n} t^m \left( \sum_{\substack{k+l = m}} \frac{1}{k!l!} \left( s^{(k)} \cdot s^{(l)} \right) \right)
\]

Now the equation is:

\[
\frac{t^{2i}}{(i!)^2} \|x_{\text{projectile}}^{(i)}\|^2 = \sum_{m=0}^{2n} t^m \left( \sum_{\substack{k+l = m}} \frac{1}{k! l!} \left( s^{(k)} \cdot s^{(l)} \right) \right)
\]

In practice, we use a single index by solving for \( l \) as \( l = m - k \). This gives us:

\[
\frac{t^{2i}}{(i!)^2} \|x_{\text{projectile}}^{(i)}\|^2 = \sum_{m=0}^{2n} t^m \left( \sum_{k=0}^{m} \frac{1}{k! (m-k)!} \left( s^{(k)} \cdot s^{(m-k)} \right) \right)
\]

To find the intersection time(s) \( t \), we now have a polynomial equation in \( t \) of degree \( 2n \).

The general form of the polynomial is:

\[
a_{2n} t^{2n} + a_{2n-1} t^{2n-1} + \cdots + a_1 t + a_0 = 0
\]

Where each coefficient \( a_m \) corresponds to:

\[
a_m=
\begin{cases}
-\frac{\|x_{\text{projectile}}^{(i)}\|^2}{(i!)^2} + \sum_{k=0}^{i} \frac{1}{k!(i-k)!} \left( s^{(k)} \cdot s^{(i-k)} \right) & \text{if } m = i
\\
\sum_{k=0}^{m} \frac{1}{k!(m-k)!} \left( s^{(k)} \cdot s^{(m-k)} \right) & \text{if } m \neq i
\end{cases}
\]