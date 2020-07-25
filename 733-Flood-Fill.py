class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        visited = set()
        opened = [(sr, sc)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        oldColor = image[sr][sc]
        while len(opened) > 0:
            cur_row, cur_col = opened.pop(0)
            image[cur_row][cur_col] = newColor
            visited.add((cur_row, cur_col))
            for d in directions:
                new_row = cur_row + d[0]
                new_col = cur_col + d[1]
                if (new_row, new_col) in visited:
                    continue

                if 0 <= new_row < len(image) and 0 <= new_col < len(image[0]):
                    if image[new_row][new_col] == oldColor:
                        opened.append((new_row, new_col))

        return image


# Performance Result:
#   Coding Time: 00:10:02
#   Time Complexity: O(N)
#   Space Complexity: O(M)
#   Runtime: 84 ms, faster than 53.84%
#   Memory Usage: 13.8 MB, less than 86.89%
