# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        values = []
        queue = [root]
        while len(queue) > 0:
            cur_node = queue.pop()
            values.append(cur_node.val)
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

        values[:] = sorted(values)
        min_dist = 1e+6
        for i in range(1, len(values)):
            min_dist = min(min_dist, abs(values[i] - values[i - 1]))

        return min_dist


# Performance Result:
#   Coding Time: 00:04:42
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 56 ms, faster than 65.69%
#   Memory Usage: 16.1 MB, less than 89.77%
