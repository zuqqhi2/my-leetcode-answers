import collections


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_cnt = collections.Counter(text)

        is_end = False
        res = 0
        word_required = {'a': 1, 'b': 1, 'l': 2, 'o': 2, 'n': 1}
        while not is_end:
            for c in word_required:
                char_cnt[c] -= word_required[c]
                if char_cnt[c] < 0:
                    is_end = True

            res += 1 if not is_end else 0

        return res


# Performance Result:
#   Coding Time: 00:03:57
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 37.23%
#   Memory Usage: 14.2 MB, less than 87.66%
