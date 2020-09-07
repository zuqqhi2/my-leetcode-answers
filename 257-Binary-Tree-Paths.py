# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []

        res = []
        opened = [(root, str(root.val))]
        while len(opened) > 0:
            cur_node, cur_path = opened.pop(0)
            if cur_node.left is None and cur_node.right is None:
                res.append(cur_path)
                continue

            if cur_node.left is not None:
                opened.insert(0,
                              (cur_node.left,
                               cur_path + "->" + str(cur_node.left.val)))
            if cur_node.right is not None:
                opened.insert(0,
                              (cur_node.right,
                               cur_path + "->" + str(cur_node.right.val)))

        return res


# Performance Result:
#   Coding Time: 00:03:58
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 77.58%
#   Memory Usage: 13.7 MB, less than 93.37%
