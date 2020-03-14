class Solution:
    def numDecodings(self, s: str) -> int:
        # Corner cases
        if len(s) >= 1 and s[0] == "0":
            return 0
        elif len(s) == 1:
            return 1

        # Dynamic Programming
        #   dp[i]: number of combinations
        #   i: index of s (i=1 means s[0]
        #   dp[0] = 1
        #   dp[i] = dp[i - 1] if s[i] can be decoded but not s[i - 1] + s[i]
        #       dp[i - 1] + 1 if s[i] and s[i - 1] + s[i] can be decoded
        #       dp[i - 1] - 1 if s[i] cannot be decoded but s[i - 1] + s[i] can
        combs = [1] + [0] * len(s)
        combs[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(s) + 1):
            si = int(s[i - 1])
            si2 = int(s[i - 2:i])
            # Single Digit
            if 1 <= si <= 9:
                combs[i] += combs[i - 1]
            # 2 Digits case
            if 10 <= si2 <= 26:
                combs[i] += combs[i - 2]

        return combs[-1]


s = Solution()
print(s.numDecodings("226"))
print(s.numDecodings("110"))
print(s.numDecodings("139"))
print(s.numDecodings("00"))
print(s.numDecodings("330"))

# Sample test case:
#   Input:
#       "226"
#   Output:
#       3

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 28 ms, faster than 83.57% of Python3
#       online submissions for Decode Ways.
#   Memory Usage: 12.9 MB, less than 100.00% of Python3
#       online submissions for Decode Ways.
