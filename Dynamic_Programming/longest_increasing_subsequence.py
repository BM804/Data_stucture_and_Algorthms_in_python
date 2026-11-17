"""Reconstruct one longest strictly increasing subsequence.

Binary search maintains the smallest tail value for each subsequence length.
A predecessor index per input value preserves enough information to rebuild
one valid subsequence after the scan.

Time: O(n log n). Extra space: O(n).
"""

from bisect import bisect_left
from typing import Sequence


def longest_increasing_subsequence(values: Sequence[int]) -> list[int]:
    """Return one longest strictly increasing subsequence; empty input gives []."""
    if not values:
        return []

    tail_values: list[int] = []
    tail_indices: list[int] = []
    previous = [-1] * len(values)

    for index, value in enumerate(values):
        position = bisect_left(tail_values, value)
        if position:
            previous[index] = tail_indices[position - 1]

        if position == len(tail_values):
            tail_values.append(value)
            tail_indices.append(index)
        else:
            tail_values[position] = value
            tail_indices[position] = index

    sequence: list[int] = []
    cursor = tail_indices[-1]
    while cursor != -1:
        sequence.append(values[cursor])
        cursor = previous[cursor]

    sequence.reverse()
    return sequence


if __name__ == "__main__":
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == [2, 3, 7, 18]
    assert longest_increasing_subsequence([0, 1, 0, 3, 2, 3]) == [0, 1, 2, 3]
    assert longest_increasing_subsequence([2, 2, 2]) == [2]
    assert longest_increasing_subsequence([-3, -2, -1]) == [-3, -2, -1]
    assert longest_increasing_subsequence([]) == []
    print("All Longest Increasing Subsequence examples passed.")
