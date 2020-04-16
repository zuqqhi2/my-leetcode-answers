# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        opened = [s]
        while len(opened) > 0:
            cur_s_node = opened.pop()
            if cur_s_node.left is not None:
                opened.append(cur_s_node.left)
            if cur_s_node.right is not None:
                opened.append(cur_s_node.right)
            if cur_s_node.val != t.val:
                continue

            opened_check = [(cur_s_node, t)]
            is_diff = False
            while len(opened_check) > 0:
                cur_s2, cur_t2 = opened_check.pop()
                if cur_s2.val != cur_t2.val:
                    is_diff = True
                    break

                if cur_s2.left is not None and cur_t2.left is not None:
                    opened_check.append((cur_s2.left, cur_t2.left))
                elif cur_s2.left is None and cur_t2.left is None:
                    pass
                else:
                    is_diff = True
                    break

                if cur_s2.right is not None and cur_t2.right is not None:
                    opened_check.append((cur_s2.right, cur_t2.right))
                elif cur_s2.right is None and cur_t2.right is None:
                    pass
                else:
                    is_diff = True
                    break

            if not is_diff:
                return True

        return False


# Sample test case:
#   Input:
#       See the site
#   Output:
#       See the site

# Performance Result:
#   Coding Time: 00:12:55
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 260 ms, faster than 40.61%
#   Memory Usage: 14 MB, less than 100.00%
