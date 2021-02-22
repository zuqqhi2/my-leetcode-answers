class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in range(len(encoded)):
            res.append(encoded[i] ^ res[i])

        return res


# Performance Result:
#   Coding Time: 00:05:06
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 220 ms, faster than 92.55%
#   Memory Usage: 15.9 MB, less than 64.84%
