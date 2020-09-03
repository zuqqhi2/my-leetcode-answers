import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_cnt = collections.Counter(ransomNote)
        m_cnt = collections.Counter(magazine)

        for c in r_cnt.keys():
            if c not in m_cnt:
                return False
            if m_cnt[c] < r_cnt[c]:
                return False

        return True


# Performance Result:
#   Coding Time: 00:06:19
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 48 ms, faster than 83.44%
#   Memory Usage: 14 MB, less than 56.99%
