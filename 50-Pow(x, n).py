class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        # if n is negative, change to positive
        repeat = n
        if n < 0:
            x = 1 / x
            repeat = -n

        result = 1.0
        cur_prod = x
        i = repeat
        while i > 0:
            if i % 2 == 1:
                result *= cur_prod
            cur_prod *= cur_prod
            i //= 2

        return result

# Sample Testcase:
#   Input:
#       2.00000, 10
#   Output:
#       1024.00000

# Performance Result:
#   Coding Time: 00:11:24
#   Time Complexity: O(log n)
#   Space Complexity: O(1)
#   Runtime: 40 ms, faster than 40.27% of Python3
#       online submissions for Pow(x, n).
#   Memory Usage: 13.8 MB, less than 6.90% of Python3
#       online submissions for Pow(x, n).
