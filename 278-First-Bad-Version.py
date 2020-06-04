# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


# Performance Result:
#   Coding Time: 00:09:15
#   Time Complexity: O(log N)
#   Space Complexity: O(1)
#   Runtime: 24 ms, faster than 91.09%
#   Memory Usage: 13.8 MB, less than 6.90%
