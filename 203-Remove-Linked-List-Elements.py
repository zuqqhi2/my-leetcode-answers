# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new_head = None
        prev_node = None
        cur_node = head
        while cur_node is not None:
            if cur_node.val != val:
                if prev_node is not None:
                    prev_node.next = cur_node
                prev_node = cur_node
                if new_head is None:
                    new_head = cur_node
            cur_node = cur_node.next

        if prev_node is not None:
            prev_node.next = None

        return new_head


# Performance Result:
#   Coding Time: 00:05:52
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 64 ms, faster than 88.27%
#   Memory Usage: 17.3 MB, less than 24.47%
