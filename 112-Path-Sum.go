/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type NextNode struct {
    Node *TreeNode
    Total int
}

func hasPathSum(root *TreeNode, targetSum int) bool {
    if root == nil {
        return false
    }

    nextNodes := []NextNode{{Node: root, Total: root.Val}}
    for len(nextNodes) > 0 {
        targetNode := nextNodes[0]
        if targetNode.Node.Left == nil && targetNode.Node.Right == nil && targetNode.Total == targetSum {
            return true
        }

        nextNodes = nextNodes[1:]
        if targetNode.Node.Left != nil {
            total := targetNode.Total + targetNode.Node.Left.Val
            nextNodes = append(nextNodes, NextNode{Node: targetNode.Node.Left, Total: total})
        }
        if targetNode.Node.Right != nil {
            total := targetNode.Total + targetNode.Node.Right.Val
            nextNodes = append(nextNodes, NextNode{Node: targetNode.Node.Right, Total: total})
        }
    }

    return false
}

// Performance Result:
//   Coding Time: 00:27:31
//   Time Complexity: O(log n)
//   Space Complexity: O(log n)
//   Runtime: 0 ms, faster than 100.00%
//   Memory Usage: 5.42 MB, less than 11.98%
