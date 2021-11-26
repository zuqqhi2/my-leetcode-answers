class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set(c for c in s if c.isdecimal())
        if len(digits) < 2:
            return -1
        else:
            return list(sorted(digits))[-2]


# Performance Result:
#   Coding Time: 00:06:25
#   Time Complexity: O(N log2 N)
#   Space Complexity: O(N)
#   Runtime: 41 ms, faster than 41.84%
#   Memory Usage: 14.4 MB, less than 22.55%
