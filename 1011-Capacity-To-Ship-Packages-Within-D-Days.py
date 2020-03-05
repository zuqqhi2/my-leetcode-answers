class Solution:
    def simulate(self, weights, D, limit) -> bool:
        package_idx = -1
        for day in range(D):
            sum_weights = 0
            while sum_weights <= limit and package_idx < len(weights):
                package_idx += 1
                if package_idx < len(weights):
                    sum_weights += weights[package_idx]

            package_idx -= 1

        if package_idx == len(weights) - 1:
            return True
        else:
            return False

    def shipWithinDays(self, weights, D: int) -> int:
        if len(weights) == 1:
            return weights[0]

        # Binary search
        start_limit = 0  # always False
        end_limit = sum(weights)  # always True
        lowest_limit = 1e+6
        while start_limit <= end_limit:
            mid_limit = start_limit + (end_limit - start_limit) // 2
            if self.simulate(weights, D, mid_limit):
                end_limit = mid_limit - 1
                if mid_limit < lowest_limit:
                    lowest_limit = mid_limit
            else:
                start_limit = mid_limit + 1

        return lowest_limit


s = Solution()
print(s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(s.shipWithinDays([3, 2, 2, 4, 1, 4], 3))
print(s.shipWithinDays([1, 2, 3, 1, 1], 4))


# Sample test case:
#   Input:
#       weights = [1,2,3,4,5,6,7,8,9,10], D = 5
#   Output:
#       15

# Performance Result:
#   Coding Time: 00:46:01
#   Time Complexity: O(N log2 N)
#   Space Complexity: O(1)
#   Runtime: 1588 ms, faster than 5.14% of Python3
#       online submissions for Capacity To Ship Packages Within D Days.
#   Memory Usage: 16 MB, less than 10.00% of Python3
#       online submissions for Capacity To Ship Packages Within D Days.
