class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        cur_dir = 0
        cur_pos = [0, 0]
        for i in range(100):
            for j in range(len(instructions)):
                if instructions[j] == 'G':
                    cur_pos[0] += dirs[cur_dir][0]
                    cur_pos[1] += dirs[cur_dir][1]
                elif instructions[j] == 'L':
                    cur_dir = (cur_dir + 1) % len(dirs)
                else:
                    cur_dir = (cur_dir - 1) % len(dirs)

            if cur_pos[0] == 0 and cur_pos[1] == 0:
                return True

        return False


# Performance Result:
#   Coding Time: 00:06:33
#   Time Complexity: O(NM)
#   Space Complexity: O(1)
#   Runtime: 56 ms, faster than 6.65%
#   Memory Usage: 14.2 MB, less than 53.49%
