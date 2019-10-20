# Algorithm: Binary Search


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if len(nums) == 0:
            return 0
        if nums[-1] < target:
            return len(nums)
        if nums[0] > target:
            return 0

        leftIdx = 0
        prevLeftIdx = -1
        rightIdx = len(nums) - 1
        prevRightIdx = -1
        while leftIdx != prevLeftIdx or rightIdx != prevRightIdx:
            prevLeftIdx = leftIdx
            prevRightIdx = rightIdx

            midIdx = (leftIdx + rightIdx) // 2
            if nums[midIdx] > target:
                rightIdx = midIdx
            elif nums[midIdx] < target:
                leftIdx = midIdx
            else:
                return midIdx

        if nums[leftIdx] < target:
            return rightIdx
        else:
            return leftIdx

# Sample Testcase:
#   Input:
#       [1,3,5,6], 5
#   Output:
#       2

# Performance Result:
#   Coding Time: 00:19:48
#   Time Complexity: O(log n)
#   Space Complexity: O(1)
#   Runtime: 60 ms, faster than 63.63% of Python3
#       online submissions for Search Insert Position.
#   Memory Usage: 14.3 MB, less than 5.97% of Python3
#       online submissions for Search Insert Position.
