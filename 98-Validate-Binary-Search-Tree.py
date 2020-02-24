# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidChild(self, cur_node, left_low_limit, right_up_limit) -> bool:
        # True if root is leaf
        if cur_node.left is None and cur_node.right is None:
            return True

        # Check 1st level children value
        if cur_node.left is not None and (cur_node.left.val >= cur_node.val or cur_node.left.val <= left_low_limit):
            return False
        if cur_node.right is not None and (cur_node.right.val <= cur_node.val or cur_node.right.val >= right_up_limit):
            return False
        
        # Check children
        if cur_node.left is not None and self.isValidChild(cur_node.left, left_low_limit, min(right_up_limit, cur_node.val)) == False:
            return False 
        if cur_node.right is not None and self.isValidChild(cur_node.right, max(left_low_limit, cur_node.val), right_up_limit) == False:
            return False

        return True

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return self.isValidChild(root, -2147483649, 2147483648)


# Sample test case:
#   Input:
#       [2,1,3]
#   Output:
#       true

# Performance Result:
#   Coding Time: 00:43:26
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 40 ms, faster than 85.00% of Python3
#       online submissions for Validate Binary Search Tree.
#   Memory Usage: 15.1 MB, less than 100.00% of Python3
#       online submissions for Validate Binary Search Tree.