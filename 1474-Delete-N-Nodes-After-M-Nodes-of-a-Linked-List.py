# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        cur_node = head
        cnt = 1
        is_remove_phase = False
        prev_node = None
        while cur_node is not None:
            if is_remove_phase and cnt > n:
                is_remove_phase = False
                prev_node.next = cur_node
                cnt = 1
            elif not is_remove_phase and cnt > m:
                is_remove_phase = True
                cnt = 1

            if not is_remove_phase:
                prev_node = cur_node
            cur_node = cur_node.next
            cnt += 1
        prev_node.next = None

        return head


# Performance Result:
#   Coding Time: 00:08:53
#   Time Complexity: O(N)
#   Space Complexity: O(1)
#   Runtime: 56 ms, faster than 99.36%
#   Memory Usage: 16.9 MB, less than 36.65%
