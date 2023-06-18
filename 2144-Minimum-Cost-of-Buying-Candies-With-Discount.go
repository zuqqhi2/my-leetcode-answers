import "sort"

func minimumCost(cost []int) int {
    sort.Slice(cost, func(i, j int) bool {
        return cost[i] > cost[j]
    })

    res := 0
    for i, v := range cost {
        if (i + 1) % 3 != 0 {
            res = res + v
        }
    }

    return res
}

// Performance Result:
//   Coding Time: 00:06:30
//   Time Complexity: O(n log n)
//   Space Complexity: O(1)
//   Runtime: 2 ms, faster than 90.48%
//   Memory Usage: 2.6 MB, less than 57.14%
