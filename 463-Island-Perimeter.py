class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    continue

                for d in dirs:
                    new_y = y + d[0]
                    new_x = x + d[1]
                    if new_y < 0 or len(grid) <= new_y \
                        or new_x < 0 or len(grid[0]) <= new_x \
                        or grid[new_y][new_x] == 0:
                        perimeter += 1

        return perimeter


# Performance Result:
#   Coding Time: 00:09:42
#   Time Complexity: O(NM)
#   Space Complexity: O(1)
#   Runtime: 644 ms, faster than 74.25% of Python3
#   Memory Usage: 14 MB, less than 60.61% of Python3
