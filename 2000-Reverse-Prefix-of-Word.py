class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        for i in range(len(word)):
            if word[i] == ch:
                if i == len(word) - 1:
                    return ''.join(list(reversed(word)))
                else:
                    return ''.join(list(reversed(word[:i + 1]))) + word[i + 1:]

        return word

# Performance Result:
#   Coding Time: 00:05:57
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 27 ms, faster than 89.99%
#   Memory Usage: 13.8 MB, less than 56.60%
