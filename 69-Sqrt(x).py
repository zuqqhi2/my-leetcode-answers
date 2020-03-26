class Solution:
    def mySqrt(self, x: int) -> int:
        # Corner case
        if x == 0:
            return 0
        if x == 1:
            return 1

        left = 1
        right = x // 2 + 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x and (mid + 1) * (mid + 1) > x:
                return mid

            if mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return left


# Sample test case:
#   Input:
#       8
#   Output:
#       2

# Performance Result:
#   Coding Time: 00:12:56
#   Time Complexity: O(log N)
#   Space Complexity: O(1)
#   Runtime: 36 ms, faster than 54.05% of Python3
#       online submissions for Sqrt(x).
#   Memory Usage: 12.9 MB, less than 100.00% of Python3
#       online submissions for Sqrt(x).
