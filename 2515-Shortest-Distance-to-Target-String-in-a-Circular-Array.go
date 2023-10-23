func closetTarget(words []string, target string, startIndex int) int {
    numOp := 0
    curIdxForward := startIndex
    curIdxBackward := startIndex
    for words[curIdxForward] != target && words[curIdxBackward] != target {
        curIdxForward++
        if curIdxForward >= len(words) {
            curIdxForward = 0
        }

        curIdxBackward--
        if curIdxBackward < 0 {
            curIdxBackward = len(words) - 1
        }

        numOp++
        if numOp >= len(words) {
            return -1
        }
    }

    return numOp
}


// Performance Result:
//   Coding Time: 00:09:74
//   Time Complexity: O(n)
//   Space Complexity: O(1)
//   Runtime: 3 ms, faster than 100.00%
//   Memory Usage: 6.66 MB, less than 84.21%
