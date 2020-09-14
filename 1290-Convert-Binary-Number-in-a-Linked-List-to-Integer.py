# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_num = []
        while head is not None:
            bin_num.append(str(head.val))
            head = head.next

        return int(''.join(bin_num), 2)


# Performance Result:
#   Coding Time: 00:04:23
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 24 ms, faster than 94.96%
#   Memory Usage: 13.6 MB, less than 95.56%
