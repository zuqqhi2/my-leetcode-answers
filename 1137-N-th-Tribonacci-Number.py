class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1

        tmp = [0] * (n + 1)
        tmp[0] = 0
        tmp[1] = tmp[2] = 1
        for i in range(3, n + 1):
            tmp[i] = tmp[i - 1] + tmp[i - 2] + tmp[i - 3]

        return tmp[-1]


# Performance Result:
#   Coding Time: 00:04:34
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 40.33%
#   Memory Usage: 14.1 MB, less than 100.00%
