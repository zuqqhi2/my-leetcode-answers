class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        d = numBottles // numExchange
        while d > 0:
            res += d
            numBottles = (d) + (numBottles % numExchange)
            d = numBottles // numExchange

        return res


# Performance Result:
#   Coding Time: 00:05:20
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 24 ms, faster than 94.35%
#   Memory Usage: 14.2 MB, less than 70.18%
