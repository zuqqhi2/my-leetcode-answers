# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Corner case
        if head is None:
            return None
        if head.next is None:
            return None

        nodes = [head]
        cur_node = head.next
        while cur_node is not None:
            nodes.append(cur_node)
            if len(nodes) > n + 1:
                nodes.pop(0)

            cur_node = cur_node.next

        if n == 1:
            nodes[0].next = None
        elif len(nodes) < n + 1:
            head = nodes[1]
        else:
            nodes[0].next = nodes[2]

        return head


# Sample test case:
#   Input:
#       linked list: 1->2->3->4->5, and n = 2
#   Output:
#       1->2->3->5

# Performance Result:
#   Coding Time: 00:15:51
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 17.17% of Python3
#       online submissions for Remove Nth Node From End of List.
#   Memory Usage: 12.8 MB, less than 100.00% of Python3
#       online submissions for Remove Nth Node From End of List.
