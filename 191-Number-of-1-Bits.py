from functools import reduce


class Solution:
    def hammingWeight(self, n: int) -> int:
        return reduce(lambda a, b: int(a) + int(b), list(format(n, 'b')))


s = Solution()
print(s.hammingWeight(11))
print(format(2512, 'b'), s.hammingWeight(2512))

# Sample test case:
#   Input:
#       11
#   Output:
#       3

# Performance Result:
#   Coding Time: 00:04:54
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 28 ms, faster than 72.60% of Python3
#       online submissions for Number of 1 Bits.
#   Memory Usage: 12.7 MB, less than 100.00% of Python3
#       online submissions for Number of 1 Bits.
