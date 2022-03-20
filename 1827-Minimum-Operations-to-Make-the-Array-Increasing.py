class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        res = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            v = nums[i] - prev
            if v > 0:
                prev = nums[i]
            elif v == 0:
                res += 1
                prev += 1
            else:
                res += -v + 1
                prev = nums[i] + -v + 1

        return res


# Performance Result:
#   Coding Time: 00:16:23
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 142 ms, faster than 76.60%
#   Memory Usage: 14.6 MB, less than 62.08%
