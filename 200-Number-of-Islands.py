class Solution:
    def traverse(self, y, x, grid):
        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]) or grid[y][x] != '1':
            return
        else:
            grid[y][x] = '0'

        self.traverse(y - 1, x, grid)
        self.traverse(y, x + 1, grid)
        self.traverse(y + 1, x, grid)
        self.traverse(y, x - 1, grid)

    def numIslands(self, grid):
        num_islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                # Traverse an island using BFS if it finds it
                if grid[y][x] == '1':
                    num_islands += 1
                    self.traverse(y, x, grid)

        return num_islands

islands=[
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]

s = Solution()
print(s.numIslands(islands))


# Sample test case:
#   Input:
#       11110
#       11010
#       11000
#       00000
#   Output:
#       1

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(NM)
#   Space Complexity: O(1)
#   Runtime: 144 ms, faster than 81.71% of Python3
#       online submissions for Number of Islands.
#   Memory Usage: 13.7 MB, less than 91.45% of Python3
#       online submissions for Number of Islands.
