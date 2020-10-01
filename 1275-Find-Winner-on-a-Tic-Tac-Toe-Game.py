class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(len(moves)):
            m = moves[i]
            board[m[0]][m[1]] = 'X' if i % 2 == 0 else 'O'

        is_pending = False
        # Horizontal
        for y in range(len(board)):
            s = ''.join(board[y])
            if s == 'XXX':
                return "A"
            elif s == 'OOO':
                return "B"
            if len(s) < 3:
                is_pending = True

        # Vertical
        for x in range(len(board[0])):
            s = board[0][x] + board[1][x] + board[2][x]
            if s == 'XXX':
                return "A"
            elif s == 'OOO':
                return "B"
            if len(s) < 3:
                is_pending = True

        # Diagonal
        s = board[0][0] + board[1][1] + board[2][2]
        if s == 'XXX':
            return "A"
        elif s == 'OOO':
            return "B"
        if len(s) < 3:
            is_pending = True

        s = board[2][0] + board[1][1] + board[0][2]
        if s == 'XXX':
            return "A"
        elif s == 'OOO':
            return "B"
        if len(s) < 3:
            is_pending = True

        return "Pending" if is_pending else "Draw"


# Performance Result:
#   Coding Time: 00:19:09
#   Time Complexity: O(N^2)
#   Space Complexity: O(N^2)
#   Runtime: 32 ms, faster than 73.79%
#   Memory Usage: 14.2 MB, less than 5.16%
