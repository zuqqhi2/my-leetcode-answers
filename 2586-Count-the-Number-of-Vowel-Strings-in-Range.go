import "regexp"

func vowelStrings(words []string, left int, right int) int {
    pattern := `^([aeiou].*[aeiou]|[aeiou])$`
    re, _ := regexp.Compile(pattern)
    res := 0
    for i := left; i <= right; i++ {
        matches := re.FindAllString(words[i], -1)
        if len(matches) > 0 {
            res++
        }
    }

    return res
}

// Performance Result:
//   Coding Time: 00:08:53
//   Time Complexity: O(n)
//   Space Complexity: O(1)
//   Runtime: 14 ms, faster than 9.88%
//   Memory Usage: 7.76 MB, less than 7.41%
