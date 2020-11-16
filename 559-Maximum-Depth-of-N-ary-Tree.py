"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        max_depth = 1
        opened = [(root, 1)]
        while len(opened) > 0:
            cur_node, cur_depth = opened.pop(0)
            max_depth = max(max_depth, cur_depth)

            for node in cur_node.children:
                opened.append((node, cur_depth + 1))

        return max_depth


# Performance Result:
#   Coding Time: 00:02:54
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 40 ms, faster than 90.49%
#   Memory Usage: 15.9 MB, less than 11.17%
