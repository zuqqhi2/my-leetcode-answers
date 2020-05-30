class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_total = -2 ** 31
        sub_total = 0
        for i in range(len(nums)):
            sub_total += nums[i]
            max_sub_total = max(max_sub_total, sub_total)
            if sub_total < 0:
                sub_total = 0

        return max_sub_total


# Performance Result:
#   Coding Time: 00:04:00
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 64 ms, faster than 81.93%
#   Memory Usage: 14.6 MB, less than 5.69%
