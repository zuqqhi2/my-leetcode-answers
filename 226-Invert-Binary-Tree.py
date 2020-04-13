# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        opened = [(root.left, root.right, root)]
        while len(opened) > 0:
            left, right, parent = opened.pop(0)
            parent.left = right
            parent.right = left

            if left is not None:
                if left.left is not None or left.right is not None:
                    opened.append((left.left, left.right, left))

            if right is not None:
                if right.left is not None or right.right is not None:
                    opened.append((right.left, right.right, right))

        return root


# Sample test case:
#   Input:
#       See the site
#   Output:
#       See the site

# Performance Result:
#   Coding Time: 00:23:57
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 24 ms, faster than 90.36%
#   Memory Usage: 13.7 MB, less than 5.41%
