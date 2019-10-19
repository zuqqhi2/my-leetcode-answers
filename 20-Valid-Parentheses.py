class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True

        stuck = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stuck.insert(0, c)
            else:
                if len(stuck) == 0:
                    return False
                bracket = stuck.pop(0)
                if (bracket == '(' and c != ')') \
                        or (bracket == '{' and c != '}') \
                        or (bracket == '[' and c != ']'):
                    return False

        if len(stuck) >= 1:
            return False
        else:
            return True


s = Solution()
print(s.isValid('{}'))

# Sample Testcase:
#   Input:
#       "()[]{}"
#   Output:
#       True

# Performance Result:
#   Coding Time: 00:07:20
#   Time Complexity: O(n)
#   Space Complexity: O(n)
#   Runtime: 40 ms, faster than 48.09% of Python3
#       online submissions for Valid Parentheses.
#   Memory Usage: 13.8 MB, less than 5.22% of Python3
#       online submissions for Valid Parentheses.
