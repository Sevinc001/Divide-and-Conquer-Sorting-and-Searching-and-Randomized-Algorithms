"""
Master Theorem Analyzer — Bonus / Theoretical Utility
=========================================================

Classifies recurrences of the form T(n) = a*T(n/b) + f(n),
assuming f(n) = Theta(n^k).

Note: this is not an algorithm itself, but a theoretical tool from the
course — it can be used to manually verify the time complexity of all
the Divide and Conquer algorithms above (Merge Sort, Karatsuba,
Fast Power). For example:

    Merge Sort:  T(n) = 2*T(n/2) + n      -> a=2, b=2, k=1
    Karatsuba:   T(n) = 3*T(n/2) + n      -> a=3, b=2, k=1
    Fast Power:  T(n) = 1*T(n/2) + O(1)   -> a=1, b=2, k=0
"""

import math


def master_theorem(a: int, b: int, k: float) -> str:
    """
    Analyzes the recurrence T(n) = a*T(n/b) + Theta(n^k).
    Requires a >= 1 and b > 1.
    """
    if a < 1 or b <= 1:
        raise ValueError("a must be >= 1 and b must be > 1")

    crit_exponent = math.log(a, b)
    print(f"Critical exponent (log_b(a)): {crit_exponent:.4f}")

    if k < crit_exponent - 1e-9:
        verdict = f"Case 1: T(n) = Theta(n^{crit_exponent:.4f})"
    elif math.isclose(k, crit_exponent, abs_tol=1e-9):
        verdict = f"Case 2: T(n) = Theta(n^{k:.4f} * log n)"
    else:
        verdict = f"Case 3: T(n) = Theta(n^{k:.4f})  (f(n) dominates)"

    print(verdict)
    return verdict


if __name__ == "__main__":
    print("Merge Sort: T(n) = 2*T(n/2) + n")
    master_theorem(a=2, b=2, k=1)

    print("\nKaratsuba: T(n) = 3*T(n/2) + n")
    master_theorem(a=3, b=2, k=1)

    print("\nFast Power: T(n) = 1*T(n/2) + 1")
    master_theorem(a=1, b=2, k=0)

    print("\nExample: T(n) = 9*T(n/3) + n^2")
    master_theorem(a=9, b=3, k=2)
