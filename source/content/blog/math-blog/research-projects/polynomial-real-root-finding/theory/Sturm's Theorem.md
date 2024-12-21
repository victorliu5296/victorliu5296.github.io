---
title: 'Sturm''s theorem for counting real roots of polynomials'
date: 2024-12-20T23:25:42-05:00
math: katex
description: "Finding real roots of univariate polynomials"
categories:
  - Research Projects
  - Polynomial Real Root-Finding
tags:
  - Sturm's Theorem
weight: 100
draft: false
---

Sturm's theorem was a significant breakthrough in early development of numerical methods for finding real roots of polynomials. Introduced in 1829 by Jacques Sturm, it provided the first robust, systematic algorithm to determine the number and location of distinct real roots of a polynomial within a given interval.

While modern, more efficient methods using [Descartes' rule of signs](./Descartes'%20Rule%20of%20Signs.md) have been developed, Sturm's theorem remains useful in algorithms such as the [b2studios algorithm](../algorithms/b2studios%20algorithm.md) for polynomials with only real distinct roots.

### Sturm's Theorem

Sturm's Theorem provides a method to determine the number of distinct real roots of a polynomial within a given interval.

#### Key Concepts

1. **Sturm Sequence**: 
   A Sturm sequence for a polynomial \( P(x) \) is a sequence of polynomials:
   \[
   P_0(x), P_1(x), P_2(x), \dots, P_n(x)
   \]
   where:
   - \( P_0(x) = P(x) \)
   - \( P_1(x) = P'(x) \) (the derivative of \( P(x) \))
   - For \( i \geq 2 \), \( P_i(x) \) is the negative remainder when \( P_{i-2}(x) \) is divided by \( P_{i-1}(x) \), ensuring the degrees of subsequent polynomials decrease until a constant or zero is reached.

2. **Sign Changes**:
   At any point \( x = c \), count the number of sign changes in the sequence \( P_0(c), P_1(c), P_2(c), \dots, P_n(c) \). Ignore zero values in determining sign changes.

3. **Root Count**:
   Let \( V(a) \) and \( V(b) \) represent the number of sign changes in the Sturm sequence evaluated at \( x = a \) and \( x = b \), respectively. The number of distinct real roots of \( P(x) \) in the interval \( (a, b) \) is:
   \[
   V(a) - V(b)
   \]

#### Properties and Applications
- **Isolation of Roots**: Sturm's theorem isolates distinct real roots by ensuring no double-counting or inclusion of complex roots.
- **Exact Count**: It precisely counts distinct real roots, even for polynomials with high multiplicities.
- **Robust**: The method handles edge cases like roots at boundaries or sign changes at infinity.

### Worked Example: Sturm's Theorem

We will use **Sturm's theorem** to determine the number of real roots of the polynomial:

\[
P(x) = x^3 - 3x + 1
\]

in the interval \((-2, 2)\).

---

### Step 1: Construct the Sturm Sequence

1. **First Polynomial (\(P_0(x)\))**:  
   \[
   P_0(x) = x^3 - 3x + 1
   \]

2. **Derivative (\(P_1(x)\))**:  
   \[
   P_1(x) = \frac{d}{dx}(x^3 - 3x + 1) = 3x^2 - 3
   \]

3. **Compute the Remainders**:
   - Divide \(P_0(x)\) by \(P_1(x)\):
     \[
     P_0(x) \div P_1(x) = \frac{x^3 - 3x + 1}{3x^2 - 3}
     \]
     The quotient is \(\frac{1}{3}x\), and the remainder is:
     \[
     R_1(x) = -\left(\frac{2x - 1}{3}\right)
     \]
     We can drop positive constant factors since they don't affect the sign. Therefore, negating and dropping \( \frac{1}{3} \), the next polynomial in the sequence is:
     \[
     P_2(x) = 2x - 1
     \]

   - Divide \(P_1(x)\) by \(P_2(x)\):
     \[
     P_1(x) \div P_2(x) = \frac{3x^2 - 3}{2x - 1}
     \]
     The quotient is \(1.5x + 1.5\), and the remainder is:
     \[
     R_2(x) = -\frac{9}{4}
     \]
     The next polynomial is:
     \[
     P_3(x) = \frac{9}{4}
     \]

   The sequence terminates here because the remainder becomes a constant.

   **Final Sturm Sequence**:
   \[
   P_0(x) = x^3 - 3x + 1, \quad P_1(x) = 3x^2 - 3, \quad P_2(x) = 2x - 1, \quad P_3(x) = \frac{9}{4}
   \]

---

### Step 2: Evaluate the Sequence at Interval Endpoints

1. **At \(x = -2\)**:
   - \(P_0(-2) = (-2)^3 - 3(-2) + 1 = -8 + 6 + 1 = -1 \quad (\text{negative})\)
   - \(P_1(-2) = 3(-2)^2 - 3 = 12 - 3 = 9 \quad (\text{positive})\)
   - \(P_2(-2) = 2(-2) - 1 = -4 - 1 = -5 \quad (\text{negative})\)
   - \(P_3(-2) = \frac{9}{4} \quad (\text{positive})\)

   **Sequence at \(x = -2\)**: \([-1, +9, -5, +9/4]\)  
   **Sign changes = 3**

2. **At \(x = 2\)**:
   - \(P_0(2) = (2)^3 - 3(2) + 1 = 8 - 6 + 1 = 3 \quad (\text{positive})\)
   - \(P_1(2) = 3(2)^2 - 3 = 12 - 3 = 9 \quad (\text{positive})\)
   - \(P_2(2) = 2(2) - 1 = 4 - 1 = 3 \quad (\text{positive})\)
   - \(P_3(2) = \frac{9}{4} \quad (\text{positive})\)

   **Sequence at \(x = 2\)**: \([+3, +9, +3, +9/4]\)  
   **Sign changes = 0**

---

### Step 3: Count the Roots

The number of distinct real roots in the interval \((-2, 2)\) is the difference in sign changes at the endpoints:
\[
\text{Number of roots} = V(-2) - V(2) = 3 - 0 = 3
\]

---

### Step 4: Verify the Roots

The polynomial \(P(x) = x^3 - 3x + 1\) has three distinct real roots, approximately located at:
\[
x \approx -1.879, \, x \approx 0.347, \, x \approx 1.532
\]
This confirms the result.

---

### Conclusion

Using Sturm's Theorem, we determined that the polynomial \(P(x) = x^3 - 3x + 1\) has exactly **three distinct real roots** in the interval \((-2, 2)\).

## Resources

- [Sturm's theorem on Wikipedia](https://en.wikipedia.org/wiki/Sturm%27s_theorem)
- [BillCookMath's interactive website to compute Sturm's sequences](https://billcookmath.com/sage/algebra/Sturms_method.html)