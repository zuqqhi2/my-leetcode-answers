# Recursion Formula
# dp[0][0] = 1
# dp[0][j] =              dp[i][j-1] = 1
# dp[i][0] = dp[i-1][j]              = 1
# dp[i][j] = dp[i-1][j] + dp[i][j-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 and n == 0:
            return 0

        # Initialize DP
        dp = [[0 for j in range(m)] for i in range(n)]
        dp[0][0] = 1
        for i in range(n):
            dp[i][0] = 1
        for j in range(m):
            dp[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


s = Solution()
print(s.uniquePaths(7, 3))

# Sample Testcase:
#   Input:
#       m = 3, n = 2
#   Output:
#       3

# Performance Result:
#   Coding Time: 00:11:13
#   Time Complexity: O(mn)
#   Space Complexity: O(mn)
#   Runtime: 40 ms, faster than 44.84% of Python3
#       online submissions for Unique Paths.
#   Memory Usage: 13.8 MB, less than 5.77% of Python3
#       online submissions for Unique Paths.
