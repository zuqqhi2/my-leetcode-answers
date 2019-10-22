# Algorithm: DP
# Recursion Formula
#   dp[i+1] = max(dp[0], ..., dp[i-1]) + v[i+1]
#   dp[0] = v[0]


class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Initialize DP array
        dp = [0] * len(nums)
        dp[0] = nums[0]

        max_money = dp[0]
        for house in range(1, len(nums)):
            local_max_money = 0
            for subHouse in range(0, house - 1):
                if local_max_money < dp[subHouse]:
                    local_max_money = dp[subHouse]

            local_max_money += nums[house]
            dp[house] = local_max_money
            if max_money < dp[house]:
                max_money = dp[house]

        return max_money


s = Solution()
print(s.rob([2, 1]))

# Sample test case:
#   Input:
#       [1,2,3,1]
#   Output:
#       4

# Performance Result:
#   Coding Time: 00:15:18
#   Time Complexity: O(n^2)
#   Space Complexity: O(n)
#   Runtime: 36 ms, faster than 81.38% of Python3
#       online submissions for House Robber.
#   Memory Usage: 13.9 MB, less than 9.09% of Python3
#       online submissions for House Robber.
