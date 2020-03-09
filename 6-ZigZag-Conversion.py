class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 0:
            return ""
        if numRows == 0:
            return ""
        if numRows == 1:
            return s

        grid = [["" for j in range(1000)] for i in range(numRows)]
        is_reverse_mode = False
        gx, gy = 0, 0
        for c in s:
            grid[gy][gx] = c

            if is_reverse_mode:
                gy -= 1
            else:
                gy += 1

            if gy >= numRows:
                gy -= 2
                gx += 1
                is_reverse_mode = True
            elif gy < 0:
                gy += 2
                gx += 1
                is_reverse_mode = False

        result_str = ''.join(grid[0])
        for i in range(1, len(grid)):
            result_str += ''.join(grid[i])
        return result_str


s = Solution()
print(s.convert("PAYPALISHIRING", 2))
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))

# Sample test case:
#   Input:
#       s = "PAYPALISHIRING", numRows = 3
#   Output:
#       "PAHNAPLSIIGYIR"

# Performance Result:
#   Coding Time: 00:16:13
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 2060 ms, faster than 5.04% of Python3
#       online submissions for ZigZag Conversion.
#   Memory Usage: 20.6 MB, less than 5.71% of Python3
#       online submissions for ZigZag Conversion.
