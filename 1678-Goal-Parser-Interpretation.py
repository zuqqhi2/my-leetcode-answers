class Solution:
    def interpret(self, command: str) -> str:
        rules = {'G': 'G', '()': 'o', '(al)': 'al'}
        buf = []
        res = []
        for i in range(len(command)):
            buf.append(command[i])
            buf_word = ''.join(buf)
            if buf_word in rules:
                res.append(rules[buf_word])
                buf = []

        return ''.join(res)


# Performance Result:
#   Coding Time: 00:04:12
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 28 ms, faster than 83.31%
#   Memory Usage: 14 MB, less than 87.12%
