import "strings"

func mostWordsFound(sentences []string) int {
    maxWords := 0
    for _, s := range sentences {
        numWords := len(strings.Split(s, " "))
        if numWords > maxWords {
            maxWords = numWords
        }
    }

    return maxWords
}


// Performance Result:
//   Coding Time: 00:02:52
//   Time Complexity: O(nm)
//   Space Complexity: O(1)
//   Runtime: 5 ms, faster than 41.80%
//   Memory Usage: 4.24 MB, less than 11.64%
