class Solution:
    def toHex(self, num: int) -> str:
        max_hex = 0xffffffff
        if num >= 0:
            return str(hex(num)).replace('0x', '')
        else:
            num *= -1
            return str(hex((num ^ max_hex) + 1)).replace('0x', '')


# Performance Result:
#   Coding Time: 00:12:15
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 28 ms, faster than 78.52%
#   Memory Usage: 14.2 MB, less than 41.36%
