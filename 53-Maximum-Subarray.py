# dp[i+1] = max(nums[i+1] + dp[i], nums[i+1])
class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 0:
            return 0

        # Check 1st number before loop
        dp = [0] * len(nums)
        dp[0] = nums[0]
        maxSum = dp[0]
        for curIdx in range(1, len(nums)):
            dp[curIdx] = max(dp[curIdx - 1] + nums[curIdx], nums[curIdx])
            if dp[curIdx] > maxSum:
                maxSum = dp[curIdx]

        return maxSum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# Sample Testcase:
#   Input:
#       [-2,1,-3,4,-1,2,1,-5,4]
#   Output:
#       6

# Performance Result:
#   Coding Time: 00:30:24
#   Time Complexity: O(n)
#   Space Complexity: O(n)
#   Runtime: 80 ms, faster than 52.60% of Python3
#       online submissions for Maximum Subarray.
#   Memory Usage: 14.7 MB, less than 5.69% of Python3
#       online submissions for Maximum Subarray.
