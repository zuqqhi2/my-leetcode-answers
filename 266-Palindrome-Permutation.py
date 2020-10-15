import collections


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnts = collections.Counter(s)
        num_cnt_1 = 0
        for c in cnts.keys():
            if cnts[c] % 2 == 1:
                num_cnt_1 += 1

        if len(s) % 2 == 0:
            return True if num_cnt_1 == 0 else False
        else:
            return True if num_cnt_1 == 1 else False


# Performance Result:
#   Coding Time: 00:04:33
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 24 ms, faster than 91.38%
#   Memory Usage: 14.1 MB, less than 100.00%
