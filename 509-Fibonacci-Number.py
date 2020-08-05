class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        else:
            return self.fib(N - 1) + self.fib(N - 2)


# Performance Result:
#   Coding Time: 00:01:56
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 1056 ms, faster than 10.95%
#   Memory Usage: 13.9 MB, less than 21.68%
