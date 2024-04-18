impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut resDigits = digits;
        let mut isCarryUp = false;
        let mut curIdx = resDigits.len() - 1;
        while isCarryUp || curIdx == resDigits.len() - 1 {
            isCarryUp = false;

            resDigits[curIdx] += 1;
            if resDigits[curIdx] >= 10 {
                resDigits[curIdx] = 0;
                isCarryUp = true;
            }

            if curIdx == 0 && isCarryUp {
                resDigits.insert(0, 1);
                break;
            } else {
                curIdx -= 1;
            }
        }

        return resDigits;
    }
}


// Performance Result:
//   Coding Time: 00:13:30
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 1 ms, faster than 71.77%
//   Memory Usage: 2.15 MB, less than 13.92%
