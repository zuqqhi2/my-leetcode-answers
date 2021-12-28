import collections


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnts = collections.Counter(nums)

        res = 0
        for digit in cnts.keys():
            if digit - 1 in cnts.keys():
                res = max(res, cnts[digit] + cnts[digit - 1])

            if digit + 1 in cnts.keys():
                res = max(res, cnts[digit] + cnts[digit - 1])

        return res


# Performance Result:
#   Coding Time: 00:08:46
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 320 ms, faster than 50.84%
#   Memory Usage: 16 MB, less than 53.87%
