class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        grid = [['' for _ in range(len(s))] for _ in range(numRows)]
        move_dir = [(1, 0), (-1, 1)]

        cur_pos = [0, 0]
        cur_md_idx = 0
        for i in range(len(s)):
            grid[cur_pos[0]][cur_pos[1]] = s[i]
            if not (0 <= cur_pos[0] + move_dir[cur_md_idx][0] < numRows):
                cur_md_idx = (cur_md_idx + 1) % 2
            cur_pos[0] += move_dir[cur_md_idx][0]
            cur_pos[1] += move_dir[cur_md_idx][1]

        result = ''
        for i in range(numRows):
            result += ''.join(grid[i])

        return result


# Performance Result:
#   Coding Time: 00:15:03
#   Time Complexity: O(N)
#   Space Complexity: O(NM)
#   Runtime: 824 ms, faster than 6.25%
#   Memory Usage: 20.8 MB, less than 5.71%
