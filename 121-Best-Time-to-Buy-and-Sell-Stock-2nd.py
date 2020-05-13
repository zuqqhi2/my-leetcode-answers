class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_gain = 0
        for i in range(1, len(prices)):
            max_gain = max(max_gain, prices[i] - min(prices[:i]))

        return max_gain


# Performance Result:
#   Coding Time: 00:06:20
#   Time Complexity: O(N^2)
#   Space Complexity: O(1)
#   Runtime: 5844 ms, faster than 5.00%
#   Memory Usage: 15.1 MB, less than 5.75%
