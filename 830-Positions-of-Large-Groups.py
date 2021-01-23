class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        cur_char = ""
        start = 0
        end = 0
        res = []
        for i in range(len(s)):
            if s[i] != cur_char:
                end = i - 1
                if end - start >= 2:
                    res.append([start, end])

                start = i
                cur_char = s[i]

        end = len(s) - 1
        if end - start >= 2:
            res.append([start, end])

        return res


# Performance Result:
#   Coding Time: 00:03:43
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 40 ms, faster than 57.80%
#   Memory Usage: 14.2 MB, less than 64.99%
