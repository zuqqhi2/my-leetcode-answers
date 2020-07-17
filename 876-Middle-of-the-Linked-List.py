# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast_runner = head
        slow_runner = head
        while fast_runner is not None and fast_runner.next is not None:
            fast_runner = fast_runner.next.next
            slow_runner = slow_runner.next

        return slow_runner


# Performance Result:
#   Coding Time: 00:04:36
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 36 ms, faster than 32.49%
#   Memory Usage: 13.9 MB, less than 25.40%
