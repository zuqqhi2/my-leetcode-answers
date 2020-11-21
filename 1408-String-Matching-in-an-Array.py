class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substr = []
        for i, word_1 in enumerate(words):
            for j, word_2 in enumerate(words):
                # check word_1 is substring of word_2
                if i != j and word_1 in word_2:
                    substr.append(word_1)

                    # avoid repeated element appending
                    break

        return substr


# Performance Result:
#   Coding Time: 00:00:00
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 40 ms, faster than 44.10%
#   Memory Usage: 14.3 MB, less than 14.21%
