impl Solution {
    pub fn binary_gap(n: i32) -> i32 {
        let binN = format!("{:b}", n);

        let mut maxDist: i32 = 0;
        let mut isChecking = false;
        let mut prev1Pos = 0;
        for idx in 0..binN.len() {
            if binN.chars().nth(idx).unwrap() == '1' {
                if isChecking && (idx - prev1Pos) as i32 > maxDist {
                    maxDist = (idx - prev1Pos) as i32;
                } else if !isChecking {
                    isChecking = true;
                }
                prev1Pos = idx;
            }
        }

        return maxDist;
    }
}


// Performance Result:
//   Coding Time: 00:11:40
//   Time Complexity: O(n)
//   Space Complexity: O(1)
//   Runtime: 0 ms, faster than 100.00%
//   Memory Usage: 2.25 MB, less than 43.75%