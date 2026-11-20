"""Find the insertion index that keeps a sorted list in order.

Runs in O(log n) time and O(1) extra space. The input must be sorted.
"""

from typing import Sequence, TypeVar

T = TypeVar("T")


def search_insert_position(values: Sequence[T], target: T) -> int:
    """Return the first index whose value is >= target, or len(values)."""
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    return left


if __name__ == "__main__":
    assert search_insert_position([1, 3, 5, 6], 5) == 2
    assert search_insert_position([1, 3, 5, 6], 2) == 1
    assert search_insert_position([1, 3, 5, 6], 7) == 4
    assert search_insert_position([1, 3, 3, 3, 8], 3) == 1
    assert search_insert_position([], 10) == 0
    print("All search-insert examples passed.")
