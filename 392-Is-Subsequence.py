class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0 and len(s) > 0:
            return False

        t_start_pos = 0
        for s_idx in range(len(s)):
            is_found = False
            for t_idx in range(t_start_pos, len(t)):
                if s[s_idx] == t[t_idx]:
                    t_start_pos = t_idx + 1
                    is_found = True
                    break

            # It couldn't find target char in a text
            if not is_found:
                return False

        return True


s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("axc", "ahbgdc"))


# Sample test case:
#   Input:
#       [[0, 30],[5, 10],[15, 20]]
#   Output:
#       2

# Performance Result:
#   Coding Time: 00:24:00
#   Time Complexity: O(MN)
#   Space Complexity: O(1)
#   Runtime: 140 ms, faster than 65.18% of Python3
#       online submissions for Is Subsequence.
#   Memory Usage: 17.4 MB, less than 26.67% of Python3
#       online submissions for Is Subsequence.
