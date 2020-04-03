class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp = [1] * len(nums)
        max_length = dp[0]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

            max_length = max(max_length, dp[i])

        return max_length


# Performance Result:
#   Coding Time: 00:08:26
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 1176 ms, faster than 40.14% of Python3
#       online submissions for Longest Increasing Subsequence.
#   Memory Usage: 14.1 MB, less than 5.13% of Python3
#       online submissions for Longest Increasing Subsequence.
