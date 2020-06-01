import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        nexts = collections.defaultdict(list)
        wordList.append(beginWord)
        word_len = len(wordList[0])
        for w in wordList:
            for i in range(word_len):
                nexts[w[:i] + '*' + w[i + 1:]].append(w)

        opened = [(beginWord, 1)]
        visited = {}
        min_path_len = 2 ** 32
        while len(opened) > 0:
            cur_node, cur_path_len = opened.pop(0)
            visited[cur_node] = True
            if cur_path_len >= min_path_len:
                continue
            if cur_node == endWord:
                min_path_len = min(min_path_len, cur_path_len)

            for i in range(word_len):
                cur_nexts = nexts[cur_node[:i] + '*' + cur_node[i + 1:]]
                for w in cur_nexts:
                    if w not in visited:
                        opened.append((w, cur_path_len + 1))

        return min_path_len if min_path_len < 2 ** 32 else 0


# Performance Result:
#   Coding Time: 00:16:20
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 1528 ms, faster than 7.76%
#   Memory Usage: 19.3 MB, less than 6.90%
