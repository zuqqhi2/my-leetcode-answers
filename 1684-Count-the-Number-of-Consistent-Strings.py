class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_char_set = {c for c in allowed}

        res = 0
        for word in words:
            ng_flg = False
            for c in word:
                if c not in allowed_char_set:
                    ng_flg = True
                    break

            if not ng_flg:
                res += 1

        return res


# Performance Result:
#   Coding Time: 00:03:41
#   Time Complexity: O(N)
#   Space Complexity: O(M)
#   Runtime: 262 ms, faster than 67.95%
#   Memory Usage: 16.1 MB, less than 81.45%
