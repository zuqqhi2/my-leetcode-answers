# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generate(self, nums, parent):
        # Generate new node
        new_node = None
        if len(nums) == 1:
            new_node = TreeNode(nums[0])
        elif len(nums) > 1:
            center_idx = len(nums) // 2
            new_node = TreeNode(nums[center_idx])
        else:
            return parent

        # Assign new node to the parent child
        if parent is not None:
            if new_node.val < parent.val:
                parent.left = new_node
            else:
                parent.right = new_node

        # Generate children
        if len(nums) >= 2:
            self.generate(nums[0:center_idx], new_node)
            self.generate((nums[center_idx+1:]), new_node)

        # To pass root node to caller
        return new_node

    def sortedArrayToBST(self, nums) -> TreeNode:
        if len(nums) == 0:
            return None

        root = self.generate(nums, None)
        return root


# Sample test case:
#   Input:
#       [-10,-3,0,5,9]
#   Output:
#       [0,-3,9,-10,null,5]

# Performance Result:
#   Coding Time: 00:18:34
#   Time Complexity: O(logN)
#   Space Complexity: O(N)
#   Runtime: 72 ms, faster than 59.44% of Python3
#       online submissions for Convert Sorted Array to Binary Search Tree.
#   Memory Usage: 15 MB, less than 100.00% of Python3
#       online submissions for Convert Sorted Array to Binary Search Tree.
