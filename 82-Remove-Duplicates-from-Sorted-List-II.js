/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 *
 * Time Complexicity: O(n)
 * Space Complexicity: O(1) because of just 3 variables without array
 */
var deleteDuplicates = function(head) {
    // If there is no node or only 1 node, immediately return a given list
    if (head == null || (head != null && head.next == null)) { return head; }

    // Scan a given list with current position and previous number position
    let currentPos = head;
    let prevNumPos = head;
    let isDuplicateFlg = false;
    while (currentPos != null) {
        // When current and next values are same, mark current as duplication
        if (currentPos.next != null && currentPos.val == currentPos.next.val) {
            isDuplicateFlg = true;
        // When current and next values are different, remove duplicate element
        } else if (currentPos.next == null
            || (currentPos.next != null && currentPos.val != currentPos.next.val)) {
            if (isDuplicateFlg) {
                // First elements are duplicated, change head position
                if (head.val == head.next.val) {
                    head = currentPos.next;
                }
                prevNumPos.next = currentPos.next;
                isDuplicateFlg = false;
            } else {
                prevNumPos = currentPos;
            }
        }
        currentPos = currentPos.next;
    }

    // This func modifies a given list, so just return head
    return head;
};

// Sample Testcase:
//   Input:
//     head object of a linked list(1:1 -> 2:2 -> 3:3 -> 4:3 -> 5:4 -> 6:4 -> 7:5 -> ...)
//   Output:
//     a list head without duplicate values(1:1 -> 2:2 -> 3:5)

// Performance Result:
//   Runtime: 68 ms, faster than 100.00% of JavaScript online submissions for Remove Duplicates from Sorted List II.
//   Memory Usage: 36.2 MB, less than 26.67% of JavaScript online submissions for Remove Duplicates from Sorted List II.
