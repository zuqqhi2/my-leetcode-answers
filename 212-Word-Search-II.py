class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(words) == 0:
            return []
        if len(board) == 0:
            return []

        # Generate Trie Tree
        root = TrieNode()
        for word in words:
            if word[0] not in root.children:
                root.children[word[0]] = TrieNode()
            cur_node = root.children[word[0]]
            for i in range(1, len(word)):
                if word[i] not in cur_node.children:
                    cur_node.children[word[i]] = TrieNode()
                cur_node = cur_node.children[word[i]]

            cur_node.is_end = True
            cur_node.word = word

        # Graph x Trie Tree search
        result = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        max_y = len(board)
        max_x = len(board[0])
        for y in range(max_y):
            for x in range(max_x):
                if board[y][x] not in root.children:
                    continue

                opened = [(y, x, root.children[board[y][x]], {})]
                while len(opened) > 0:
                    cur_y, cur_x, cur_node, cur_visited = opened.pop(0)
                    cur_visited[(cur_y, cur_x)] = True
                    if cur_node.is_end:
                        result.add(cur_node.word)

                    for d in directions:
                        new_y = cur_y + d[0]
                        new_x = cur_x + d[1]
                        if not (0 <= new_y < max_y and 0 <= new_x < max_x):
                            continue

                        if (new_y, new_x) in cur_visited:
                            continue

                        if board[new_y][new_x] in cur_node.children:
                            new_visited = dict.fromkeys(cur_visited, True)
                            opened.append((new_y, new_x, cur_node.children[
                                board[new_y][new_x]], new_visited))

        return list(result)


# Performance Result:
#   Coding Time: 00:38:47
#   Time Complexity: O(M 4 3^(L-1)), where M is the board size and L is the max length of words
#   Space Complexity: O(M 4 3^(L-1))
#   Runtime: 408 ms, faster than 41.73%
#   Memory Usage: 32 MB, less than 91.67%
