class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True

        char_score_map = {}
        for i, c in enumerate(order):
            char_score_map[c] = i + 1

        # Scoring for each word
        max_len = max([len(w) for w in words])
        scores = []
        for i in range(len(words)):
            score = 0
            for k in range(len(words[i])):
                score = score * 100 + char_score_map[words[i][k]]
            for k in range(max_len - len(words[i])):
                score *= 100
            scores.append(score)

        # Check order
        for i in range(1, len(words)):
            if scores[i] < scores[i - 1]:
                return False
        return True


# Performance Result:
#   Coding Time: 00:17:39
#   Time Complexity: O(NM)
#   Space Complexity: O(N)
#   Runtime: 40 ms, faster than 34.71%
#   Memory Usage: 13.9 MB, less than 5.55%
