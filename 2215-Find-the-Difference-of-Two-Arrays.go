func findDifference(nums1 []int, nums2 []int) [][]int {
    cnts1 := make(map[int]int)
    for _, v := range nums1 {
        cnts1[v]++
    }
    cnts2 := make(map[int]int)
    for _, v := range nums2 {
        cnts2[v]++
    }

    res1 := make([]int, 0, 4)
    for v := range cnts1 {
        _, ok := cnts2[v]
        if !ok { res1 = append(res1, v) }
    }
    res2 := make([]int, 0, 4)
    for v := range cnts2 {
        _, ok := cnts1[v]
        if !ok { res2 = append(res2, v) }
    }

    return [][]int{res1, res2}
}


// Performance Result:
//   Coding Time: 00:08:31
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 34 ms, faster than 47.30%
//   Memory Usage: 8.3 MB, less than 5.40%
