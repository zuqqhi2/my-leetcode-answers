import collections


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        cnts = collections.Counter(arr)
        for k in cnts:
            if cnts[k] / float(length) > 0.25:
                return k

        return arr[0]


# Performance Result:
#   Coding Time: 00:02:47
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 128 ms, faster than 16.15%
#   Memory Usage: 15.6 MB, less than 38.99%
