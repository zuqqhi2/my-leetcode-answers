class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0

        # Dynamic Programming
        #   dp[0][0] = 1
        #   dp[0][x] = dp[y][0] = 0
        #   dp[y+1][x+1] = dp[y][x+1] + dp[y+1][x]
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        dp[1][1] = 1

        for y in range(1, n + 1):
            for x in range(1, m + 1):
                if y == 1 and x == 1:
                    continue
                dp[y][x] = dp[y - 1][x] + dp[y][x - 1]

        return dp[-1][-1]


# Performance Result:
#   Coding Time: 00:10:14
#   Time Complexity: O(NM)
#   Space Complexity: O(NM)
#   Runtime: 36 ms, faster than 16.83%
#   Memory Usage: 13.6 MB, less than 5.77%
