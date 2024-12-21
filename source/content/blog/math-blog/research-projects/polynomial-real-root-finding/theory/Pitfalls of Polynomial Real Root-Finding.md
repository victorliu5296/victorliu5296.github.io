---
title: 'Pitfalls of Polynomial Real Root Finding'
date: 2024-12-20T10:42:19-05:00
math: katex
description: "Common caveats when finding real roots of polynomials and how to mitigate them"
categories:
  - Research Projects
  - Polynomial Real Root-Finding
tags:
  - Numerical Analysis
  - Numerical Stability
weight: 100
draft: false
---

Finding the real roots of polynomials is a fundamental problem in mathematics and has applications across various fields, including engineering, physics, and computer science. While seemingly straightforward, numerical methods for polynomial root finding can be surprisingly subtle and prone to various pitfalls. This article explores some of these common caveats and discusses strategies for mitigating their effects.

## Instability in Numerical Methods

Several numerical methods exist for finding polynomial roots, such as the bisection method, the Newton-Raphson method, the Durand-Kerner method, and methods based on companion matrices and eigenvalue computations. However, these methods can suffer from numerical instability, particularly when dealing with polynomials of high degree or those with clustered roots.

### Deflation

Deflation is a common technique used to find multiple roots of a polynomial. After finding one root, the polynomial is divided by the corresponding linear factor to obtain a lower-degree polynomial. This process is repeated to find subsequent roots. However, deflation can introduce significant numerical errors. If the first root is computed with some error, this error is propagated and amplified in subsequent deflation steps, leading to increasingly inaccurate results for the remaining roots.

*Example:* Consider a polynomial with roots very close to each other. An error in the first root found will significantly impact the accuracy of the remaining roots computed through deflation.

*Mitigation:* One approach to mitigate the instability of deflation is to refine the computed roots using the original polynomial instead of the deflated polynomial. This can be done using iterative methods like Newton-Raphson. Another approach is to use methods that find all roots simultaneously, avoiding the sequential nature of deflation.

### Sensitivity to Coefficients

Polynomial roots can be highly sensitive to small perturbations in the coefficients of the polynomial. This is especially true for polynomials with multiple or closely spaced roots, and especially for polynomials of very high degree. A tiny change in a coefficient can lead to significant changes in the location of the roots.

*Example:* Wilkinson's polynomial, $(x-1)(x-2)\dotsm(x-20)$, famously demonstrates this sensitivity. A small change in one coefficient can drastically alter the roots.

*Mitigation:* This sensitivity highlights the tradeoff of using high-precision arithmetic when working with polynomials. Yes, it costs more, but it will reduce likelihood of damage by numerical instability. It also emphasizes the need for robust algorithms that are less susceptible to coefficient perturbations.

## Working with Complex Numbers Beyond the Real Axis

While this article focuses on finding *real* roots, many polynomials have complex roots. Numerical methods often compute complex roots even when searching for real roots. It is crucial to handle these complex values correctly.

*Issue:* Naively discarding complex roots without proper analysis can lead to missed real roots. Due to computational limitations, real roots in algorithms operating on complex numbers often have a very small imaginary component, even though the actual root is real.

*Mitigation:* When using numerical methods that can produce complex roots, it's essential to check the imaginary parts of the computed roots. If the imaginary part is sufficiently close to zero (within a defined tolerance), the real part can be tested to satisfy a tolerance bound. If it is close, we can also iterate a refinement method like Newton-Raphson. It is also important to be aware of complex conjugate pairs; in a real polynomial, if $a + bi$ is a root, then $a - bi$ is also a root.

## Further Reading

* [Wikipedia: Numerical Stability](https://en.wikipedia.org/wiki/Numerical_stability)
* [Wikipedia: Numerical Analysis](https://en.wikipedia.org/wiki/Numerical_analysis)