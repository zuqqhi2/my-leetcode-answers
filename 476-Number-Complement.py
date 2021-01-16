class Solution:
    def findComplement(self, num: int) -> int:
        num_digit = 1
        while 2 ** num_digit <= num:
            num_digit += 1

        return num ^ (2 ** num_digit - 1)


# Performance Result:
#   Coding Time: 00:04:00
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 28 ms, faster than 82.52%
#   Memory Usage: 14 MB, less than 90.81%
