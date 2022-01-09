class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, key=lambda x: -x)
        for i in range(2, len(nums)):
            if nums[i - 2] < nums[i - 1] + nums[i]:
                return nums[i - 2] + nums[i - 1] + nums[i]

        return 0


# Performance Result:
#   Coding Time: 00:21:17
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 188 ms, faster than 72.61%
#   Memory Usage: 15.8 MB, less than 20.03%
