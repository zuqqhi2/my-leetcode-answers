class Solution:
    def boldWords(self, words, S):
        N = len(S)
        mask = [False] * N
        for i in range(N):
            prefix = S[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in range(i, min(i+len(word), N)):
                        mask[j] = True

        ans = []
        for incl, grp in itertools.groupby(zip(S, mask), lambda z: z[1]):
            if incl: ans.append("<b>")
            ans.append("".join(z[0] for z in grp))
            if incl: ans.append("</b>")
        return "".join(ans)


# Performance Result:
#   Coding Time: - (I gave up at 41:11 min)
#   Time Complexity: O(NML)
#   Space Complexity: O(N)
#   Runtime: 108 ms, faster than 34.48%
#   Memory Usage: 14.5 MB, less than 34.48%
