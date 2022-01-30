class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = format(n, 'b')
        for i in range(1, len(bits)):
            if bits[i - 1] == bits[i]:
                return False

        return True


# Performance Result:
#   Coding Time: 00:03:17
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 50 ms, faster than 17.31%
#   Memory Usage: 13.9 MB, less than 98.08%
