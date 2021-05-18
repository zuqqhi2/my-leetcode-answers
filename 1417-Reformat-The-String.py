class Solution:
    def reformat(self, s: str) -> str:
        alpha_chars = []
        digit_chars = []
        for c in s:
            if c.isdigit():
                digit_chars.append(c)
            else:
                alpha_chars.append(c)

        if abs(len(alpha_chars) - len(digit_chars)) <= 1:
            if len(alpha_chars) >= len(digit_chars):
                res = alpha_chars.pop(0)
                while len(alpha_chars) > 0:
                    res += digit_chars.pop(0) + alpha_chars.pop(0)
                if len(digit_chars) >= 1:
                    res += digit_chars.pop(0)
                return res
            else:
                res = digit_chars.pop(0)
                while len(digit_chars) > 0:
                    res += alpha_chars.pop(0) + digit_chars.pop(0)
                return res
        else:
            return ''


# Performance Result:
#   Coding Time: 00:08:24
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 40 ms, faster than 86.80%
#   Memory Usage: 14.4 MB, less than 11.58%
