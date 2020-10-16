class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatests = [-1] * len(arr)
        cur_max = 0
        for i in reversed(range(1, len(arr))):
            cur_max = max(cur_max, arr[i])
            greatests[i] = cur_max

        res = [-1] * len(arr)
        for i in range(len(arr) - 1):
            res[i] = greatests[i + 1]

        return res


# Performance Result:
#   Coding Time: 00:05:00
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 120 ms, faster than 89.59%
#   Memory Usage: 15.3 MB, less than 99.86%
