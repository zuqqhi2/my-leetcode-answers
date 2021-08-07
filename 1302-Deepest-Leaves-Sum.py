import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        leaf_sum = collections.defaultdict(int)
        max_deep = 0
        opened = [(root, 1)]
        while len(opened) > 0:
            cur_node, cur_deep = opened.pop(0)

            if cur_node.left is None and cur_node.right is None:
                leaf_sum[cur_deep] += cur_node.val
                max_deep = max(max_deep, cur_deep)

            if cur_node.left is not None:
                opened.append((cur_node.left, cur_deep + 1))
            if cur_node.right is not None:
                opened.append((cur_node.right, cur_deep + 1))

        return leaf_sum[max_deep]


# Performance Result:
#   Coding Time: 00:06:15
#   Time Complexity: O(N)
#   Space Complexity: O(H)
#   Runtime: 104 ms, faster than 37.89%
#   Memory Usage: 17.8 MB, less than 40.48%
