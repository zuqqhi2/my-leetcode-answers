impl Solution {
    pub fn row_and_maximum_ones(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let mut maxNumOne = 0;
        let mut maxNumOneIdx = 0;
        for row in (0..mat.len()) {
            let mut numOne = 0;
            for v in &mat[row] {
                if *v == 1 {
                    numOne += 1;
                }
            }

            if maxNumOne < numOne {
                maxNumOne = numOne;
                maxNumOneIdx = row;
            }
        }

        return vec![maxNumOneIdx as i32, maxNumOne];
    }
}

// Performance Result:
//   Coding Time: 00:19:07
//   Time Complexity: O(N)
//   Space Complexity: O(1)
//   Runtime: 14 ms, faster than 73.33%
//   Memory Usage: 2.18 MB, less than 93.33%
