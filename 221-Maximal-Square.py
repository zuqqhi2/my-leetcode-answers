class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_len = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == '0':
                    continue

                length = 1
                is_square = True
                while is_square:
                    for y2 in range(y, y + length):
                        for x2 in range(x, x + length):
                            if matrix[y2][x2] == '0':
                                is_square = False

                    if is_square and y + length < len(
                        matrix) and x + length < len(matrix[0]):
                        length += 1
                    elif not is_square:
                        length -= 1
                        break
                    else:
                        break

                max_len = max(max_len, length)

        return max_len * max_len


# Performance Result:
#   Coding Time: 00:19:27
#   Time Complexity: O(NM^2)
#   Space Complexity: O(1)
#   Runtime: 468 ms, faster than 5.16%
#   Memory Usage: 15.4 MB, less than 56.77%
