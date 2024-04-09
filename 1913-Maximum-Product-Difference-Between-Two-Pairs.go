func maxProductDifference(nums []int) int {
    sort.Ints(nums)

    tail := len(nums) - 1
    return (nums[tail] * nums[tail - 1]) - (nums[0] * nums[1])
}


// Performance Result:
//   Coding Time: 00:04:59
//   Time Complexity: O(n log n)
//   Space Complexity: O(1)
//   Runtime: 18 ms, faster than 75.63%
//   Memory Usage: 6.30 MB, less than 72.27%
