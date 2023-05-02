func countPrefixes(words []string, s string) int {
    res := 0
    for _, w := range words {
        prefSize := len(w)
        if len(s) < len(w) {
            prefSize = len(s)
        }

        if w == s[:prefSize] {
            res += 1
        }
    }

    return res
}


// Performance Result:
//   Coding Time: 00:05:36
//   Time Complexity: O(N)
//   Space Complexity: O(1)
//   Runtime: 0 ms, faster than 100%
//   Memory Usage: 3.7 MB, less than 96.83%
