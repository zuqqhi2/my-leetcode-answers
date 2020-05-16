class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_map = {w: True for w in wordDict}
        word_len_list = [len(w) for w in wordDict]

        # Dynamic Programming
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for length in word_len_list:
                if i - length < 0:
                    continue

                if dp[i - length] and s[i - length:i] in word_map:
                    dp[i] = True

        return dp[-1]


# Performance Result:
#   Coding Time: 00:15:32
#   Time Complexity: O(NM)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 78.44%
#   Memory Usage: 14 MB, less than 5.55%
