class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        while n > 0:
            n //= 5
            zero_count += n
        return zero_count


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(log_5 N)
#   Space Complexity: O(1)
#   Runtime: 28 ms, faster than 78.94%
#   Memory Usage: 13.6 MB, less than 96.98%
