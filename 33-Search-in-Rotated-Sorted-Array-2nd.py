class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        min_val_idx = -1
        if nums[-1] > nums[0]:
            min_val_idx = 0
        if len(nums) == 2 and nums[0] > nums[1]:
            min_val_idx = 1

        # Find rotated point by binary search
        if min_val_idx == -1:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if mid > 0 and nums[mid - 1] > nums[mid]:
                    min_val_idx = mid
                    break

                if nums[mid] > nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1

        # Find target value
        left = 0
        right = min_val_idx - 1
        if target < nums[0]:
            left = min_val_idx
            right = len(nums) - 1
        elif min_val_idx == 0:
            right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# Performance Result:
#   Coding Time: 00:26:35
#   Time Complexity: O(log N)
#   Space Complexity: O(1)
#   Runtime: 48 ms, faster than 22.98%
#   Memory Usage: 14.2 MB, less than 6.29%
