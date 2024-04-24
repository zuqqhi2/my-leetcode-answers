use std::collections::HashMap;

impl Solution {
    pub fn most_frequent_even(nums: Vec<i32>) -> i32 {
        let mut freqs = HashMap::new();
        let mut maxFreq = 0;
        for v in nums {
            if v % 2 == 1 { continue; }
            let count = freqs.entry(v).or_insert(0);
            *count += 1;
            if *count > maxFreq { maxFreq = *count; }
        }

        return match freqs.iter().filter(|(&k, &v)| v == maxFreq).min_by_key(|&k| k) {
            Some(v) => *v.0 as i32,
            None => -1,
        }
    }
}

// Performance Result:
//   Coding Time: 00:09:54
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 7 ms, faster than 82.14%
//   Memory Usage: 2.10 MB, less than 100.00%
