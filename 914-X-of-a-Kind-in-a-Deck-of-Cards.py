class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from fractions import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N log^2 N)
#   Space Complexity: O(N)
#   Runtime: 276 ms, faster than 5.22%
#   Memory Usage: 14.1 MB, less than 11.11%
