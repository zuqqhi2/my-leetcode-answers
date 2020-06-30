class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result *= 26
            result += ord(s[i]) - ord("A") + 1

        return result


# Performance Result:
#   Coding Time: 00:03:03
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 52 ms, faster than 8.37%
#   Memory Usage: 13.9 MB, less than 44.12%
