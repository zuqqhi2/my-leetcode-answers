class Solution:
    def generatePowerSet(self, nums, cur_pos=0, cur_res=[]):
        if cur_pos >= len(nums):
            return [cur_res]

        # Skip
        result = self.generatePowerSet(nums, cur_pos + 1, cur_res)
        # Take
        result.extend(
            self.generatePowerSet(nums, cur_pos + 1, cur_res + [nums[cur_pos]]))

        return result

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.generatePowerSet(nums)


# Performance Result:
#   Coding Time: 00:11:19
#   Time Complexity: O(N 2^N)
#   Space Complexity: O(N 2^N)
#   Runtime: 28 ms, faster than 89.29% of Python3
#       online submissions for Subsets.
#   Memory Usage: 14.2 MB, less than 5.95% of Python3
#       online submissions for Subsets.
