class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [[A[y][x] for y in range(len(A))] for x in range(len(A[0]))]


# Performance Result:
#   Coding Time: 00:02:00
#   Time Complexity: O(NM)
#   Space Complexity: O(NM)
#   Runtime: 72 ms, faster than 80.97%
#   Memory Usage: 14.7 MB, less than 9.45%
