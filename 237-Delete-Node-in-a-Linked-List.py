# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next is not None:
            node.val, node.next = node.next.val, node.next.next


# Performance Result:
#   Coding Time: -
#   Time Complexity: O(1)
#   Space Complexity: O(1)
#   Runtime: 60 ms, faster than 5.68%
#   Memory Usage: 14.2 MB, less than 42.63%
#   Memo: Too many dislikes question and I couldn't understand the problem
