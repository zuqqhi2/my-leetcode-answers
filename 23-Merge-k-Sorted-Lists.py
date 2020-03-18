# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        """
        :param List[ListNode] lists:
        :rtype: ListNode
        :return:
        """
        # Corner case
        if len(lists) == 0:
            return None

        # n-pointer
        num_ended = 0
        pointers = []
        for node in lists:
            pointers.append(node)
            if node is None:
                num_ended += 1

        result_head = None
        cur_result_node = None
        while num_ended < len(lists):
            # Find minimum value from pointers
            cur_min_val = 1e+6
            min_idx = -1
            for i, node in enumerate(pointers):
                if node is None:
                    continue
                if cur_min_val > node.val:
                    cur_min_val = node.val
                    min_idx = i

            # Generate node and connect from head
            if result_head is None:
                result_head = ListNode(cur_min_val)
                cur_result_node = result_head
            else:
                new_node = ListNode(cur_min_val)
                cur_result_node.next = new_node
                cur_result_node = new_node

            # Move minimum value pointer to next
            pointers[min_idx] = pointers[min_idx].next
            if pointers[min_idx] is None:
                num_ended += 1

        return result_head


# Sample test case:
#   Input:
#       [
#           1->4->5,
#           1->3->4,
#           2->6
#       ]
#   Output:
#       1->1->2->3->4->4->5->6

# Performance Result:
#   Coding Time: 00:16:17
#   Time Complexity: O(NM)
#   Space Complexity: O(N)
#   Runtime: 7372 ms, faster than 5.00% of Python3
#       online submissions for Merge k Sorted Lists.
#   Memory Usage: 17.1 MB, less than 31.82% of Python3
#       online submissions for Merge k Sorted Lists.
