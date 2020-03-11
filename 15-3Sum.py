class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype List[List[int]]
        """
        # Corner cases
        if nums is None:
            return []
        if len(nums) == 0:
            return []
        if len(nums) <= 2:
            return []

        nums.sort()

        res = set()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1

        return list(res)


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))

# Sample test case:
#   Input:
#       [-1, 0, 1, 2, -1, -4]
#   Output:
#       [
#           [-1, 0, 1],
#           [-1, -1, 2]
#       ]

# Performance Result:
#   Coding Time: -
#   Time Complexity: ?
#   Space Complexity: O(1)
#   Runtime: 2084 ms, faster than 12.52% of Python3
#       online submissions for 3Sum.
#   Memory Usage: 15.6 MB, less than 100.00% of Python3
#       online submissions for 3Sum.
