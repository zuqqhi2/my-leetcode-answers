# Data Structure: Hash
# Algorithm:
#   1. generate hash key for each text use following formula
#       \sigma^n_i=0 ascii_code(t[i])
#   2. if the key exists, append a text into existing array
#

import collections


class Solution:
    def groupAnagrams(self, strs):
        if len(strs) == 0:
            return [[]]

        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


# Sample test case:
#   Input:
#       ["eat", "tea", "tan", "ate", "nat", "bat"]
#   Output:
#       [
#           ["ate","eat","tea"],
#           ["nat","tan"],
#           ["bat"]
#       ]

# Performance Result:
#   Coding Time: 00:32:13
#   Time Complexity: O(nk log k)
#   Space Complexity: O(nk)
#   Runtime: 116 ms, faster than 65.61% of Python3
#       online submissions for Group Anagrams.
#   Memory Usage: 17.9 MB, less than 24.53% of Python3
#       online submissions for Group Anagrams.
