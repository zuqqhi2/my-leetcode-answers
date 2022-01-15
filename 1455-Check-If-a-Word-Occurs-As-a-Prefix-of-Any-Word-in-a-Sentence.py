class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        prefix_len = len(searchWord)
        prefixes = {}
        words = sentence.split(' ')
        for i in range(len(words)):
            prefix = ''.join(
                [words[i][j] for j in range(min(len(words[i]), prefix_len))])
            if prefix not in prefixes:
                prefixes[prefix] = i + 1

        return prefixes[searchWord] if searchWord in prefixes else -1


# Performance Result:
#   Coding Time: 00:06:44
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 28 ms, faster than 84.03%
#   Memory Usage: 14.1 MB, less than 91.83%
