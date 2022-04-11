class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        words = []
        for i in range(len(s) - 2):
            words.append(s[i:i + 3])

        res = 0
        for word in words:
            if word[0] == word[1] or word[0] == word[2] or word[1] == word[2]:
                continue
            else:
                res += 1

        return res


# Performance Result:
#   Coding Time: 00:12:05
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 64 ms, faster than 83.54%
#   Memory Usage: 13.9 MB, less than 81.15%
