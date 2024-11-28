---
title: 'Deriving PDF of Normal Distribution'
date: 2024-09-14T20:18:51-04:00
math: katex
summary: "An elementary derivation of the PDF of a normal distribution."
categories:
  - Applied Mathematics
topics:
  - [Statistics, Probability Theory]
tags: [Normal Distribution, Maximum Entropy, Central Limit Theorem]
weight: 100
---

I scoured the internet for a simple derivation of the probability density function of a normal distribution, but I could not easily find one. Most of them were either too vague or too technical.

Therefore, in this post, I wish to present an informal derivation of the probability density function of a normal distribution. The goal is to avoid being too technical or mathematically involved (trying to avoid the reference to hard-to-prove theorems). All the while, I hope it provides a certain intuition about the normal distribution.

I want to focus on the Central Limit Theorem: it is a mathematical result that states the distribution arising from adding more and more independent samples from the same distribution will converge to a normal distribution.

An important implication of the CLT is that as the number of samples grows large, adding one more sample doesn't significantly alter the overall distribution. This property hints at a kind of stability or equilibrium state that the normal distribution represents.

To understand this equilibrium state better, we can draw an analogy from physics, specifically from thermodynamics and statistical mechanics. In these fields, systems tend to evolve towards states of maximum entropy, which represent the most probable configurations.

Entropy, in the context of information theory and statistics, measures the uncertainty or randomness of a probability distribution. A distribution with high entropy contains less specific information and is, in a sense, more "spread out" or less constrained.

By applying this concept of maximum entropy to probability distributions, we can derive the form of the normal distribution. We'll show that among all possible distributions with a given mean and variance, the normal distribution is the one that maximizes entropy. This approach not only yields the correct mathematical form but also provides insight into why the normal distribution is so common in nature and statistical phenomena.

## Step 1: Define Entropy for Continuous Distributions

For a continuous probability distribution with PDF \(p(x)\), the differential entropy \(H\) is defined as:

\[
\begin{aligned}
H :=& \,\mathbb{E}_{X \sim p}[-\log p(X)] \\
=& -\int_{-\infty}^{\infty} p(x) \log(p(x)) dx
\end{aligned}
\]

## Step 2: Establish Constraints

We'll impose two natural constraints on our distribution:

1. The total probability must sum to 1:
   \[
   \int_{-\infty}^{\infty} p(x) dx = 1
   \]

2. The distribution has a fixed variance \(\sigma^2\):
   \[
   \mathbb{E}_{X \sim p}[(X-\mathbb{E}[X])^2] = \int_{-\infty}^{\infty} x^2 p(x) dx = \sigma^2
   \]

Note that we are not constraining the mean \(\mathbb{E}[X]\) of the distribution since if the solution exists, then we can easily shift the distribution by adding a constant to the random variable \(X\), e.g. using \(X - \mu\) for a mean \(\mu\) other than zero.

## Step 3: Set Up the Optimization Problem

We want to maximize the entropy subject to these constraints. We can use the method of Lagrange multipliers to solve this optimization problem. Let's form the Lagrangian:

\[
L = -\int_{-\infty}^{\infty} p(x) \ln(p(x)) dx + \lambda_1 \left(\int_{-\infty}^{\infty} p(x) dx - 1\right) + \lambda_2 \left(\int_{-\infty}^{\infty} x^2 p(x) dx - \sigma^2\right)
\]

Where \(\lambda_1\) and \(\lambda_2\) are Lagrange multipliers.

## Step 4: Find the Extremum

To maximize entropy, we need to find where the [functional derivative](https://en.wikipedia.org/wiki/Functional_derivative) of \(L\) with respect to \(p(x)\) is zero:

\[
\frac{\delta L}{\delta p(x)} = -\ln(p(x)) - 1 + \lambda_1 + \lambda_2 x^2 = 0
\]

## Step 5: Solve for p(x)

Rearranging the above equation:

\[
\ln(p(x)) = \lambda_1 - 1 + \lambda_2 x^2
\]

Taking the exponential of both sides:

\[
p(x) = e^{\lambda_1 - 1} e^{\lambda_2 x^2}
\]

## Step 6: Determine the Constants

Let \(A = e^{\lambda_1 - 1}\) and \(B = \lambda_2\). Then:

\[
p(x) = A e^{Bx^2}
\]

Let's apply constraint 1:

\[
\int_{-\infty}^{\infty} p(x) dx = 1
\]

\[
\int_{-\infty}^{\infty} A e^{Bx^2} dx = 1
\]

\[
A \int_{-\infty}^{\infty} e^{Bx^2} dx = 1
\]

This integral is the famous Gaussian integral, which converges when \(B < 0\). We know that

\[
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
\]

Using substitution,

\[
\int_{-\infty}^{\infty} e^{Bx^2} dx = \frac{\sqrt{\pi}}{\sqrt{-B}}
\]

Hence,

\[
A \left( \frac{\sqrt{\pi}}{\sqrt{-B}} \right) = 1
\]

\[
A = \frac{\sqrt{-B}}{\sqrt{\pi}}
\]

Now, we apply constraint 2:

\[
\int_{-\infty}^{\infty} x^2 p(x) dx = \sigma^2
\]

\[
\int_{-\infty}^{\infty} x^2 A e^{Bx^2} dx = \sigma^2
\]

\[
\frac{-B}{\sqrt{\pi}} \int_{-\infty}^{\infty} x^2 e^{Bx^2} dx = \sigma^2
\]

We can solve this by applying integration by parts or using Wolfram Alpha.

\[
\frac{-B}{\sqrt{\pi}} \left( \frac{\sqrt{\pi}}{2(-B)^{\frac{3}{2}}} \right) = \sigma^2
\]

Hence,

\[
B = -\frac{1}{2\sigma^2}
\]

And plugging back in for \(A\):

\[
A = \frac{\sqrt{-B}}{\sqrt{\pi}} = \frac{1}{\sigma\sqrt{2\pi}}
\]
## Step 7: Final Form

Substituting these values, we get the normal distribution PDF:

\[
p(x|\sigma) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{x^2}{2\sigma^2}}
\]

This is the standard form of the normal distribution, which indeed involves \(e^{-x^2}\) as part of its expression.

Since this is an even function, it is symmetric around zero. In addition, if you wish to shift it so that the mean is zero, we can subtract the mean from the input \(x\):

\[
p(x| \mu, \sigma) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
\]

## Conclusion

Through the principle of maximum entropy, we've derived the probability density function of the normal distribution. This approach reveals why the normal distribution is so ubiquitous in nature and statistics:

1. It maximizes entropy given a fixed variance, making it the least informative (or most uncertain) distribution consistent with this constraint.

2. This property aligns with the Central Limit Theorem, explaining why the sum of many independent random variables tends towards a normal distribution, just like how physical systems tend towards maximum entropy states.

This perspective tying physics to statistics offers valuable insight into why the normal distribution emerges so frequently across diverse fields of study.