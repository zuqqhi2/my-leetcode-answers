class Solution:
    def traverse(self, grid, y, x, area_size=0):
        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]) or grid[y][x] != 1:
            return area_size

        grid[y][x] = 0
        area_size += 1

        area_size = self.traverse(grid, y - 1, x, area_size)
        area_size = self.traverse(grid, y, x + 1, area_size)
        area_size = self.traverse(grid, y + 1, x, area_size)
        area_size = self.traverse(grid, y, x - 1, area_size)

        return area_size

    def maxAreaOfIsland(self, grid):
        max_area = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] != 1:
                    continue

                area_size = self.traverse(grid, y, x)
                print(y, x, area_size)
                if area_size > max_area:
                    max_area = area_size

        return max_area


grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
]

s = Solution()
print(s.maxAreaOfIsland(grid))

# Sample test case:
#   Input:
#       11110
#       11010
#       11000
#       00000
#   Output:
#       9

# Performance Result:
#   Coding Time: 00:14:56
#   Time Complexity: O(NM)
#   Space Complexity: O(1)
#   Runtime: 140 ms, faster than 88.28% of Python3
#       online submissions for Max Area of Island.
#   Memory Usage: 15.3 MB, less than 90.91% of Python3
#       online submissions for Max Area of Island.
