func bestHand(ranks []int, suits []byte) string {
    // Check Flush
    isFlush := true
    for _, v := range suits {
        if v != suits[0] {
            isFlush = false
            break
        }
    }
    if isFlush {
        return "Flush"
    }

    // Check Three of a Kind
    // Check Pair
    rankCounts := make(map[int]int)
    for _, v := range ranks {
        rankCounts[v] = rankCounts[v] + 1
    }

    isThreeOfAKind := false
    isPair := false
    for _, v := range rankCounts {
        if v >= 3 {
            isThreeOfAKind = true
        }
        if v >= 2 {
            isPair = true
        }
    }

    if isThreeOfAKind {
        return "Three of a Kind"
    }
    if isPair {
        return "Pair"
    }

    return "High Card"
}


// Performance Result:
//   Coding Time: 00:11:34
//   Time Complexity: O(n)
//   Space Complexity: O(n)
//   Runtime: 2 ms, faster than 8.00%
//   Memory Usage: 2.00 MB, less than 8.00%
