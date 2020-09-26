class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for y in range(1, len(matrix)):
            for x in range(1, len(matrix[0])):
                if matrix[y][x] != matrix[y - 1][x - 1]:
                    return False

        return True


# Performance Result:
#   Coding Time: 00:01:00
#   Time Complexity: O(NM)
#   Space Complexity: O(1)
#   Runtime: 80 ms, faster than 97.84%
#   Memory Usage: 14.1 MB, less than 5.32%
