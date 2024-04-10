func minimumOperations(nums []int) int {
    numOperations := 0
    isContinue := true
    for isContinue {
        isContinue = false

        smallest := 1000
        for _, v := range nums {
            if v > 0 && smallest > v {
                smallest = v
                isContinue = true
            }
        }
        if isContinue {
            numOperations++
        }

        for i := 0; i < len(nums); i++ {
            if nums[i] <= 0 {
                continue
            }

            nums[i] = nums[i] - smallest
        }
    }

    return numOperations
}


// Performance Result:
//   Coding Time: 00:06:56
//   Time Complexity: O(nm)
//   Space Complexity: O(1)
//   Runtime: 2 ms, faster than 34.15%
//   Memory Usage: 2.24 MB, less than 56.10%
