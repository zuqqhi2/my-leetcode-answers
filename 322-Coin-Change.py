# Algorithm: Dynamic Programming
# Recursion Formula
#   dp[i][j] : i is coin id, j is amount
#   dp[i+1][j] = min(dp[i][j], dp[i][j-a[i]] + 1, dp[i][j-2*a[i]] + 2, ...)
class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        elif len(coins) == 0:
            return -1

        # Initialize DP array
        initial_val = 1000000
        dp = [initial_val for _ in range(amount + 1)]
        dp[0] = 0

        # Loop
        for a in range(amount + 1):
            for i in range(len(coins)):
                if a >= coins[i]:
                    dp[a] = min(dp[a], dp[a - coins[i]] + 1)

        if dp[amount] == initial_val:
            return -1
        else:
            return dp[amount]


s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([2], 3))
print(s.coinChange([1, 2], 2))
print(s.coinChange([2, 5, 10, 1], 27))


# Sample test case:
#   Input:
#       s = "leetcode"
#       wordDict = ["leet", "code"]
#   Output:
#       True

# Performance Result:
#   Coding Time: Timeout
#   Time Complexity: O(n * a)
#   Space Complexity: O(a)
#   Runtime: 1720 ms, faster than 21.91% of Python3
#       online submissions for Coin Change.
#   Memory Usage: 12.9 MB, less than 100.00% of Python3
#       online submissions for Coin Change.
