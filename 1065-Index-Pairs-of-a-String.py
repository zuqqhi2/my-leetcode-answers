class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        len_text = len(text)
        res = []
        for start in range(len_text):
            for word in words:
                end = start + len(word)
                if end > len_text:
                    continue
                if text[start:end] == word:
                    res.append([start, end - 1])

        return sorted(res)


# Performance Result:
#   Coding Time: 00:10:23
#   Time Complexity: O(NM)
#   Space Complexity: O(N)
#   Runtime: 40 ms, faster than 76.40%
#   Memory Usage: 14.5 MB, less than 23.29%
