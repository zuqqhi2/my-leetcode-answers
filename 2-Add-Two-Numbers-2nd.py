# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode(0)
        cur_res = new_head
        carry = 0
        cur_l1 = l1
        cur_l2 = l2
        while cur_l1 is not None or cur_l2 is not None:
            tmp = cur_l1.val if cur_l1 is not None else 0
            tmp += cur_l2.val if cur_l2 is not None else 0
            tmp += carry
            cur_res.next = ListNode(tmp % 10)
            cur_res = cur_res.next

            carry = tmp // 10

            if cur_l1 is not None:
                cur_l1 = cur_l1.next
            if cur_l2 is not None:
                cur_l2 = cur_l2.next

        if carry > 0:
            cur_res.next = ListNode(carry)

        return new_head.next


# Performance Result:
#   Coding Time: 00:14:32
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 112 ms, faster than 5.72%
#   Memory Usage: 14 MB, less than 5.67%
