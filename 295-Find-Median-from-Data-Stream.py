import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        # Balancing
        heapq.heappush(self.min_heap, -self.max_heap[0])
        heapq.heappop(self.max_heap)

        # Manazing size
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -self.min_heap[0])
            heapq.heappop(self.min_heap)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return (-self.max_heap[0] + self.min_heap[0]) * 0.5


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Sample test case:
#   Input:
#       addNum(1)
#       addNum(2)
#       findMedian() -> 1.5
#       addNum(3)
#       findMedian() -> 2
#   Output:
#       [null, null, null, 1.5, null, 2.0]

# Performance Result:
#   Coding Time: -
#   Time Complexity: O(log N)
#   Space Complexity: O(N)
#   Runtime: 216 ms, faster than 47.73% of Python3
#       online submissions for Find Median from Data Stream.
#   Memory Usage: 24.1 MB, less than 6.67% of Python3
#       online submissions for Find Median from Data Stream.
