class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        left_idx = 0
        right_idx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                left_idx = i + 1
                right_idx = i + 1
            else:
                max_num = max(max_num, right_idx - left_idx + 1)
                right_idx = i + 1

        return max_num


# Performance Result:
#   Coding Time: 00:02:16
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 388 ms, faster than 9.81%
#   Memory Usage: 14.4 MB, less than 50.05%
