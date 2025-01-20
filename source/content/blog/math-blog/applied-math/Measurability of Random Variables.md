---
title: 'Measurability of Random Variables'
date: 2024-10-11T22:30:45-04:00
summary: "Motivating the definition of measurability for random variables"
math: katex
categories:
  - Applied Mathematics
topics:
  - Probability Theory
  - Measure Theory
tags:
  - Random Variables
  - Measurability
  - Sigma-Algebra
weight: 100
draft: false
---

### \( \mathcal{F} \)-Measurability and Examples

#### Motivation and Problem

Measurability is crucial in probability theory for defining random variables that allow probability assignments to events. For a random variable \( X: \Omega \to \mathbb{R} \) to be useful in a probability space \( (\Omega, \mathcal{F}, P) \), it must be compatible with the sigma-algebra \( \mathcal{F} \).

If \( X \) is not \( \mathcal{F} \)-measurable, certain Borel sets in \( \mathbb{R} \) won't correspond to measurable events in \( \Omega \), making it impossible to calculate probabilities for \( X \).

Informally, a random variable \( X \) is \( \mathcal{F} \)-measurable if the information provided by \( \mathcal{F} \) is sufficient to determine the values of \( X \). This means that the events defined by \( \mathcal{F} \) are detailed enough to describe the outcomes of \( X \) in a way that allows us to assign probabilities to these outcomes.

Think of \( \mathcal{F} \) as describing the "level of detail" or "lens" through which you view the sample space \( \Omega \). If \( X \) outputs values that depend on details outside this lens, it's not \( \mathcal{F} \)-measurable.

In simpler terms, \( X \) is \( \mathcal{F} \)-measurable if knowing the events in \( \mathcal{F} \) tells us everything we need to know about the possible values of \( X \).

#### Formal Definition of \( \mathcal{F} \)-Measurability

A random variable \( X: \Omega \to \mathbb{R} \) is \( \mathcal{F} \)-measurable if for every Borel set \( B \subseteq \mathbb{R} \), the preimage \( X^{-1}(B) \) is in \( \mathcal{F} \).

This all sounds very vague and abstract. Let's see some examples.

---

### Simple Examples: Coin Flip

Let’s take an example involving a coin flip, one of the simplest random phenomena, to illustrate measurability.

#### Setup

1. **Sample space**: \( \Omega = \{\text{H}, \text{T}\} \), representing heads and tails.
2. **Sigma-algebra \( \mathcal{F} \)**: \( \mathcal{F} = \{\emptyset, \{\text{H}\}, \{\text{T}\}, \Omega\} \).
3. **Random variable \( X \)**:
   \[
   X(\omega) =
   \begin{cases}
   1, & \text{if } \omega = \text{H}, \\
   -1, & \text{if } \omega = \text{T}.
   \end{cases}
   \]

#### Checking \( \mathcal{F} \)-Measurability

To determine if \( X \) is \( \mathcal{F} \)-measurable, we need to verify that for any Borel set \( B \subseteq \mathbb{R} \), the preimage \( X^{-1}(B) \in \mathcal{F} \).

1. For \( B = \{1\} \):
   \[
   X^{-1}(\{1\}) = \{\text{H}\} \in \mathcal{F}.
   \]

2. For \( B = \{-1\} \):
   \[
   X^{-1}(\{-1\}) = \{\text{T}\} \in \mathcal{F}.
   \]

3. For \( B = \{1, -1\} \):
   \[
   X^{-1}(\{1, -1\}) = \{\text{H}, \text{T}\} = \Omega \in \mathcal{F}.
   \]

Since \( X^{-1}(B) \) is in \( \mathcal{F} \) for all Borel sets \( B \), \( X \) is \( \mathcal{F} \)-measurable. 

#### Exercise
For this example, we have \( \mathcal{F} = \mathcal{P}(\Omega) \), the power set of \( \Omega \). Can you show that for any \( X: \Omega \to \mathbb{R} \), \( X \) is \( \mathcal{P}(\Omega) \)-measurable?

#### Negative Example: Coin Flip with Insufficient \( \mathcal{F} \)

Now consider the same random variable \( X \), but with a smaller sigma-algebra:
\[
\mathcal{F} = \{\emptyset, \Omega\}.
\]

1. For \( B = \{1\} \):
   \[
   X^{-1}(\{1\}) = \{\text{H}\} \notin \mathcal{F}.
   \]

2. For \( B = \{-1\} \):
   \[
   X^{-1}(\{-1\}) = \{\text{T}\} \notin \mathcal{F}.
   \]

In this case, \( X \) is not \( \mathcal{F} \)-measurable because \( \mathcal{F} \) doesn’t provide enough "detail" to distinguish between heads and tails.

#### Negative Example: Non-\( \mathcal{F} \)-Measurable Random Variable

**Setup:**
1. **Sample space**: \( \Omega = [0, 1] \).
2. **Sigma-algebra \( \mathcal{F} \)**: \( \mathcal{F} = \{\emptyset, \Omega\} \).
3. **Random variable \( X \)**: \( X(\omega) = \omega \).

**Checking \( \mathcal{F} \)-Measurability:**
- For \( X \) to be \( \mathcal{F} \)-measurable, \( X^{-1}(B) \) must be in \( \mathcal{F} \) for every Borel set \( B \).
- Consider \( B = [0, 0.5] \):
  \[
  X^{-1}([0, 0.5]) = [0, 0.5] \notin \mathcal{F}
  \]
- Thus, \( X \) is not \( \mathcal{F} \)-measurable.

#### Fixing the Problem: Restricting \( X \)

**New Random Variable \( X' \):**
\[
X'(\omega) =
\begin{cases}
1, & \text{if } \omega \in \Omega = [0, 1] \\
0, & \text{otherwise}
\end{cases}
\]

**Checking \( \mathcal{F} \)-Measurability of \( X' \):**
- If \( 1 \in B \):
  \[
  X'^{-1}(B) = \Omega \in \mathcal{F}
  \]
- If \( 1 \notin B \):
  \[
  X'^{-1}(B) = \emptyset \in \mathcal{F}
  \]
- Thus, \( X' \) is \( \mathcal{F} \)-measurable.

#### Positive Example: \( \mathcal{F} \)-Measurable Random Variable

**Setup:**
1. **Sample space**: \( \Omega = \{1, 2, 3\} \).
2. **Sigma-algebra \( \mathcal{F} \)**: \( \mathcal{F} = \{\emptyset, \{1\}, \{2, 3\}, \Omega\} \).
3. **Random variable \( X \)**:
   \[
   X(1) = 0, \quad X(2) = 1, \quad X(3) = 1
   \]

**Checking \( \mathcal{F} \)-Measurability:**
- For \( B = \{0\} \):
  \[
  X^{-1}(\{0\}) = \{1\} \in \mathcal{F}
  \]
- For \( B = \{1\} \):
  \[
  X^{-1}(\{1\}) = \{2, 3\} \in \mathcal{F}
  \]
- Thus, \( X \) is \( \mathcal{F} \)-measurable.

### Sigma-Algebra Generated by a Random Variable

What if instead of fitting the random variable to the sigma-algebra, we wanted to find the smallest sigma-algebra that fits the random variable?

Given a random variable \( X: \Omega \to \mathbb{R} \) on a probability space \( (\Omega, \mathcal{F}, P) \), the sigma-algebra generated by \( X \), denoted \( \sigma(X) \), is the smallest sigma-algebra making \( X \) measurable. It represents the information content of \( X \).

#### Definition

\[
\sigma(X) = \{ X^{-1}(B) : B \in \mathcal{B}(\mathbb{R}) \}
\]

where \( \mathcal{B}(\mathbb{R}) \) is the Borel sigma-algebra on \( \mathbb{R} \).

#### Properties

1. **Subset of \( \mathcal{F} \)**: \( \sigma(X) \subseteq \mathcal{F} \).
2. **Generating Events**: Includes events like \( \{ X \leq a \} \), \( \{ X > b \} \).
3. **Measurability**: Any \( Y = g(X) \) for measurable \( g \) is \( \sigma(X) \)-measurable.

#### Example 1: Identity Random Variable

Consider \( \Omega = [0, 1] \) and \( X(\omega) = \omega \).

**Key Events in \( \sigma(X) \)**:
1. \( \{ \omega : X(\omega) \leq 0.5 \} = [0, 0.5] \)
2. \( \{ \omega : X(\omega) > 0.7 \} = (0.7, 1] \)
3. \( \{ \omega : 0.3 \leq X(\omega) \leq 0.6 \} = [0.3, 0.6] \)

These intervals and their complements, unions, and intersections form \( \sigma(X) \).

#### Example 2: Piecewise Random Variable

Consider \( \Omega = [0, 1] \) and \( X \) defined as:
\[
X(\omega) =
\begin{cases}
0, & \text{if } 0 \leq \omega < 0.5 \\
1, & \text{if } 0.5 \leq \omega \leq 1
\end{cases}
\]

**Key Events in \( \sigma(X) \)**:
1. \( \{ \omega : X(\omega) = 0 \} = [0, 0.5) \)
2. \( \{ \omega : X(\omega) = 1 \} = [0.5, 1] \)
3. \( \{ \omega : X(\omega) \leq 0.5 \} = [0, 0.5) \)

These events capture the information provided by \( X \), illustrating how \( \sigma(X) \) includes all necessary events to describe \( X \)'s outcomes.

#### Conclusion

The sigma-algebra \( \sigma(X) \) generated by a random variable \( X \) encapsulates the information content of \( X \), including all events describable by \( X \)'s values. Understanding \( \sigma(X) \) is crucial for analyzing probabilistic models and dependencies.

---

### Exercises

#### Exercise 0: Showing Measurability

Can you show that for any \( X: \Omega \to \mathbb{R} \), \( X \) is \( \mathcal{P}(\Omega) \)-measurable, where \( \mathcal{P}(\Omega) \) is the power set of \( \Omega \) (collection of all subsets of \( \Omega \))?

#### Exercise 1: Checking Measurability
Let \( \Omega = \{a, b, c, d\} \), and define a sigma-algebra \( \mathcal{F} \) as:
\[
\mathcal{F} = \{\emptyset, \{a, b\}, \{c, d\}, \Omega\}.
\]
Define the random variable \( X: \Omega \to \mathbb{R} \) as:
\[
X(a) = 1, \quad X(b) = 1, \quad X(c) = -1, \quad X(d) = -1.
\]

1. Verify whether \( X \) is \( \mathcal{F} \)-measurable.
2. Identify the preimages of the sets \( B = \{1\} \) and \( B = \{-1\} \), and check if they belong to \( \mathcal{F} \).

---

#### Exercise 2: Constructing a Sigma-Algebra
Let \( \Omega = [0, 1] \) and define a random variable \( X(\omega) = \lfloor 10\omega \rfloor \). 

1. Construct the sigma-algebra \( \sigma(X) \) generated by \( X \).
2. Identify the events in \( \sigma(X) \) that correspond to:
   - \( \{X \leq 5\} \),
   - \( \{X = 3\} \),
   - \( \{X \geq 7\} \).

---

#### Exercise 3: Measurability with Coarse Sigma-Algebra
Consider \( \Omega = [0, 1] \) with the trivial sigma-algebra \( \mathcal{F} = \{\emptyset, \Omega\} \). Let \( X(\omega) = \sin(2\pi\omega) \).

1. Show that \( X \) is not \( \mathcal{F} \)-measurable.
2. Suggest a sigma-algebra that would make \( X \) measurable.

---

#### Exercise 4: Measurability with Piecewise Random Variables
Let \( \Omega = [0, 1] \), and define:
\[
X(\omega) =
\begin{cases}
0, & \text{if } 0 \leq \omega < 0.25, \\
1, & \text{if } 0.25 \leq \omega < 0.75, \\
2, & \text{if } 0.75 \leq \omega \leq 1.
\end{cases}
\]

1. Construct the sigma-algebra \( \sigma(X) \) generated by \( X \).
2. Write down the preimages \( X^{-1}(B) \) for \( B = \{0\} \), \( B = \{1\} \), and \( B = \{0, 2\} \).

---

#### Exercise 5: Non-Measurable Functions (Advanced)
Let \( \Omega = [0, 1] \) with the Lebesgue sigma-algebra, and consider the characteristic function of the rationals in \( [0, 1] \):
\[
X(\omega) =
\begin{cases}
1, & \text{if } \omega \in \mathbb{Q}, \\
0, & \text{if } \omega \notin \mathbb{Q}.
\end{cases}
\]

1. Show that \( X \) is measurable with respect to the Lebesgue sigma-algebra.
2. What happens if \( \mathcal{F} \) is the trivial sigma-algebra \( \{\emptyset, \Omega\} \)? Is \( X \) still measurable?