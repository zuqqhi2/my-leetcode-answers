func numberOfPairs(nums []int) []int {
    res := []int{0, 0}

    cnts := map[int]int{}
    for _, v := range nums {
        cnts[v] += 1
        if cnts[v] % 2 == 0 {
            res[0] += 1
        }
    }

    for k := range cnts {
        if cnts[k] % 2 != 0 {
            res[1] += 1
        }
    }

    return res
}


// Performance Result:
//   Coding Time: 00:14:44
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 4 ms, faster than 8.16%
//   Memory Usage: 2.4 MB, less than 61.22%
