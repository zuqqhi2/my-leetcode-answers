# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        opened = [(root, 0)]
        next_lv_opened = []
        result = []
        while len(opened) > 0 or len(next_lv_opened) > 0:
            cur_node, cur_height = None, -1
            if len(opened) > 0:
                cur_node, cur_height = opened.pop(0)
            else:
                opened = next_lv_opened
                next_lv_opened = []
                cur_node, cur_height = opened.pop(0)

            if cur_height + 1 > len(result):
                result.append([])
            result[cur_height].append(cur_node.val)

            if cur_height % 2 == 0:
                if cur_node.left is not None:
                    next_lv_opened.insert(0, (cur_node.left, cur_height + 1))
                if cur_node.right is not None:
                    next_lv_opened.insert(0, (cur_node.right, cur_height + 1))
            else:
                if cur_node.right is not None:
                    next_lv_opened.insert(0, (cur_node.right, cur_height + 1))
                if cur_node.left is not None:
                    next_lv_opened.insert(0, (cur_node.left, cur_height + 1))

        return result


# Performance Result:
#   Coding Time: 00:23:50
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 24 ms, faster than 97.00%
#   Memory Usage: 13.9 MB, less than 5.41%
