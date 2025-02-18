---
title: '1985 AHSME Problem 29'
date: 2025-02-18T17:27:55-05:00
summary: ""
math: katex
categories:
  - Competitive Math
tags:
  - Counting
weight: 100
draft: false
---

## 1985 AHSME Problems/Problem 29
### Problem
In their base $10$ representations, the integer $a$ consists of a sequence of $1985$ eights and the integer $b$ consists of a sequence of $1985$ fives. What is the sum of the digits of the base $10$ representation of the integer $9ab$?

$\mathrm{(A)\ } 15880 \qquad \mathrm{(B) \ }17856 \qquad \mathrm{(C) \  } 17865 \qquad \mathrm{(D) \  } 17874 \qquad \mathrm{(E) \  }19851$

#### Solution

Factor:
$a = 888\dots 888 = 8\underbrace{(111\dots 111)}_{1985 \times \text{1's}}$
$b = 555\dots 555 = 5\underbrace{(111\dots 111)}_{1985 \times \text{1's}}$

$9ab = 9(8(111\dots 111))(5(111\dots 111))=40\cdot 9{\underbrace{(111\dots 111)}_{1985 \times \text{1's}}}^2$

Curiously, notice that $9(111\dots 111)=999\dots 999=10^{1985}-1$. This is not a coincidence, as you can verify this from the geometric sum form:

$$9\sum_{i=0}^{1984} 10^i=9\frac{10^{1985}-1}{10-1}=10^{1985}-1$$

Now, we have something like $40(10^{1985}-1)(111\dots 111)$, which we expand by distributing:

$$=40(\underbrace{111\dots 111}_{1985\times \text{1's}}\underbrace{000\dots 000}_{1985\times \text{0's}}-\underbrace{111\dots 111}_{1985 \times \text{1's}})$$

We can now calculate this fairly simply:

$$40(\underbrace{111\dots 11}_{1984\times \text{1's}}0\underbrace{888\dots 88}_{1984\times \text{8's}}9)$$

$$=\underbrace{444\dots 444}_{1984\times \text{4's}}3\underbrace{555\dots 555}_{1984\times \text{5's}}60$$

Hence, the digit sum is $9\cdots 1984 + 3 + 6 + 0=9\cdots 1985 = 9(2000-15)=18000-135=\boxed{\textbf{(C) }17865}$.