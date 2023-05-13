func validPath(n int, edges [][]int, source int, destination int) bool {
    if n == 1 {
        return true
    }

    next := map[int][]int{}
    for _, edge := range edges {
        next[edge[0]] = append(next[edge[0]], edge[1])
        next[edge[1]] = append(next[edge[1]], edge[0])
    }

    queue := []int{source}
    visited := make(map[int]bool)
    for len(queue) > 0 {
        curNode := queue[0]
        queue = queue[1:]

        for _, n := range next[curNode] {
            if n == destination {
                return true
            }

            if _, ok := visited[n]; !ok {
                queue = append(queue, n)
                visited[n] = true
            }
        }
    }

    return false
}

// Performance Result:
//   Coding Time: 00:21:01
//   Time Complexity: O(max(|V|, |E|))
//   Space Complexity: O(max(|V|, |E|))
//   Runtime: 359 ms, faster than 62.40%
//   Memory Usage: 46.2 MB, less than 50.37%
