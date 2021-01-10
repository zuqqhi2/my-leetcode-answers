# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inorder_list = []

        def traverse(root: TreeNode) -> None:
            if root.left is not None:
                traverse(root.left)

            inorder_list.append(root)

            if root.right is not None:
                traverse(root.right)

        traverse(root)

        for i in range(len(inorder_list)):
            inorder_list[i].left = None
            if i < len(inorder_list) - 1:
                inorder_list[i].right = inorder_list[i + 1]
            else:
                inorder_list[i].right = None

        return inorder_list[0]


# Performance Result:
#   Coding Time: 00:17:09
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 59.75%
#   Memory Usage: 14.5 MB, less than 6.78%
