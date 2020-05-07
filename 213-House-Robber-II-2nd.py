class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # dp[i] = max(dp[i - 1], dp[i] + dp[i - 2])
        dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        dp[0][0] = nums[0]
        dp[1][0] = max(nums[0], nums[1])
        dp[1][1] = nums[1]
        for i in range(2, len(nums)):
            if i == len(nums) - 1:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][1] + nums[i])
                continue

            for j in range(2):
                dp[i][j] = max(dp[i - 1][j], dp[i - 2][j] + nums[i])

        return max(dp[-1][0], dp[-1][1])


# Performance Result:
#   Coding Time: 00:12:22
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 28 ms, faster than 80.39%
#   Memory Usage: 14 MB, less than 5.56%
