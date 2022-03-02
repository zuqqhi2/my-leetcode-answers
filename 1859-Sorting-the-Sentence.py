class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        res = [''] * len(words)
        for word in words:
            res[int(word[-1]) - 1] = word[:-1]

        return ' '.join(res)


# Performance Result:
#   Coding Time: 00:03:35
#   Time Complexity: O(N)
#   Space Complexity: O(M)
#   Runtime: 40 ms, faster than 57.68%
#   Memory Usage: 13.8 MB, less than 98.37%
