class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        is_minus = False
        if num < 0:
            is_minus = True
            num *= -1

        res = ""
        while num >= 7:
            res = str(num % 7) + res
            num //= 7

        if num > 0:
            res = str(num) + res

        return "-" + res if is_minus else res


# Performance Result:
#   Coding Time: 00:07:21
#   Time Complexity: O(log_7 N)
#   Space Complexity: O(1)
#   Runtime: 40 ms, faster than 20.12%
#   Memory Usage: 14.2 MB, less than 100.00%
