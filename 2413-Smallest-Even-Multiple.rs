impl Solution {
    pub fn smallest_even_multiple(n: i32) -> i32 {
        if n % 2 == 0 { return n; }
        else { return n * 2; }
    }
}


// Performance Result:
//   Coding Time: 00:06:01
//   Time Complexity: O(1)
//   Space Complexity: O(1)
//   Runtime: 0 ms, faster than 100.00%
//   Memory Usage: 1.96 MB, less than 98.21%
