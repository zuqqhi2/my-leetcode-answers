class Solution:
    def lengthOfLIS(self, nums) -> int:
        if len(nums) == 0:
            return 0

        dp = [1] * len(nums)
        maxLIS = 1
        for i in range(1, len(nums)):
            maxSubLIS = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxSubLIS = max(dp[j], maxSubLIS)

            dp[i] = maxSubLIS + 1

            maxLIS = max(dp[i], maxLIS)

        return maxLIS

# Sample Testcase:
#   Input:
#       [10,9,2,5,3,7,101,18]
#   Output:
#       4

# Performance Result:
#   Coding Time: 00:28:51
#   Time Complexity: O(n^2)
#   Space Complexity: O(n)
#   Runtime: 992 ms, faster than 52.27% of Python3
#       online submissions for Longest Increasing Subsequence.
#   Memory Usage: 13.8 MB, less than 5.13% of Python3
#       online submissions for Longest Increasing Subsequence.
