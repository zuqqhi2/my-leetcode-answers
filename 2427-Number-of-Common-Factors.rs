impl Solution {
    pub fn common_factors(a: i32, b: i32) -> i32 {
        let mut res: i32 = 1; // 1 is always common factor
        for factor in 2..std::cmp::min(a, b) + 1 {
            if a % factor == 0 && b % factor == 0 {
                res += 1;
            }
        }
        return res;
    }
}


// Performance Result:
//   Coding Time: 00:05:13
//   Time Complexity: O(n)
//   Space Complexity: O(1)
//   Runtime: 0 ms, faster than 100.00%
//   Memory Usage: 2.08 MB, less than 52.63%