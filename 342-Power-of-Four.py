class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 0:
            return False

        bin_num = format(num, 'b')
        num_bin_digit = len(bin_num)
        for i in range(1, num_bin_digit):
            if bin_num[i] == '1':
                return False

        if num_bin_digit % 2 == 1:
            return True
        else:
            return False


# Performance Result:
#   Coding Time: 00:13:36
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 28 ms, faster than 88.81%
#   Memory Usage: 14 MB, less than 16.67%
