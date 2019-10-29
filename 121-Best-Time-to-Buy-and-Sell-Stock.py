class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            return 0

        max_profit = 0
        min_price = 1e+6
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))

# Sample test case:
#   Input:
#       [7,1,5,3,6,4]
#   Output:
#       5

# Performance Result:
#   Coding Time: 00:23:48
#   Time Complexity: O(n)
#   Space Complexity: O(1)
#   Runtime: 68 ms, faster than 93.96% of Python3
#       online submissions for Best Time to Buy and Sell Stock.
#   Memory Usage: 14.5 MB, less than 5.75% of Python3
#       online submissions for Best Time to Buy and Sell Stock.
