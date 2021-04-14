class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1


# Performance Result:
#   Coding Time: 00:02:45
#   Time Complexity: O(log N)
#   Space Complexity: O(1)
#   Runtime: 236 ms, faster than 59.65%
#   Memory Usage: 15.5 MB, less than 90.13%
