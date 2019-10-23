# Algorithm: Dynamic Programming
# Recursion Formula
#   dp[i+1] = max(dp[i-1], ..., dp[0]) + v[i+1]
#   dp[0] = v[0]
#   dp[n-1] = max(dp[n-2], ..., dp[1]) + v[i+1]


class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Initialize DP
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp_without_0 = [0] * len(nums)
        dp_without_0[0] = 0
        dp_without_0[1] = nums[1]

        # Calculate DP
        max_money = dp[0]
        max_money_without_0 = dp[1]
        if dp[1] > max_money:
            max_money = dp[1]
        for house_id in range(2, len(nums)):
            local_max_money = 0
            local_max_money_witout_0 = 0
            for dp_id in range(0, house_id - 1):
                if dp[dp_id] > local_max_money and house_id < len(nums) - 1:
                    local_max_money = dp[dp_id]

                if dp_without_0[dp_id] > local_max_money_witout_0:
                    local_max_money_witout_0 = dp_without_0[dp_id]

            dp[house_id] = local_max_money + nums[house_id]
            if dp[house_id] > max_money:
                max_money = dp[house_id]

            dp_without_0[house_id] = local_max_money_witout_0 + nums[house_id]
            if dp_without_0[house_id] > max_money_without_0:
                max_money_without_0 = dp_without_0[house_id]

        return max(max_money, max_money_without_0)


# Sample test case:
#   Input:
#       [2,3,2]
#   Output:
#       3

# Performance Result:
#   Coding Time: 00:29:37
#   Time Complexity: O(n^2)
#   Space Complexity: O(n)
#   Runtime: 40 ms, faster than 53.74% of Python3
#       online submissions for House Robber II.
#   Memory Usage: 13.9 MB, less than 5.56% of Python3
#       online submissions for House Robber II.
