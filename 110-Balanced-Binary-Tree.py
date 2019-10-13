# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    isBalancedFlg = True

    def checkBalance(self, node, depth):
        if node.left is None and node.right is None:
            return [depth, depth]

        leftDepth = None
        rightDepth = None
        if node.left is not None:
            leftDepth = self.checkBalance(node.left, depth + 1)
        if node.right is not None:
            rightDepth = self.checkBalance(node.right, depth + 1)

        leftDepthMax = depth
        if leftDepth is not None:
            if leftDepth[0] < leftDepth[1]:
                leftDepthMax = leftDepth[1]
            else:
                leftDepthMax = leftDepth[0]

        rightDepthMax = depth
        if rightDepth is not None:
            if rightDepth[0] < rightDepth[1]:
                rightDepthMax = rightDepth[1]
            else:
                rightDepthMax = rightDepth[0]

        if abs(leftDepthMax - rightDepthMax) > 1:
            self.isBalancedFlg = False

        return [leftDepthMax, rightDepthMax]

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        self.checkBalance(root, 1)
        return self.isBalancedFlg

# Sample Testcase:
#   Input:
#     [3,9,20,null,null,15,7]
#   Output:
#     True

# Performance Result:
#   Coding Time: 00:28:45
#   Time Complexity: O(n)
#   Space Complexity: O(1)
#   Runtime: 72 ms, faster than 36.76% of Python3
#       online submissions for Balanced Binary Tree.
#   Memory Usage: 18.7 MB, less than 37.14% of Python3
#       online submissions for Balanced Binary Tree.
