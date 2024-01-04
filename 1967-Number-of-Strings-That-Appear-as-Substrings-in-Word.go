import "strings"

func numOfStrings(patterns []string, word string) int {
    res := 0
    for _, s := range patterns {
        searchRes := strings.Index(word, s)
        if searchRes >= 0 {
            res++
        }
    }

    return res
}


// Performance Result:
//   Coding Time: 00:04:37
//   Time Complexity: O(n)
//   Space Complexity: O(1)
//   Runtime: 2 ms, faster than 72.22%
//   Memory Usage: 2.63 MB, less than 52.78%
