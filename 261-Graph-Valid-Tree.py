from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges) -> bool:
        """
        :param int n: num nodes
        :param List[List[int]] edges: undirected graph's edge
        :rtype: bool
        :return: is it a tree or not
        """
        # Corner case
        if n == 0:
            return False
        elif n == 1 and len(edges) == 0:
            return True

        neighbors = defaultdict(list)
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])

        # Not tree if there is abandoned node
        # n = 1 case is handled above
        if len([n for n in neighbors if len(neighbors[n]) == 0]):
            return False

        # Depth First Search
        stack = [0]
        parent = {0: -1}
        while len(stack) > 0:
            cur_node = stack.pop()
            for child in neighbors[cur_node]:
                # Skip parent
                if child == parent[cur_node]:
                    continue
                # there is a loop if not parent child is in visited list
                if child in parent:
                    return False

                parent[child] = cur_node
                stack.append(child)

        return len(parent.keys()) == n


s = Solution()
print(s.validTree(5, [[0,1], [0,2], [0,3], [1,4]]))
print(s.validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))

# Sample test case:
#   Input:
#       [
#           "wrt",
#           "wrf",
#           "er",
#           "ett",
#           "rftt"
#       ]
#   Output:
#       "wertf"

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 92 ms, faster than 86.78% of Python3 online submissions for Graph Valid Tree.
#   Memory Usage: 14 MB, less than 83.33% of Python3 online submissions for Graph Valid Tree.
