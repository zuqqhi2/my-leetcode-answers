impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        let mut res: i32 = 0;
        for op in operations {
            if op == "++X" || op == "X++" { res += 1; }
            else { res -= 1; }
        }

        return res;
    }
}

// Performance Result:
//   Coding Time: 00:01:53
//   Time Complexity: O(N)
//   Space Complexity: O(1)
//   Runtime: 0 ms, faster than 100.00%
//   Memory Usage: 2.08 MB, less than 97.10%
