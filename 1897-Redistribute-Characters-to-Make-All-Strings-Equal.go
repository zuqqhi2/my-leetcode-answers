func makeEqual(words []string) bool {
    targetCount := len(words)
    if targetCount == 1 {
        return true
    }

    chars := map[rune]int{}
    for _, word := range words {
        for _, c := range word {
            chars[c] = chars[c] + 1
        }
    }

    for _, v := range chars {
        if v % targetCount != 0 {
            return false
        }
    }

    return true
}


// Performance Result:
//   Coding Time: 00:09:35
//   Time Complexity: O(nm)
//   Space Complexity: O(m)
//   Runtime: 14 ms, faster than 7.69%
//   Memory Usage: 3.93 MB, less than 38.46%
