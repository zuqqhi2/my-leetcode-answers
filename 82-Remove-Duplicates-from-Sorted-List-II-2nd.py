# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head

        first_nodes = {}
        val_count = defaultdict(int)
        cur = head
        while cur is not None:
            val_count[cur.val] += 1
            if cur not in first_nodes:
                first_nodes[cur.val] = cur
            cur = cur.next

        new_head = None
        prev = None
        cur = None
        for k in sorted(first_nodes.keys()):
            if val_count[k] != 1:
                continue

            if new_head is None:
                new_head = first_nodes[k]
                cur = new_head
            else:
                cur = first_nodes[k]
                prev.next = cur

            prev = cur

        if cur is not None:
            cur.next = None

        return new_head


# Performance Result:
#   Coding Time: 00:26:41
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 40 ms, faster than 63.03% of Python3
#       online submissions for Remove Duplicates from Sorted List II.
#   Memory Usage: 14 MB, less than 8.00% of Python3
#       online submissions for Remove Duplicates from Sorted List II.
