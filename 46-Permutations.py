# Algorithm: Recursion
# [1, 2, 3]
#   => permute([2, 3]) + permute([1, 3]) + permute([1, 2])
#   => [[2, 3], [3, 2]] + [[1, 3],


class Solution:
    def swap(self, nums):
        if len(nums) <= 1:
            return nums
        if len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]

        sub_permuted_sets = []
        for i in range(len(nums)):
            sub_nums = nums.copy()
            sub_nums.pop(i)

            sub_set = self.swap(sub_nums)
            sub_set = [[nums[i]] + arr for arr in sub_set]
            sub_permuted_sets += sub_set

        return sub_permuted_sets

    def permute(self, nums):
        if nums is None:
            return None
        elif len(nums) == 0:
            return [[]]
        elif len(nums) == 1:
            return [[nums[0]]]

        return self.swap(nums)


s = Solution()
print(s.permute([1, 2]))
print(s.permute([1, 2, 3]))

# Sample test case:
#   Input:
#       [1,2,3]
#   Output:
#       [
#           [1,2,3],
#           [1,3,2],
#           [2,1,3],
#           [2,3,1],
#           [3,1,2],
#           [3,2,1]
#       ]

# Performance Result:
#   Coding Time: 00:27:45
#   Time Complexity: O(n! / (n - k)!)
#   Space Complexity: O(n!)
#   Runtime: 52 ms, faster than 38.69% of Python3
#       online submissions for Permutations.
#   Memory Usage: 13.9 MB, less than 5.36% of Python3
#       online submissions for Permutations.
