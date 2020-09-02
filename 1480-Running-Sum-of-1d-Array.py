class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        acc = nums[0]
        for i in range(1, len(nums)):
            nums[i] += acc
            acc = nums[i]

        return nums


# Performance Result:
#   Coding Time: 00:01:30
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 52 ms, faster than 42.33%
#   Memory Usage: 14.2 MB, less than 16.52%
