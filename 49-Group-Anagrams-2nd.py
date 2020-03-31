from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_maps = {}
        idx_maps = {}
        num_elem = 0
        result = []
        for s in strs:
            char_map = defaultdict(int)
            for c in s:
                char_map[c] += 1

            key = ','.join(
                sorted(["%s:%d" % (c, cnt) for c, cnt in char_map.items()]))
            if key not in char_maps:
                char_maps[key] = char_map
                idx_maps[key] = num_elem
                num_elem += 1
                result.append([s])
            else:
                result[idx_maps[key]].append(s)

        return result


# Performance Result:
#   Coding Time: 00:15:55
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 148 ms, faster than 10.61% of Python3
#       online submissions for Group Anagrams.
#   Memory Usage: 20.4 MB, less than 11.32% of Python3
#       online submissions for Group Anagrams.
