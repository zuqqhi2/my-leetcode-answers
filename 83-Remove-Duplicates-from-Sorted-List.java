/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    /*
     * Time complexity: O(n)
     * Space complexity: O(n)
     */
    public ListNode deleteDuplicates(ListNode head) {
        // If there is no list, just return an empty list.
        if (head == null) { return null; }

        // Traverse a given list from head keeping node value history.
        ListNode current = head;
        ListNode prev = head;
        HashMap<Integer, Boolean> history = new HashMap<Integer, Boolean>();
        while (current != null) {
            // If history already have a value, remove current node from given list.
            if (history.containsKey(current.val)) {
                prev.next = current.next;
            } else {
                prev = current;
            }

            // Save current node value
            history.put(current.val, true);

            // Go to next node
            current = current.next;
        }

        // Return just head because given list is modified
        return head;
    }
}

// Sample Testcase:
//   Input:
//     head object of a linked list(1:1 -> 2:1 -> 3:2 -> ...)
//   Output:
//     a list head without duplicate values

// Performance Result:
//   Runtime: 2 ms, faster than 6.29% of Java online submissions for Remove Duplicates from Sorted List.
//   Memory Usage: 37.4 MB, less than 85.45% of Java online submissions for Remove Duplicates from Sorted List.
