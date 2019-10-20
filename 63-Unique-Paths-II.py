# Algorithm: Dynamic Programming
#   dp[i][j] = dp[i-1][j] + dp[i][j-1] (Down + Right)
#   dp[i][j] =              dp[i][j-1] if dp[i-1][j] is obstacle
#   dp[i][j] = dp[i-1][j]              if dp[i][j-1] is obstacle
#   dp[0][0] = 1
#   dp[0][j] = 1
#   dp[i][0] = 1


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if len(obstacleGrid) == 0:
            return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]:
            return 0

        # Initialize DP array
        sizeY = len(obstacleGrid)
        sizeX = len(obstacleGrid[0])
        dp = [[0 for _ in range(sizeX)] for _ in range(sizeY)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1

        # Fill in the DP array using recursion formula
        for y in range(0, sizeY):
            for x in range(0, sizeX):
                if y == 0 and x == 0:
                    continue

                dp[y][x] = 0
                if y >= 1:
                    if obstacleGrid[y - 1][x] == 0:
                        dp[y][x] += dp[y - 1][x]
                if x >= 1:
                    if obstacleGrid[y][x - 1] == 0:
                        dp[y][x] += dp[y][x - 1]

        return dp[-1][-1]

# Sample Testcase:
#   Input:
#       [
#         [0,0,0],
#         [0,1,0],
#         [0,0,0]
#       ]
#   Output:
#       2

# Performance Result:
#   Coding Time: 00:17:00
#   Time Complexity: O(mn)
#   Space Complexity: O(mn)
#   Runtime: 52 ms, faster than 85.41% of Python3
#       online submissions for Unique Paths II.
#   Memory Usage: 13.9 MB, less than 8.89% of Python3
#       online submissions for Unique Paths II.
