# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Corner case
        if head is None:
            return None
        if head.next is None:
            return head

        # 2-pointers
        left = head
        right = head.next
        head.next = None
        while right is not None:
            tmp = right.next
            right.next = left
            left = right
            right = tmp

        return left


# Performance Result:
#   Coding Time: 00:04:10
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 36 ms, faster than 53.67% of Python3
#       online submissions for Reverse Linked List.
#   Memory Usage: 15.4 MB, less than 25.00% of Python3
#       online submissions for Reverse Linked List.
