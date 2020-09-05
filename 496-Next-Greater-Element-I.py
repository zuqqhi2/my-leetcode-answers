class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[
        int]:
        nexts = {}
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                if nums2[i] < nums2[j]:
                    nexts[nums2[i]] = nums2[j]
                    break

        res = []
        for i in range(len(nums1)):
            if nums1[i] in nexts:
                res.append(nexts[nums1[i]])
            else:
                res.append(-1)

        return res


# Performance Result:
#   Coding Time: 00:06:55
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 52 ms, faster than 72.21%
#   Memory Usage: 13.9 MB, less than 87.78%
