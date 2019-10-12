package main

import "container/heap"

// Min heap
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// KthLarges is to find k-th largest value from integer array
type KthLargest struct {
	k    int
	nums *IntHeap
}

func Constructor(k int, nums []int) KthLargest {
	// Push initial array to heap tree
	h := &IntHeap{}
	heap.Init(h)
	for _, value := range nums {
		heap.Push(h, value)
	}

	// Remove smaller values less than k-th largest value
	for len(*h) > k {
		heap.Pop(h)
	}

	// Creage instance and return
	return KthLargest{k: k, nums: h}
}

func (this *KthLargest) Add(val int) int {
	// When heap tree size is smaller than k, just push
	if len(*this.nums) < this.k {
		heap.Push(this.nums, val)
		// When larger value is coming, remove smallest value
	} else if val > (*this.nums)[0] {
		heap.Push(this.nums, val)
		heap.Pop(this.nums)
	}

	// Return smallest value because heap tree only have top k values
	return (*this.nums)[0]
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * obj := Constructor(k, nums);
 * param_1 := obj.Add(val);
 */

// Sample Testcase:
//   Input:
//     k: 3
//     initial array: [4,5,8,2]
//     new values after initial array: 3, 5, 10, 9, 4
//   Output:
//     4, 5, 5, 8, 8

// Performance Result:
//   Runtime: 32 ms, faster than 96.95% of Go online submissions for Kth Largest Element in a Stream.
//   Memory Usage: 7.9 MB, less than 42.86% of Go online submissions for Kth Largest Element in a Stream.
