import collections


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        cnts = collections.Counter(A)
        for key in cnts:
            if cnts[key] >= len(A) // 2:
                return key

        return A[0]


# Performance Result:
#   Coding Time: 00:01:44
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 200 ms, faster than 74.76%
#   Memory Usage: 15.6 MB, less than 35.77%
