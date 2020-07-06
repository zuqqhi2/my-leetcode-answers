class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(log_3 n)
#   Space Complexity: O(1)
#   Runtime: 128 ms, faster than 17.12%
#   Memory Usage: 14 MB, less than 11.97%
