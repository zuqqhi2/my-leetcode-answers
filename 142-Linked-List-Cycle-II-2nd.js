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
 */
var detectCycle = function(head) {
    // Corner case
    if (head === null) {
        return null;
    }
    if (head.next === null) {
        return null;
    }
    if (head.next.next === null) {
        return null;
    }

    //var visited = [];
    const visited = new Map();
    cur_node = head;
    while (!(visited.has(cur_node))) {
        if (cur_node.next === null) { return null; }
        visited.set(cur_node, true);
        cur_node = cur_node.next;
    }

    return cur_node;
};

// Performance Result:
//  Coding Time: 00:21:05K
//  Time Complexity: O(N)
//  Space Complexity: O(N)
//  Runtime: 72 ms, faster than 45.71% of JavaScript online submissions for Linked List Cycle II.
//  Memory Usage: 37.4 MB, less than 31.25% of JavaScript online submissions for Linked List Cycle II.
