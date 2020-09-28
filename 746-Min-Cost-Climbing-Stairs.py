class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[i] for i in range(len(cost))]
        dp.append(0)
        cost.append(0)
        for i in range(2, len(dp)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return dp[-1]


# Performance Result:
#   Coding Time: 00:10:17
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 56 ms, faster than 83.91%
#   Memory Usage: 14.5 MB, less than 9.67%
