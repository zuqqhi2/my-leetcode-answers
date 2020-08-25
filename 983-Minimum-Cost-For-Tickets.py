class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # DP
        # dp[i]: i is an index of days arr
        # dp[0] = 1_000_000
        # dp[i + j] = min(dp[i + j], dp[i] + costs[0])
        # ...
        if len(days) == 0 or len(costs) == 0:
            return 0

        dp = [1_000_000] * (len(days) + 1)
        dp[0] = 0
        for i in range(len(days)):
            # 1 day pass
            dp[i + 1] = min(dp[i + 1], dp[i] + costs[0])
            # 7, 30 days pass
            is_done_7 = False
            is_done_30 = False
            for j in range(i, len(days)):
                diff = days[j] - days[i] + 1
                if not is_done_7 and diff > 7:
                    dp[j] = min(dp[j], dp[i] + costs[1])
                    is_done_7 = True
                elif not is_done_7 and j == len(days) - 1:
                    dp[j + 1] = min(dp[j + 1], dp[i] + costs[1])
                    is_done_7 = True

                if not is_done_30 and diff > 30:
                    dp[j] = min(dp[j], dp[i] + costs[2])
                    is_done_30 = True
                elif not is_done_30 and j == len(days) - 1:
                    dp[j + 1] = min(dp[j + 1], dp[i] + costs[2])
                    is_done_30 = True

                if is_done_7 and is_done_30:
                    break

        return dp[-1]


# Performance Result:
#   Coding Time: 00:31:17
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 92 ms, faster than 9.62%
#   Memory Usage: 13.9 MB, less than 68.88%
