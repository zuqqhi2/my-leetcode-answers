# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [root.val]

        ret = []
        if root.left is not None:
            ret.extend(self.postorderTraversal(root.left))
        if root.right is not None:
            ret.extend(self.postorderTraversal(root.right))

        ret.append(root.val)

        return ret


# Performance Result:
#   Coding Time: 00:04:38
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 28 ms, faster than 83.88%
#   Memory Usage: 14.1 MB, less than 73.42%
