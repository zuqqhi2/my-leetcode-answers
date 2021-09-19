class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = [[False for _ in range(len(board[0]))] for _ in
                   range(len(board))]
        num_fleet = 0
        for y in range(len(board)):
            for x in range(len(board[0])):
                if visited[y][x]:
                    continue

                visited[y][x] = True
                if board[y][x] == '.':
                    continue

                num_fleet += 1
                h_flag = False
                for x2 in range(x + 1, len(board[0])):
                    visited[y][x2] = True
                    if board[y][x2] == '.':
                        break
                    else:
                        h_flag = True

                v_flag = False
                for y2 in range(y + 1, len(board)):
                    visited[y2][x] = True
                    if board[y2][x] == '.':
                        break
                    else:
                        v_flag = True

                if h_flag and v_flag:
                    num_fleet += 1

        return num_fleet


# Performance Result:
#   Coding Time: 00:10:17
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 76 ms, faster than 55.31%
#   Memory Usage: 15 MB, less than 31.02%
