import collections


class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(1, len(s)):
            max_score = max(max_score, collections.Counter(s[:i])['0'] +
                            collections.Counter(s[i:])['1'])

        return max_score


# Performance Result:
#   Coding Time: 00:05:22
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 132 ms, faster than 6.97%
#   Memory Usage: 14.3 MB, less than 14.99%
