class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur_node = self.root
        for i in range(len(word)):
            if word[i] not in cur_node.children:
                cur_node.children[word[i]] = TrieNode()
            cur_node = cur_node.children[word[i]]

        cur_node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        opened = [(self.root, 0)]
        n = len(word)
        while len(opened) > 0:
            cur_node, cur_idx = opened.pop()
            if cur_idx == n and cur_node.is_end:
                return True

            if cur_idx == n:
                continue

            if word[cur_idx] == '.':
                for k, node in cur_node.children.items():
                    opened.append((node, cur_idx + 1))
            elif word[cur_idx] in cur_node.children:
                opened.append((cur_node.children[word[cur_idx]], cur_idx + 1))

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
wd = WordDictionary()
wd.addWord('a')
wd.addWord('ab')
print(wd.search('a'))


# Performance Result:
#   Coding Time: 00:26:47
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 392 ms, faster than 27.60%
#   Memory Usage: 28.5 MB, less than 8.70%
