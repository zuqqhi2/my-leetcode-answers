func minTimeToType(word string) int {
    alphabets := map[string]int {
        "a": 1, "b": 2, "c": 3,
        "d": 4, "e": 5, "f": 6,
        "g": 7, "h": 8, "i": 9,
        "j": 10, "k": 11, "l": 12,
        "m": 13, "n": 14, "o": 15,
        "p": 16, "q": 17, "r": 18,
        "s": 19, "t": 20, "u": 21,
        "v": 22, "w": 23, "x": 24,
        "y": 25, "z": 26}

    cur := "a"
    res := 0
    for _, c := range word {
        if cur == string(c) {
            res += 1
        } else {
            diff_pos := alphabets[string(c)] - alphabets[cur]
            if alphabets[cur] > alphabets[string(c)] {
                diff_pos = alphabets[cur] - alphabets[string(c)]
            }

            counter_clockwisee_diff := 26 - alphabets[string(c)] + alphabets[cur]
            if diff_pos > counter_clockwisee_diff {
                diff_pos = counter_clockwisee_diff
            }

            clockwise_diff := 26 - alphabets[cur] + alphabets[string(c)]
            if diff_pos > clockwise_diff {
                diff_pos = clockwise_diff
            }

            res += diff_pos + 1
            cur = string(c)
        }
    }

    return res
}


// Performance Result:
//   Coding Time: 00:19:23
//   Time Complexity: O(N)
//   Space Complexity: O(1)
//   Runtime: 4 ms, faster than 52.38%
//   Memory Usage: 2.1 MB, less than 61.90%
