class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1_num = 0
        max1_idx = 0
        for i in range(len(nums)):
            if nums[i] > max1_num:
                max1_num = nums[i]
                max1_idx = i

        del nums[max1_idx]

        max2_num = 0
        max2_idx = 0
        for i in range(len(nums)):
            if nums[i] > max2_num:
                max2_num = nums[i]
                max2_idx = i

        return (max1_num - 1) * (max2_num - 1)


# Performance Result:
#   Coding Time: 00:03:53
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 52 ms, faster than 53.02%
#   Memory Usage: 14.2 MB, less than 100.00%
