"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traverse(root: 'Node') -> List[int]:
            res = []
            for node in root.children:
                res.extend(traverse(node))
            res.append(root.val)
            return res

        if root is None:
            return []
        else:
            return traverse(root)


# Performance Result:
#   Coding Time: 00:09:22
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 124 ms, faster than 5.01%
#   Memory Usage: 16.2 MB, less than 23.63%
