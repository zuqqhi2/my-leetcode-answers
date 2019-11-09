# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return None, None

        if root.val <= V:
            sub_trees = self.splitBST(root.right, V)
            root.right = sub_trees[0]
            return root, sub_trees[1]
        else:
            sub_trees = self.splitBST(root.left, V)
            root.left = sub_trees[1]
            return sub_trees[0], root


# Sample test case:
#   Input:
#       root = [4,2,6,1,3,5,7], V = 2
#   Output:
#       [[2,1],[4,3,6,null,null,5,7]]

# Performance Result:
#   Coding Time: Timeout
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 28 ms, faster than 98.21% of Python3
#       online submissions for Split BST.
#   Memory Usage: 12.8 MB, less than 100.00% of Python3
#       online submissions for Split BST.
