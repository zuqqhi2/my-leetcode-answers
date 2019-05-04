/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */
class Solution {
    /// Reverse a linked list
    /// Time Complexity: O(n)
    /// Space Complexity: O(n)
    ///
    /// - Parameters:
    ///   - head: a head node of a given linked list
    /// - Returns: a head node of a reversed given linked list
    func reverseList(_ head: ListNode?) -> ListNode? {
        // Create a node array of a given linked list
        var nodeStack: [ListNode] = []
        var currentPos: ListNode? = head
        while currentPos != nil {
            nodeStack.append(currentPos!)
            currentPos = currentPos?.next
        }

        // Keep first node in a result
        currentPos = nodeStack.popLast()
        var prevPos: ListNode? = currentPos
        let tailPos: ListNode? = currentPos

        // Switch next node and previous node
        while currentPos != nil {
            currentPos = nodeStack.popLast()
            prevPos?.next = currentPos
            prevPos = currentPos
        }

        // Set nil to last node next property
        prevPos?.next = nil

        // Return first node(last node of a given list)
        return tailPos
    }
}

// Sample Testcase:
//   Input:
//     head object of a linked list(1:1 -> 2:2 -> 3:3 -> 4:4 -> 5:5 -> nil)
//   Output:
//     a reversed list head(1:5 -> 2:4 -> 3:3 -> 4:2 -> 5:1 -> nil)

// Performance Result:
//   Runtime: 20 ms, faster than 63.54% of Swift online submissions for Reverse Linked List.
//   Memory Usage: 19.9 MB, less than 31.11% of Swift online submissions for Reverse Linked List.
