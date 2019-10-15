# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        stuck = [[root, root.val]]

        while len(stuck) >= 1:
            curElem = stuck.pop(0)
            curNode = curElem[0]
            curSum = curElem[1]

            # Leaf
            if curNode.left is None and curNode.right is None:
                if curSum == sum:
                    return True
            # Not Leaf
            else:
                if curNode.left is not None:
                    stuck.insert(0, [curNode.left, curSum + curNode.left.val])
                if curNode.right is not None:
                    stuck.insert(
                        0, [curNode.right, curSum + curNode.right.val])

        return False

# Sample Testcase:
#   Input:
#       [5,4,8,11,null,13,4,7,2,null,null,null,1]
#       22
#   Output:
#       True

# Performance Result:
#   Coding Time: 00:11:24
#   Time Complexity: O(n)
#   Space Complexity: O(n)
#   Runtime: 52 ms, faster than 63.25% of Python3
#       online submissions for Path Sum.
#   Memory Usage: 15.7 MB, less than 5.45% of Python3
#       online submissions for Path Sum.
