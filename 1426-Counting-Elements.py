import collections


class Solution:
    def countElements(self, arr: List[int]) -> int:
        cnts = collections.Counter(arr)
        res = 0
        for key in cnts:
            if key + 1 in cnts:
                res += cnts[key]

        return res


# Performance Result:
#   Coding Time: 00:02:34
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 68.70%
#   Memory Usage: 14.4 MB, less than 18.26%
