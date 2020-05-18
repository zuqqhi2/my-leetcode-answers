class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            st = s
            pat = s[:i]
            st = st.replace(pat, '')
            if len(st) == 0:
                return True
        return False


# Performance Result:
#   Coding Time: 00:06:56
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 5648 ms, faster than 5.01%
#   Memory Usage: 13.9 MB, less than 7.14%
