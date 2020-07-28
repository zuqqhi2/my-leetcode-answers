class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True

        bases1 = {}
        bases2 = {}
        bases1[s[0]] = ord(s[0]) - ord(t[0])
        bases2[t[0]] = ord(t[0]) - ord(s[0])
        for i in range(1, len(s)):
            if s[i] not in bases1 and t[i] not in bases2:
                bases1[s[i]] = ord(s[i]) - ord(t[i])
                bases2[t[i]] = ord(t[i]) - ord(s[i])
                continue

            if (s[i] in bases1 and bases1[s[i]] != ord(s[i]) - ord(t[i])) \
                or (t[i] in bases2 and bases2[t[i]] != ord(t[i]) - ord(s[i])):
                return False

        return True


# Performance Result:
#   Coding Time: 00:12:10
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 84 ms, faster than 12.02%
#   Memory Usage: 13.8 MB, less than 93.43%
