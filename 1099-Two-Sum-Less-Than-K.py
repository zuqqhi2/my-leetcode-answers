class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = -1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < k:
                    max_sum = max(max_sum, nums[i] + nums[j])

        return max_sum


# Performance Result:
#   Coding Time: 00:02:40
#   Time Complexity: O(NM)
#   Space Complexity: O(1)
#   Runtime: 124 ms, faster than 5.31%
#   Memory Usage: 14.3 MB, less than 50.69%
