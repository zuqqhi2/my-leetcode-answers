import collections


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int],
                     informTime: List[int]) -> int:
        nexts = collections.defaultdict(list)
        for i in range(n):
            nexts[manager[i]].append(i)

        max_time = 0
        opened = [(nexts[-1][0], 0)]
        while len(opened) > 0:
            cur_node, cur_time = opened.pop(0)
            max_time = max(max_time, cur_time)
            for next_node in nexts[cur_node]:
                opened.append((next_node, cur_time + informTime[cur_node]))

        return max_time


# Performance Result:
#   Coding Time: 00:29:29
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 1836 ms, faster than 21.43%
#   Memory Usage: 43.4 MB, less than 58.86%
