import collections


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        pos1_y = defaultdict(list)
        pos1_x = defaultdict(list)

        for y in range(len(mat)):
            for x in range(len(mat[0])):
                if mat[y][x] == 1:
                    pos1_y[y].append(x)
                    pos1_x[x].append(y)

        res = 0
        for y in pos1_y.keys():
            if len(pos1_y[y]) == 1 and len(pos1_x[pos1_y[y][0]]) == 1:
                res += 1

        return res


# Performance Result:
#   Coding Time: 00:06:29
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 156 ms, faster than 94.16%
#   Memory Usage: 14.8 MB, less than 23.08%
