class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return str1 if str1 else str2
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        elif str1[: len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2) :], str2)
        else:
            return ''


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(log N) ?
#   Space Complexity: O(1)
#   Runtime: 28 ms, faster than 87.13%
#   Memory Usage: 13.8 MB, less than 55.83%
