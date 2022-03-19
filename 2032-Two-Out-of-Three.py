import collections

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int],
                      nums3: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        nums3_set = set(nums3)

        nums12_set = nums1_set.intersection(nums2_set)
        nums13_set = nums1_set.intersection(nums3_set)
        nums23_set = nums2_set.intersection(nums3_set)

        res = [n for n in nums12_set]
        res.extend([n for n in nums13_set])
        res.extend([n for n in nums23_set])
        return list(set(res))

# Performance Result:
#   Coding Time: 00:10:34
#   Time Complexity: O(N)
#   Space Complexity: O(M)
#   Runtime: 94 ms, faster than 60.63%
#   Memory Usage: 14 MB, less than 19.61%
