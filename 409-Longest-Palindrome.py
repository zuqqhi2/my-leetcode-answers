import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = collections.Counter(s)
        is_center_occupied = False
        res = 0
        for k in cnt.keys():
            if not is_center_occupied and cnt[k] % 2 != 0:
                res += cnt[k]
                is_center_occupied = True
            elif is_center_occupied and cnt[k] % 2 != 0:
                res += max(cnt[k] - 1, 0)
            else:
                res += cnt[k]

        return res


# Performance Result:
#   Coding Time: 00:05:41
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 76.06%
#   Memory Usage: 14 MB, less than 5.51%
