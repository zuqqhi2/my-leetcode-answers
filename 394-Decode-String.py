import re


class Solution:
    def decodeString(self, s: str) -> str:
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-zA-Z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
        return s


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(K)
#   Space Complexity: O(1)
#   Runtime: 24 ms, faster than 93.58%
#   Memory Usage: 13.7 MB, less than 82.65%
