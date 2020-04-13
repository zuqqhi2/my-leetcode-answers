# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return None
        if t1 is None and t2 is not None:
            return t2
        if t1 is not None and t2 is None:
            return t1

        new_head = None
        opened = [(t1, t2, None, True)]
        while len(opened) > 0:
            op1, op2, parent, is_left = opened.pop(0)
            new_node = TreeNode(op1.val + op2.val)
            if parent is None:
                new_head = new_node
            elif is_left:
                parent.left = new_node
            else:
                parent.right = new_node

            if op1.left is not None or op2.left is not None:
                if op1.left is not None and op2.left is not None:
                    opened.append((op1.left, op2.left, new_node, True))
                elif op1.left is not None and op2.left is None:
                    opened.append((op1.left, TreeNode(0), new_node, True))
                else:
                    opened.append((TreeNode(0), op2.left, new_node, True))

            if op1.right is not None or op2.right is not None:
                if op1.right is not None and op2.right is not None:
                    opened.append((op1.right, op2.right, new_node, False))
                elif op1.right is not None and op2.right is None:
                    opened.append((op1.right, TreeNode(0), new_node, False))
                else:
                    opened.append((TreeNode(0), op2.right, new_node, False))

        return new_head


# Performance Result:
#   Coding Time: 00:14:00
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 120 ms, faster than 6.33%
#   Memory Usage: 14.8 MB, less than 5.72%
