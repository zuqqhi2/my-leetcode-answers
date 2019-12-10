import heapq

class KthLargest:

    def __init__(self, k, nums):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        if len(self.heap) >= self.k:
            if val < self.heap[0]:
                return self.heap[0]
            else:
                heapq.heappop(self.heap)
        heapq.heappush(self.heap, val)
        return self.heap[0]



kl = KthLargest(3, [4, 5, 8, 2])
print(kl.add(3))
print(kl.add(5))
print(kl.add(10))
print(kl.add(9))
print(kl.add(4))


# Sample test case:
#   Input:
#       int k = 3;
#       int[] arr = [4,5,8,2];
#       KthLargest kthLargest = new KthLargest(3, arr);
#       kthLargest.add(3);   // returns 4
#       kthLargest.add(5);   // returns 5
#       kthLargest.add(10);  // returns 5
#       kthLargest.add(9);   // returns 8
#       kthLargest.add(4);   // returns 8
#   Output:
#       4, 5, 5, 8, 8

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(?)
#   Space Complexity: O(?)
#   Runtime: 128 ms, faster than 26.95% of Python3
#       online submissions for Kth Largest Element in a Stream.
#   Memory Usage: 16.4 MB, less than 100.00% of Python3
#       online submissions for Kth Largest Element in a Stream.
