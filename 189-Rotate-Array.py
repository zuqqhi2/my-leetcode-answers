class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


# Performance Result:
#   Coding Time: 00:03:40
#   Time Complexity: O(1)
#   Space Complexity: O(1)
#   Runtime: 116 ms, faster than 26.60%
#   Memory Usage: 15.3 MB, less than 46.04%
