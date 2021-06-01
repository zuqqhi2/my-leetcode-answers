# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        res = []
        stack = [root]
        while len(stack) > 0:
            cur_node = stack.pop(0)
            res.append(cur_node.val)
            if cur_node.right is not None:
                stack.insert(0, cur_node.right)
            if cur_node.left is not None:
                stack.insert(0, cur_node.left)

        return res


# Performance Result:
#   Coding Time: 00:04:17
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 40 ms, faster than 6.17%
#   Memory Usage: 14.3 MB, less than 43.08%
