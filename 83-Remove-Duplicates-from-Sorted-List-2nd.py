# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Corner case
        if head is None:
            return None
        if head.next is None:
            return head

        # 2-pointers
        left_node = head
        right_node = head.next
        is_same_prev = False
        while right_node is not None:
            if left_node.val == right_node.val:
                is_same_prev = True
            elif left_node.val != right_node.val and is_same_prev:
                left_node.next = right_node
                left_node = left_node.next
                is_same_prev = False
            else:
                left_node = left_node.next

            right_node = right_node.next

        if is_same_prev:
            left_node.next = None

        return head


# Performance Result:
#   Coding Time: 00:08:53
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 44 ms, faster than 34.91% of Python3
#       online submissions for Remove Duplicates from Sorted List.
#   Memory Usage: 13.8 MB, less than 6.45% of Python3
#       online submissions for Remove Duplicates from Sorted List.
