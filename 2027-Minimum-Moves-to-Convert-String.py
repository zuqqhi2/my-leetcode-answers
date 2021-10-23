class Solution:
    def minimumMoves(self, s: str) -> int:
        num_turn = 0
        idx = 0
        while idx < len(s):
            if s[idx] == 'X':
                idx += 3
                num_turn += 1
            else:
                idx += 1

        return num_turn


# Performance Result:
#   Coding Time: 00:34:34
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 49 ms, faster than 27.60%
#   Memory Usage: 14.3 MB, less than 16.30%
