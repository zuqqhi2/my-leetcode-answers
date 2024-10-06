use std::collections::HashMap;

impl Solution {
    pub fn largest_unique_number(nums: Vec<i32>) -> i32 {
        let mut numCounts: HashMap<i32, i32> = HashMap::new();

        for v in nums {
            let cnt = numCounts.entry(v).or_insert(0);
            *cnt += 1;
        }

        let mut numCountVec: Vec<(&i32, &i32)> = numCounts.iter().collect();
        numCountVec.sort_by(|a, b| (*b.0).cmp(a.0));
        for (i, &v) in numCountVec.iter().enumerate() {
            if *v.1 == 1 {
                return *v.0;
            }
        }
        return -1;
    }
}


// Performance Result:
//   Coding Time: 00:21:46
//   Time Complexity: O(n log n)
//   Space Complexity: O(n)
//   Runtime: 1 ms, faster than 74.42%
//   Memory Usage: 2.18 MB, less than 46.51%