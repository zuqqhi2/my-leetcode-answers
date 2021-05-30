class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        num_r = 0
        num_l = 0
        for i in range(len(s)):
            if s[i] == 'R':
                num_r += 1
            else:
                num_l += 1

            if num_r == num_l:
                res += 1
                num_r = 0
                num_l = 0

        return res


# Performance Result:
#   Coding Time: 00:02:40
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 28 ms, faster than 81.47%
#   Memory Usage: 14.2 MB, less than 39.81%
