from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        word_length = len(beginWord)

        # Create dist1 list
        dist1_list = defaultdict(list)
        for word in wordList:
            for i in range(word_length):
                dist1_list[word[:i] + "*" + word[i+1:]].append(word)

        # Create visited dict
        visited = defaultdict(bool)

        min_num_tf = 10000000
        queue = [(beginWord, 1)]
        while queue:
            cur_item = queue.pop(0)
            cur_word = cur_item[0]
            cur_num_tf = cur_item[1]

            visited[cur_word] = True

            for i in range(word_length):
                for word in dist1_list[cur_word[:i] + "*" + cur_word[i+1:]]:
                    if word == cur_word or word in visited.keys():
                        continue

                    if word == endWord and cur_num_tf + 1 < min_num_tf:
                        min_num_tf = cur_num_tf + 1
                    elif cur_num_tf + 1 < min_num_tf:
                        queue.append((word, cur_num_tf + 1))

        if min_num_tf == 10000000:
            return 0
        else:
            return min_num_tf


s = Solution()
print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(s.ladderLength("hot", "dog", ["hot", "dog"]))

# Sample test case:
#   Input:
#       beginWord = "hit",
#       endWord = "cog",
#       wordList = ["hot","dot","dog","lot","log","cog"]
#   Output:
#       5

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(MN)
#   Space Complexity: O(MN)
#   Runtime: 1624 ms, faster than 5.03% of Python3
#       online submissions for Word Ladder.
#   Memory Usage: 18.3 MB, less than 6.90% of Python3
#       online submissions for Word Ladder.
