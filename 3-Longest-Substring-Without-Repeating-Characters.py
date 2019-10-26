# Algorithm
#   length + 1 if str[i] is not in existed char hash
#   clear the length and hash if str[i] is in existed char hash

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_length = 1
        char_memory = {}
        cur_start_pos = 0
        for cur_end_pos in range(len(s)):
            if s[cur_end_pos] in char_memory:
                cur_start_pos = max(cur_start_pos, char_memory[s[cur_end_pos]])

            max_length = max(max_length, cur_end_pos - cur_start_pos)
            char_memory[s[cur_end_pos]] = cur_end_pos

        return max_length


# Sample test case:
#   Input:
#       "abcabcbb"
#   Output:
#       3

# Performance Result:
#   Coding Time: 00:42:04
#   Time Complexity: O(n)
#   Space Complexity: O(min(n, m)), m is number of unique characters
#   Runtime: 72 ms, faster than 58.47% of Python3 online
#       submissions for Longest Substring Without Repeating Characters.
#   Memory Usage: 14.1 MB, less than 5.10% of Python3 online
#       submissions for Longest Substring Without Repeating Characters.
