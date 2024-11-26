impl Solution {
    pub fn digit_sum(s: String, k: i32) -> String {
        let mut res: String = s;
        while res.len() > k as usize {
            let mut newRes: String = "".to_string();
            for i in (0..res.len()).step_by(k as usize) {
                let mut sumRes: i32 = 0;
                for j in 0..(k as usize) {
                    if i + j < res.len() {
                        sumRes += &res[(i+j)..(i+j+1)].parse::<i32>().unwrap();
                    }
                }
                newRes = format!("{}{}", newRes, sumRes.to_string());
            }
            res = newRes;
        }

        return res;
    }
}


// Performance Result:
//   Coding Time: 00:30:36
//   Time Complexity: O(n^2)
//   Space Complexity: O(n)
//   Runtime: 0 ms, faster than 100.00%
//   Memory Usage: 2.33 MB, less than 46.15%