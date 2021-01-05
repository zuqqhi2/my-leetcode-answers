import collections


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        nexts = collections.defaultdict(list)
        for p in paths:
            nexts[p[0]].append(p[1])
            if p[1] not in nexts:
                nexts[p[1]] = []

        for city in nexts:
            if len(nexts[city]) == 0:
                return city

        return ""


# Performance Result:
#   Coding Time: 00:05:12
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 52 ms, faster than 74.43%
#   Memory Usage: 14.1 MB, less than 84.85%
