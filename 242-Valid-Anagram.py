from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = defaultdict(int)
        for i in range(len(s)):
            s_map[s[i]] += 1

        t_map = defaultdict(int)
        for i in range(len(t)):
            t_map[t[i]] += 1

        for key in s_map.keys():
            if s_map[key] != t_map[key]:
                return False

        return True


# Sample test case:
#   Input:
#       s = "anagram", t = "nagaram"
#   Output:
#       True

# Performance Result:
#   Coding Time: 00:03:11
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 84 ms, faster than 5.04% of Python3
#       online submissions for Valid Anagram.
#   Memory Usage: 14.1 MB, less than 9.38% of Python3
#       online submissions for Valid Anagram.
