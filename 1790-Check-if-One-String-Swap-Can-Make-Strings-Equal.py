class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        diff_1_idx = -1
        diff_cnt = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue

            diff_cnt += 1
            if diff_cnt > 2:
                return False

            if diff_1_idx != -1 and not (
                s1[diff_1_idx] == s2[i] and s1[i] == s2[diff_1_idx]):
                return False
            else:
                diff_1_idx = i

        if diff_cnt == 1:
            return False

        return True


# Performance Result:
#   Coding Time: 00:10:49
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 24 ms, faster than 96.58%
#   Memory Usage: 14.3 MB, less than 22.31%
