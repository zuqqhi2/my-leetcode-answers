/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type NextNode struct {
    Total int
    Node *TreeNode
}

func sumRootToLeaf(root *TreeNode) int {
    nextNodes := []NextNode{{Total: root.Val, Node: root}}
    res := 0
    for len(nextNodes) > 0 {
        node := nextNodes[0]
        nextNodes = nextNodes[1:]

        if node.Node.Left == nil && node.Node.Right == nil {
            res = res + node.Total
        }

        if node.Node.Left != nil {
            nextNodes = append(nextNodes,
                NextNode{Total: node.Total * 2 + node.Node.Left.Val, Node: node.Node.Left})
        }
        if node.Node.Right != nil {
            nextNodes = append(nextNodes,
                NextNode{Total: node.Total * 2 + node.Node.Right.Val, Node: node.Node.Right})
        }
    }

    return res
}


// Performance Result:
//   Coding Time: 00:29:19
//   Time Complexity: O(log n)
//   Space Complexity: O(log n)
//   Runtime: 3 ms, faster than 70.49%
//   Memory Usage: 3.50 MB, less than 6.56%
