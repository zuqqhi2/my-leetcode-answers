class Solution:
    def backtrack(self, cur_arr, nums, first=0):
        print(cur_arr, first)
        if first == len(nums):
            return [cur_arr]

        result = []
        result += self.backtrack(cur_arr + [nums[first]], nums, first + 1)
        result += self.backtrack(cur_arr, nums, first + 1)

        return result


    def subsets(self, nums):
        if nums is None:
            return None
        elif len(nums) == 0:
            return [[]]
        elif len(nums) == 1:
            return [[], [nums[0]]]

        result = self.backtrack([], nums)

        return result


# Sample test case:
#   Input:
#       [1,2,3]
#   Output:
#       [
#         [3],
#         [1],
#         [2],
#         [1,2,3],
#         [1,3],
#         [2,3],
#         [1,2],
#         []
#       ]

# Performance Result:
#   Coding Time: 00:24:11
#   Time Complexity: O(n)
#   Space Complexity: O(2^n)
#   Runtime: 40 ms, faster than 75.92% of Python3
#       online submissions for Subsets.
#   Memory Usage: 14 MB, less than 5.95% of Python3
#       online submissions for Subsets.
