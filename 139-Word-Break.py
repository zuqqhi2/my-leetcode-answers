class Solution:
    def wordBreak(self, s, wordDict):
        if len(s) == 0:
            return True
        elif wordDict is None:
            return False
        elif len(wordDict) == 0:
            return False

        # Create DP array
        dp = [False] * len(s)
        dp[0] = s[0] in wordDict

        # Update dp array using recursion formula
        for idx in range(1, len(s)):
            for j in reversed(range(idx + 1)):
                if (j == 0 or dp[j - 1]) and s[j:idx+1] in wordDict:
                    dp[idx] = True
                    break

        return dp[-1]


s = Solution()
print(s.wordBreak('leetcode', ['leet', 'code']))



# Sample test case:
#   Input:
#       s = "leetcode"
#       wordDict = ["leet", "code"]
#   Output:
#       True

# Performance Result:
#   Coding Time: 00:37:12
#   Time Complexity: O(n ^ 2)
#   Space Complexity: O(n)
#   Runtime: 48 ms, faster than 55.27% of Python3
#       online submissions for Word Break.
#   Memory Usage: 13.8 MB, less than 5.55% of Python3
#       online submissions for Word Break.
