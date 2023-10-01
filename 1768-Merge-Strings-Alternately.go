func mergeAlternately(word1 string, word2 string) string {
    idx1 := 0
    idx2 := 0
    res := ""
    for idx1 < len(word1) || idx2 < len(word2) {
        if idx1 < len(word1) {
            res = res + (string)(word1[idx1])
            idx1++
        }
        if idx2 < len(word2) {
            res = res + (string)(word2[idx2])
            idx2++
        }
    }

    return res
}


// Performance Result:
//   Coding Time: 00:05:46
//   Time Complexity: O(nm)
//   Space Complexity: O(nm)
//   Runtime: 2 ms, faster than 38.64%
//   Memory Usage: 2.71 MB, less than 14.53%
