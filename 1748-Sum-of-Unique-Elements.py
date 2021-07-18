import collections


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        res = 0
        for k in cnt:
            if cnt[k] == 1:
                res += k

        return res


# Performance Result:
#   Coding Time: 00:01:15
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 28 ms, faster than 94.46%
#   Memory Usage: 14.2 MB, less than 70.85%
