impl Solution {
    pub fn largest_good_integer(num: String) -> String {
        let mut res: &str = "-1";
        if num.len() == 3 {
            if num.chars().nth(0).unwrap() == num.chars().nth(1).unwrap() && num.chars().nth(0).unwrap() == num.chars().nth(2).unwrap() {
                res = &num;
            }
        }

        for endIdx in 3..(num.len() + 1) {
            let targetNumStr = &num[(endIdx - 3)..endIdx];
            if targetNumStr.chars().nth(0).unwrap() != targetNumStr.chars().nth(1).unwrap() || targetNumStr.chars().nth(0).unwrap() != targetNumStr.chars().nth(2).unwrap() {
                continue;
            }

            let curNum: i32 = res.parse().unwrap();
            let newNum: i32 = targetNumStr.parse().unwrap();
            if newNum > curNum {
                res = targetNumStr;
            }
        }

        if res == "-1" {
            return "".to_string();
        } else {
            return res.to_string();
        }
    }
}


// Performance Result:
//   Coding Time: 00:11:50
//   Time Complexity: O(n)
//   Space Complexity: O(1)
//   Runtime: 1 ms, faster than 84.38%
//   Memory Usage: 2.14 MB, less than 40.63%