class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res_prod = 1
        res_sum = 0
        while n > 0:
            cur_digit = n % 10
            res_prod *= cur_digit
            res_sum += cur_digit
            n //= 10

        return res_prod - res_sum


# Performance Result:
#   Coding Time: 00:01:34
#   Time Complexity: O(log_10 N)
#   Space Complexity: O(1)
#   Runtime: 12 ms, faster than 100.00%
#   Memory Usage: 14 MB, less than 99.95%
