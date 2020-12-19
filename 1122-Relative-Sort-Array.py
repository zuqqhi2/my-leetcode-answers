import collections


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_cnt = collections.Counter(arr1)

        res = []
        for i in range(len(arr2)):
            res.extend([arr2[i] for _ in range(arr1_cnt[arr2[i]])])
            del arr1_cnt[arr2[i]]

        remains = []
        for k in arr1_cnt:
            remains.extend([k for _ in range(arr1_cnt[k])])
        res.extend(list(sorted(remains)))

        return res


# Performance Result:
#   Coding Time: 00:04:18
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 28 ms, faster than 97.16%
#   Memory Usage: 14.5 MB, less than 17.23%
