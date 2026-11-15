"""Find the fewest coins needed to make an amount using unlimited coins.

Bottom-up dynamic programming builds the answer for every amount up to the
target. Return None when the target cannot be formed.

Time: O(amount * number_of_coins). Extra space: O(amount).
"""

from typing import Sequence


def minimum_coin_change(coins: Sequence[int], amount: int) -> int | None:
    """Return the minimum coin count; reject negative amounts/nonpositive coins."""
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if any(coin <= 0 for coin in coins):
        raise ValueError("coin denominations must be positive")

    unreachable = amount + 1
    best = [0] + [unreachable] * amount

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                best[current_amount] = min(
                    best[current_amount], best[current_amount - coin] + 1
                )

    return None if best[amount] == unreachable else best[amount]


if __name__ == "__main__":
    assert minimum_coin_change([1, 2, 5], 11) == 3
    assert minimum_coin_change([2], 3) is None
    assert minimum_coin_change([], 8) is None
    assert minimum_coin_change([2, 3], 0) == 0

    try:
        minimum_coin_change([0, 1], 4)
    except ValueError:
        pass
    else:
        raise AssertionError("zero-value coin should raise ValueError")

    try:
        minimum_coin_change([1], -1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative amount should raise ValueError")

    print("All Minimum Coin Change examples passed.")
