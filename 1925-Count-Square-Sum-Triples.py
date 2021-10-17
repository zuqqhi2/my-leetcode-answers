import math


class Solution:
    def countTriples(self, n: int) -> int:
        res = 0

        for a in range(1, n):
            for b in range(a + 1, n + 1):
                c2 = a * a + b * b
                c = int(math.sqrt(c2))
                if c * c == c2 and 1 <= c <= n and c != a and c != b:
                    res += 2

        return res


# Performance Result:
#   Coding Time: 00:09:54
#   Time Complexity: O(N^2)
#   Space Complexity: O(1)
#   Runtime: 430 ms, faster than 56.97%
#   Memory Usage: 14.3 MB, less than 17.58%
