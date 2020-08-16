class Solution:
    def findPermutation(self, s: str) -> List[int]:
        res = [1] * (len(s) + 1)
        stack = []
        cur_idx = 0
        for i in range(1, len(s) + 1):
            if s[i - 1] == 'I':
                stack.insert(0, i)
                while len(stack) > 0:
                    res[cur_idx] = stack.pop(0)
                    cur_idx += 1
            else:
                stack.insert(0, i)

        stack.insert(0, len(s) + 1)
        while len(stack) > 0:
            res[cur_idx] = stack.pop(0)
            cur_idx += 1

        return res


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 144 ms, faster than 22.55%
#   Memory Usage: 15 MB, less than 51.96%
