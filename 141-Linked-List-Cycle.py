# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Runner(object):
    def __init__(self, node, speed=1):
        """
        node should be ListNode
        speed = 1 means moving to next node in 1 time step
        """
        self.node = node
        self.speed = speed
        self.count = 0

    def step(self):
        """
        Move to next node with speed
        """
        self.count += 1
        if self.count >= self.speed:
            self.count = 0
            self.node = self.node.next

    def hasNext(self):
        """
        Check runner reaches end or not
        """
        if self.node.next is not None:
            return True
        else:
            return False

    def isSamePosition(self, runner):
        """
        Compare two runners' position.
        Some time node value is duplicated, so compare object.
        """
        if self.node == runner.node:
            return True
        else:
            return False

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool

        Loop detection by Floyd's Tortoise and Hare
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if head is None:
            return False

        # Let two different speed runners race
        fast_runner = Runner(head, 1)
        slow_runner = Runner(head, 2)
        while fast_runner.hasNext():
            fast_runner.step()
            slow_runner.step()
            # If they meet, that means there is a loop
            if fast_runner.isSamePosition(slow_runner):
                return True

        # There is a node which next = None, there is no loop
        return False

# Sample Testcase:
#   Input:
#     head object of a linked list(1:3 -> 2:2 -> 3:0 -> 4:-4 -> 2:2 -> ...)
#   Output:
#     true

# Performance Result:
#   Runtime: 84 ms, faster than 6.51% of Python online submissions for Linked List Cycle.
#   Memory Usage: 18.1 MB, less than 5.04% of Python online submissions for Linked List Cycle.
