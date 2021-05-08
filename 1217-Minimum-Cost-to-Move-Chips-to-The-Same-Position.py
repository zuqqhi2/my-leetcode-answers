import collections


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        coin_pos = collections.Counter(position)

        min_cost = 1_000_000
        for p1 in coin_pos:
            cost = 0
            for p2 in coin_pos:
                if p1 == p2:
                    continue

                cost += coin_pos[p2] if abs(p1 - p2) % 2 == 1 else 0

            min_cost = min(min_cost, cost)

        return min_cost


# Performance Result:
#   Coding Time: 00:11:25 (most of time understanding how to calc the cost)
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 72 ms, faster than 5.64%
#   Memory Usage: 14.3 MB, less than 50.92%
