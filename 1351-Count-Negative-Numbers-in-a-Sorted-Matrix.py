class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        num_neg = 0

        for y in reversed(range(len(grid))):
            for x in reversed(range(len(grid[0]))):
                if grid[y][x] < 0:
                    num_neg += 1
                else:
                    break

        return num_neg


# Performance Result:
#   Coding Time: 00:02:37
#   Time Complexity: O(NM)
#   Space Complexity: O(1)
#   Runtime: 120 ms, faster than 51.71%
#   Memory Usage: 15.2 MB, less than 45.82%
