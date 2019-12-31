# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        max_depth = 1
        stuck = [(root, max_depth)]
        while len(stuck) > 0:
            cur_node = stuck.pop(0)

            if max_depth < cur_node[1]:
                max_depth = cur_node[1]

            if cur_node[0].left is not None:
                stuck.insert(0, (cur_node[0].left, cur_node[1] + 1))

            if cur_node[0].right is not None:
                stuck.insert(0, (cur_node[0].right, cur_node[1] + 1))

        return max_depth


# Sample test case:
#   Input:
#       [3,9,20,null,null,15,7]
#   Output:
#       3

# Performance Result:
#   Coding Time: 00:05:08
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 32 ms, faster than 98.34% of Python3
#       online submissions for Maximum Depth of Binary Tree.
#   Memory Usage: 14 MB, less than 100.00% of Python3
#       online submissions for Maximum Depth of Binary Tree.
