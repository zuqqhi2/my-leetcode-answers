func checkValid(matrix [][]int) bool {
    n := len(matrix)
    // Row base check
    for y := 0; y < n; y++ {
        variety := map[int]bool{}
        for x := 0; x < n; x++ {
            variety[matrix[y][x]] = true
        }
        if len(variety) != n {
            return false
        }
    }

    // Column base check
    for x := 0; x < n; x++ {
        variety := map[int]bool{}
        for y := 0; y < n; y++ {
            variety[matrix[y][x]] = true
        }
        if len(variety) != n {
            return false
        }
    }

    return true
}

// Performance Result:
//   Coding Time: 00:07:49
//   Time Complexity: O(n^2)
//   Space Complexity: O(n)
//   Runtime: 178 ms, faster than 23.33%
//   Memory Usage: 8 MB, less than 6.67%
