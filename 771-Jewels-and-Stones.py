class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = {c for c in J}

        res = 0
        for c in S:
            res += 1 if c in jewels else 0

        return res


# Performance Result:
#   Coding Time: 00:03:03
#   Time Complexity: O(N)
#   Space Complexity: O(M)
#   Runtime: 24 ms, faster than 93.92%
#   Memory Usage: 14 MB, less than 5.59%
