# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Corner Case
        if node is None:
            return None
        if node is not None:
            if len(node.neighbors) == 0:
                return Node(node.val)

        # Breadth First Search
        opened = [node]
        new_nodes = {node.val: Node(node.val)}
        while len(opened) > 0:
            cur_target = opened.pop(0)

            # Create or load new node corresponds to current target
            # for abandoned node
            new_cur_node = None
            if cur_target.val not in new_nodes:
                new_nodes[cur_target.val] = Node(cur_target.val)
            new_cur_node = new_nodes[cur_target.val]

            # Create neighbors
            for i in range(len(cur_target.neighbors)):
                cur_nb_node = cur_target.neighbors[i]

                # If a neighbor is new, creating new node
                if cur_nb_node.val not in new_nodes:
                    new_nodes[cur_nb_node.val] = Node(cur_nb_node.val)
                    # Add neighbors to open list
                    opened.append(cur_nb_node)
                new_cur_node.neighbors.append(new_nodes[cur_nb_node.val])

        return new_nodes[node.val]


# Sample test case:
#   Input:
#       [3,2,1,0,4]
#   Output:
#       False

# Performance Result:
#   Coding Time: 00:20:06
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 40 ms, faster than 29.48% of Python3
#       online submissions for Clone Graph.
#   Memory Usage: 13 MB, less than 100.00% of Python3
#       online submissions for Clone Graph.
