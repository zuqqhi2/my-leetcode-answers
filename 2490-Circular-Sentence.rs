impl Solution {
    pub fn is_circular_sentence(sentence: String) -> bool {
        let words: Vec<&str> = sentence.split(" ").collect();
        if words.len() <= 0 {
            return true
        } else if words.len() == 1 {
            if words[0].chars().nth(0).unwrap() == words[0].chars().last().unwrap() {
                return true;
            } else {
                return false;
            }
        }

        let firstWordHeadChar = words[0].chars().nth(0).unwrap();
        let mut prevWordTailChar: char = 'a';
        for (idx, word) in words.iter().enumerate() {
            let wordTailChar = word.chars().last().unwrap();
            if idx == 0 {
                prevWordTailChar = wordTailChar;
            } else if idx == words.len() - 1 {
                if word.chars().nth(0).unwrap() != prevWordTailChar {
                    return false;
                }

                if wordTailChar != firstWordHeadChar {
                    return false;
                }
            } else {
                if word.chars().nth(0).unwrap() != prevWordTailChar {
                    return false;
                }

                prevWordTailChar = wordTailChar;
            }
        }

        return true
    }
}

// Performance Result:
//   Coding Time: 00:23:32
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 1 ms, faster than 100.00%
//   Memory Usage: 2.12 MB, less than 83.33%
