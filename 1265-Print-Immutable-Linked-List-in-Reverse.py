# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        nodes = []
        cur_node = head
        while cur_node is not None:
            nodes.append(cur_node)
            cur_node = cur_node.getNext()

        nodes[:] = reversed(nodes)
        for i in range(len(nodes)):
            nodes[i].printValue()


# Performance Result:
#   Coding Time: 00:06:22
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 36 ms, faster than 68.20%
#   Memory Usage: 14.6 MB, less than 79.26%
