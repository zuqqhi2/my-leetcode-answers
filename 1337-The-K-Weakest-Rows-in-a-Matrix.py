import heapq


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weakest_heap = []
        for y in range(len(mat)):
            num_soldier = sum(mat[y])
            heapq.heappush(weakest_heap, (num_soldier, y))

        return [heapq.heappop(weakest_heap)[1] for _ in range(k)]


# Performance Result:
#   Coding Time: 00:04:41
#   Time Complexity: O(N log N)
#   Space Complexity: O(N)
#   Runtime: 112 ms, faster than 39.31%
#   Memory Usage: 14.7 MB, less than 44.87%
