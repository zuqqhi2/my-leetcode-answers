impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let mut res = Vec::new();

        let mut idx = 0;
        while idx < nums.len() {
            let startDigit = nums[idx];
            while idx + 1 < nums.len() && nums[idx] + 1 == nums[idx + 1] {
                idx += 1;
            }

            if startDigit != nums[idx] {
                res.push(format!("{}->{}", startDigit, nums[idx]))
            } else {
                res.push(format!("{}", nums[idx]))
            }

            idx += 1;
        }

        return res;
    }
}


// Performance Result:
//   Coding Time: 00:11:41
//   Time Complexity: O(n)
//   Space Complexity: O(n)
//   Runtime: 0 ms, faster than 100.00%
//   Memory Usage: 2.09 MB, less than 88.46%