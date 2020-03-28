class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Corner case
        if len(matrix) == 0:
            return None
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return None

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        changed = {}
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] != 0:
                    continue
                elif (y, x) in changed:
                    continue

                opened = []
                for move in dirs:
                    cur_y = y
                    cur_x = x
                    while 0 <= cur_y + move[0] < len(matrix) and 0 <= cur_x + \
                        move[1] < len(matrix[0]):
                        cur_y += move[0]
                        cur_x += move[1]
                        if matrix[cur_y][cur_x] != 0:
                            opened.append((cur_y, cur_x))

                while len(opened) > 0:
                    cur_node = opened.pop(0)
                    changed[cur_node] = True
                    matrix[cur_node[0]][cur_node[1]] = 0


# Sample test case:
#   Input:
#       [
#           [1,1,1],
#           [1,0,1],
#           [1,1,1]
#       ]
#   Output:
#       [
#           [1,0,1],
#           [0,0,0],
#           [1,0,1]
#       ]

# Performance Result:
#   Coding Time: 00:19:23
#   Time Complexity: O(MN(M + N))
#   Space Complexity: O(MN)
#   Runtime: 172 ms, faster than 5.54% of Python3
#       online submissions for Set Matrix Zeroes.
#   Memory Usage: 15.8 MB, less than 5.13% of Python3
#       online submissions for Set Matrix Zeroes.
