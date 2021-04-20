class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        cur_depth = 0
        is_valid = True
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.insert(0, s[i])
                cur_depth += 1
                max_depth = max(max_depth, cur_depth)
            elif s[i] == ')':
                elem = stack.pop(0)
                if elem != '(':
                    is_valid = False
                cur_depth -= 1

        return 0 if not is_valid else max_depth


# Performance Result:
#   Coding Time: 00:04:33
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 51.85%
#   Memory Usage: 14.3 MB, less than 40.77%
