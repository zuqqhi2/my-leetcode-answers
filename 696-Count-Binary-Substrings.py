class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Run-Length Coding
        encoded_s = []
        cur_char = s[0]
        cur_char_cnt = 1
        for idx in range(1, len(s)):
            if cur_char != s[idx]:
                encoded_s.append((cur_char, cur_char_cnt))
                cur_char = s[idx]
                cur_char_cnt = 1
            else:
                cur_char_cnt += 1
        encoded_s.append((cur_char, cur_char_cnt))

        # Count the pattern
        res = 0
        for start in range(len(encoded_s) - 1):
            end = start + 1
            res += min(encoded_s[start][1], encoded_s[end][1])
        return res


# Performance Result:
#   Coding Time: 00:15:36
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 204 ms, faster than 38.19%
#   Memory Usage: 16.1 MB, less than 5.56%
