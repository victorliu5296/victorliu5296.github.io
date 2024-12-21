---
title: 'Descartes'' Rule of Signs'
date: 2024-12-20T10:28:50-05:00
math: katex
description: "A powerful theorem for determining the existing of roots in a given interval"
categories:
  - Research Projects
  - Polynomial Real Root-Finding
tags:
  - Descartes' Rule of Signs
  - Budan's Theorem
weight: 100
draft: false
---

### Descartes' Rule of Signs: An Overview

**Descartes' Rule of Signs** is a theorem that estimates the possible number of positive and negative real roots of a polynomial based on its coefficients' sign changes. It provides an upper bound on real roots but does not locate them.

---

### **The Rule**

For a polynomial \( P(x) = a_nx^n + \dots + a_0 \):

1. **Positive Real Roots**:
   - Count sign changes in \( P(x) \)'s coefficients (ignoring zeroes).
   - The number of positive roots equals the count of sign changes or less by an even integer.

2. **Negative Real Roots**:
   - Replace \( x \) with \( -x \) to form \( P(-x) \).
   - Count sign changes in \( P(-x) \)'s coefficients.
   - The number of negative roots equals the count of sign changes or less by an even integer.

---

### **Example**

For \( P(x) = 2x^5 - 3x^4 + x^3 - 6x^2 + 4x - 8 \):

1. **Positive Real Roots**:
   - Coefficients: \( 2, -3, 1, -6, 4, -8 \); sign changes: 5.
   - Possible positive roots: \( 5, 3, 1 \).

2. **Negative Real Roots**:
   - \( P(-x) = -2x^5 - 3x^4 - x^3 - 6x^2 - 4x - 8 \); no sign changes.
   - Possible negative roots: \( 0 \).

---

### **Key Considerations**

1. **Multiplicity**: Repeated roots are counted separately.
2. **Upper Bound**: Provides an upper limit on real roots; actual counts are less by even integers.

### **Limitations**

- The rule only provides the number of possible roots, not their locations or exact values. This is fine, since we can use bisection to do the searching.
- It does not distinguish between simple and repeated roots. However, this can be fixed by computing the greatest common divisor of the polynomial with its own derivative, which eliminates repeated roots.

---

### Budan's Theorem

Budan's theorem is a generalization of Descartes' rule of signs using [function transformations](./Refresher%20on%20Function%20Trasnformations%20for%20Interval%20Arithmetic/_index.md) by analyzing roots within specific intervals. It uses linear fractional transformations (shifting) to analyze sign changes in transformed polynomials.

**The Theorem (Formal Statement):**

> Let \(P(x)\) be a polynomial of degree \(n\) with real coefficients. Let \(a\) and \(b\) be real numbers with \(a < b\). Let \(v(c)\) denote the number of sign changes in the sequence of coefficients of the polynomial \(P(x+c)\) for any real number \(c\). Then, the number of real roots of \(P(x)\) in the open interval \((a, b)\), counted with multiplicities, satisfies the following:
>
> Number of roots in \((a, b)\) \(\equiv v(a) - v(b) \pmod{2}\)
>
> and
>
> Number of roots in \((a, b)\) \(\le v(a) - v(b)\)

**Why the "Multiple of 2" Matters:**

The "or less than it by a positive even integer" part is crucial. It arises because complex roots of polynomials with real coefficients always occur in conjugate pairs. Therefore, if the difference in sign changes doesn't perfectly account for the real roots within the interval, the deficit must be due to pairs of complex roots, hence an even number.

**Interpretation:**

*   If \(v(a) - v(b) = 0\), then there *must* be exactly zero roots.
*   If \(v(a) - v(b) = 1\), then there *must* be exactly one root.
*   If \(v(a) - v(b) \ge 2\), then the test is *inconclusive*. There could be zero, one, or more roots (up to \(v(a) - v(b)\), and the number of roots will have the same parity as \(v(a)-v(b)\)), so we keep checking.

This is *extremely* useful for root-finding algorithms, since it allows us to quickly classify an interval as either to be discarded, to be refined to isolate a single root, or to continue to be split into smaller intervals for potentially several roots. Computing this is more efficient than computing the Sturm chain.

### Key Points

*   Budan's theorem generalizes Descartes' rule for interval analysis.
*   These tools are fundamental to modern root-finding methods beyond Sturm's theorem (e.g., Vincent-Collins-Akritas or Vincent-Akritas-Strzebonski).

## Resources

- [Descartes' Rule of Signs](https://en.wikipedia.org/wiki/Descartes%27_rule_of_signs)
- [Budan's Theorem](https://en.wikipedia.org/wiki/Budan%27s_theorem)