# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if root is None:
            return None, None

        if root.val <= V:
            sub_roots = self.splitBST(root.right, V)
            root.right = sub_roots[0]
            return root, sub_roots[1]
        else:
            sub_roots = self.splitBST(root.left, V)
            root.left = sub_roots[1]
            return sub_roots[0], root


# Performance Result:
#   Coding Time: 00:13:50
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 36 ms, faster than 26.18%
#   Memory Usage: 13.8 MB, less than 100.00%
