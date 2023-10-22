func checkIfPangram(sentence string) bool {
    charCounts := map[rune]bool{
        rune("a"[0]): false, rune("b"[0]): false, rune("c"[0]): false, rune("d"[0]): false,
        rune("e"[0]): false, rune("f"[0]): false, rune("g"[0]): false, rune("h"[0]): false,
        rune("i"[0]): false, rune("j"[0]): false, rune("k"[0]): false, rune("l"[0]): false,
        rune("m"[0]): false, rune("n"[0]): false, rune("o"[0]): false, rune("p"[0]): false,
        rune("q"[0]): false, rune("r"[0]): false, rune("s"[0]): false, rune("t"[0]): false,
        rune("u"[0]): false, rune("v"[0]): false, rune("w"[0]): false, rune("x"[0]): false,
        rune("y"[0]): false, rune("z"[0]): false}

    for _, c := range sentence {
        charCounts[c] = true
    }

    for _, v := range charCounts {
        if !v {
            return false
        }
    }

    return true
}

// Performance Result:
//   Coding Time: 00:14:05
//   Time Complexity: O(n)
//   Space Complexity: O(1)
//   Runtime: 2 ms, faster than 55.63%
//   Memory Usage: 2.15 MB, less than 11.88%
