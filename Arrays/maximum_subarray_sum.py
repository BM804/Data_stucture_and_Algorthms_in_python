"""Find the largest sum among all non-empty contiguous subarrays.

Kadane's algorithm either extends the best subarray ending at the prior
position or starts a new one at the current value.

Time: O(n). Extra space: O(1).
"""
from typing import Sequence


def maximum_subarray_sum(numbers: Sequence[int]) -> int:
    """Return the maximum contiguous-subarray sum; raise ValueError if empty."""
    if not numbers:
        raise ValueError("numbers must contain at least one value")

    best_ending_here = best_overall = numbers[0]
    for value in numbers[1:]:
        best_ending_here = max(value, best_ending_here + value)
        best_overall = max(best_overall, best_ending_here)
    return best_overall


if __name__ == "__main__":
    assert maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert maximum_subarray_sum([-8, -3, -6, -2, -5, -4]) == -2
    assert maximum_subarray_sum([5]) == 5
    assert maximum_subarray_sum([0, 0, 0]) == 0
    try:
        maximum_subarray_sum([])
    except ValueError:
        pass
    else:
        raise AssertionError("empty input should raise ValueError")
    print("All Maximum Subarray Sum examples passed.")
