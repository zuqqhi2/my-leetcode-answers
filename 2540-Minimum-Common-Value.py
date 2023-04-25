import collections

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        cnts = collections.Counter(nums1)

        min_val = -1
        for v in nums2:
            if v in cnts and (v < min_val or min_val == -1):
                min_val = v

        return min_val

# Performance Result:
#   Coding Time: 00:05:06
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 457 ms, faster than 71.45%
#   Memory Usage: 39.2 MB, less than 31.98%
