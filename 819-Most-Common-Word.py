from collections import defaultdict
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-z ]', ' ', paragraph)
        banned_dict = {w: True for w in banned}

        words = paragraph.split(' ')
        max_freq = 0
        max_word = ''
        word_freq = defaultdict(int)
        for w in words:
            if len(w) == 0 or w in banned_dict:
                continue

            word_freq[w] += 1
            if word_freq[w] > max_freq:
                max_freq = word_freq[w]
                max_word = w

        return max_word


# Performance Result:
#   Coding Time: 00:08:03
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 51.31%
#   Memory Usage: 13.8 MB, less than 5.88%
