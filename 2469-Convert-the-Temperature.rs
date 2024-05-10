impl Solution {
    pub fn convert_temperature(celsius: f64) -> Vec<f64> {
        return vec![celsius + 273.15, celsius * 1.8 + 32.0]
    }
}

// Performance Result:
//   Coding Time: 00:01:51
//   Time Complexity: O(1)
//   Space Complexity: O(1)
//   Runtime: 0 ms, faster than 100.00%
//   Memory Usage: 1.97 MB, less than 95.77%