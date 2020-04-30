class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 0:
            return -1
        if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:
            return 1 if obstacleGrid[0][0] == 0 else 0

        # Dynamic Programming
        #   dp[y][x] = dp[y-1][x] + dp[y][x-1]
        dp = [[0 for _ in range(len(obstacleGrid[0]) + 1)] for _ in
              range(len(obstacleGrid) + 1)]
        dp[1][1] = 1

        for y in range(1, len(obstacleGrid) + 1):
            for x in range(1, len(obstacleGrid[0]) + 1):
                if y == 1 and x == 1:
                    continue

                if obstacleGrid[y - 1][x - 1] == 1:
                    continue

                if obstacleGrid[y - 2][x - 1] == 0 and obstacleGrid[y - 1][
                    x - 2] == 0:
                    dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
                elif obstacleGrid[y - 2][x - 1] == 0:
                    dp[y][x] = dp[y - 1][x]
                elif obstacleGrid[y - 1][x - 2] == 0:
                    dp[y][x] = dp[y][x - 1]

        return dp[-1][-1]


# Performance Result:
#   Coding Time: 00:11:10
#   Time Complexity: O(N M)
#   Space Complexity: O(N M)
#   Runtime: 40 ms, faster than 92.72%
#   Memory Usage: 13.8 MB, less than 8.89%
