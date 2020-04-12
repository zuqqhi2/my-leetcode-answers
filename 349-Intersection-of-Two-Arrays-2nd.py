class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(sorted(set(nums1)))
        nums2 = list(sorted(set(nums2)))

        result = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] < nums2[j]:
                    break

                if nums1[i] == nums2[j]:
                    result.append(nums2[j])

        return result


# Performance Result:
#   Coding Time: 00:03:11
#   Time Complexity: O(N^2)
#   Space Complexity: O(1)
#   Runtime: 144 ms, faster than 5.35%
#   Memory Usage: 13.9 MB, less than 5.88%
