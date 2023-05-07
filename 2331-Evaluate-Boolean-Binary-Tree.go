/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func traversal(root *TreeNode) bool {
    var left, right bool
    if root.Left != nil {
        left = traversal(root.Left)
    }
    if root.Right != nil {
        right = traversal(root.Right)
    }

    if root.Left != nil && root.Right != nil {
        // OR
        if root.Val == 2 {
            return left || right
        } else {
            return left && right
        }
    } else {
        if root.Val == 0 {
            return false
        } else {
            return true
        }
    }
}

func evaluateTree(root *TreeNode) bool {
    return traversal(root)
}


// Performance Result:
//   Coding Time: 00:10:54
//   Time Complexity: O(|V|)
//   Space Complexity: O(|V|)
//   Runtime: 16 ms, faster than 12.96%
//   Memory Usage: 6.6 MB, less than 77.78%
