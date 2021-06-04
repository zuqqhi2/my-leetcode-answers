class Solution:
    def isPathCrossing(self, path: str) -> bool:
        move = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}

        cur_pos = [0, 0]
        visited = set()
        visited.add((0, 0))
        for i in range(len(path)):
            cur_pos[0] += move[path[i]][0]
            cur_pos[1] += move[path[i]][1]
            if (cur_pos[0], cur_pos[1]) in visited:
                return True

            visited.add((cur_pos[0], cur_pos[1]))

        return False


# Performance Result:
#   Coding Time: 00:05:35
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 20.15%
#   Memory Usage: 14.5 MB, less than 31.88%
