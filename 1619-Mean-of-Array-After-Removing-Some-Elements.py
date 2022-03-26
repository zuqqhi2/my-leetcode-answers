class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr[:] = list(sorted(arr))
        num_delete = int(len(arr) * 0.05)
        arr[:] = arr[num_delete:-num_delete]
        return sum(arr) / float(len(arr))


# Performance Result:
#   Coding Time: 00:10:01
#   Time Complexity: O(N log2 N)
#   Space Complexity: O(1)
#   Runtime: 64 ms, faster than 83.54%
#   Memory Usage: 13.9 MB, less than 81.15%
