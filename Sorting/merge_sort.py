"""Sort integers with stable, recursive merge sort.

The input is copied before sorting, so callers retain their original sequence.
During merging, equal values are taken from the left half first to preserve
the order of equal-key items (stability).

Time: O(n log n). Extra space: O(n) for the working arrays and O(log n)
for recursion.
"""

from typing import Sequence


def merge_sort(values: Sequence[int]) -> list[int]:
    """Return values in ascending order without modifying the input."""
    items = list(values)
    buffer = items.copy()

    def sort_range(start: int, end: int) -> None:
        if end - start <= 1:
            return

        middle = (start + end) // 2
        sort_range(start, middle)
        sort_range(middle, end)

        left, right = start, middle
        for output in range(start, end):
            if left < middle and (right >= end or items[left] <= items[right]):
                buffer[output] = items[left]
                left += 1
            else:
                buffer[output] = items[right]
                right += 1

        items[start:end] = buffer[start:end]

    sort_range(0, len(items))
    return items


if __name__ == "__main__":
    original = [5, -1, 3, 3, 0, 8, -4]
    assert merge_sort(original) == [-4, -1, 0, 3, 3, 5, 8]
    assert original == [5, -1, 3, 3, 0, 8, -4]
    assert merge_sort([]) == []
    assert merge_sort([7]) == [7]
    assert merge_sort([2, 1]) == [1, 2]
    print("All Merge Sort examples passed.")
