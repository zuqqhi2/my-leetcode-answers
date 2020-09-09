class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cur_sum = 0
        cum_min = 1000
        for i in range(len(nums)):
            cur_sum += nums[i]
            cum_min = min(cum_min, cur_sum)

        return abs(cum_min) + 1 if cum_min < 0 else 1


# Performance Result:
#   Coding Time: 00:05:50
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 28 ms, faster than 88.71%
#   Memory Usage: 13.8 MB, less than 62.55%
