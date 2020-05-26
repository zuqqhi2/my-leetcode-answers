class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 1:
            return True

        type_id = 0  # 0: TBD, 1: Increasing, 2: Decreasing
        for i in range(1, len(A)):
            diff = A[i] - A[i - 1]
            if diff > 0:
                if type_id == 2:
                    return False
                type_id = 1 if type_id == 0 else type_id
            elif diff < 0:
                if type_id == 1:
                    return False
                type_id = 2 if type_id == 0 else type_id
        return True


# Performance Result:
#   Coding Time: 00:12:29
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 540 ms, faster than 35.14%
#   Memory Usage: 19.8 MB, less than 5.26%
