class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)
        for i in range(n):
            res += mat[i][i]
            if i != n - 1 - i:
                res += mat[n - 1 - i][i]

        return res

# Performance Result:
#   Coding Time: 00:02:41
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 104 ms, faster than 79.61%
#   Memory Usage: 14.4 MB, less than 64.12%
