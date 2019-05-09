/**
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 *
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    prev_idx = 0;
    cur_idx = 1;
    while (cur_idx < nums.length) {
        if (nums[prev_idx] == nums[cur_idx]) {
            // Remove current index element
            // It reduce length as well, so no current position update
            nums.splice(cur_idx, 1);
        } else {
            prev_idx = cur_idx; cur_idx += 1;
        }
    }

    return nums.length;
};

// Sample Testcase:
//   Input:
//     [1,1,2]
//   Output:
//     2
//     (but given array should be [1,2])

// Performance Result:
//   Coding Time: 00:25:29 (understanding return value takes time)
//   Runtime: 84 ms, faster than 68.90% of JavaScript online submissions for Remove Duplicates from Sorted Array.
//   Memory Usage: 37.3 MB, less than 30.70% of JavaScript online submissions for Remove Duplicates from Sorted Array.
