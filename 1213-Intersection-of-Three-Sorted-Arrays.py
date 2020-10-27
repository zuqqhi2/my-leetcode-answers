class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int],
                           arr3: List[int]) -> List[int]:
        s1 = set(arr1)
        s2 = set(arr2)
        s3 = set(arr3)
        s_all = s1 & s2 & s3

        return [arr1[i] for i in range(len(arr1)) if arr1[i] in s_all]


# Performance Result:
#   Coding Time: 00:03:26
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 76 ms, faster than 88.34%
#   Memory Usage: 14.7 MB, less than 21.37%
