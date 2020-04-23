class Solution:
    def simulate(self, weights: List[int], D: int, cap: int) -> bool:
        num_days = 0
        while len(weights) > 0:
            num_days += 1
            shipped_weight = 0
            while len(weights) > 0 and shipped_weight < cap:
                shipped_weight += weights[0]
                if shipped_weight > cap:
                    break
                else:
                    weights.pop(0)

        if num_days <= D:
            return True
        else:
            return False

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        max_weight = max(weights)
        total_weight = sum(weights)

        # Binary search
        left = max(weights)  # never success when cap is less than this
        right = sum(weights)  # if cap is this, required date is 1 day
        while left <= right:
            mid = left + (right - left) // 2
            if self.simulate(weights[:], D, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


# Performance Result:
#   Coding Time: 00:24:07
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 8176 ms, faster than 5.02%
#   Memory Usage: 16.9 MB, less than 10.00%
