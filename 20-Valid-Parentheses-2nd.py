class Solution:
    def isValid(self, s: str) -> bool:
        # Corner cases
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False

        # Stack
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.insert(0, c)
            else:
                if len(stack) == 0:
                    return False
                open_blacket = stack.pop(0)
                if (c == ')' and open_blacket != '(') or (
                    c == ']' and open_blacket != '[') or (
                    c == '}' and open_blacket != '{'):
                    return False

        if len(stack) > 0:
            return False
        else:
            return True


# Performance Result:
#   Coding Time: 00:05:38
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 17.74% of Python3
#       online submissions for Valid Parentheses.
#   Memory Usage: 13 MB, less than 98.26% of Python3
#       online submissions for Valid Parentheses.
