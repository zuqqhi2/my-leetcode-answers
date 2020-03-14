class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        """
        :param List[int] nums: number list
        :param int target: target number
        :rtype: int
        :return: number of combinations to make target number with sum
        """
        # Corner cases
        if nums is None:
            return 0
        if len(nums) == 0:
            return 0
        if len(nums) == 1 and nums[0] != target:
            return 0
        elif len(nums) == 1 and nums[0] == target:
            return 1

        # Dynamic Programming
        nums = sorted(nums)
        combs = [1] + [0] * target

        for i in range(target + 1):
            for num in nums:
                if i < num:
                    break
                if i == num:
                    combs[i] += 1
                if i > num:
                    combs[i] += combs[i - num]

        return combs[target]


s = Solution()
print(s.combinationSum4([1, 2, 3], 4))

# Sample test case:
#   Input:
#       nums = [1, 2, 3], target = 4
#   Output:
#       7

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(NM)
#   Space Complexity: O(N)
#   Runtime: 48 ms, faster than 34.17% of Python3 online submissions for Combination Sum IV.
#   Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Combination Sum IV.
