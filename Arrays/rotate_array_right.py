"""Rotate a sequence right by a given number of positions.

The three-reversal method moves a suffix to the front in linear time. The
input is copied first, so the caller's sequence is left unchanged.

Time: O(n). Extra space: O(n) for the returned list.
"""

from typing import Sequence


def rotate_array_right(values: Sequence[int], steps: int) -> list[int]:
    """Return a right rotation; steps must be non-negative."""
    if steps < 0:
        raise ValueError("steps must be non-negative")

    rotated = list(values)
    if not rotated:
        return rotated

    shift = steps % len(rotated)

    def reverse(start: int, end: int) -> None:
        while start < end:
            rotated[start], rotated[end] = rotated[end], rotated[start]
            start += 1
            end -= 1

    reverse(0, len(rotated) - 1)
    reverse(0, shift - 1)
    reverse(shift, len(rotated) - 1)
    return rotated


if __name__ == "__main__":
    original = [1, 2, 3, 4, 5]
    assert rotate_array_right(original, 2) == [4, 5, 1, 2, 3]
    assert rotate_array_right(original, 7) == [4, 5, 1, 2, 3]
    assert rotate_array_right(original, 0) == original
    assert rotate_array_right([], 4) == []
    assert original == [1, 2, 3, 4, 5]

    try:
        rotate_array_right([1, 2], -1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative steps should raise ValueError")

    print("All Rotate Array Right examples passed.")
