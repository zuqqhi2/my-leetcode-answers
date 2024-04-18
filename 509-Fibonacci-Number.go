func fib(n int) int {
    if n == 0 {
        return 0
    } else if n == 1 {
        return 1
    } else {
        return fib(n - 1) + fib(n - 2)
    }
}


// Performance Result:
//   Coding Time: 00:01:02
//   Time Complexity: O(n)
//   Space Complexity: O(1)
//   Runtime: 13 ms, faster than 9.17%
//   Memory Usage: 2.08 MB, less than 54.77%
