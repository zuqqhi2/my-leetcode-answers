class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        res = [0] * (len(S) + 1)
        max_num = 0
        min_num = 0
        for i in range(len(S)):
            if S[i] == 'I':
                res[i + 1] = max_num + 1
                max_num += 1
            else:
                res[i + 1] = min_num - 1
                min_num -= 1

        return [res[i] + abs(min_num) for i in range(len(res))]


# Performance Result:
#   Coding Time: 00:05:53
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 72 ms, faster than 36.10%
#   Memory Usage: 15.6 MB, less than 8.42%
