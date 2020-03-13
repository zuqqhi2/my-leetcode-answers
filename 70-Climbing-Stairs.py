class Solution:
    def climbStairs(self, n: int) -> int:
        # Corner cases
        if n == 0:
            return 0
        elif n == 1:
            return 1

        # Dynamic Programming
        #   dp[1] = 1
        #   dp[2] = 2
        #   dp[i] = dp[i - 1] + dp[i - 2]  # 1 step + 2 steps
        dp = [1, 2]  # keep only last 2
        for i in range(3, n + 1):
            dp.append(dp[0] + dp[1])
            del dp[0]

        return dp[-1]


s = Solution()
print(s.climbStairs(3))


# Sample test case:
#   Input:
#       [3,0,1]
#   Output:
#       2

# Performance Result:
#   Coding Time: 00:06:19
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 16 ms, faster than 99.50% of Python3
#       online submissions for Climbing Stairs.
#   Memory Usage: 12.6 MB, less than 100.00% of Python3
#       online submissions for Climbing Stairs.
