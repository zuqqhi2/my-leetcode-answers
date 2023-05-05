func repeatedCharacter(s string) byte {
    cnts := make(map[rune]int)
    for _, c := range s {
        cnts[c]++
        if cnts[c] >= 2 {
            return byte(c)
        }
    }

    return byte('a')
}


// Performance Result:
//   Coding Time: 00:02:50
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 0 ms, faster than 100%
//   Memory Usage: 1.9 MB, less than 68.66%
