# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Corner cases
        if head is None:
            return False
        if head.next is None:
            return False

        # Tartoize
        turtle1_pos = head.next
        turtle1_speed = 2
        turtle2_pos = head
        turtle2_speed = 1

        while turtle1_pos != turtle2_pos:
            if turtle1_pos.next is not None and turtle1_pos.next.next is not None:
                turtle1_pos = turtle1_pos.next.next
            else:
                return False

            turtle2_pos = turtle2_pos.next

        return True


# Performance Result:
#   Coding Time: 00:06:35
#   Algorithm: The Tortoise and the Hare
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 52 ms, faster than 33.42% of Python3
#       online submissions for Linked List Cycle.
#   Memory Usage: 15.9 MB, less than 100.00% of Python3
#       online submissions for Linked List Cycle.
