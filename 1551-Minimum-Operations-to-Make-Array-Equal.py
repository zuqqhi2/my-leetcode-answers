class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 1:
            return sum([2 * i for i in range(1, ((n - 1) // 2) + 1)])
        else:
            return sum([(2 * i) + 1 for i in range(n // 2)])


# Performance Result:
#   Coding Time: 00:11:30
#   Time Complexity: O(n)
#   Space Complexity: O(N)
#   Runtime: 64 ms, faster than 49.81%
#   Memory Usage: 14.7 MB, less than 11.18%
