func findCenter(edges [][]int) int {
    cnts := make(map[int]int)
    maxVal := 0
    maxNode := 0
    for _, edge := range edges {
        cnts[edge[0]]++
        if cnts[edge[0]] > maxVal {
            maxVal = cnts[edge[0]]
            maxNode = edge[0]
        }

        cnts[edge[1]]++
        if cnts[edge[1]] > maxVal {
            maxVal = cnts[edge[1]]
            maxNode = edge[1]
        }
    }

    return maxNode
}

// Performance Result:
//   Coding Time: 00:03:41
//   Time Complexity: O(|V|)
//   Space Complexity: O(|V|)
//   Runtime: 197 ms, faster than 5.26%
//   Memory Usage: 17.9 MB, less than 28.95%
