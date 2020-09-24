class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = [0] * 60
        res = 0
        for t in time:
            res += c[-t % 60]
            c[t % 60] += 1
        return res


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 244 ms, faster than 66.74%
#   Memory Usage: 17 MB, less than 60.04%
