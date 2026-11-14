"""Find the longest substring that contains no repeated characters.

A moving left boundary skips past the previous copy of a repeated character.
The first longest substring is returned when several have equal length.

Time: O(n). Extra space: O(min(n, alphabet size)).
"""


def longest_unique_substring(text: str) -> str:
    """Return the longest contiguous substring with all distinct characters."""
    last_seen: dict[str, int] = {}
    window_start = 0
    best_start = 0
    best_length = 0

    for index, character in enumerate(text):
        previous_index = last_seen.get(character, -1)
        if previous_index >= window_start:
            window_start = previous_index + 1

        last_seen[character] = index
        window_length = index - window_start + 1
        if window_length > best_length:
            best_start = window_start
            best_length = window_length

    return text[best_start : best_start + best_length]


if __name__ == "__main__":
    assert longest_unique_substring("abcabcbb") == "abc"
    assert longest_unique_substring("bbbbb") == "b"
    assert longest_unique_substring("pwwkew") == "wke"
    assert longest_unique_substring("dvdf") == "vdf"
    assert longest_unique_substring("abba") == "ab"
    assert longest_unique_substring("") == ""
    print("All Longest Unique Substring examples passed.")
