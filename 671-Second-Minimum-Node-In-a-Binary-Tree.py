# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        min_2nd = 2 ** 32
        opened = [root]
        while len(opened) > 0:
            cur_node = opened.pop(0)
            if cur_node.val > root.val:
                min_2nd = min(min_2nd, cur_node.val)

            if cur_node.left is not None:
                opened.append(cur_node.left)
            if cur_node.right is not None:
                opened.append(cur_node.right)
        return min_2nd if min_2nd < 2 ** 32 else -1


# Performance Result:
#   Coding Time: 00:12:54
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 32 ms, faster than 44.95%
#   Memory Usage: 13.9 MB, less than 10.00%
