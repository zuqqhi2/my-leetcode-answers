class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        ans = 0
        for center in range(2*N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans


# Sample test case:
#   Input:
#       "aaa"
#   Output:
#       6

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N^2)
#   Space Complexity: O(1)
#   Runtime: 112 ms, faster than 90.31% of Python3
#       online submissions for Palindromic Substrings.
#   Memory Usage: 14 MB, less than 50.00% of Python3
#       online submissions for Palindromic Substrings.
