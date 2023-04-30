func greatestLetter(s string) string {
    existsUpper := map[uint8]bool {}
    // Check upper letters
    for _, c := range s {
        letterCode := uint8(c)
        if letterCode < 97 {
            existsUpper[letterCode + 32] = true
        }
    }

    // Check lower letters and result
    greatestLetterCode := uint8(0)
    for _, c := range s {
        letterCode := uint8(c)
        _, ok := existsUpper[letterCode]
        if letterCode >= 97 && ok && letterCode > greatestLetterCode {
            greatestLetterCode = letterCode
        }
    }

    if greatestLetterCode == 0 {
        return ""
    } else {
        return string(int(greatestLetterCode) - 32)
    }
}


// Performance Result:
//   Coding Time: 00:18:56
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 6 ms, faster than 42.11%
//   Memory Usage: 2.2 MB, less than 73.68%
