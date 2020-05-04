class Solution:
    def rob(self, nums: List[int]) -> int:
        # Dynamic Programming
        dp = [0] * len(nums)
        result = 0
        for i in range(len(nums)):
            dp[i] = nums[i]
            old_max = 0
            for j in range(i - 1):
                old_max = max(old_max, dp[j])
            dp[i] += old_max
            result = max(result, dp[i])

        return result


# Performance Result:
#   Coding Time: 00:12:56
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 14.68%
#   Memory Usage: 13.9 MB, less than 9.09%
