import collections


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        for k in cnt.keys():
            if cnt[k] == 1:
                return k

        return -1


# Performance Result:
#   Coding Time: 00:04:25
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 92 ms, faster than 50.05%
#   Memory Usage: 16.1 MB, less than 91.72%
