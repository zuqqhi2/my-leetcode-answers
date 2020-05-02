# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        opened = [(root, 0)]
        result = []
        while len(opened) > 0:
            cur_node, cur_height = opened.pop(0)
            if len(result) - 1 < cur_height:
                result.append([])
            result[cur_height].append(cur_node.val)

            if cur_node.left is not None:
                opened.append((cur_node.left, cur_height + 1))

            if cur_node.right is not None:
                opened.append((cur_node.right, cur_height + 1))

        return result


# Performance Result:
#   Coding Time: 00:05:15
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 44 ms, faster than 11.97%
#   Memory Usage: 14 MB, less than 16.13%
