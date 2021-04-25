import collections


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        indexes = collections.Counter(nums)
        num_good = 0
        for k in indexes:
            num_good += indexes[k] * (indexes[k] - 1) // 2

        return num_good


# Performance Result:
#   Coding Time: 00:04:41
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 38.91%
#   Memory Usage: 14.3 MB, less than 43.06%
