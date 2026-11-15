"""Find the first index of a target in a sorted sequence.

The lower-bound search keeps the left half whenever its midpoint is greater
than or equal to the target. This makes duplicates resolve to the first
matching position.

Precondition: values are sorted in non-decreasing order.
Time: O(log n). Extra space: O(1).
"""

from typing import Sequence


def binary_search_first(values: Sequence[int], target: int) -> int | None:
    """Return the first matching index, or None when target is absent."""
    low, high = 0, len(values)

    while low < high:
        middle = (low + high) // 2
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle

    if low < len(values) and values[low] == target:
        return low
    return None


if __name__ == "__main__":
    assert binary_search_first([1, 2, 2, 2, 5], 2) == 1
    assert binary_search_first([-8, -3, 0, 4, 9], -8) == 0
    assert binary_search_first([-8, -3, 0, 4, 9], 9) == 4
    assert binary_search_first([1, 3, 5], 4) is None
    assert binary_search_first([], 1) is None
    print("All Binary Search First examples passed.")
