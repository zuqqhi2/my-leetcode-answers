class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        opened = [(0, [0])]
        end_node = len(graph) - 1
        while len(opened) > 0:
            cur_node, cur_path = opened.pop(0)
            if cur_node == end_node:
                paths.append(cur_path)
                continue

            for n in graph[cur_node]:
                opened.append((n, cur_path + [n]))

        return paths


# Performance Result:
#   Coding Time: 00:07:19
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 131 ms, faster than 23.10%
#   Memory Usage: 15.9 MB, less than 11.80%
