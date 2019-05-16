impl Solution {
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut max_so_far = nums[0];
        let mut max_ending_here = 0;

        // Kadane Algorithm
        for i in 0..nums.len() {
            max_ending_here += nums[i];
            if max_so_far < max_ending_here { max_so_far = max_ending_here }
            if max_ending_here < 0 { max_ending_here = 0 }
        }

        return max_so_far
    }
}

// Sample Testcase:
//   Input:
//     [-2,1,-3,4,-1,2,1,-5,4]
//   Output:
//     6

// Performance Result:
//   Coding TIme: 00:15:17
//   Runtime: 0 ms, faster than 100.00% of Rust online submissions for Maximum Subarray.
//   Memory Usage: 2.6 MB, less than 61.54% of Rust online submissions for Maximum Subarray.
