import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k

        heapq.heapify(self.heap)
        for i in range(len(nums) - k):
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# Performance Result:
#   Coding Time: 00:14:01
#   Time Complexity: O(log N)
#   Space Complexity: O(N)
#   Runtime: 128 ms, faster than 42.72%
#   Memory Usage: 17.8 MB, less than 8.70%
