"""
Fast Power (Fast Exponentiation) — Divide and Conquer
========================================================

Computing a^b naively takes O(b) time (b multiplications).
With Divide and Conquer, this can be reduced to O(log b):

    a^b = (a^2)^(b/2)          if b is even
    a^b = a * (a^2)^((b-1)/2)  if b is odd
"""


def fast_power(a: int, b: int) -> int:
    """Computes a^b in O(log b) time (b must be a non-negative integer)."""
    if b < 0:
        raise ValueError("This implementation only supports non-negative exponents")

    # Base cases
    if b == 0:
        return 1
    if b == 1:
        return a

    # Divide: compute the square
    half = fast_power(a, b // 2)

    # Conquer: square the half-result
    result = half * half

    # Combine: adjust for odd exponents
    if b % 2 != 0:
        result *= a

    return result


if __name__ == "__main__":
    tests = [(2, 10), (3, 0), (5, 1), (7, 13), (2, 100)]
    for base, exponent in tests:
        result = fast_power(base, exponent)
        expected = base ** exponent
        status = "✅" if result == expected else "❌"
        print(f"{base}^{exponent} = {result}  {status}")
        assert result == expected
