func abs(a int) int {
    if a < 0 {
        return -1 * a
    } else {
        return a
    }
}

func findClosestNumber(nums []int) int {
    res := 1000000
    for _, n := range nums {
        if abs(res) > abs(n) {
            res = n
        } else if abs(res) == abs(n) && n > res {
            res = n
        }
    }

    return res
}


// Performance Result:
//   Coding Time: 00:06:07
//   Time Complexity: O(n)
//   Space Complexity: O(1)
//   Runtime: 21 ms, faster than 41.03%
//   Memory Usage: 6.56 MB, less than 94.87%
