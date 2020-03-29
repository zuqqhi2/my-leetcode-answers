class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Corner case
        if len(matrix) == 0:
            return []

        VISITED = -10000000
        cur_y = -1
        cur_x = -1
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cur_dir_idx = 0
        opened = [(0, 0)]
        result = []
        while len(opened) > 0:
            cur_y, cur_x = opened.pop(0)
            result.append(matrix[cur_y][cur_x])
            matrix[cur_y][cur_x] = VISITED

            new_y = cur_y + directions[cur_dir_idx][0]
            new_x = cur_x + directions[cur_dir_idx][1]
            if 0 <= new_y < len(matrix) and 0 <= new_x < len(matrix[0]) and \
                matrix[new_y][new_x] != VISITED:
                opened.append((new_y, new_x))
            else:
                new_dir_idx = (cur_dir_idx + 1) % 4
                while len(opened) == 0 and new_dir_idx != cur_dir_idx:
                    new_y = cur_y + directions[new_dir_idx][0]
                    new_x = cur_x + directions[new_dir_idx][1]
                    if 0 <= new_y < len(matrix) and 0 <= new_x < len(
                        matrix[0]) and matrix[new_y][new_x] != VISITED:
                        opened.append((new_y, new_x))
                        cur_dir_idx = new_dir_idx

                    new_dir_idx = (new_dir_idx + 1) % 4

        return result


# Sample test case:
#   Input:
#       [
#           [ 1, 2, 3 ],
#           [ 4, 5, 6 ],
#           [ 7, 8, 9 ]
#       ]
#   Output:
#       [1,2,3,6,9,8,7,4,5]

# Performance Result:
#   Coding Time: 00:18:04
#   Time Complexity: O(MN)
#   Space Complexity: O(1)
#   Runtime: 32 ms, faster than 19.68% of Python3
#       online submissions for Spiral Matrix.
#   Memory Usage: 13.8 MB, less than 8.70% of Python3
#       online submissions for Spiral Matrix.
