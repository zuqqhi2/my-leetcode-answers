class Solution:
    def findMin(self, nums) -> int:
        low_idx = 0
        high_idx = len(nums) - 1

        min_val = 1e+6
        while low_idx < high_idx:
            mid_idx = low_idx + (high_idx - low_idx) // 2
            if nums[mid_idx] < min_val:
                min_val = nums[mid_idx]

            print(low_idx, mid_idx, high_idx)
            if nums[mid_idx] > nums[high_idx]:
                low_idx = mid_idx + 1
            elif nums[mid_idx] < nums[high_idx]:
                high_idx = mid_idx - 1

        return min(nums[low_idx], min_val)


s = Solution()
print(s.findMin([3,4,5,1,2]))
print(s.findMin([4,5,6,7,0,1,2]))


# Sample test case:
#   Input:
#       [3,4,5,1,2]
#   Output:
#       1

# Performance Result:
#   Coding Time: 00:18:56
#   Time Complexity: O(log2 N)
#   Space Complexity: O(1)
#   Runtime: 40 ms, faster than 58.51% of Python3
#       online submissions for Find Minimum in Rotated Sorted Array.
#   Memory Usage: 12.9 MB, less than 100.00% of Python3
#       online submissions for Find Minimum in Rotated Sorted Array.
