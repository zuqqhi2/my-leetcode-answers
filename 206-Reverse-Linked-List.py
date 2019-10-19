# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        stuck = []
        curNode = head
        while curNode is not None:
            stuck.insert(0, curNode)
            curNode = curNode.next

        newHead = stuck.pop(0)
        curNode = newHead
        numNode = len(stuck)
        for i in range(numNode):
            curNode.next = stuck.pop(0)
            curNode = curNode.next
        curNode.next = None

        return newHead


# Sample Testcase:
#   Input:
#       1->2->3->4->5->NULL
#   Output:
#       5->4->3->2->1->NULL

# Performance Result:
#   Coding Time: 00:07:50
#   Time Complexity: O(n)
#   Space Complexity: O(n)
#   Runtime: 52 ms, faster than 9.29% of Python3
#       online submissions for Reverse Linked List.
#   Memory Usage: 15.1 MB, less than 31.82% of Python3
#       online submissions for Reverse Linked List.
