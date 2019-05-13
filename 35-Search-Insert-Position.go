// Time Complexity: O(log n)
// Space Complexity: O(1)
func searchInsert(nums []int, target int) int {
    // If an empty list is given or target is smallest value in the list, return 0
    if len(nums) == 0 || target < nums[0] { return 0 }
    // If target is largest value in the list, return size
    if target > nums[len(nums)-1] { return len(nums) }

    // Search using binary search
    left := 0
    right := len(nums) - 1
    mid := (left + right) / 2
    for left < right {
        if target == nums[mid] {
            return mid
        } else if target < nums[mid] {
            right = mid
        } else {
            left = mid
        }
        prev_mid := mid
        mid = (left + right) / 2

        // If middle index is not changed,
        // no target value inside the list but right idx will be right place
        // if we inesrt target into the list
        if mid == prev_mid { return right }
    }

    return 0
}

// Sample Testcase:
//   Input:
//     nums = [1,3,5,6]
//     tareget = 5
//   Output:
//     2

// Performance Result:
//   Coding Time: 00:13:35
//   Runtime: 4 ms, faster than 99.04% of Go online submissions for Search Insert Position.
//   Memory Usage: 3.1 MB, less than 9.38% of Go online submissions for Search Insert Position.
