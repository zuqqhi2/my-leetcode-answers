# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        opened = [(root, "")]
        res = 0
        while len(opened) > 0:
            cur_node, cur_bit = opened.pop(0)
            if cur_node.left is None and cur_node.right is None:
                res += int(cur_bit + str(cur_node.val), 2)
                continue

            if cur_node.right is not None:
                opened.insert(0, (cur_node.right, cur_bit + str(cur_node.val)))
            if cur_node.left is not None:
                opened.insert(0, (cur_node.left, cur_bit + str(cur_node.val)))

        return res


# Performance Result:
#   Coding Time: 00:04:42
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 73.54%
#   Memory Usage: 14.4 MB, less than 100.00%
