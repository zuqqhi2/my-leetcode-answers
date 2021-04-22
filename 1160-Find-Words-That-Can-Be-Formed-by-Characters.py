import collections


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_cnt = collections.Counter(chars)
        length = 0
        for word in words:
            word_cnt = collections.Counter(word)
            can_be_formed = True
            for c in word_cnt:
                if c not in chars_cnt:
                    can_be_formed = False
                    break

                if chars_cnt[c] < word_cnt[c]:
                    can_be_formed = False
                    break

            length += len(word) if can_be_formed else 0

        return length


# Performance Result:
#   Coding Time: 00:04:23
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 156 ms, faster than 68.55%
#   Memory Usage: 14.5 MB, less than 98.96%
