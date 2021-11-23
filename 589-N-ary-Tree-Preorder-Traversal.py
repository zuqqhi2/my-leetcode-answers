"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        opened = [root]
        res = []
        while len(opened) > 0:
            cur_node = opened.pop(0)
            res.append(cur_node.val)
            if cur_node.children is not None:
                for i in reversed(range(len(cur_node.children))):
                    opened.insert(0, cur_node.children[i])

        return res


# Performance Result:
#   Coding Time: 00:05:07
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 66 ms, faster than 19.19%
#   Memory Usage: 15.9 MB, less than 98.98%
