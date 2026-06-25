from __future__ import annotations

from bisect import bisect_left


def longest_increasing_subsequence(values: list[int]) -> int:
    """Return the length of the longest strictly increasing subsequence."""
    tails: list[int] = []

    for value in values:
        index = bisect_left(tails, value)
        if index == len(tails):
            tails.append(value)
        else:
            tails[index] = value

    return len(tails)


def edit_distance(left: str, right: str) -> int:
    """Compute Levenshtein edit distance using O(min(n, m)) memory."""
    if len(left) < len(right):
        left, right = right, left

    previous = list(range(len(right) + 1))

    for i, left_char in enumerate(left, start=1):
        current = [i]
        for j, right_char in enumerate(right, start=1):
            insertion = current[j - 1] + 1
            deletion = previous[j] + 1
            substitution = previous[j - 1] + (left_char != right_char)
            current.append(min(insertion, deletion, substitution))
        previous = current

    return previous[-1]
