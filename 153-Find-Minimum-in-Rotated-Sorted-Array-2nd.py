class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[0]


# Performance Result:
#   Coding Time: 00:01:18
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 44 ms, faster than 15.74% of Python3
#       online submissions for Find Minimum in Rotated Sorted Array.
#   Memory Usage: 13.9 MB, less than 6.00% of Python3
#       online submissions for Find Minimum in Rotated Sorted Array.
