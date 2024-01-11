func maximumCount(nums []int) int {
    negCount := 0
    posCount := 0
    for _, v := range nums {
        if v > 0 {
            posCount++
        } else if v < 0 {
            negCount++
        }
    }

    if posCount > negCount {
        return posCount
    } else {
        return negCount
    }
}


// Performance Result:
//   Coding Time: 00:02:30
//   Time Complexity: O(n)
//   Space Complexity: O(1)
//   Runtime: 11 ms, faster than 82.72%
//   Memory Usage: 6.40 MB, less than 60.49%
