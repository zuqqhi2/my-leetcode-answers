class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr[:] = sorted(arr)

        min_dist = 1_000_000
        for i in range(1, len(arr)):
            min_dist = min(min_dist, arr[i] - arr[i - 1])

        res = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_dist:
                res.append([arr[i - 1], arr[i]])

        return res


# Performance Result:
#   Coding Time: 00:03:06
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 356 ms, faster than 74.17%
#   Memory Usage: 27.7 MB, less than 8.36%
