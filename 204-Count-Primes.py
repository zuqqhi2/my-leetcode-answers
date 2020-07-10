class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                s[i * i:n:i] = [0] * len(s[i * i:n:i])
        return sum(s)


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(n^{0.5})
#   Space Complexity: O(n)
#   Runtime: 244 ms, faster than 89.59%
#   Memory Usage: 37.1 MB, less than 19.78%
