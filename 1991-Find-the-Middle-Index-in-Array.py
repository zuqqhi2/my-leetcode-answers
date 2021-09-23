class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        acc_nums = [0] * len(nums)
        acc_nums[0] = nums[0]
        for i in range(1, len(nums)):
            acc_nums[i] = acc_nums[i - 1] + nums[i]

        for i in range(len(nums)):
            if i == 0 and acc_nums[-1] - acc_nums[i] == 0:
                return i
            elif i > 0 and acc_nums[i - 1] == acc_nums[-1] - acc_nums[i]:
                return i
        return -1


# Performance Result:
#   Coding Time: 00:09:58
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 94.46%
#   Memory Usage: 14.2 MB, less than 48.69%
