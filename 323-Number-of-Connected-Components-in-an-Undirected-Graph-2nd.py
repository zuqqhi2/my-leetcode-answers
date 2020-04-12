from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        num_comp = 0
        visited = {}
        for node in graph.keys():
            if node in visited:
                continue

            num_comp += 1

            opened = [node]
            while len(opened) > 0:
                cur_node = opened.pop(0)
                visited[cur_node] = True

                for next_node in graph[cur_node]:
                    if next_node not in visited:
                        opened.append(next_node)

        if len(graph.keys()) < n:
            num_comp += n - len(graph.keys())

        return num_comp


# Performance Result:
#   Coding Time: 00:08:50
#   Time Complexity: O(|E| + |N|^2)
#   Space Complexity: O(|E| + |N|)
#   Runtime: 120 ms, faster than 20.23%
#   Memory Usage: 14.9 MB, less than 100.00%
