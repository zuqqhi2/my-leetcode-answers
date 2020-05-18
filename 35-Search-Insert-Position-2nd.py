class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left


# Performance Result:
#   Coding Time: 00:07:13
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 52 ms, faster than 48.52%
#   Memory Usage: 14.6 MB, less than 5.97%
