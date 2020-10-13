class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = format(x, 'b')
        y_bin = format(y, 'b')

        if len(x_bin) > len(y_bin):
            y_bin = "0" * (len(x_bin) - len(y_bin)) + y_bin
        elif len(y_bin) > len(x_bin):
            x_bin = "0" * (len(y_bin) - len(x_bin)) + x_bin

        res = 0
        for i in range(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                res += 1

        return res


# Performance Result:
#   Coding Time: 00:05:28
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 51.02%
#   Memory Usage: 14.1 MB, less than 99.89%
