class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g[:] = sorted(g)
        s[:] = sorted(s)
        res = 0
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j] >= g[i]:
                    res += 1
                    del s[j]
                    break

        return res


# Performance Result:
#   Coding Time: 00:07:37
#   Time Complexity: O(NM)
#   Space Complexity: O(1)
#   Runtime: 1292 ms, faster than 5.46%
#   Memory Usage: 15.4 MB, less than 79.29%
