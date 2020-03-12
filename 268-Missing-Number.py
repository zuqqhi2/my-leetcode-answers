class Solution:
    def missingNumber(self, nums) -> int:
        """
        :type List[int]
        """
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return nums[-1] + 1


# Sample test case:
#   Input:
#       [3,0,1]
#   Output:
#       2

# Performance Result:
#   Coding Time: 00:03:49
#   Time Complexity: O(N log N)
#   Space Complexity: O(1)
#   Runtime: 148 ms, faster than 41.76% of Python3
#       online submissions for Missing Number.
#   Memory Usage: 13.9 MB, less than 96.77% of Python3
#       online submissions for Missing Number.
