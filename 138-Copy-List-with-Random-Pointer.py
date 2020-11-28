"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        cur_node = head
        dest_head = None
        prev_node = dest_head
        dest_node_list = []
        cur_idx = 0
        while cur_node is not None:
            if cur_idx == 0:
                dest_head = Node(head.val)
                prev_node = dest_head
            else:
                prev_node.next = Node(cur_node.val)
                prev_node = prev_node.next
            dest_node_list.append(prev_node)

            cur_node = cur_node.next
            cur_idx += 1

        cur_src_node = head
        cur_dest_node = dest_head
        while cur_src_node is not None:
            if cur_src_node.random is None:
                cur_dest_node.random = None
            else:
                cur_idx = 0
                cur_check_node = head
                while cur_check_node != cur_src_node.random:
                    cur_check_node = cur_check_node.next
                    cur_idx += 1
                cur_dest_node.random = dest_node_list[cur_idx]

            cur_src_node = cur_src_node.next
            cur_dest_node = cur_dest_node.next

        return dest_head


# Performance Result:
#   Coding Time: 00:29:33
#   Time Complexity: O(N^2)
#   Space Complexity: O(N)
#   Runtime: 60 ms, faster than 5.24%
#   Memory Usage: 15 MB, less than 17.87%
