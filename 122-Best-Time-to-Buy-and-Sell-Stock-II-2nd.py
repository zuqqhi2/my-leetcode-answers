class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        profit = 0
        stock_price = -1
        cur_idx = 1
        while cur_idx < len(prices):
            while cur_idx < len(prices) and prices[cur_idx] - prices[
                cur_idx - 1] <= 0:
                cur_idx += 1

            stock_price = prices[cur_idx - 1]

            while cur_idx < len(prices) and prices[cur_idx] - prices[
                cur_idx - 1] >= 0:
                cur_idx += 1

            profit += prices[cur_idx - 1] - stock_price
            stock_price = -1

        return profit


# Performance Result:
#   Coding Time: 00:08:42
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 60 ms, faster than 82.12%
#   Memory Usage: 15.1 MB, less than 7.32%
