"""Find the shortest substring containing all characters of a pattern.

Character counts form a sliding window. The right edge grows the window
until it covers the pattern; then the left edge shrinks it to the smallest
valid window. Repeated pattern characters are counted individually.

Time: O(len(text) + len(pattern)). Extra space: O(k), where k is the number
of distinct characters stored in the count map.
"""

from collections import Counter


def minimum_window_substring(text: str, pattern: str) -> str:
    """Return the shortest covering substring, or an empty string if none exists.

    If several minimum windows have the same length, the earliest is returned.
    Character matching is exact and case-sensitive.
    """
    if not pattern or len(pattern) > len(text):
        return ""

    needed = Counter(pattern)
    missing = len(pattern)
    left = 0
    best_start = 0
    best_length = len(text) + 1

    for right, character in enumerate(text):
        if needed[character] > 0:
            missing -= 1
        needed[character] -= 1

        if missing == 0:
            while needed[text[left]] < 0:
                needed[text[left]] += 1
                left += 1

            window_length = right - left + 1
            if window_length < best_length:
                best_start = left
                best_length = window_length

            needed[text[left]] += 1
            missing += 1
            left += 1

    if best_length > len(text):
        return ""
    return text[best_start : best_start + best_length]


if __name__ == "__main__":
    assert minimum_window_substring("ADOBECODEBANC", "ABC") == "BANC"
    assert minimum_window_substring("AAABBC", "AABC") == "AABBC"
    assert minimum_window_substring("a", "a") == "a"
    assert minimum_window_substring("a", "aa") == ""
    assert minimum_window_substring("anything", "") == ""
    assert minimum_window_substring("abxxcd", "ac") == "abxxc"
    print("All Minimum Window Substring examples passed.")
