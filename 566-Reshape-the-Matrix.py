class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[
        List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        res = [[0 for _ in range(c)] for _ in range(r)]
        cur_r = 0
        cur_c = 0
        for y in range(len(mat)):
            for x in range(len(mat[0])):
                res[cur_r][cur_c] = mat[y][x]
                cur_c += 1
                if cur_c >= c:
                    cur_r += 1
                    cur_c = 0

        return res


# Performance Result:
#   Coding Time: 00:05:15
#   Time Complexity: O(NM)
#   Space Complexity: O(NM)
#   Runtime: 80 ms, faster than 97.19%
#   Memory Usage: 15.1 MB, less than 74.55%
