import collections


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pos = collections.defaultdict(list)
        max_dist = -1
        for i in range(len(s)):
            pos[s[i]].append(i)
            if len(pos[s[i]]) >= 2:
                max_dist = max(max_dist, i - pos[s[i]][0] - 1)

        return max_dist


# Performance Result:
#   Coding Time: 00:04:02
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 24 ms, faster than 97.89%
#   Memory Usage: 14.3 MB, less than 49.47%
