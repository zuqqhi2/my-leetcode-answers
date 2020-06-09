# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(root1: TreeNode, root2: TreeNode) -> bool:
            is_same_child = True
            if root1.left is not None and root2.left is not None:
                if root1.left.val != root2.left.val:
                    is_same_child = False
            elif root1.left is not None or root2.left is not None:
                is_same_child = False

            if root1.right is not None and root2.right is not None:
                if root1.right.val != root2.right.val:
                    is_same_child = False
            elif root1.right is not None or root2.right is not None:
                is_same_child = False

            return is_same_child

        # Check corner cases
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        # Main
        opened = [(root1, root2)]
        while len(opened) > 0:
            cur1, cur2 = opened.pop(0)

            # Flip equivalent check
            if not helper(cur1, cur2):
                cur1.left, cur1.right = cur1.right, cur1.left
                if not helper(cur1, cur2):
                    return False

            if cur1.left is not None:
                opened.append((cur1.left, cur2.left))
            if cur1.right is not None:
                opened.append((cur1.right, cur2.right))

        return True


# Performance Result:
#   Coding Time: 00:12:14
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 48 ms, faster than 9.00%
#   Memory Usage: 13.7 MB, less than 80.49%
