"""Two Sum: find two distinct indices whose values add to a target.

The dictionary stores each value's most recent index, so each element is
processed once. This gives O(n) expected time and O(n) extra space.
"""

from typing import Optional, Sequence, Tuple


def two_sum(numbers: Sequence[int], target: int) -> Optional[Tuple[int, int]]:
    """Return indices of two values adding to target, or None if no pair exists.

    Each index is used at most once. If more than one pair is possible, the
    first pair found while scanning from left to right is returned.
    """
    index_by_value = {}

    for index, value in enumerate(numbers):
        complement = target - value
        if complement in index_by_value:
            return index_by_value[complement], index
        index_by_value[value] = index

    return None


if __name__ == "__main__":
    # The same value may be used twice only when it occurs at two indices.
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 3], 6) == (0, 1)
    assert two_sum([-4, 8, 1], 4) == (0, 2)
    assert two_sum([1, 2, 3], 10) is None
    print("All Two Sum examples passed.")
