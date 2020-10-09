class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False

        pattern_map = {}
        word_map = {}
        for i in range(len(pattern)):
            if words[i] not in pattern_map and pattern[i] not in word_map:
                pattern_map[words[i]] = pattern[i]
                word_map[pattern[i]] = words[i]
            elif (words[i] in pattern_map and pattern[i] not in word_map) or (
                words[i] not in pattern_map and pattern[i] in word_map):
                return False
            else:
                if not (pattern_map[words[i]] == pattern[i] and word_map[
                    pattern[i]] == words[i]):
                    return False

        return True


# Performance Result:
#   Coding Time: 00:13:53
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 24 ms, faster than 91.38%
#   Memory Usage: 14.1 MB, less than 100.00%
