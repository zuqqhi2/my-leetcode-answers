from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        res_str = str(int(''.join([str(A[i]) for i in range(len(A))]), 10) + K)
        return [int(res_str[i], 10) for i in range(len(res_str))]


# Performance Result:
#   Coding Time: 00:05:40
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 300 ms, faster than 65.62%
#   Memory Usage: 15.1 MB, less than 91.87%
