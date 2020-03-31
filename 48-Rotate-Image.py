class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Corner case
        if len(matrix) == 0:
            return None
        if len(matrix) == 1:
            return None

        start_y = 0
        end_y = len(matrix) - 1
        start_x = 0
        end_x = len(matrix[0]) - 1

        while end_y - start_y >= 1:
            points = [(start_y, start_x), (start_y, end_x),
                      (end_y, end_x), (end_y, start_x)]
            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for i in range(end_x - start_x):
                # Change values
                tmp = matrix[points[0][0]][points[0][1]]
                for j in range(4):
                    k = (j + 1) % 4
                    dy = points[k][0]
                    dx = points[k][1]

                    tmp2 = matrix[dy][dx]
                    matrix[dy][dx] = tmp
                    tmp = tmp2

                # Move
                for j in range(4):
                    points[j] = (points[j][0] + moves[j][0],
                                 points[j][1] + moves[j][1])

            start_y += 1
            end_y -= 1
            start_x += 1
            end_x -= 1


# Sample test case:
#   Input:
#       [
#           [ 1, 2, 3 ],
#           [ 4, 5, 6 ],
#           [ 7, 8, 9 ]
#       ]
#   Output:
#       [
#           [ 7, 4, 1 ],
#           [ 8, 5, 2 ],
#           [ 9, 6, 3 ]
#       ]

# Performance Result:
#   Coding Time: 00:20:50
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 32 ms, faster than 74.45% of Python3
#       online submissions for Rotate Image.
#   Memory Usage: 13.7 MB, less than 6.25% of Python3
#       online submissions for Rotate Image.
