class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letter = []
        special_char = {}
        for i in range(len(S)):
            if S[i].isalpha():
                letter.append(S[i])
            else:
                special_char[i] = S[i]

        letter[:] = reversed(letter)

        res = ""
        for i in range(len(S)):
            if i not in special_char:
                res += letter.pop(0)
            else:
                res += special_char[i]

        return res


# Performance Result:
#   Coding Time: 00:04:36
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 54.50%
#   Memory Usage: 14 MB, less than 99.92%
