class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        elif len(A) == 0:
            return True

        for start_idx in range(len(B)):
            if A[0] != B[start_idx]:
                continue

            for i in range(len(A)):
                if A[i] != B[(start_idx + i) % len(B)]:
                    break

                if i == len(A) - 1:
                    return True

        return False


# Performance Result:
#   Coding Time: 00:06:29
#   Time Complexity: O(N^2)
#   Space Complexity: O(1)
#   Runtime: 36 ms, faster than 21.67%
#   Memory Usage: 14.3 MB, less than 5.09%
