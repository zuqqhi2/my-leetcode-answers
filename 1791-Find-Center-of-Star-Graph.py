import functools

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return functools.reduce(lambda a, b: b.intersection(a), [set(l) for l in edges]).pop()


# Performance Result:
#   Coding Time: 00:09:24
#   Time Complexity: O(E)
#   Space Complexity: O(E)
#   Runtime: 900 ms, faster than 52.82%
#   Memory Usage: 56.8 MB, less than 5.06%
