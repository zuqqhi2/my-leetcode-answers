# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        MAX_DEPTH_LIMIT = 1000000
        min_depth = MAX_DEPTH_LIMIT
        opened = []
        if root is not None:
            opened.append((root, 1))

        while len(opened) > 0:
            cur_node, cur_depth = opened.pop(0)

            if cur_node.left is None and cur_node.right is None:
                min_depth = min(min_depth, cur_depth)
                continue

            if cur_node.left is not None and cur_depth + 1 < min_depth:
                opened.append((cur_node.left, cur_depth + 1))
            if cur_node.right is not None and cur_depth + 1 < min_depth:
                opened.append((cur_node.right, cur_depth + 1))

        return min_depth if min_depth < MAX_DEPTH_LIMIT else 0


# Performance Result:
#   Coding Time: 00:08:26
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 48 ms, faster than 23.42% of Python3
#       online submissions for Minimum Depth of Binary Tree.
#   Memory Usage: 14.9 MB, less than 62.16% of Python3
#       online submissions for Minimum Depth of Binary Tree.
