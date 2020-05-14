class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for i in range(len(logs)):
            elems = logs[i].split(' ')
            if elems[1].isdecimal():
                digit_logs.append(logs[i])
            else:
                letter_logs.append(' '.join(elems[1:]) + ' ' + elems[0])

        letter_logs = sorted(letter_logs)

        result = []
        for i in range(len(letter_logs)):
            elems = letter_logs[i].split(' ')
            result.append(elems[-1] + ' ' + ' '.join(elems[:-1]))
        result.extend(digit_logs)

        return result


# Performance Result:
#   Coding Time: 00:14:14
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 66.50%
#   Memory Usage: 13.9 MB, less than 7.69%
