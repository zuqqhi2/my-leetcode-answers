import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        opened = [(root, 0, 0)]
        tmp_res = collections.defaultdict(list)
        min_x = 2 ** 32
        max_x = -2 ** 31
        while len(opened) > 0:
            cur_node, cur_x, cur_y = opened.pop(0)
            if len(tmp_res[cur_x]) < cur_y + 1:
                for _ in range(cur_y + 1 - len(tmp_res[cur_x])):
                    tmp_res[cur_x].append([])
            tmp_res[cur_x][cur_y].append(cur_node.val)

            min_x = min(min_x, cur_x)
            max_x = max(max_x, cur_x)

            if cur_node.left is not None:
                opened.append((cur_node.left, cur_x - 1, cur_y + 1))
            if cur_node.right is not None:
                opened.append((cur_node.right, cur_x + 1, cur_y + 1))

        res = []
        for i in range(min_x, max_x + 1):
            cur_elem = []
            for y in range(len(tmp_res[i])):
                if len(tmp_res[i][y]) > 1:
                    cur_elem.extend(sorted(tmp_res[i][y]))
                else:
                    cur_elem.extend(tmp_res[i][y])
            res.append(cur_elem)

        return res


# Performance Result:
#   Coding Time: 00:28:29
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 28 ms, faster than 96.01%
#   Memory Usage: 14.2 MB, less than 9.28%
