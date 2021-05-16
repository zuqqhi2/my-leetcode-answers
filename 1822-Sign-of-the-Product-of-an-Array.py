class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for num in nums:
            if num > 0:
                res *= 1
            elif num < 0:
                res *= -1
            else:
                res *= 0
                break

        return res


# Performance Result:
#   Coding Time: 00:01:30
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 56 ms, faster than 87.92%
#   Memory Usage: 14.1 MB, less than 99.81%
