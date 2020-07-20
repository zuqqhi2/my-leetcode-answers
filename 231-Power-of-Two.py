class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False

        for i in range(int(math.sqrt(n)) + 2):
            if 2 ** i == n:
                return True

        return False


# Performance Result:
#   Coding Time: 00:03:49
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 9384 ms, faster than 7.95%
#   Memory Usage: 13.9 MB, less than 32.23%
