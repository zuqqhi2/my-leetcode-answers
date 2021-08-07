# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode,
                      target: TreeNode) -> TreeNode:
        opened = [(original, cloned)]
        while len(opened) > 0:
            cur_ori, cur_clon = opened.pop(0)
            if cur_ori.val == target.val:
                return cur_clon

            if cur_ori.left is not None:
                opened.append((cur_ori.left, cur_clon.left))
            if cur_ori.right is not None:
                opened.append((cur_ori.right, cur_clon.right))

        return None


# Performance Result:
#   Coding Time: 00:04:24
#   Time Complexity: O(N)
#   Space Complexity: O(H)
#   Runtime: 632 ms, faster than 58.81%
#   Memory Usage: 24.1 MB, less than 81.51%
