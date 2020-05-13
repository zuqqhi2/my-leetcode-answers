class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        upper_limit = max(candies)
        result = [False] * len(candies)
        for i in range(len(candies)):
            result[i] = candies[i] + extraCandies >= upper_limit
        return result


# Performance Result:
#   Coding Time: 00:05:13
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 28 ms, faster than 98.18%
#   Memory Usage: 14 MB, less than 100.00%
