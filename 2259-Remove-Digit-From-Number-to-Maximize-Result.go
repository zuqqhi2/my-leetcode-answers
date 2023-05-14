import "sort"

func removeDigit(number string, digit byte) string {
    candidates := []string{}
    for i, v := range number {
        if byte(v) == digit {
            candidates = append(candidates, number[:i] + number[i + 1:])
        }
    }
    if len(candidates) == 1 {
        return candidates[0]
    }

    sort.Slice(candidates, func(i, j int) bool {
        return candidates[i] > candidates[j]
    })

    return candidates[0]
}

// Performance Result:
//   Coding Time: 00:13:22
//   Time Complexity: O(n)
//   Space Complexity: O(n)
//   Runtime: 3 ms, faster than 8.33%
//   Memory Usage: 2.3 MB, less than 8.33%
