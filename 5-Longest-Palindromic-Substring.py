from typing import *


class Solution:
    def longestPalindrome(self, input: str) -> str:
        N: int = len(input)
        palindromes: MutableSet[Tuple[int, int]] = set()
        answer: str = ""

        for windowLen in range(1, N + 1):
            for start in range(N - windowLen + 1):
                end: int = start + windowLen - 1    # Inclusive

                if input[start] == input[end] and \
                        (end - start < 2 or (start + 1, end - 1) in palindromes):

                    palindromes.add((start, end))
                    palindromes.discard((start + 1, end - 1))   # Won't need this again.

                    if windowLen > len(answer):
                        answer = input[start: end + 1]

        return answer


# Sample test case:
#   Input:
#       "babad"
#   Output:
#       "bab"

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 4620 ms, faster than 27.51% of Python3
#       online submissions for Longest Palindromic Substring.
#   Memory Usage: 14 MB, less than 20.17% of Python3
#       online submissions for Longest Palindromic Substring.
