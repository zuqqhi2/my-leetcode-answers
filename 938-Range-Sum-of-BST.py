# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        opened = [root]
        result = 0
        while len(opened) > 0:
            cur_node = opened.pop(0)
            result += cur_node.val if L <= cur_node.val <= R else 0

            if cur_node.left is not None:
                opened.append(cur_node.left)
            if cur_node.right is not None:
                opened.append(cur_node.right)

        return result


# Performance Result:
#   Coding Time: 00:18:20
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 572 ms, faster than 5.28%
#   Memory Usage: 22 MB, less than 5.94%
