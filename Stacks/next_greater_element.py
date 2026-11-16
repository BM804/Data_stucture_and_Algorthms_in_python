"""Find the next strictly greater value to the right of each array element.

Indices whose next greater value is not known stay on a stack. When a
larger value appears, it resolves every smaller value at the top.

Time: O(n). Extra space: O(n).
"""

from typing import Sequence


def next_greater_elements(values: Sequence[int]) -> list[int]:
    """Return each element's next strictly greater value, or -1 if absent."""
    answers = [-1] * len(values)
    unresolved: list[int] = []

    for index, value in enumerate(values):
        while unresolved and values[unresolved[-1]] < value:
            answers[unresolved.pop()] = value
        unresolved.append(index)

    return answers


if __name__ == "__main__":
    assert next_greater_elements([4, 5, 2, 25]) == [5, 25, 25, -1]
    assert next_greater_elements([13, 7, 6, 12]) == [-1, 12, 12, -1]
    assert next_greater_elements([2, 2, 3]) == [3, 3, -1]
    assert next_greater_elements([]) == []
    print("All Next Greater Element examples passed.")
