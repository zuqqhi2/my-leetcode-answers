impl Solution {
    pub fn similar_pairs(words: Vec<String>) -> i32 {
        let mut charWords: Vec<String> = vec![];
        for word in words {
            let v: Vec<char> = word.chars().collect();
            let mut y = v.clone();
            y.sort_by(|a, b| a.cmp(b));
            y.dedup();
            charWords.push(String::from_iter(y));
        }
        
        let mut res: i32 = 0;
        for i in 0..(charWords.len() - 1) {
            for j in (i + 1)..charWords.len() {
                if charWords[i] == charWords[j] {
                    res += 1;
                }
            }
        }

        return res;
    }
}

// Performance Result:
//   Coding Time: 00:14:31
//   Time Complexity: O(n^2)
//   Space Complexity: O(n)
//   Runtime: 12 ms, faster than 40.00%
//   Memory Usage: 2.23 MB, less than 53.55%