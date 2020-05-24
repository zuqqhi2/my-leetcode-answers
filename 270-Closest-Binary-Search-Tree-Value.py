# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest_val = root.val
        cur_node = root
        while cur_node is not None:
            if abs(target - cur_node.val) < abs(target - closest_val):
                closest_val = cur_node.val

            if target < cur_node.val:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        return closest_val


# Performance Result:
#   Coding Time: 00:09:08
#   Time Complexity: O(log N)
#   Space Complexity: O(1)
#   Runtime: 40 ms, faster than 71.98%
#   Memory Usage: 15.8 MB, less than 7.14%
