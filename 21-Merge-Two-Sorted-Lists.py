# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # if one of given list is None, no need to merge
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        prev_node = None
        result_head = None
        cur_l1_node = l1
        cur_l2_node = l2

        # Decide head(choose smaller value node)
        if cur_l1_node.val <= cur_l2_node.val:
            prev_node = cur_l1_node
            result_head = cur_l1_node
            cur_l1_node = cur_l1_node.next
        else:
            prev_node = cur_l2_node
            result_head = cur_l2_node
            cur_l2_node = cur_l2_node.next

        # Until one of list reaches to the end,
        # scan each node of both and choose smaller node
        while cur_l1_node is not None and cur_l2_node is not None:
            if cur_l1_node.val <= cur_l2_node.val:
                prev_node.next = cur_l1_node
                cur_l1_node = cur_l1_node.next
            else:
                prev_node.next = cur_l2_node
                cur_l2_node = cur_l2_node.next

            prev_node = prev_node.next

        # Append not None list's remaining nodes
        cur_node = cur_l1_node
        if cur_l1_node is None:
            cur_node = cur_l2_node
        while cur_node is not None:
            prev_node.next = cur_node
            cur_node = cur_node.next
            prev_node = prev_node.next

        return result_head

# Sample Testcase:
#   Input:
#     1->2->4, 1->3->4
#   Output:
#     1->1->2->3->4->4

# Performance Result:
#   Coding Time: 00:10:15
#   Runtime: 44 ms, faster than 90.00% of Python3 online submissions for Merge Two Sorted Lists.
#   Memory Usage: 13.3 MB, less than 5.06% of Python3 online submissions for Merge Two Sorted Lists.
