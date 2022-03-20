class Solution:
    def check(self, nums: List[int]) -> bool:
        min_val = min(nums)
        argmin = -1
        for i in range(len(nums)):
            if nums[i] == min_val and nums[i] < nums[i - 1]:
                argmin = i

        for i in range(1, len(nums)):
            pos = (argmin + i) % len(nums)
            if nums[pos] < nums[pos - 1]:
                return False

        return True


# Performance Result:
#   Coding Time: 00:13:04
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 63 ms, faster than 19.02%
#   Memory Usage: 13.8 MB, less than 97.21%
