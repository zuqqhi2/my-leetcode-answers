class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = -1
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_sum += nums[i]
            else:
                max_sum = max(max_sum, cur_sum)
                cur_sum = nums[i]

        return max(max_sum, cur_sum)


# Performance Result:
#   Coding Time: 00:03:59
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 32 ms, faster than 82.18%
#   Memory Usage: 14.1 MB, less than 89.27%
