class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = {}
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        num_rows = len(grid)
        num_cols = len(grid[0])
        for y in range(num_rows):
            for x in range(num_cols):
                if (y, x) in visited:
                    continue

                if grid[y][x] == 0:
                    continue

                cur_area = 0
                opened = [(y, x)]
                while len(opened) > 0:
                    cur_y, cur_x = opened.pop(0)
                    if (cur_y, cur_x) in visited:
                        continue

                    cur_area += 1
                    visited[(cur_y, cur_x)] = True

                    for d in directions:
                        new_y = cur_y + d[0]
                        new_x = cur_x + d[1]
                        if 0 <= new_y < num_rows and 0 <= new_x < num_cols and \
                            grid[new_y][new_x] == 1 and (
                        new_y, new_x) not in visited:
                            opened.append((new_y, new_x))

                max_area = max(max_area, cur_area)

        return max_area


# Performance Result:
#   Coding Time: 00:11:03
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 148 ms, faster than 52.57% of Python3
#       online submissions for Max Area of Island.
#   Memory Usage: 14.1 MB, less than 100.00% of Python3
#       online submissions for Max Area of Island.
