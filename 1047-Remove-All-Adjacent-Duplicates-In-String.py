class Solution:
    def removeDuplicates(self, S: str) -> str:
        is_there_dup_letter = True
        while is_there_dup_letter:
            is_there_dup_letter = False

            for i in range(1, len(S)):
                if S[i] == S[i - 1]:
                    is_there_dup_letter = True
                    S = S[:i - 1] + S[i + 1:]
                    break

        return S


# Performance Result:
#   Coding Time: 00:04:40
#   Time Complexity: O(N^2)
#   Space Complexity: O(1)
#   Runtime: 8436 ms, faster than 5.00%
#   Memory Usage: 13.9 MB, less than 88.47%
