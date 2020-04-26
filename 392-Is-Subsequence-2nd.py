class ListNode:
    def __init__(self, s: str):
        self.s = s
        self.next = None


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Corner cases
        if len(t) == 0 and len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        elif len(s) == 0:
            return True

        # Generate s list
        head = ListNode("")
        cur_node = head
        for i in range(len(s)):
            cur_node.next = ListNode(s[i])
            cur_node = cur_node.next

        # Search
        cur_node = head
        for i in range(len(t)):
            if t[i] == cur_node.next.s:
                cur_node = cur_node.next
                if cur_node.next is None:
                    return True

        return False


# Performance Result:
#   Coding Time: 00:11:28
#   Time Complexity: O(N)
#   Space Complexity: O(M)
#   Runtime: 156 ms, faster than 63.38%
#   Memory Usage: 18.4 MB, less than 26.67%
