impl Solution {
    pub fn arithmetic_triplets(nums: Vec<i32>, diff: i32) -> i32 {
        let mut res: i32 = 0;
        for targetIdx in 1..(nums.len() - 1) {
            let mut isFound: bool = false;
            for left in 0..targetIdx {
                if nums[targetIdx] - nums[left] == diff {
                    isFound = true;
                }
            }
            if !isFound { continue; }

            isFound = false;
            for right in (targetIdx + 1)..nums.len() {
                if nums[right] - nums[targetIdx] == diff {
                    isFound = true;
                }
            }
            if !isFound { continue; }

            res += 1;
        }

        return res;
    }
}


// Performance Result:
//   Coding Time: 00:11:50
//   Time Complexity: O(n ^ 2)
//   Space Complexity: O(1)
//   Runtime: 1 ms, faster than 85.71%
//   Memory Usage: 2.04 MB, less than 90.48%