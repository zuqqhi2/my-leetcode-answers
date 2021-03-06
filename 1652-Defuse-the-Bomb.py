class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(code)):
            idx = 0
            new_val = 0
            for j in range(1, abs(k) + 1):
                idx = (i + j) % len(code) if k > 0 else (i - j) % len(code)
                new_val += code[idx]
            res.append(new_val)

        return res


# Performance Result:
#   Coding Time: 00:24:47
#   Time Complexity: O(NM)
#   Space Complexity: O(N)
#   Runtime: 60 ms, faster than 22.93%
#   Memory Usage: 14.1 MB, less than 85.76%
