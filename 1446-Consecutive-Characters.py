class Solution:
    def maxPower(self, s: str) -> int:
        cur_char = s[0]
        cur_length = 1
        max_length = 1
        for i in range(1, len(s)):
            if cur_char != s[i]:
                cur_char = s[i]
                cur_length = 1
            else:
                cur_length += 1

            max_length = max(max_length, cur_length)

        return max_length


# Performance Result:
#   Coding Time: 00:05:07
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 36 ms, faster than 89.32%
#   Memory Usage: 14.1 MB, less than 81.42%
