class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int],
                destination: List[int]) -> bool:
        opened = [(start)]
        visited = set()
        visited.add((start[0], start[1]))
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        max_y = len(maze) - 1
        max_x = len(maze[0]) - 1
        while len(opened) > 0:
            cur_y, cur_x = opened.pop(0)
            if cur_y == destination[0] and cur_x == destination[1]:
                return True

            for d in dirs:
                new_y = cur_y + d[0]
                new_x = cur_x + d[1]
                if not (0 <= new_y <= max_y and 0 <= new_x <= max_x) or \
                    maze[new_y][new_x] == 1:
                    continue

                while 0 <= new_y <= max_y and 0 <= new_x <= max_x and \
                    maze[new_y][new_x] == 0:
                    new_y += d[0]
                    new_x += d[1]
                new_y -= d[0]
                new_x -= d[1]
                if (new_y, new_x) in visited:
                    continue
                visited.add((new_y, new_x))

                opened.insert(0, (new_y, new_x))

        return False


# Performance Result:
#   Coding Time: 00:14:58
#   Time Complexity: O(NM)
#   Space Complexity: O(N)
#   Runtime: 292 ms, faster than 88.25%
#   Memory Usage: 14.3 MB, less than 53.54%
