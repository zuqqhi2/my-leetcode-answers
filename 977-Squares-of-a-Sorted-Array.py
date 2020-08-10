class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return list(sorted([num * num for num in A]))


# Performance Result:
#   Coding Time: 00:01:46
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 220 ms, faster than 95.68%
#   Memory Usage: 15.8 MB, less than 34.58%
