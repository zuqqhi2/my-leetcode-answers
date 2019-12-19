class Solution:
    def generate(self, n, results=[], cur_text="(", num_open=1, num_close=0):
        # Skip if it violates the format
        if n == 0 or num_open < num_close or num_open > n or num_close > n:
            return results

        # Add new text if it finishes to generate
        if num_open == num_close and num_open == n:
            results.append(cur_text)
            return results

        results = self.generate(n, results,
                                cur_text + "(", num_open + 1, num_close)
        results = self.generate(n, results,
                                cur_text + ")", num_open, num_close + 1)

        return results

    def generateParenthesis(self, n):
        return self.generate(n, results=[])


s = Solution()
print(s.generateParenthesis(3))
print(s.generateParenthesis(1))
#print(s.generateParenthesis(10))


# Sample test case:
#   Input:
#       3
#   Output:
#       ['((()))', '(()())', '(())()', '()(())', '()()()']

# Performance Result:
#   Coding Time: 00:19:09
#   Time Complexity: O(4^n / (n * sqrt(n)))
#   Space Complexity: O(4^n / (n * sqrt(n)))
#   Runtime: 36 ms, faster than 71.22% of Python3
#       online submissions for Generate Parentheses.
#   Memory Usage: 12.9 MB, less than 100.00% of Python3
#       online submissions for Generate Parentheses.
