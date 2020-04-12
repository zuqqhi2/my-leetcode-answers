# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        p_opened = [p]
        q_opened = [q]
        while len(p_opened) > 0:
            cur_p = p_opened.pop(0)
            cur_q = q_opened.pop(0)

            if cur_p.val != cur_q.val:
                return False

            if cur_p.left is not None and cur_q.left is not None:
                p_opened.insert(0, cur_p.left)
                q_opened.insert(0, cur_q.left)
            elif cur_p.left is None and cur_q.left is None:
                pass
            else:
                return False

            if cur_p.right is not None and cur_q.right is not None:
                p_opened.insert(0, cur_p.right)
                q_opened.insert(0, cur_q.right)
            elif cur_p.right is None and cur_q.right is None:
                pass
            else:
                return False

        return True


# Sample test case:
#   Input:
#       See the site
#   Output:
#       See the site

# Performance Result:
#   Coding Time: 00:06:41
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 29.67%
#   Memory Usage: 13.8 MB, less than 5.72%
