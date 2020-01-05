# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if root is None:
            return None

        # BFS with zigzag
        result = []
        queue = [(root, 1)]  # node, level
        while len(queue) > 0:
            cur_elem = queue.pop(0)

            # Registering current node to the result array
            if len(result) < cur_elem[1]:
                result.append([cur_elem[0].val])
            else:
                result[cur_elem[1] - 1].append(cur_elem[0].val)

            # Enqueuing children to the queue
            if cur_elem[0].left is not None:
                queue.append((cur_elem[0].left, cur_elem[1] + 1))

            if cur_elem[0].right is not None:
                queue.append((cur_elem[0].right, cur_elem[1] + 1))

        for i in range(len(result)):
            if i % 2 == 1:
                result[i] = reversed(result[i])

        return result


# Performance Result:
#   Coding Time: 00:25:20
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 53.86% of Python3
#       online submissions for Binary Tree Zigzag Level Order Traversal.
#   Memory Usage: 12.7 MB, less than 100.00% of Python3
#       online submissions for Binary Tree Zigzag Level Order Traversal.
