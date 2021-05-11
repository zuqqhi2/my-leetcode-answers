# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def traverse(root: TreeNode, res: List[int]) -> List[int]:
            if root.left is not None:
                traverse(root.left, res)
            res.append(root.val)
            if root.right is not None:
                traverse(root.right, res)

            return res

        if root is None:
            return []
        else:
            return traverse(root, [])


# Performance Result:
#   Coding Time: 00:05:01
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 52.77%
#   Memory Usage: 14.1 MB, less than 74.98%
