"""
Merge Sort — Divide and Conquer Sorting Algorithm
====================================================

Idea:
    1. Split the array in half (Divide)
    2. Recursively sort each half (Conquer)
    3. Merge the two sorted halves back together (Combine)

Time complexity: O(n log n) — in all cases (best/average/worst)
Space complexity: O(n) — for the auxiliary arrays

This is one of the canonical examples of the "Divide and Conquer" paradigm:
its recurrence T(n) = 2T(n/2) + O(n) is the textbook example of
Case 2 of the Master Theorem, giving O(n log n).
"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """Sorts the array in ascending order and returns a new list."""
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """Merges two sorted lists into a single sorted list. O(n)."""
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def count_inversions(arr: List[int]) -> int:
    """
    Bonus: an inversion counter built on top of Merge Sort.
    (pairs i < j where arr[i] > arr[j])
    This is a classic application of divide and conquer — the naive
    approach is O(n^2), while the merge-sort-based approach is O(n log n).
    """
    def sort_and_count(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, inv_left = sort_and_count(a[:mid])
        right, inv_right = sort_and_count(a[mid:])

        merged, inv_split = [], 0
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inv_split += len(left) - i  # every element taken from the right forms an inversion with all remaining elements on the left
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_left + inv_right + inv_split

    _, total = sort_and_count(arr)
    return total


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", data)
    print("Sorted array:  ", merge_sort(data))
    print("Inversion count:", count_inversions(data))
