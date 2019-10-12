# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        # Traverse all nodes of left tree and right tree
        queue = [[root.left, root.right]]
        while len(queue) >= 1:
            cur_elem = queue.pop(0)
            if cur_elem[0] is None or cur_elem[1] is None:
                if cur_elem[0] != cur_elem[1]:
                    return False
            else:
                if cur_elem[0].val != cur_elem[1].val:
                    return False
                # Check each nodes in symmetric
                queue.append([cur_elem[0].left, cur_elem[1].right])
                queue.append([cur_elem[0].right, cur_elem[1].left])

        # If it's false, already return False before this line
        return True

# Sample Testcase:
#   Input:
#     [1,2,2,3,4,4,3]
#   Output:
#     True

# Performance Result:
#   Coding Time: 00:11:28
#   Runtime: 36 ms, faster than 93.28% of Python3
#       online submissions for Symmetric Tree.
#   Memory Usage: 14 MB, less than 5.17% of Python3
#       online submissions for Symmetric Tree.
