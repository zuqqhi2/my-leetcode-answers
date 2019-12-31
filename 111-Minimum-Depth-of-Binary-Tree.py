# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        min_depth = 10000000
        stuck = [(root, 1)]

        while len(stuck) > 0:
            cur_node = stuck.pop(0)

            if cur_node[0].left is None and cur_node[0].right is None:
                if cur_node[1] < min_depth:
                    min_depth = cur_node[1]

            if cur_node[0].left is not None:
                stuck.insert(0, (cur_node[0].left, cur_node[1] + 1))

            if cur_node[0].right is not None:
                stuck.insert(0, (cur_node[0].right, cur_node[1] + 1))

        return min_depth


# Sample test case:
#   Input:
#       [3,9,20,null,null,15,7]
#   Output:
#       2

# Performance Result:
#   Coding Time: 00:04:02
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 48 ms, faster than 55.33% of Python3
#       online submissions for Minimum Depth of Binary Tree.
#   Memory Usage: 13.8 MB, less than 100.00% of Python3
#       online submissions for Minimum Depth of Binary Tree.
