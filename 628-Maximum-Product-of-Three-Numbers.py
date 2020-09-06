class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        s1 = nums[-1] * nums[-2] * nums[-3]  # for positive
        s2 = nums[-1] * nums[0] * nums[1]  # for negative
        return max(s1, s2)


# Performance Result:
#   Coding Time: 00:05:42
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 272 ms, faster than 85.14%
#   Memory Usage: 14.7 MB, less than 96.09%
