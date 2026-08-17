"""
Karatsuba Multiplication — Divide and Conquer for Large Integer Multiplication
================================================================================

Grade-school method: O(n^2)
Karatsuba method:     O(n^1.585) = O(n^log2(3))

Idea:
    x = x1 * 10^(n/2) + x0
    y = y1 * 10^(n/2) + y0

    x * y = x1*y1 * 10^n + (x1*y0 + x0*y1) * 10^(n/2) + x0*y0

    A naive approach requires 4 recursive multiplications
    (x1y1, x1y0, x0y1, x0y0). Karatsuba's key insight is that the
    same result can be obtained with only 3 recursive multiplications:

        A = x1 * y1
        B = x0 * y0
        C = (x1 + x0) * (y1 + y0)
        middle_term = C - A - B   # = x1*y0 + x0*y1

    Recurrence: T(n) = 3*T(n/2) + O(n)  ->  by the Master Theorem, O(n^log2(3))
"""


def karatsuba(x: int, y: int) -> int:
    """Multiplies two integers using the Karatsuba algorithm (supports negative numbers)."""
    # Separate the sign and work with positive integers
    sign = -1 if (x < 0) ^ (y < 0) else 1
    x, y = abs(x), abs(y)

    result = _karatsuba_positive(x, y)
    return sign * result


def _karatsuba_positive(x: int, y: int) -> int:
    # Base case: multiply small numbers directly (recursion stopping point)
    if x < 10 or y < 10:
        return x * y

    # Split at the midpoint based on the larger operand's digit count
    n = max(len(str(x)), len(str(y)))
    half = n // 2

    power = 10 ** half
    x1, x0 = divmod(x, power)
    y1, y0 = divmod(y, power)

    # Divide & Conquer: only 3 recursive calls
    a = _karatsuba_positive(x1, y1)                 # high * high
    b = _karatsuba_positive(x0, y0)                 # low * low
    c = _karatsuba_positive(x1 + x0, y1 + y0)        # product of the sums

    middle = c - a - b                               # x1*y0 + x0*y1

    return a * (10 ** (2 * half)) + middle * (10 ** half) + b


if __name__ == "__main__":
    # The 64-digit numbers from the course's programming assignment
    num1 = 3141592653589793238462643383279502884197169399375105820974944592
    num2 = 2718281828459045235360287471352662497757247093699959574966967627

    result = karatsuba(num1, num2)
    print("Karatsuba result:", result)
    print("Python built-in (for verification):", num1 * num2)
    assert result == num1 * num2
    print("✅ Results match")
