# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_parent = None
        x_depth = -1
        y_parent = None
        y_depth = -1
        opened = [(root, 0, None)]
        while len(opened) > 0:
            cur_node, cur_depth, cur_parent = opened.pop(0)
            if cur_node.val == x:
                x_depth = cur_depth
                x_parent = cur_parent
            if cur_node.val == y:
                y_depth = cur_depth
                y_parent = cur_parent
            if x_depth != -1 and y_depth != -1:
                break

            if cur_node.left is not None:
                opened.append((cur_node.left, cur_depth + 1, cur_node))
            if cur_node.right is not None:
                opened.append((cur_node.right, cur_depth + 1, cur_node))

        return True if x_parent != y_parent and x_depth == y_depth else False


# Performance Result:
#   Coding Time: 00:04:57
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 73.74%
#   Memory Usage: 14.1 MB, less than 7.78%
