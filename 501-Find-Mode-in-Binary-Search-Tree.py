import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        cnt = collections.defaultdict(int)
        max_freq = 0

        opened = [root]
        while len(opened) > 0:
            cur_node = opened.pop(0)
            cnt[cur_node.val] += 1
            if cnt[cur_node.val] > max_freq:
                max_freq = cnt[cur_node.val]

            if cur_node.left is not None:
                opened.append(cur_node.left)
            if cur_node.right is not None:
                opened.append(cur_node.right)

        return [num for num in cnt.keys() if cnt[num] == max_freq]


# Performance Result:
#   Coding Time: 00:05:32
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 60 ms, faster than 42.07%
#   Memory Usage: 18.1 MB, less than 99.68%
