class Solution:
    def countLetters(self, S: str) -> int:
        num_patterns = len(S)
        for start in range(len(S) - 1):
            chars = set()
            chars.add(S[start])
            for end in range(start + 1, len(S)):
                if S[end] not in chars:
                    break
                else:
                    num_patterns += 1

        return num_patterns


# Performance Result:
#   Coding Time: 00:03:53
#   Time Complexity: O(N^2)
#   Space Complexity: O(1)
#   Runtime: 256 ms, faster than 5.01%
#   Memory Usage: 14.2 MB, less than 45.09%
