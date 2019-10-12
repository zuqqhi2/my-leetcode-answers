package main

import "fmt"

// TreeNode Definition
// type TreeNode struct {
//     Val int
//     Left *TreeNode
//     Right *TreeNode
// }
//
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrderBottom(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}
	result := [][]int{{}}
	result[0] = []int{root.Val}

	nodeQueue := []*TreeNode{}
	depthQueue := []int{}

	// Breadth First Search
	nodeQueue = append(nodeQueue, root)
	depthQueue = append(depthQueue, 1)
	//curNode := root

	for len(nodeQueue) >= 1 {
		//for curNode.Left != nil || curNode.Right != nil {
		// Dequeue
		curNode := nodeQueue[0]
		nodeQueue = nodeQueue[1:]
		curDepth := depthQueue[0]
		depthQueue = depthQueue[1:]

		// Append child nodes to queue
		if len(result)-1 < curDepth && (curNode.Left != nil || curNode.Right != nil) {
			result = append(result, []int{})
		}
		if curNode.Left != nil {
			nodeQueue = append(nodeQueue, curNode.Left)
			depthQueue = append(depthQueue, curDepth+1)
			result[curDepth] = append(result[curDepth], curNode.Left.Val)
		}
		if curNode.Right != nil {
			nodeQueue = append(nodeQueue, curNode.Right)
			depthQueue = append(depthQueue, curDepth+1)
			result[curDepth] = append(result[curDepth], curNode.Right.Val)
		}
	}

	// Reverse
	for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
		result[i], result[j] = result[j], result[i]
	}
	return result
}

func main() {
	fmt.Println("### Case 1: [[]] ###")
	fmt.Println(levelOrderBottom(nil))

	fmt.Println("### Case 2: [[1]] ###")
	root1 := TreeNode{1, nil, nil}
	fmt.Println(levelOrderBottom(&root1))

	fmt.Println("### Case 3: [[2],[1]] ###")
	c21 := TreeNode{2, nil, nil}
	root2 := TreeNode{1, &c21, nil}
	fmt.Println(levelOrderBottom(&root2))

	fmt.Println("### Case 4: [[4, 5], [2, 3],[1]] ###")
	c31 := TreeNode{4, nil, nil}
	c32 := TreeNode{5, nil, nil}
	c33 := TreeNode{2, nil, nil}
	c34 := TreeNode{3, &c31, &c32}
	root3 := TreeNode{1, &c33, &c34}
	fmt.Println(levelOrderBottom(&root3))
}

// Sample Testcase:
//   Input:
//     [3,9,20,null,null,15,7]
//   Output:
//     [
//	     [15,7],
//	     [9,20],
//	     [3]
//	   ]

// Performance Result:
//   Coding Time: 01:01:25
//	 Runtime: 4 ms, faster than 52.26% of Go
//		online submissions for Binary Tree Level Order Traversal II.
//	 Memory Usage: 5.9 MB, less than 100.00% of Go
//		online submissions for Binary Tree Level Order Traversal II.
