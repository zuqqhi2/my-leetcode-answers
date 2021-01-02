import functools


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return functools.reduce(lambda a, b: a ^ b,
                                [start + 2 * i for i in range(n)])


# Performance Result:
#   Coding Time: 00:03:40
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 53.88%
#   Memory Usage: 14.4 MB, less than 16.75%
