class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            max_wealth = max(max_wealth, sum(accounts[i]))

        return max_wealth


# Performance Result:
#   Coding Time: 00:01:33
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 52 ms, faster than 72.17%
#   Memory Usage: 14.2 MB, less than 59.84%
