# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0

        num_paths = 0
        opened = [root]
        while len(opened) > 0:
            cur_start = opened.pop(0)

            opened2 = [(cur_start, cur_start.val)]
            while len(opened2) > 0:
                cur_node, cur_sum = opened2.pop(0)
                if cur_sum == sum:
                    num_paths += 1

                if cur_node.left is not None:
                    opened2.append((cur_node.left, cur_sum + cur_node.left.val))
                if cur_node.right is not None:
                    opened2.append(
                        (cur_node.right, cur_sum + cur_node.right.val))

            if cur_start.left is not None:
                opened.append(cur_start.left)
            if cur_start.right is not None:
                opened.append(cur_start.right)

        return num_paths


# Performance Result:
#   Coding Time: 00:07:56
#   Time Complexity: O(N^2)
#   Space Complexity: O(1)
#   Runtime: 1200 ms, faster than 7.74%
#   Memory Usage: 14.2 MB, less than 97.52%
