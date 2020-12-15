class Solution:
    def removeVowels(self, S: str) -> str:
        res = ""
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        for i in range(len(S)):
            if S[i] not in vowels:
                res += S[i]

        return res


# Performance Result:
#   Coding Time: 00:02:29
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 41.84%
#   Memory Usage: 14.3 MB, less than 24.22%
