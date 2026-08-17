Merge Sort — Divide and Conquer Sorting AlgorithmConcept:
Divide the array into two halves (Divide)Recursively sort each half (Conquer)Combine the two sorted halves 
(Combine / Merge)Time complexity:  O(n log n) — in all cases (best, average, worst)Space complexity: 
$O(n)$ — for auxiliary arraysThis is the core example of the course's "Divide and Conquer" section: 
the recurrence relation T(n) = 2T(n/2) + O(n)  is a classic example of the Master Theorem
(case 2 -> O(n log n))."

====================================================

"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """Massivi artan ardıcıllıqla sıralayır və yeni siyahı qaytarır."""
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """İki sıralanmış siyahını bir sıralanmış siyahıda birləşdirir. O(n)."""
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
    Bonus: Merge Sort-un üzərində qurulmuş inversiya sayğacı.
    (i < j və arr[i] > arr[j] olan cütlərin sayı)
    Bu, "divide and conquer"in klassik tətbiqlərindən biridir —
    naiv üsulla O(n^2), merge sort əsaslı üsulla O(n log n).
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
                inv_split += len(left) - i  # sağdan gələn hər ədəd, qalan bütün sol elementlərlə inversiya yaradır
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_left + inv_right + inv_split

    _, total = sort_and_count(arr)
    return total


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Orijinal massiv:", data)
    print("Sıralanmış:     ", merge_sort(data))
    print("İnversiya sayı: ", count_inversions(data))
