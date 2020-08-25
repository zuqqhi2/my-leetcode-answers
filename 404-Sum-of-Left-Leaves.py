# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0

        res = 0
        opened = [(root, False)]
        while len(opened) > 0:
            cur_node, is_left = opened.pop(0)
            if is_left and cur_node.left is None and cur_node.right is None:
                res += cur_node.val
                continue

            if cur_node.left is not None:
                opened.append((cur_node.left, True))
            if cur_node.right is not None:
                opened.append((cur_node.right, False))

        return res


# Performance Result:
#   Coding Time: 00:03:47
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 81.05%
#   Memory Usage: 14.1 MB, less than 83.35%
