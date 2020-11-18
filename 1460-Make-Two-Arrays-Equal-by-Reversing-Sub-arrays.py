import collections


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        cnt_target = collections.Counter(target)
        cnt_arr = collections.Counter(arr)

        for k in cnt_arr.keys():
            if k not in cnt_target:
                return False
            if cnt_target[k] != cnt_arr[k]:
                return False

        return True


# Performance Result:
#   Coding Time: 00:03:15
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 80 ms, faster than 44.02%
#   Memory Usage: 14.5 MB, less than 26.61%
