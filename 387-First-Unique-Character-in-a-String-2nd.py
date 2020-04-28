from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(int)
        first_idx = {}
        for i in range(len(s)):
            freq[s[i]] += 1
            if s[i] not in first_idx:
                first_idx[s[i]] = i

        result = 1_000_000
        for k in first_idx.keys():
            if freq[k] == 1:
                result = min(result, first_idx[k])

        return result if result < 1_000_000 else -1


# Performance Result:
#   Coding Time: 00:04:40
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 132 ms, faster than 45.49%
#   Memory Usage: 13.8 MB, less than 6.52%
