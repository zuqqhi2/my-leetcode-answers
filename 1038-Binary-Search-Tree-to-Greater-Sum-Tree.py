# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        desc_nodes = []
        opened = [root]
        while len(opened) > 0:
            cur_node = opened.pop(0)
            desc_nodes.append(cur_node)
            if cur_node.left is not None:
                opened.append(cur_node.left)
            if cur_node.right is not None:
                opened.append(cur_node.right)

        desc_nodes[:] = list(reversed(sorted(desc_nodes, key=lambda x: x.val)))
        acc = 0
        for i in range(len(desc_nodes)):
            acc += desc_nodes[i].val
            desc_nodes[i].val = acc

        return root


# Performance Result:
#   Coding Time: 00:06:50
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 62.46%
#   Memory Usage: 14.2 MB, less than 87.39%
