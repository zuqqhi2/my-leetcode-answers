class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices) - 1):
            is_appended = False
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    res.append(prices[i] - prices[j])
                    is_appended = True
                    break
            if not is_appended:
                res.append(prices[i])

        res.append(prices[-1])
        return res


# Performance Result:
#   Coding Time: 00:05:31
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 52 ms, faster than 71.56%
#   Memory Usage: 14.4 MB, less than 19.51%
