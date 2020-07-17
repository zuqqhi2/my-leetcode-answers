# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None:
            if root.val == val:
                return root

            if val < root.val:
                root = root.left
            else:
                root = root.right
        return None


# Performance Result:
#   Coding Time: 00:01:50
#   Time Complexity: O(log N)
#   Space Complexity: O(1)
#   Runtime: 100 ms, faster than 24.56%
#   Memory Usage: 15.8 MB, less than 25.69%
