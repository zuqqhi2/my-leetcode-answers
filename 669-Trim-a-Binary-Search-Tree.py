# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root.left is None and root.right is None:
            if root.val < low or root.val > high:
                return None
            else:
                return root

        if root.left is not None:
            root.left = self.trimBST(root.left, low, high)
        if root.right is not None:
            root.right = self.trimBST(root.right, low, high)

        if low <= root.val <= high:
            return root
        elif root.val < low:
            return root.right
        else:
            return root.left


# Performance Result:
#   Coding Time: 00:14:15
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 52 ms, faster than 66.81%
#   Memory Usage: 16.1 MB, less than 90.85%
