# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        pivot_idx = len(nums) // 2
        root = TreeNode(nums[pivot_idx])

        root.left = None
        if pivot_idx > 0:
            root.left = self.sortedArrayToBST(nums[0:pivot_idx])

        root.right = None
        if pivot_idx < len(nums) - 1:
            root.right = self.sortedArrayToBST(nums[pivot_idx + 1:])

        return root


# Performance Result:
#   Coding Time: 00:08:53
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 72 ms, faster than 75.89%
#   Memory Usage: 16.2 MB, less than 6.45%
