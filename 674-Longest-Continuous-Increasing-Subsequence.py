class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        res = 0
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                res = max(res, cur)
                cur = 1
            else:
                cur += 1

        return max(res, cur)


# Performance Result:
#   Coding Time: 00:03:01
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 72 ms, faster than 90.23%
#   Memory Usage: 15.2 MB, less than 100.00%
