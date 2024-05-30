use std::collections::HashSet;

impl Solution {
    pub fn find_max_k(nums: Vec<i32>) -> i32 {
        let mut tmpNums = nums;
        let mut numSet: HashSet<i32> = tmpNums.iter().cloned().collect();

        tmpNums.sort();
        for idx in (0..tmpNums.len()).rev() {
            if numSet.contains(&-tmpNums[idx]) {
                return tmpNums[idx]
            }
        }

        return -1;
    }
}


// Performance Result:
//   Coding Time: 00:10:19
//   Time Complexity: O(n)
//   Space Complexity: O(n)
//   Runtime: 6 ms, faster than 7.16%
//   Memory Usage: 2.18 MB, less than 59.84%