import collections


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 136 ms, faster than 48.66%
#   Memory Usage: 14.3 MB, less than 18.95%
