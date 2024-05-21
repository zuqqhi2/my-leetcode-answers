impl Solution {
    pub fn max_width_of_vertical_area(points: Vec<Vec<i32>>) -> i32 {
        let mut tmpPoints: Vec<Vec<i32>> = points;
        tmpPoints.sort_by(|a, b| a[0].partial_cmp(&(b[0])).unwrap());
        
        let mut res: i32 = 0;
        for idx in 1..(tmpPoints.len() - 1) {
            if tmpPoints[idx][0] - tmpPoints[idx - 1][0] > res {
                res = tmpPoints[idx][0] - tmpPoints[idx - 1][0];
            }
        }
        return res;
    }
}


// Performance Result:
//   Coding Time: 00:08:04
//   Time Complexity: O(n log n)
//   Space Complexity: O(n)
//   Runtime: 43 ms, faster than 8.51%
//   Memory Usage: 9.48 MB, less than 100.00%