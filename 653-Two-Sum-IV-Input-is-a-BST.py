import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        cnt = collections.defaultdict(int)
        opened = [root]
        while len(opened) > 0:
            cur = opened.pop(0)
            cnt[cur.val] += 1
            if cur.left is not None:
                opened.append(cur.left)
            if cur.right is not None:
                opened.append(cur.right)

        for key in cnt.keys():
            if k - key in cnt and key != k - key:
                return True

        return False


# Performance Result:
#   Coding Time: 00:07:27
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 132 ms, faster than 13.88%
#   Memory Usage: 16.1 MB, less than 34.31%
