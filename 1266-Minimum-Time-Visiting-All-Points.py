class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(points)):
            res += max(abs(points[i - 1][0] - points[i][0]),
                       abs(points[i - 1][1] - points[i][1]))

        return res


# Performance Result:
#   Coding Time: 00:04:24
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 72 ms, faster than 37.81%
#   Memory Usage: 13.9 MB, less than 43.86%
