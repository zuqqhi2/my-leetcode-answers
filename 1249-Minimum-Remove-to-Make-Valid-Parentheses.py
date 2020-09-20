class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ')' and len(stack) > 0 and stack[0][0] == '(':
                stack.pop(0)
            elif s[i] in ('(', ')'):
                stack.insert(0, (s[i], i))

        skip_idx = set()
        for item in stack:
            skip_idx.add(item[1])

        res = []
        for i in range(len(s)):
            if i in skip_idx:
                continue
            else:
                res.append(s[i])

        return ''.join(res)


# Performance Result:
#   Coding Time: 00:09:52
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 172 ms, faster than 37.24%
#   Memory Usage: 15.5 MB, less than 52.03%
