import (
    "fmt"
    "strings"
)

func makeFancyString(s string) string {
    var res []string
    var prevCount int32 = 1
    var prevChar int32 = 0
    for _, c := range s {
        if c == prevChar {
            prevCount += 1
            if prevCount < 3 {
                res = append(res, string(c))
            }
        } else {
            prevCount = 1
            prevChar = c
            res = append(res, string(c))
        }
    }

    return strings.Join(res[:], "")
}

// Performance Result:
//   Coding Time: 00:16:10
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 318 ms, faster than 7.41%
//   Memory Usage: 13.8 MB, less than 7.41%
