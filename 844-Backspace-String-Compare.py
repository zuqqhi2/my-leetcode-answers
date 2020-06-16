class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(S: str) -> str:
            num_backsp = 0
            idx = 0
            while idx < len(S):
                if S[idx] == '#':
                    num_backsp += 1
                elif num_backsp > 0:
                    left_idx = max(0, idx - num_backsp * 2)
                    S = S[:left_idx] + S[idx:]
                    idx = max(0, idx - num_backsp * 2)
                    num_backsp = 0

                idx += 1

            if num_backsp > 0:
                left_idx = max(0, idx - num_backsp * 2)
                S = S[:left_idx] + S[idx:]

            return S

        return helper(S) == helper(T)


# Performance Result:
#   Coding Time: 00:19:29
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 32 ms, faster than 53.29%
#   Memory Usage: 13.8 MB, less than 52.27%
