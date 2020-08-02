class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False


# Performance Result:
#   Coding Time: 00:02:32
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 28 ms, faster than 86.51%
#   Memory Usage: 13.8 MB, less than 73.81%
