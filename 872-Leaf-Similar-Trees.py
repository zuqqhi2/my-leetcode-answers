# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_leaf_values(self, root: Optional[TreeNode]) -> [int]:
        res = []
        opened = [root]
        while len(opened) > 0:
            cur_node = opened.pop(0)
            if cur_node.left is None and cur_node.right is None:
                res.append(cur_node.val)
                continue

            if cur_node.right is not None:
                opened.insert(0, cur_node.right)
            if cur_node.left is not None:
                opened.insert(0, cur_node.left)

        return res

    def leafSimilar(self, root1: Optional[TreeNode],
                    root2: Optional[TreeNode]) -> bool:
        tree1_values = self.get_leaf_values(root1)
        tree2_values = self.get_leaf_values(root2)

        if len(tree1_values) != len(tree2_values):
            return False

        for i in range(len(tree1_values)):
            if tree1_values[i] != tree2_values[i]:
                return False

        return True


# Performance Result:
#   Coding Time: 00:10:25
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 74 ms, faster than 5.85%
#   Memory Usage: 14.3 MB, less than 70.12%
