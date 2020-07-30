class Solution:
    def convertToTitle(self, n: int) -> str:
        res = []
        base = ord('A')
        while n > 0:
            res.insert(0, chr(base + (n - 1) % 26))
            n = (n - 1) // 26

        return ''.join(res)


# Performance Result:
#   Coding Time: 00:18:23
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 48 ms, faster than 14.76%
#   Memory Usage: 13.9 MB, less than 33.33%
