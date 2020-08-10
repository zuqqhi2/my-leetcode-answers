import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # If there is an independent orange(1) => -1
        # If there is no rotten orange => -1
        # Find longest dist fresh oragen from a rotten orange and measure the dist
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        max_y = len(grid)
        max_x = len(grid[0])
        dists = collections.defaultdict(lambda: 2 ** 32)
        for y in range(max_y):
            for x in range(max_x):
                if grid[y][x] == 0:
                    continue

                if grid[y][x] == 1:
                    dists[(y, x)] = dists[(y, x)]
                    continue

                # check longest dist
                opened = [(y, x, 0)]
                visited = set()
                while len(opened) > 0:
                    cur_y, cur_x, cur_dist = opened.pop(0)
                    visited.add((cur_y, cur_x))
                    dists[(cur_y, cur_x)] = min(dists[(cur_y, cur_x)], cur_dist)

                    for d in dirs:
                        new_y = cur_y + d[0]
                        new_x = cur_x + d[1]
                        if 0 <= new_y < max_y and 0 <= new_x < max_x and \
                            grid[new_y][new_x] == 1:
                            if (new_y, new_x) in visited:
                                continue

                            opened.append((new_y, new_x, cur_dist + 1))

        # no rotten orange
        if len(dists.keys()) == 0:
            return 0

        res = max([dist for dist in dists.values()])
        if res == 2 ** 32:
            return -1
        else:
            return res


# Performance Result:
#   Coding Time: 00:41:27
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 64 ms, faster than 46.89%
#   Memory Usage: 13.8 MB, less than 57.40%
