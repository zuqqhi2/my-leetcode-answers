# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return None

        # BFS
        result = []
        queue = [(root, 1)]  # Node, Level
        while len(queue) > 0:
            cur_elem = queue.pop(0)
            if len(result) < cur_elem[1]:
                result.append([cur_elem[0].val])
            else:
                result[cur_elem[1] - 1].append(cur_elem[0].val)

            if cur_elem[0].left is not None:
                queue.append((cur_elem[0].left, cur_elem[1] + 1))

            if cur_elem[0].right is not None:
                queue.append((cur_elem[0].right, cur_elem[1] + 1))

        return result


# Performance Result:
#   Coding Time: 00:08:30
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 73.09% of Python3
#       online submissions for Binary Tree Level Order Traversal.
#   Memory Usage: 12.9 MB, less than 100.00% of Python3
#       online submissions for Binary Tree Level Order Traversal.
