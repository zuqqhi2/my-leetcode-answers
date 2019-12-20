class Solution:
    def countComponents(self, n, edges):
        num_components = 0

        # Initialize maps
        edge_map = {}
        reached_map = {}
        for edge in edges:
            if edge[0] in edge_map:
                edge_map[edge[0]].append(edge[1])
            else:
                edge_map[edge[0]] = [edge[1]]

            if edge[1] in edge_map:
                edge_map[edge[1]].append(edge[0])
            else:
                edge_map[edge[1]] = [edge[0]]

            reached_map[edge[0]] = False
            reached_map[edge[1]] = False

        # Count no edge node
        num_components += n - len(reached_map.keys())

        # Traversal
        for node in edge_map.keys():
            # Skip nodes already checked
            if reached_map[node]:
                continue

            # Traversal with BFS
            num_components += 1
            reached_map[node] = True
            queue = [n for n in edge_map[node]]
            while len(queue) > 0:
                cur_node = queue.pop(0)
                reached_map[cur_node] = True
                if cur_node in edge_map:
                    queue.extend([n for n in edge_map[cur_node] if not reached_map[n]])

        return num_components


s = Solution()
print(s.countComponents(5, [[0, 1], [1, 2], [3, 4]]))
print(s.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
print(s.countComponents(5, [[0, 1], [0, 2], [2, 3], [2, 4]]))
print(s.countComponents(4, [[2, 3], [1, 2], [1, 3]]))
print(s.countComponents(10, [[5, 6], [0, 2], [1, 7], [5, 9], [1, 8], [3, 4], [0, 6], [0, 7], [0, 3], [8, 9]]))


# Sample test case:
#   Input:
#       n = 5, edges = [[0, 1], [1, 2], [3, 4]]
#   Output:
#       2

# Performance Result:
#   Coding Time: 00:30:01
#   Time Complexity: O(n)
#   Space Complexity: O(n)
#   Runtime: 116 ms, faster than 63.39% of Python3
#       online submissions for Number of Connected Components in an Undirected Graph.
#   Memory Usage: 14 MB, less than 100.00% of Python3
#       online submissions for Number of Connected Components in an Undirected Graph.
