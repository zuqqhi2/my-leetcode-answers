import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = collections.Counter(nums1)

        res = []
        for num in nums2:
            if num in cnt1 and cnt1[num] > 0:
                res.append(num)
                cnt1[num] -= 1

        return res


# Performance Result:
#   Coding Time: 00:02:14
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 92 ms, faster than 9.21%
#   Memory Usage: 13.9 MB, less than 62.77%
