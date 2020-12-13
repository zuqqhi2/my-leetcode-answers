class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        max_limit = int(sqrt(num)) + 1
        for i in range(max_limit):
            if num == i ** 2:
                return True

        return False


# Performance Result:
#   Coding Time: 00:14:14
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 60 ms, faster than 5.62%
#   Memory Usage: 14.2 MB, less than 40.72%
