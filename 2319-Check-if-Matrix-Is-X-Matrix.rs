impl Solution {
    pub fn check_x_matrix(grid: Vec<Vec<i32>>) -> bool {
        for y in 0..grid.len() {
            for x in 0..grid[0].len() {
                if y == x {
                    if grid[y][x] == 0 { return false; }
                } else if x == grid.len() - y - 1 {
                    if grid[y][grid.len() - y - 1] == 0 { return false; }
                } else if grid[y][x] != 0 {
                    return false; }
            }
        }

        return true;
    }
}


// Performance Result:
//   Coding Time: 00:08:35
//   Time Complexity: O(n^2)
//   Space Complexity: O(1)
//   Runtime: 4 ms, faster than 91.67%
//   Memory Usage: 2.36 MB, less than 58.33%