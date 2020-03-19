class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Corner case
        if len(grid) == 0:
            return 0
        if len(grid) == 1 and len(grid[0]) == 1:
            if grid[0][0] == '0':
                return 0
            else:
                return 1

        # Detph First Search
        visited = {}
        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        num_islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (y, x) in visited:
                    continue
                if grid[y][x] == '0':
                    visited[(y, x)] = True
                    continue

                num_islands += 1
                opened = [(y, x)]
                while len(opened) > 0:
                    cur_node = opened.pop(0)
                    visited[cur_node] = True
                    for move in moves:
                        new_y = cur_node[0] + move[0]
                        new_x = cur_node[1] + move[1]
                        if new_y < 0 or new_y >= len(
                            grid) or new_x < 0 or new_x >= len(grid[0]):
                            continue
                        if (new_y, new_x) not in visited and grid[new_y][
                            new_x] == '1':
                            opened.insert(0, (new_y, new_x))

        return num_islands


# Performance Result:
#   Coding Time: 00:10:53
#   Time Complexity: O(NM)
#   Space Complexity: O(NM)
#   Runtime: 176 ms, faster than 20.67% of Python3
#       online submissions for Number of Islands.
#   Memory Usage: 21.1 MB, less than 5.13% of Python3
#       online submissions for Number of Islands.
