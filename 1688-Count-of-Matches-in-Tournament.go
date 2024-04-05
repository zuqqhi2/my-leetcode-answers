func numberOfMatches(n int) int {
    numMatches := 0
    for n > 1 {
        if n % 2 == 0 {
            numMatches = numMatches + n / 2
            n = n / 2
        } else {
            numMatches = numMatches + (n - 1) / 2
            n = (n - 1) / 2 + 1
        }
    }

    return numMatches
}


// Performance Result:
//   Coding Time: 00:03:41
//   Time Complexity: O(log n)
//   Space Complexity: O(1)
//   Runtime: 1 ms, faster than 73.11%
//   Memory Usage: 2.18 MB, less than 28.57%
