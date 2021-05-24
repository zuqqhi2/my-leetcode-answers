class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        y_max = [0] * len(matrix[0])
        x_min = [10 ** 6] * len(matrix)
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                y_max[x] = max(y_max[x], matrix[y][x])
                x_min[y] = min(x_min[y], matrix[y][x])

        x_min_set = set(x_min)
        y_max_set = set(y_max)
        return list(x_min_set & y_max_set)


# Performance Result:
#   Coding Time: 00:16:57
#   Time Complexity: O(NM)
#   Space Complexity: O(N + M)
#   Runtime: 152 ms, faster than 19.11%
#   Memory Usage: 14.7 MB, less than 40.21%
