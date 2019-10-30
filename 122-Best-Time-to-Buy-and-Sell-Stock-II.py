# Algorithm: Backtrack


class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 0:
            return 0

        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))

# Sample test case:
#   Input:
#       [7,1,5,3,6,4]
#   Output:
#       7

# Performance Result:
#   Coding Time: 00:33:50
#   Time Complexity: O(n)
#   Space Complexity: O(1)
#   Runtime: 60 ms, faster than 99.69% of Python3
#       online submissions for Best Time to Buy and Sell Stock II.
#   Memory Usage: 14.7 MB, less than 7.32% of Python3
#       online submissions for Best Time to Buy and Sell Stock II.
