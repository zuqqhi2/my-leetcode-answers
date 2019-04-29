# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Just using simple way to get an answer like the following.
        1. get integer number from given linked lists
        2. sum of integers
        3. generate a linked list by seeing each digit of step2 result
        """

        def fetchValueFromListNode(node: ListNode) -> int:
            """
            Traverse given linked list and generate 1 integer.
            If given list is something like this (2 -> 4 -> 3),
            this function returns 3 * 100 + 4 * 10 + 2.
            """
            curNode = node
            result = curNode.val
            loopCount = 1
            while curNode.next is not None:
                curNode = curNode.next
                result += curNode.val * (10 ** loopCount)
                loopCount += 1

            return result

        # Get integers from given lists
        value1 = fetchValueFromListNode(l1)
        value2 = fetchValueFromListNode(l2)
        sumVal = value1 + value2

        # Generate an answer linked list
        # by traversing array from top
        sumValList = str(sumVal)
        curListNode = ListNode(sumValList[0])
        prevListNode = None
        for idx in range(1, len(sumValList)):
            prevListNode = curListNode
            curListNode = ListNode(sumValList[idx])
            curListNode.next = prevListNode

        return curListNode

# Sample Testcase:
#   Input:
#     (2 -> 4 -> 3) + (5 -> 6 -> 4)
#   Output:
#     7 -> 0 -> 8

# Performance Result:
#   Runtime: 84 ms, faster than 83.22% of Python3 online submissions for Add Two Numbers.
#   Memory Usage: 13.3 MB, less than 5.21% of Python3 online submissions for Add Two Numbers.
