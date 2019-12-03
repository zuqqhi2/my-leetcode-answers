class Solution:
    def firstUniqChar(self, s):
        char_pos = {}
        for i, c in enumerate(s):
            if c not in char_pos:
                char_pos[c] = i
            else:
                char_pos[c] = -1

        for key in char_pos.keys():
            if char_pos[key] != -1:
                return char_pos[key]

        return -1


# Sample test case:
#   Input:
#       ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
#   Output:
#       2

# Performance Result:
#   Coding Time: 00:03:02
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 96 ms, faster than 84.34% of Python3
#       online submissions for First Unique Character in a String.
#   Memory Usage: 12.8 MB, less than 100.00% of Python3
#       online submissions for First Unique Character in a String.
