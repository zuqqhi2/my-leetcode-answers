class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        word_length = len(word)
        num_rows = len(board)
        num_columns = len(board[0])
        for y in range(num_rows):
            for x in range(num_columns):
                if board[y][x] != word[0]:
                    continue

                # Depth First Search
                word_idx = 0
                visited = {}
                opened = [(y, x, word_idx, {})]
                while len(opened) > 0:
                    cur_elem = opened.pop(0)
                    cur_y, cur_x = cur_elem[0], cur_elem[1]
                    cur_word_idx = cur_elem[2]
                    cur_visited = cur_elem[3]
                    cur_visited[(cur_y, cur_x)] = True
                    if cur_word_idx == word_length - 1:
                        return True

                    for d in directions:
                        new_y = cur_y + d[0]
                        new_x = cur_x + d[1]
                        new_word_idx = cur_word_idx + 1
                        if (new_y, new_x) in cur_visited:
                            continue

                        new_visited = dict.fromkeys(cur_visited, True)
                        if 0 <= new_y < num_rows and 0 <= new_x < num_columns and \
                            word[new_word_idx] == board[new_y][new_x]:
                            opened.insert(0, (
                            new_y, new_x, new_word_idx, new_visited))

        return False


# Sample test case:
#   Input:
#       [
#           ['A','B','C','E'],
#           ['S','F','C','S'],
#           ['A','D','E','E']
#       ],
#       word = "ABCCED"
#   Output:
#       True

# Performance Result:
#   Coding Time: 00:20:02
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 452 ms, faster than 16.99% of Python3
#       online submissions for Word Search.
#   Memory Usage: 28.3 MB, less than 6.38% of Python3
#       online submissions for Word Search.
