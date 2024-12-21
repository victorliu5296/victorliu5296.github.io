# b2studios Algorithm for Polynomial Root Finding
import numpy as np
from sympy import symbols, Poly, div, gcd
import pandas as pd

# Step 1: Polynomial Root-Finding with Bisection and Cauchy Bound
def derivative(coeffs):
    degree = len(coeffs) - 1
    return [coeffs[i] * (degree - i) for i in range(degree)]

def cauchy_bound(coeffs):
    leading_coeff = coeffs[0]
    coeffs_abs = [abs(c / leading_coeff) for c in coeffs[1:]]
    return 1 + max(coeffs_abs)

def bisection_method(func, a, b, epsilon):
    while abs(b - a) > epsilon:
        c = (a + b) / 2
        func_c = func(c)
        if abs(func_c) < epsilon:
            return c
        elif func(a) * func_c < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def find_roots(coeffs, epsilon):
    if len(coeffs) == 2:
        a, b = coeffs
        return [-b / a]

    derivative_coeffs = derivative(coeffs)
    derivative_roots = find_roots(derivative_coeffs, epsilon)

    bound = cauchy_bound(coeffs)
    intervals = []

    if derivative_roots:
        intervals = [(-bound, derivative_roots[0])]
        intervals += [(derivative_roots[i], derivative_roots[i + 1]) for i in range(len(derivative_roots) - 1)]
        intervals += [(derivative_roots[-1], bound)]
    else:
        intervals = [(-bound, bound)]

    def poly_func(x):
        return sum(c * x**i for i, c in enumerate(reversed(coeffs)))

    roots = []
    for a, b in intervals:
        a_val, b_val = poly_func(a), poly_func(b)
        if a_val * b_val <= 0:
            root = bisection_method(poly_func, a, b, epsilon)
            if root is not None:
                roots.append(root)
    return roots

# Step 2: Sturm's Sequence for Distinct Roots Verification
def sturm_sequence(p):
    x = symbols('x')
    sequence = [p, p.diff()]
    while sequence[-1] != 0:
        _, remainder = div(sequence[-2], sequence[-1])
        sequence.append(-remainder)
    return sequence[:-1]

def count_sign_changes(sequence, value):
    if value == float('inf'):
        value = 1e12
    elif value == float('-inf'):
        value = -1e12

    signs = [np.sign(Poly(poly).eval(value)) for poly in sequence]
    return sum(
        1 for i in range(len(signs) - 1)
        if signs[i] * signs[i + 1] < 0
    )

def sturm_real_root_count(coeffs):
    x = symbols('x')
    sturm_seq = sturm_sequence(Poly(coeffs, x))
    inf_count = count_sign_changes(sturm_seq, float('inf'))
    neg_inf_count = count_sign_changes(sturm_seq, float('-inf'))
    return neg_inf_count - inf_count

def has_distinct_real_roots(coeffs):
    x = symbols('x')
    p = Poly(coeffs, x)
    p_prime = p.diff()
    return gcd(p, p_prime) == 1

# Step 3: Examples and Results
def polynomial_from_roots(roots):
    coeffs = [1]
    for root in roots:
        coeffs = np.polymul(coeffs, [1, -root])
    return coeffs.tolist()

examples = {
    "Example 1": [-4, -2, 1, 3],
    "Example 2": [-5, -1, 2, 4],
    "Example 3": [-10, -3, 0, 5, 7],
    "Example 4": [-6, -2, 0.5, 2.5, 4.5, 6],
}

results = []

for name, roots in examples.items():
    coeffs = polynomial_from_roots(roots)
    computed_roots = find_roots(coeffs, 1e-6)

    distinct_check = has_distinct_real_roots(coeffs)
    real_root_count = sturm_real_root_count(coeffs)

    results.append({
        "Name": name,
        "Original Roots": roots,
        "Coefficients": coeffs,
        "Computed Roots": computed_roots,
        "Has Distinct Real Roots": distinct_check,
        "Real Root Count (Sturm)": real_root_count,
        "Degree": len(coeffs) - 1
    })

print(pd.DataFrame(results).to_string())