func Min(x, y int) int {
 if x < y {
   return x
 }
 return y
}

func Max(x, y int) int {
 if x > y {
   return x
 }
 return y
}

func minMaxGame(nums []int) int {
    length := len(nums)
    prev := nums
    isMin := true
    for length > 1 {
        next := make([]int, length / 2)
        for i := 0; i < length - 1; i = i + 2 {
            if isMin {
                next[i / 2] = Min(prev[i], prev[i + 1])
                isMin = false
            } else {
                next[i / 2] = Max(prev[i], prev[i + 1])
                isMin = true
            }
        }
        prev = next
        length /= 2
    }

    return prev[0]
}


// Performance Result:
//   Coding Time: 00:12:29
//   Time Complexity: O(NM)
//   Space Complexity: O(N)
//   Runtime: 6 ms, faster than 56%
//   Memory Usage: 3.6 MB, less than 20%
