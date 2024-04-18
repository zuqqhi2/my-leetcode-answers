use std::collections::HashMap;

impl Solution {
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
        let mut maxFreq = 0;
        let mut valCounts = HashMap::new();
        for e in nums {
            let count = valCounts.entry(e).or_insert(0);
            *count += 1;
            if *count > maxFreq {
                maxFreq = *count;
            }
        }

        let mut res = 0;
        for (k, v) in &valCounts {
            if *v == maxFreq {
                res += *v;
            }
        }

        return res;
    }
}

// Performance Result:
//   Coding Time: 00:09:53
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 2 ms, faster than 51.30%
//   Memory Usage: 2.15 MB, less than 19.59%
