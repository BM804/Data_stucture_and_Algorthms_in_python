"""Merge overlapping intervals without modifying the caller's input.

Intervals are inclusive pairs (start, end) with start <= end. Sorting by
start lets one pass combine each interval with the most recent merged one.

Time: O(n log n). Extra space: O(n), including the returned list.
"""

from typing import Sequence


def merge_intervals(intervals: Sequence[tuple[int, int]]) -> list[tuple[int, int]]:
    """Return sorted, non-overlapping intervals; touching at an endpoint merges."""
    ordered = sorted(intervals)
    if any(start > end for start, end in ordered):
        raise ValueError("each interval must have start <= end")

    merged: list[tuple[int, int]] = []
    for start, end in ordered:
        if not merged or start > merged[-1][1]:
            merged.append((start, end))
        else:
            previous_start, previous_end = merged[-1]
            merged[-1] = (previous_start, max(previous_end, end))
    return merged


if __name__ == "__main__":
    assert merge_intervals([(8, 10), (1, 3), (2, 6), (15, 18)]) == [
        (1, 6), (8, 10), (15, 18)
    ]
    assert merge_intervals([(1, 5), (2, 3), (5, 7)]) == [(1, 7)]
    assert merge_intervals([]) == []
    assert merge_intervals([(4, 4)]) == [(4, 4)]
    try:
        merge_intervals([(3, 1)])
    except ValueError:
        pass
    else:
        raise AssertionError("reversed interval should raise ValueError")
    print("All Merge Intervals examples passed.")
