class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles // numExchange > 0:
            res += numBottles // numExchange
            numBottles = (numBottles // numExchange) + (
                    numBottles % numExchange)

        return res


# Performance Result:
#   Coding Time: 00:05:20
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 52 ms, faster than 6.98%
#   Memory Usage: 14 MB, less than 98.56%
