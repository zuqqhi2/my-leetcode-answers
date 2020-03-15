class Solution:
    def pacificAtlantic(self, matrix):
        """
        :param List[List[int]] matrix: heights of each cell
        :rtype: List[List[int]]
        :return: List of grid coordinates where water can flow to the both
        """
        # Corner cases
        if len(matrix) == 0:
            return []
        if len(matrix) == 1 or len(matrix[0]) == 1:
            return [[y, x] for y in range(len(matrix)) for x in
                    range(len(matrix[0]))]

        # Depth First Search
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        results = []
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                is_reached_to_pacific = False
                is_reached_to_atlantic = False
                opened = [[y, x]]
                visited = {}
                while len(opened) > 0:
                    cur_pos = opened.pop(0)
                    visited[cur_pos[0] * 1000 + cur_pos[1]] = True

                    # Reach check
                    if cur_pos[0] == 0 or cur_pos[1] == 0:
                        is_reached_to_pacific = True
                    if cur_pos[0] == len(matrix) - 1 \
                        or cur_pos[1] == len(matrix[0]) - 1:
                        is_reached_to_atlantic = True
                    if is_reached_to_atlantic and is_reached_to_pacific:
                        results.append([y, x])
                        break

                    # Adding new cells to the open list
                    for direction in directions:
                        new_pos = [cur_pos[0] + direction[0], cur_pos[1] + direction[1]]
                        if new_pos[0] * 1000 + new_pos[1] not in visited:
                            if matrix[new_pos[0]][new_pos[1]] <= matrix[cur_pos[0]][cur_pos[1]]:
                                opened.insert(0, new_pos)

        return results



# Sample test case:
#   Input:
#       See LeetCode
#   Output:
#       See LeetCode

# Performance Result:
#   Coding Time: 00:26:11
#   Time Complexity: O(|V|^2)
#   Space Complexity: O(3|V|)
#   Runtime: 4416 ms, faster than 5.01% of Python3
#       online submissions for Pacific Atlantic Water Flow.
#   Memory Usage: 13.9 MB, less than 90.00% of Python3
#       online submissions for Pacific Atlantic Water Flow.
