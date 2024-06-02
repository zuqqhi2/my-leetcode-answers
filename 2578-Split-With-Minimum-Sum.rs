impl Solution {
    pub fn split_num(num: i32) -> i32 {
        let mut digits: Vec<i32> = vec![];
        let mut tmpNum = num;
        while tmpNum > 0 {
            digits.push(tmpNum % 10);
            tmpNum /= 10;
        }
        digits.sort();
        
        let mut res1: i32 = digits[0];
        let mut res2: i32 = digits[1];
        for i in 2..digits.len() {
            if i % 2 == 0 {
                res1 = res1 * 10 + digits[i];
            } else {
                res2 = res2 * 10 + digits[i]; 
            }
        }
        
        return res1 + res2;
    }
}


// Performance Result:
//   Coding Time: 00:08:21
//   Time Complexity: O(n)
//   Space Complexity: O(1)
//   Runtime: 1 ms, faster than 66.67%
//   Memory Usage: 2.18 MB, less than 11.11%