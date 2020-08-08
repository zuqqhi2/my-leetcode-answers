class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0

        # dp[n + 1][c_i] = min(dp[n][c_j] + costs[n + 1][c_i], ...) (j != i)
        dp = [[0 for _ in range(len(costs[0]) + 1)] for _ in
              range(len(costs) + 1)]
        for i in range(1, len(costs) + 1):
            for c in range(1, len(costs[0]) + 1):
                for cf in range(1, len(costs[0]) + 1):
                    if c == cf:
                        continue

                    if dp[i][c] == 0:
                        dp[i][c] = dp[i - 1][cf] + costs[i - 1][c - 1]
                    else:
                        dp[i][c] = min(dp[i][c],
                                       dp[i - 1][cf] + costs[i - 1][c - 1])

        return min(dp[-1][1:])

# Performance Result:
#   Coding Time: 00:18:25
#   Time Complexity: O(NM^2) M = num colors
#   Space Complexity: O(NM)
#   Runtime: 72 ms, faster than 51.31%
#   Memory Usage: 13.9 MB, less than 51.99%
