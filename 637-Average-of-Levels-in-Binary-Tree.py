# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        level_sum = []
        level_cnt = []
        opened = [(root, 0)]
        while len(opened) > 0:
            cur_node, cur_level = opened.pop(0)

            if len(level_sum) - 1 < cur_level:
                level_sum.append(0)
                level_cnt.append(0)
            level_sum[cur_level] += cur_node.val
            level_cnt[cur_level] += 1

            if cur_node.left is not None:
                opened.append((cur_node.left, cur_level + 1))
            if cur_node.right is not None:
                opened.append((cur_node.right, cur_level + 1))

        res = [0] * len(level_sum)
        for i in range(len(res)):
            res[i] = level_sum[i] / level_cnt[i]

        return res


# Performance Result:
#   Coding Time: 00:05:15
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 52 ms, faster than 55.99%
#   Memory Usage: 16.3 MB, less than 28.85%
