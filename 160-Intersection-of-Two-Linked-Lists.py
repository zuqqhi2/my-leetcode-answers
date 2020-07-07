# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        setA = set()
        while headA is not None:
            setA.add(headA)
            headA = headA.next

        while headB is not None:
            if headB in setA:
                return headB

            headB = headB.next

        return headB


# Performance Result:
#   Coding Time: 00:05:41
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 272 ms, faster than 6.71%
#   Memory Usage: 29.3 MB, less than 19.93%
