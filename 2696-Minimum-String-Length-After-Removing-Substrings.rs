impl Solution {
    pub fn min_length(s: String) -> i32 {
        let mut curS = s;
        let mut mAB = curS.find("AB");
        let mut mCD = curS.find("CD");
        while mAB.is_some() || mCD.is_some() {
            let mut isRemoved = false;
            if let Some(idx) = mAB {
                curS.remove(idx);
                curS.remove(idx);
                isRemoved = true;
            }

            if !isRemoved {
                if let Some(idx) = mCD {
                    curS.remove(idx);
                    curS.remove(idx);
                }
            }

            mAB = curS.find("AB");
            mCD = curS.find("CD");
        }

        return curS.len() as i32;
    }
}

// Performance Result:
//   Coding Time: 00:11:48
//   Time Complexity: O(n^m)
//   Space Complexity: O(n)
//   Runtime: 8 ms, faster than 30.00%
//   Memory Usage: 2.06 MB, less than 70.00%