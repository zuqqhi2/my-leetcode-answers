# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if root is None:
            return 0

        values = []

        opened = [root]
        while len(opened) > 0:
            cur_node = opened.pop(0)
            values.append(cur_node.val)

            if cur_node.left is not None:
                opened.append(cur_node.left)
            if cur_node.right is not None:
                opened.append(cur_node.right)

        values[:] = sorted(values)
        min_dist = values[1] - values[0]
        for i in range(2, len(values)):
            min_dist = min(min_dist, values[i] - values[i - 1])

        return min_dist


# Performance Result:
#   Coding Time: 00:07:41
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 20 ms, faster than 99.48%
#   Memory Usage: 14.4 MB, less than 39.34%
