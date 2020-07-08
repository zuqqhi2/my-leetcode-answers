# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head is not None:
            vals.append(head.val)
            head = head.next

        vals_reversed = list(reversed(vals))
        for i in range(len(vals)):
            if vals[i] != vals_reversed[i]:
                return False

        return True


# Performance Result:
#   Coding Time: 00:03:01
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 120 ms, faster than 10.62%
#   Memory Usage: 24.2 MB, less than 15.30%
