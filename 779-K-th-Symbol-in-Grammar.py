class Solution:
    def kthGrammar(self, N, K):
        if N == 1:
            return 0
        else:
            return (1 - K % 2) ^ self.kthGrammar(N - 1, int((K + 1) / 2))


s = Solution()
print(s.kthGrammar(1, 1))
print(s.kthGrammar(2, 1))
print(s.kthGrammar(2, 2))
print(s.kthGrammar(4, 5))
print(s.kthGrammar(30, 434991989))

# Sample test case:
#   Input:
#       N = 4, K = 5
#   Output:
#       1

# Performance Result:
#   Coding Time: Timeout
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 20 ms, faster than 100.00% of Python3
#       online submissions for K-th Symbol in Grammar.
#   Memory Usage: 12.5 MB, less than 100.00% of Python3
#       online submissions for K-th Symbol in Grammar.
