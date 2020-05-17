class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic Programming
        # dp[i]: number of used coins with total i value
        # dp[i + coins[j]] = min(dp[i] + 1)
        dp = [1_000_000] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            if i > 0 and dp[i] == 1_000_000:
                continue

            for j in range(len(coins)):
                if i + coins[j] >= len(dp):
                    continue

                dp[i + coins[j]] = min(dp[i + coins[j]], dp[i] + 1)

        if dp[-1] == 1_000_000:
            return -1
        else:
            return dp[-1]


# Performance Result:
#   Coding Time: 00:12:10
#   Time Complexity: O(NM)
#   Space Complexity: O(N)
#   Runtime: 2044 ms, faster than 21.59%
#   Memory Usage: 14 MB, less than 30.56%
