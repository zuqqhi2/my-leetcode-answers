func maxSum(nums []int) int {
    digitIdxMap := map[int][]int{}
    for idx, v := range nums {
        maxDigit := 0
        for v > 0 {
            digit := v % 10
            if digit > maxDigit {
                maxDigit = digit
            }
            v = v / 10
        }
        digitIdxMap[maxDigit] = append(digitIdxMap[maxDigit], idx)
    }

    maxSum := 0
    for _, v := range digitIdxMap {
        if len(v) < 2 {
            continue
        }

        for i := 0; i < len(v) - 1; i++ {
            for j := 1; j < len(v); j++ {
                if i == j {
                    continue
                }

                localSum := nums[v[i]] + nums[v[j]]
                if localSum > maxSum {
                    maxSum = localSum
                }
            }
        }
    }

    if maxSum == 0 {
        return -1
    } else {
        return maxSum
    }
}


// Performance Result:
//   Coding Time: 00:17:48
//   Time Complexity: O(n^2)
//   Space Complexity: O(n)
//   Runtime: 14 ms, faster than 66.67%
//   Memory Usage: 5.48 MB, less than 18.52%
