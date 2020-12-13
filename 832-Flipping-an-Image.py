class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        length = len(A)
        for y in range(length):
            A[y][:] = reversed(A[y])
            A[y][:] = [A[y][xi] ^ 1 for xi in range(length)]

        return A


# Performance Result:
#   Coding Time: 00:04:13
#   Time Complexity: O(NM)
#   Space Complexity: O(1)
#   Runtime: 48 ms, faster than 75.59%
#   Memory Usage: 14.2 MB, less than 13.09%
