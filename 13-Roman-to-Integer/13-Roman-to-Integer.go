package main

import "fmt"

// Time Complexity : O(n)
// Space Complexity: O(1)
func romanToInt(s string) int {
    // Var for calculation result
    result := 0

    // Step value
    step := 1

    // Process for each chars
    for idx := 0; idx < len(s); idx += step {
        // Pick up max 2 length sub string
        pattern := fmt.Sprintf("%+v", s[idx:idx + 1])
        if idx + 2 <= len(s) {
            pattern = fmt.Sprintf("%+v", s[idx:idx + 2])
        }

        // Combination pattern check
        flgCombProcessed := false
        switch pattern {
            case "IV": { result += 4;   flgCombProcessed = true; }
            case "IX": { result += 9;   flgCombProcessed = true; }
            case "XL": { result += 40;  flgCombProcessed = true; }
            case "XC": { result += 90;  flgCombProcessed = true; }
            case "CD": { result += 400; flgCombProcessed = true; }
            case "CM": { result += 900; flgCombProcessed = true; }
        }

        // Single pattern check
        if !flgCombProcessed {
            switch pattern[0] {
                case 'I': result += 1
                case 'V': result += 5
                case 'X': result += 10
                case 'L': result += 50
                case 'C': result += 100
                case 'D': result += 500
                case 'M': result += 1000
            }
        }

        // Move 2 chars if this iteration's pattern is combination pattern
        if flgCombProcessed {
            step = 2
        } else {
            step = 1
        }

        // Debug Print
        // fmt.Printf("%d %+v %d\n", idx, pattern, result)
    }

    return result
}

// Sample Testcase:
//   Input:
//     MCMXCIV
//   Output:
//     1994

// Performance Result:
//   Runtime: 4 ms, faster than 91.09% of Go online submissions for Roman to Integer.
//   Memory Usage: 3.9 MB, less than 14.29% of Go online submissions for Roman to Integer.
