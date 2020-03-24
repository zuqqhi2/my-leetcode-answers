# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Corner case
        if head is None:
            return None
        if head.next is None:
            return None

        # Create backward list
        tail = ListNode(head.val)
        cur_node = head.next
        num_nodes = 1
        while cur_node is not None:
            new_node = ListNode(cur_node.val)
            new_node.next = tail
            tail = new_node
            cur_node = cur_node.next
            num_nodes += 1

        # Reorder
        left_cur_node = head
        right_cur_node = tail
        for i in range(num_nodes // 2):
            tmp_node = left_cur_node.next
            left_cur_node.next = right_cur_node
            left_cur_node = tmp_node

            # For even num nodes case
            if num_nodes % 2 == 0 and i == num_nodes // 2 - 1:
                right_cur_node.next = None
                break

            tmp_node = right_cur_node.next
            right_cur_node.next = left_cur_node
            right_cur_node = tmp_node

        # For odd num nodes case
        if num_nodes % 2 == 1:
            left_cur_node.next = None


# Sample test case:
#   Input:
#       1->2->3->4->5
#   Output:
#       1->5->2->4->3

# Performance Result:
#   Coding Time: 00:34:13
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 128 ms, faster than 7.61% of Python3
#       online submissions for Reorder List.
#   Memory Usage: 22.6 MB, less than 7.69% of Python3
#       online submissions for Reorder List.
