import collections


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        word_map = collections.defaultdict(list)
        for i, w in enumerate(words):
            word_map[w].append(i)

        min_dist = 2 ** 32
        for i in word_map[word1]:
            for j in word_map[word2]:
                min_dist = min(min_dist, abs(i - j))

        return min_dist


# Performance Result:
#   Coding Time: 00:12:32
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 76 ms, faster than 25.92%
#   Memory Usage: 17.5 MB, less than 12.50%
