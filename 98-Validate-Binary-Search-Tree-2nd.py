# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode, min_limit=-2 ** 32,
                   max_limit=2 ** 32) -> bool:
        if root is None:
            return True

        if not self.isValidBST(root.left, min_limit, min(max_limit, root.val)):
            return False

        if not self.isValidBST(root.right, max(min_limit, root.val), max_limit):
            return False

        if min_limit < root.val < max_limit:
            return True
        else:
            return False


# Performance Result:
#   Coding Time: 00:24:14
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 48 ms, faster than 40.27%
#   Memory Usage: 16.5 MB, less than 5.75%
