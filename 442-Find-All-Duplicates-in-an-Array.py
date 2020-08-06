import collections


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        res = []
        for key in cnt.keys():
            if cnt[key] == 2:
                res.append(key)

        return res


# Performance Result:
#   Coding Time: 00:02:25
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 376 ms, faster than 89.11%
#   Memory Usage: 22.4 MB, less than 10.49%
