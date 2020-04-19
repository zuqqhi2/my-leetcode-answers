from collections import defaultdict


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head

        val_cnt = defaultdict(int)
        val_head_node = {}
        cur_node = head
        while cur_node is not None:
            val_cnt[cur_node.val] += 1
            if cur_node.val not in val_head_node:
                val_head_node[cur_node.val] = cur_node
            cur_node = cur_node.next

        targets = list(sorted([k for k in val_cnt.keys() if val_cnt[k] == 1]))
        if len(targets) == 0:
            return None

        new_head = val_head_node[targets[0]]
        cur_node = new_head
        for i in range(0, len(targets) - 1):
            cur_node.next = val_head_node[targets[i + 1]]
            cur_node = cur_node.next
        cur_node.next = None

        return new_head


# Performance Result:
#   Coding Time: 00:22:15
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 48 ms, faster than 8.39%
#   Memory Usage: 13.9 MB, less than 8.00%
