class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left_idx = 0
        right_idx = 0
        max_length = 0
        while right_idx < len(s):
            if s[right_idx] in chars:
                del chars[s[left_idx]]
                left_idx += 1
                continue

            chars[s[right_idx]] = True
            if right_idx - left_idx + 1 > max_length:
                max_length = right_idx - left_idx + 1

            right_idx += 1

        return max_length


# Performance Result:
#   Coding Time: 00:09:48
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 64 ms, faster than 60.49% of Python3
#       online submissions for Longest Substring Without Repeating Characters.
#   Memory Usage: 12.9 MB, less than 100.00% of Python3
#       online submissions for Longest Substring Without Repeating Characters.
