/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */
class Solution {
    func buildSubBST(_ subNums: [Int]) -> TreeNode? {
        if subNums.count <= 0 {
            return nil
        }
        else if subNums.count == 1 {
            return TreeNode(subNums[0])
        }
        
        let midIdx = subNums.count / 2
        let rootNode = TreeNode(subNums[midIdx])
        
        let leftSubNums: [Int] = Array(subNums.prefix(midIdx))
        rootNode.left = buildSubBST(leftSubNums)
        
        let rightSubNums: [Int] = Array(subNums.suffix(subNums.count - midIdx - 1))
        rootNode.right = buildSubBST(rightSubNums)
        
        return rootNode
    }
    
    func sortedArrayToBST(_ nums: [Int]) -> TreeNode? {
        if nums.count <= 0 {
            return nil
        }
        
        return buildSubBST(nums)
    }
}

// Sample Testcase:
//   Input:
//     [-10,-3,0,5,9]
//   Output:
//     [0,-3,9,-10,null,5]

// Performance Result:
//   Coding Time: 00:30:50
//   Runtime: 72 ms, faster than 19.74% of Swift
//      online submissions for Convert Sorted Array to Binary Search Tree.
//   Memory Usage: 22.4 MB, less than 33.33% of Swift
//      online submissions for Convert Sorted Array to Binary Search Tree.
