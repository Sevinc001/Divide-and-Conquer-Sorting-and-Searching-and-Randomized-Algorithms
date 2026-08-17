"""
Randomized Selection (QuickSelect) — Randomized Algorithms
==============================================================

Problem: Find the k-th smallest element in an unsorted array
         (e.g., finding the median: k = n//2).

Naive approach: sort the array -> O(n log n)
QuickSelect: reuses QuickSort's partitioning idea, but at each step
             recurses into only ONE side (discarding the other)
             -> expected time O(n)!

Recurrence (expected case): T(n) = T(n/2) + O(n)  ->  O(n)
Worst-case (very low probability, if bad pivots keep being chosen): O(n^2)

This is one of the clearest illustrations of how randomization can
simultaneously simplify an algorithm and speed it up.
"""

import random
from typing import List


def randomized_selection(arr: List[int], k: int) -> int:
    """
    Returns the k-th smallest element of arr (k is 1-indexed,
    i.e. k=1 -> minimum, k=n -> maximum).
    """
    if not (1 <= k <= len(arr)):
        raise ValueError("k must be between 1 and len(arr)")

    a = arr[:]  # copy to avoid mutating the original array
    return _select(a, 0, len(a) - 1, k - 1)  # work with a 0-indexed target internally


def _select(a: List[int], lo: int, hi: int, target_index: int) -> int:
    if lo == hi:
        return a[lo]

    pivot_index = _randomized_partition(a, lo, hi)

    if pivot_index == target_index:
        return a[pivot_index]
    elif target_index < pivot_index:
        return _select(a, lo, pivot_index - 1, target_index)
    else:
        return _select(a, pivot_index + 1, hi, target_index)


def _randomized_partition(a: List[int], lo: int, hi: int) -> int:
    rand_index = random.randint(lo, hi)
    a[rand_index], a[hi] = a[hi], a[rand_index]

    pivot = a[hi]
    i = lo - 1
    for j in range(lo, hi):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[hi] = a[hi], a[i + 1]
    return i + 1


def median(arr: List[int]) -> float:
    """Bonus: computes the median using randomized_selection."""
    n = len(arr)
    if n % 2 == 1:
        return randomized_selection(arr, n // 2 + 1)
    else:
        lower = randomized_selection(arr, n // 2)
        upper = randomized_selection(arr, n // 2 + 1)
        return (lower + upper) / 2


if __name__ == "__main__":
    data = [7, 10, 4, 3, 20, 15, 1, 9]
    sorted_check = sorted(data)

    for k in range(1, len(data) + 1):
        result = randomized_selection(data, k)
        expected = sorted_check[k - 1]
        status = "✅" if result == expected else "❌"
        print(f"k={k}: {result} (expected: {expected}) {status}")
        assert result == expected

    print("\nMedian:", median(data), "| verified against sorted():",
          (sorted_check[len(data)//2 - 1] + sorted_check[len(data)//2]) / 2)
