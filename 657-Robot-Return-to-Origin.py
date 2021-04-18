class Solution:
    def judgeCircle(self, moves: str) -> bool:
        actions = {'U': (0, -1), 'R': (1, 0), 'D': (0, 1), 'L': (-1, 0)}
        cur_pos = [0, 0]
        for i in range(len(moves)):
            cur_pos[0] += actions[moves[i]][0]
            cur_pos[1] += actions[moves[i]][1]

        if cur_pos[0] == 0 and cur_pos[1] == 0:
            return True
        else:
            return False


# Performance Result:
#   Coding Time: 00:03:38
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 100 ms, faster than 6.31%
#   Memory Usage: 14.5 MB, less than 21.40%
