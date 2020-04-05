import math


class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0

        if self.kthGrammar(N - 1, int(math.ceil(K / 2))) == 0:
            if K % 2 == 1:
                return 0
            else:
                return 1
        else:
            if K % 2 == 1:
                return 1
            else:
                return 0


# Performance Result:
#   Coding Time: 00:18:42
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 15.27% of Python3
#       online submissions for K-th Symbol in Grammar.
#   Memory Usage: 13.9 MB, less than 25.00% of Python3
#       online submissions for K-th Symbol in Grammar.
