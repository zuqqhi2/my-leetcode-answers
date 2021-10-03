class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = 1e+10
        min_idx = -1
        for i in range(len(points)):
            if x != points[i][0] and y != points[i][1]:
                continue

            dist = abs(x - points[i][0]) + abs(y - points[i][1])
            if dist < min_dist:
                min_dist = dist
                min_idx = i

        return min_idx


# Performance Result:
#   Coding Time: 00:03:37
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 753 ms, faster than 34.79%
#   Memory Usage: 19.4 MB, less than 41.23%
