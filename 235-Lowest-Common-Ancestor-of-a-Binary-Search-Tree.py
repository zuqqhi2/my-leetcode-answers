# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        parents = {}
        is_p_reached = False
        p_height = 0
        is_q_reached = False
        q_height = 0
        opened = [(root, 1)]
        while len(opened) > 0 or (not is_p_reached and not is_q_reached):
            cur_node, cur_height = opened.pop(0)
            if cur_node == p:
                is_p_reached = True
                p_height = cur_height
            elif cur_node == q:
                is_q_reached = True
                q_height = cur_height

            if cur_node.left is not None:
                parents[cur_node.left] = cur_node
                opened.append((cur_node.left, cur_height + 1))

            if cur_node.right is not None:
                parents[cur_node.right] = cur_node
                opened.append((cur_node.right, cur_height + 1))

        cur_p_node = p
        cur_q_node = q
        while cur_p_node != cur_q_node:
            if p_height > q_height:
                cur_p_node = parents[cur_p_node]
                p_height -= 1
            elif p_height < q_height:
                cur_q_node = parents[cur_q_node]
                q_height -= 1
            else:
                cur_p_node = parents[cur_p_node]
                p_height -= 1
                cur_q_node = parents[cur_q_node]
                q_height -= 1

        return cur_p_node


# Performance Result:
#   Coding Time: 00:26:58
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 108 ms, faster than 7.38%
#   Memory Usage: 18 MB, less than 5.55%
