# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        idx_inorder = -1
        while root.val not in inorder:
            preorder = preorder[1:]
            root = TreeNode(preorder[0])
        idx_inorder = inorder.index(root.val)

        if len(preorder) <= 1:
            return root

        if idx_inorder >= 1:
            root.left = self.buildTree(preorder[1:], inorder[:idx_inorder])
        if idx_inorder + 1 < len(inorder):
            root.right = self.buildTree(preorder[1:], inorder[idx_inorder + 1:])
        return root


# Performance Result:
#   Coding Time: 00:23:07
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 304 ms, faster than 17.09%
#   Memory Usage: 87.7 MB, less than 13.16%
