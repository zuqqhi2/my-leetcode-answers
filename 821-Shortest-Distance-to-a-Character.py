class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        c_pos = set()
        for i in range(len(S)):
            if S[i] == C:
                c_pos.add(i)

        res = []
        for i in range(len(S)):
            for j in range(len(S)):
                if i + j in c_pos or i - j in c_pos:
                    res.append(j)
                    break

        return res


# Performance Result:
#   Coding Time: 00:05:30
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 52 ms, faster than 47.68%
#   Memory Usage: 14.3 MB, less than 100.00%
