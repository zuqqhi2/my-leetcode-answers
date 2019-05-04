impl Solution {
    /// Convert roman number to integer
    /// Time Complexity: O(n)
    /// Space Complexity: O(1)
    pub fn roman_to_int(s: String) -> i32 {
        // Will be stored calculated answer integer
        let mut result = 0;
        // For skipping next char when it finds special combination
        let mut skip_flg = false;

        // Scan a given roman number string
        for i in 0..s.len() {
            // Skip when there was special combination
            if skip_flg { skip_flg = false; continue; }

            // Check special combination
            let mut pair_number = s.get(i..i+2);
            if pair_number == Some("IV")      { result += 4;   skip_flg = true; }
            else if pair_number == Some("IX") { result += 9;   skip_flg = true; }
            else if pair_number == Some("XL") { result += 40;  skip_flg = true; }
            else if pair_number == Some("XC") { result += 90;  skip_flg = true; }
            else if pair_number == Some("CD") { result += 400; skip_flg = true; }
            else if pair_number == Some("CM") { result += 900; skip_flg = true; }
            else {
                // Convert 1 roman number char to integer and sum
                let curChar = s.get(i..i+1);
                if curChar == Some("I")      { result += 1;    }
                else if curChar == Some("V") { result += 5;    }
                else if curChar == Some("X") { result += 10;   }
                else if curChar == Some("L") { result += 50;   }
                else if curChar == Some("C") { result += 100;  }
                else if curChar == Some("D") { result += 500;  }
                else if curChar == Some("M") { result += 1000; }
            }
        }

        return result;
    }
}

// Sample Testcase:
//   Input:
//     "MCMXCIV"
//   Output:
//     1994

// Performance Result:
//   Runtime: 8 ms, faster than 100.00% of Rust online submissions for Roman to Integer.
//   Memory Usage: 2.4 MB, less than 87.50% of Rust online submissions for Roman to Integer.
