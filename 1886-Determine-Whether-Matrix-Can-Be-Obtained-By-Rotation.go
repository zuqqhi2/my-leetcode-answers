func findRotation(mat [][]int, target [][]int) bool {
    n := len(mat)
    for i := 0; i < 4; i++ {
        // Rotate
        if i > 0 {
            tmpMat := make([][]int, n)
            for y := 0; y < n; y++ {
                tmpMat[y] = make([]int, n)
            }

            for y := 0; y < n; y++ {
                for x := 0; x < n; x++ {
                    tmpMat[x][n - 1 - y] = mat[y][x]
                }
            }
            mat = tmpMat
        }

        // Check
        isValid := true
        for y := 0; y < n; y++ {
            for x := 0; x < n; x++ {
                if mat[y][x] != target[y][x] {
                    isValid = false
                }
            }
        }

        if isValid {
            return true
        }
    }

    return false
}


// Performance Result:
//   Coding Time: 00:22:48
//   Time Complexity: O(n^2)
//   Space Complexity: O(n^2)
//   Runtime: 3 ms, faster than 72.73%
//   Memory Usage: 2.47 MB, less than 9.09%
