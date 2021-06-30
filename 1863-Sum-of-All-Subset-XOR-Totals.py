import itertools


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        ret = 0
        for l in range(1, len(nums) + 1):
            it = itertools.combinations(nums, l)
            for e in it:
                s = e[0]
                for i in range(1, len(e)):
                    s ^= e[i]
                ret += s

        return ret


# Performance Result:
#   Coding Time: 00:10:34
#   Time Complexity: O(N^2)
#   Space Complexity: O(N^2)
#   Runtime: 88 ms, faster than 52.18%
#   Memory Usage: 14.2 MB, less than 61.85%
