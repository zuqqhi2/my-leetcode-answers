class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        max_sum = 0
        for right_L in range(L - 1, len(A)):
            left_L = right_L - L + 1
            sum_L = sum(A[left_L:right_L + 1])
            for right_M in range(M - 1, len(A)):
                left_M = right_M - M + 1
                if max(left_L, left_M) <= min(right_L, right_M):
                    continue

                sum_M = sum(A[left_M:right_M + 1])
                max_sum = max(max_sum, sum_L + sum_M)

        return max_sum


# Performance Result:
#   Coding Time: 00:15:55
#   Time Complexity: O(N^2)
#   Space Complexity: O(1)
#   Runtime: 2448 ms, faster than 5.24%
#   Memory Usage: 14.1 MB, less than 11.76%
