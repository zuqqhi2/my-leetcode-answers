class Solution:
    def add(self, a: int, b: int) -> int:
        while b:
            c = a & b
            a = a ^ b
            b = c << 1
        return a

    def subtract(self, a: int, b: int) -> int:
        while b:
            bor = ~a & b
            a = a ^ b
            b = bor << 1
        return a

    def getSum(self, a: int, b: int) -> int:
        a, b = min(a, b), max(a, b)
        if a < 0 and b < 0:
            return self.add(a, b)
        if a < 0:
            if -a > b:
                return -1 * self.subtract(-a, b)
            else:
                return self.subtract(b, -a)

        return self.add(a, b)


s = Solution()
print(s.getSum(-2, 3))


# Sample test case:
#   Input:
#       a = 1, b = 2
#   Output:
#       3

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 20 ms, faster than 96.22% of Python3
#       online submissions for Sum of Two Integers.
#   Memory Usage: 12.7 MB, less than 100.00% of Python3
#       online submissions for Sum of Two Integers.
