# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        opened = [(root, root.val)]
        while len(opened) > 0:
            cur_node, cur_sum = opened.pop()
            if cur_node.left is None and cur_node.right is None and cur_sum == sum:
                return True

            if cur_node.right is not None:
                opened.append((cur_node.right, cur_sum + cur_node.right.val))
            if cur_node.left is not None:
                opened.append((cur_node.left, cur_sum + cur_node.left.val))

        return False


# Performance Result:
#   Coding Time: 00:05:55
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 44 ms, faster than 57.26%
#   Memory Usage: 15.5 MB, less than 5.45%
