class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        low_idx = 0
        high_idx = len(nums) - 1

        # no target value in the list
        # if no rotated and target is out of value range
        if nums[low_idx] < nums[high_idx]:
            if target < nums[low_idx]:
                return -1
            elif target > nums[high_idx]:
                return -1

        # Binary search to find the pivot idx
        while low_idx <= high_idx:
            if nums[low_idx] == target:
                return low_idx
            elif nums[high_idx] == target:
                return high_idx

            mid_idx = low_idx + (high_idx - low_idx) // 2
            if nums[mid_idx] == target:
                return mid_idx

            if nums[low_idx] <= nums[mid_idx]:
                if nums[low_idx] <= target < nums[mid_idx]:
                    high_idx = mid_idx - 1
                else:
                    low_idx = mid_idx + 1
            else:
                if nums[mid_idx] < target <= nums[high_idx]:
                    low_idx = mid_idx + 1
                else:
                    high_idx = mid_idx - 1

        return -1


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
print(s.search([4, 5, 6, 7, 8, 1, 2, 3], 8))
print(s.search([1, 3], 2))
print(s.search([3, 1], 0))
print(s.search([5, 1, 2, 3, 4], 1))


# Sample test case:
#   Input:
#       nums = [4,5,6,7,0,1,2], target = 0
#   Output:
#       4

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(log2 N)
#   Space Complexity: O(1)
#   Runtime: 40 ms, faster than 65.99% of Python3
#       online submissions for Search in Rotated Sorted Array.
#   Memory Usage: 12.9 MB, less than 100.00% of Python3
#       online submissions for Search in Rotated Sorted Array.
