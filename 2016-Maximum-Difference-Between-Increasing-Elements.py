class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                if diff > res and diff > 0:
                    res = diff

        return res


# Performance Result:
#   Coding Time: 00:05:23
#   Time Complexity: O(N^2)
#   Space Complexity: O(1)
#   Runtime: 293 ms, faster than 19.74%
#   Memory Usage: 16.5 MB, less than 5.41%
