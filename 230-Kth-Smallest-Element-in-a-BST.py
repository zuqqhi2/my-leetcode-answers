# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    NO_RESULT = -1_000_000

    def findkthSmallest(self, root: TreeNode, k: int) -> (int, int):
        if root.left is not None:
            k, res = self.findkthSmallest(root.left, k)
            if k == 0 and res != self.NO_RESULT:
                return 0, res

        k -= 1
        if k == 0:
            return 0, root.val

        if root.right is not None:
            k, res = self.findkthSmallest(root.right, k)
            if k == 0 and res != self.NO_RESULT:
                return 0, res

        return k, self.NO_RESULT

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        _, result = self.findkthSmallest(root, k)
        return result


# Performance Result:
#   Coding Time: 00:32:02
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 52 ms, faster than 56.79%
#   Memory Usage: 17.9 MB, less than 5.45%
