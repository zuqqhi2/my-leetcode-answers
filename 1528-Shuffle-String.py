class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""] * len(s)
        for i in range(len(indices)):
            res[indices[i]] = s[i]

        return ''.join(res)


# Performance Result:
#   Coding Time: 00:04:29
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 44 ms, faster than 98.79%
#   Memory Usage: 14.3 MB, less than 24.08%
