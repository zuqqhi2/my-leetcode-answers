func shiftGrid(grid [][]int, k int) [][]int {
    if len(grid) == 1 && len(grid[0]) == 1 {
        return grid
    }

    tmpGrid := make([][]int, len(grid))
    for y := 0; y < len(grid); y++ {
        tmpGrid[y] = make([]int, len(grid[0]))
    }

    for y := 0; y < len(grid); y++ {
        for x := 0; x < len(grid[0]); x++ {
            nextY := y
            nextX := x + k
            for nextX >= len(grid[0]) {
                nextX = nextX - len(grid[0])
                nextY++
            }
            for nextY >= len(grid) {
                nextY = nextY - len(grid)
            }
            tmpGrid[nextY][nextX] = grid[y][x]
        }
    }

    return tmpGrid
}

// Performance Result:
//   Coding Time: 00:13:34
//   Time Complexity: O(nm)
//   Space Complexity: O(nm)
//   Runtime: 13 ms, faster than 96.39%
//   Memory Usage: 6.93 MB, less than 65.06%
