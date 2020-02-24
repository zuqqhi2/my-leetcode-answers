# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    preorder_list = []

    def buildSubTree(self, inorder) -> TreeNode:
        # Create root node
        cur_node = TreeNode(self.preorder_list.pop(0))
        
        # Find current node in inorder list
        cur_node_idx_in_inorder = inorder.index(cur_node.val)

        # Build left and right subtree
        if cur_node_idx_in_inorder > 0:
            cur_node.left = self.buildSubTree(inorder[:cur_node_idx_in_inorder])
        if cur_node_idx_in_inorder < len(inorder) - 1:
            cur_node.right = self.buildSubTree(inorder[cur_node_idx_in_inorder+1:])

        return cur_node

    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        elif len(preorder) != len(inorder):
            return None
        
        self.preorder_list = preorder
        return self.buildSubTree(inorder)


# Sample test case:
#   Input:
#       preorder = [3,9,20,15,7]
#       inorder = [9,3,15,20,7]
#   Output:
#       Tree [3,9,null,null,20,null,null,null,null,15,7]

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 140 ms, faster than 54.91% of Python3
#       online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
#   Memory Usage: 51.2 MB, less than 71.05% of Python3
#       online submissions for Construct Binary Tree from Preorder and Inorder Traversal.