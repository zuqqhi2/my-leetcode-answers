class Solution:
    def freqAlphabets(self, s: str) -> str:
        codes = s.split('#')
        if codes[-1] != '':
            last_codes = list(codes[-1])
            del codes[-1]
            codes.extend(last_codes)

        res = ""
        for i in range(len(codes)):
            if len(codes[i]) == 0:
                continue
            elif len(codes[i]) > 2:
                for j in range(len(codes[i]) - 2):
                    res += chr(int(codes[i][j]) + 96)

            res += chr(int(codes[i][-2:]) + 96)

        return res


# Performance Result:
#   Coding Time: 00:17:37
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 61.83%
#   Memory Usage: 14.1 MB, less than 93.06%
