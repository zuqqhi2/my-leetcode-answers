class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums[:] = sorted(nums)
        sum_min = 0
        for i in range(0, len(nums), 2):
            sum_min += min(nums[i], nums[i + 1])

        return sum_min


# Performance Result:
#   Coding Time: 00:04:10
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 292 ms, faster than 11.04%
#   Memory Usage: 16.8 MB, less than 84.57%
