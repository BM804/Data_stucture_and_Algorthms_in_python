"""Return each array position's product without using division.

For each index, multiply the product of values to its left by the product
of values to its right. This naturally handles zeros and negative values.

Time: O(n). Extra space: O(1), excluding the returned list.
"""

from typing import Sequence


def product_except_self(numbers: Sequence[int]) -> list[int]:
    """Build products excluding each index; empty input returns an empty list."""
    products = [1] * len(numbers)

    prefix = 1
    for index, value in enumerate(numbers):
        products[index] = prefix
        prefix *= value

    suffix = 1
    for index in range(len(numbers) - 1, -1, -1):
        products[index] *= suffix
        suffix *= numbers[index]

    return products


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([0, 1, 2, 0]) == [0, 0, 0, 0]
    assert product_except_self([]) == []
    assert product_except_self([7]) == [1]
    print("All Product Except Self examples passed.")
