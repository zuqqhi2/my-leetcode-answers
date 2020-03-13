class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Corner cases
        if len(text1) == 0 or len(text2) == 0:
            return 0

        # Dynamic Programming
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[-1][-1]


s = Solution()
print(s.longestCommonSubsequence("abcde", "ace"))

# Sample test case:
#   Input:
#       text1 = "abcde", text2 = "ace"
#   Output:
#       3

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(NM)
#   Space Complexity: O(NM)
#   Runtime: 448 ms, faster than 58.96% of Python3
#       online submissions for Longest Common Subsequence.
#   Memory Usage: 21.4 MB, less than 100.00% of Python3
#       online submissions for Longest Common Subsequence.
