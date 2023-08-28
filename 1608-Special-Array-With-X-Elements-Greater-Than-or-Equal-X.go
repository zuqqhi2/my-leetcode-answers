func specialArray(nums []int) int {
    maxX := 0
    for _, v := range nums {
        if v > 0 {
            maxX += 1
        }
    }

    for i := maxX; i >= 1; i-- {
        cnt := 0
        for _, v := range nums {
            if v >= i {
                cnt++
            }
        }
        if cnt == i {
            return i
        }
    }

    return -1
}


// Performance Result:
//   Coding Time: 00:13:45
//   Time Complexity: O(n^2)
//   Space Complexity: O(1)
//   Runtime: 2 ms, faster than 53.33%
//   Memory Usage: 2.18 MB, less than 100.00%
