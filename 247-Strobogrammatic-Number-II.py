class Solution:
    def findStrobogrammatic(self, n):
        nums = n % 2 * list('018') or ['']
        while n > 1:
            n -= 2
            nums = [a + num + b for a, b in '00 11 88 69 96'.split()[n < 2:] for num in nums]
        return nums


s = Solution()
print(s.findStrobogrammatic(1))
print(s.findStrobogrammatic(2))
print(s.findStrobogrammatic(3))
print(s.findStrobogrammatic(4))
print(s.findStrobogrammatic(5))


# Sample test case:
#   Input:
#       n = 2
#   Output:
#       ["11","69","88","96"]

# Performance Result:
#   Coding Time: 00:16:39
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 92 ms, faster than 99.64% of Python3
#       online submissions for Strobogrammatic Number II.
#   Memory Usage: 19.7 MB, less than 100.00% of Python3
#       online submissions for Strobogrammatic Number II.
