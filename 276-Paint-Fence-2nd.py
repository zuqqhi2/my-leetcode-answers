class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k

        same = k
        diff = k * (k - 1)
        for i in range(2, n):
            same, diff = diff, (same + diff) * (k - 1)

        return same + diff


# Performance Result:
#   Coding Time: 00:07:16
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 28 ms, faster than 78.64%
#   Memory Usage: 14 MB, less than 100.00%
